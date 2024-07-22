import os
import shutil
import json
import argparse
import glob

###############
# jsonからベースモデルを取得
# file_path: 対象ファイルのフルパス
def getBaseModel(file_path):
    # 対象ファイルのベースネーム（拡張子を除いた名前）を取得
    base_name = os.path.splitext(file_path)[0]

    # 対象ファイルと同名で異なる拡張子を持つファイルパスを作成
    civitai_info_file = base_name + '.civitai.info'
    cm_info_json_file = base_name + '.cm-info.json'

    # 優先順位に基づいてファイルの存在を確認し、ファイルパスを選択
    if os.path.exists(cm_info_json_file):
        info_file = cm_info_json_file
    elif os.path.exists(civitai_info_file):
        info_file = civitai_info_file
    else:
        return None

    # 選択されたファイルを読み込んで "BaseModel" の内容を取得
    with open(info_file, 'r') as f:
        info_data = json.load(f)
        return info_data.get("BaseModel") or info_data.get("baseModel")


###############
# ファイルを移動
# file_path: 対象ファイルのフルパス
# src_base_dir: 移動元のベースフォルダ
# dest_base_dir: 移動先のベースフォルダ
# category: 追加分類フォルダ
def moveFiles(file_path, srcBaseDir, destBaseDir, base_model, action=''):
    # 移動元のベースフォルダから相対パスを取得
    relative_path = os.path.relpath(file_path, srcBaseDir)
    # 相対パスからファイル名を除いたパスを取得
    relative_dir = os.path.dirname(relative_path)
    # 移動先のフォルダを構築
    dest_dir = os.path.join(destBaseDir, base_model, relative_dir)

    # 移動先のディレクトリが存在しない場合は作成
    if not os.path.exists(dest_dir):
        if action == 'copy' or action == 'move':
            os.makedirs(dest_dir)

    # 対象ファイルのベースネーム（拡張子を除いた名前）を取得
    base_name, _ = os.path.splitext(file_path)
    # base_name で始まるすべてのファイルを探す
    files_to_move = glob.glob(os.path.join(os.path.dirname(file_path), base_name + '.*'))



    # 移動対象のすべての拡張子ファイルを探す
    for current_file in files_to_move:
        # 移動先のフルパスを構築
        dest_path = os.path.join(dest_dir, os.path.basename(current_file))
        print(dest_path)

        # nomove が False の場合にファイルを移動
        if action == 'copy':
            shutil.copy(current_file, dest_path)
        elif action == 'move':
            shutil.move(current_file, dest_path)


###############
# 下層フォルダの .safetensors を取得して処理
def searchModels(src_base_dir, dest_base_dir, action=''):
    # src_base_dir 以下の全てのファイルとディレクトリを再帰的に探索
    for root, dirs, files in os.walk(src_base_dir):
        for file in files:
            # 拡張子が .safetensors のファイルを探す
            if file.endswith('.safetensors'):
                file_path = os.path.join(root, file)
                # base_model を取得
                base_model = getBaseModel(file_path)

                if base_model:
                    # ファイルを移動
                    moveFiles(file_path, src_base_dir, dest_base_dir, base_model, action)


#####################
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Search and move model files.')
    parser.add_argument('--src', required=True, help='Source base directory')
    parser.add_argument('--dest', required=True, help='Destination base directory')
    parser.add_argument('--action', help='copy or move')

    args = parser.parse_args()

    searchModels(args.src, args.dest, args.action)