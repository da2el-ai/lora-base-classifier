# LoRA Base Classifier

- LoRA / LyCORIS などを BaseModel ごとにフォルダ分類するPythonスクリプトです。
- PowerShellやコマンドプロンプトから実行してください。
- [CivitaiHelper](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper) または [StabilityMatrix](https://github.com/LykosAI/StabilityMatrix) が生成するJSONファイルを参照しています。
- そのため拡張子 `.civitai.info`、`.cm-info.json` が存在しないファイルは対象外です。

## Usage

`lora` フォルダ以下を `move_test` にコピーするサンプルです。

### ファイル構成
```
StableDiffusion/
  +-- models/
      +-- move_test/ 👈 移動先
      +-- lora/      👈 移動元
          +-- costume/
              +-- swimsuit.safetensors  👈 SD 1.5
              +-- swimsuit.civitai.info
              +-- swimsuit.cm-info.json
              +-- swimsuit.preview.png
              +-- bunny.safetensors  👈 Pony
              +-- bunny.civitai.info
              +-- bunny.cm-info.json
              +-- bunny.preview.png
```

### 実行コマンド

```
> python lora-base-classifier --src c:\StableDiffusion\models\lora --dest c:\StableDiffusion\models\move_test --action copy
```

実行結果が表示されます。
```
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.civitai.info
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.cm-info.json
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.preview.jpeg
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.preview.png
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.safetensors
c:\StableDiffusion\Models\move_test\SD 1.5\costume\slskmz_v2.txt
c:\StableDiffusion\Models\move_test\SDXL 1.0\costume\sukumizu_xl_long.civitai.info
c:\StableDiffusion\Models\move_test\SDXL 1.0\costume\sukumizu_xl_long.cm-info.json
c:\StableDiffusion\Models\move_test\SDXL 1.0\costume\sukumizu_xl_long.preview.jpeg
c:\StableDiffusion\Models\move_test\SDXL 1.0\costume\sukumizu_xl_long.preview.png
c:\StableDiffusion\Models\move_test\SDXL 1.0\costume\sukumizu_xl_long.safetensors
```



### 実行後

```
StableDiffusion/
  +-- models/
      +-- move_test/
          +-- SD 1.5/
          |   +-- costume/
          |       +-- swimsuit.safetensors
          |       +-- swimsuit.civitai.info
          |       +-- swimsuit.cm-info.json
          |       +-- swimsuit.preview.png
          +-- Pony/
              +-- costume/
                  +-- bunny.safetensors
                  +-- bunny.civitai.info
                  +-- bunny.cm-info.json
                  +-- bunny.preview.png
```

## Options

### --src（必須/require）
- 移動元のファイルがあるフォルダ
- 例: --src c:\StableDiffusion\models\lora

### --dest（必須/require）
- 移動先のフォルダ
- **`--src` とは違うフォルダを指定してください**
- 例: --dest c:\StableDiffusion\models\move_test

### --action [move / copy]
- `--action move`: 移動
- `--action copy`: コピー
- 無指定の時は移動先のリストが表示されるだけで、ファイルに変化はありません。
- 実際に移動を行う前に移動先が確認できます。

## .cm-info.json を生成する方法

[StabilityMatrix](https://github.com/LykosAI/StabilityMatrix) で管理している方はこちらの方法をおすすめします。

1. StabilityMatrixの `Checkpoint Manager` タブを開く
2. 左側のフォルダ一覧から `Lora` フォルダを開く
3. `Find Connected Metadata` をクリックして実行


## .civitai.info を生成する方法

CivitaiHelperは更新が止まってたり、Fork版があったりするので**正直どれが使えるのかよくわかりません。** 各自で調べてください。

1. [CivitaiHelper](https://github.com/butaixianran/Stable-Diffusion-Webui-Civitai-Helper)をStableDiffusion webui A1111版にインストール
2. `Civital Helper` タブを開く
3. `Scan Models for Civitai` で **`lora`だけをONにする**
4. `Scan` をクリックして実行

