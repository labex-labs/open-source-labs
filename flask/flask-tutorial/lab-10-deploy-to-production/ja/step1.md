# アプリケーションの構築

まず、アプリケーション用のwheelファイルを作成する必要があります。これには`build`ツールを使用します。まだインストールしていない場合は、pipを使って`build`ツールをインストールします：

```bash
# Install the build tool
pip install build
```

次に、`build`ツールを使ってwheelファイルを作成します：

```bash
# Build the wheel file
python -m build --wheel
```

wheelファイルは、`dist`ディレクトリに`flaskr-1.0.0-py3-none-any.whl`のような名前であるはずです。
