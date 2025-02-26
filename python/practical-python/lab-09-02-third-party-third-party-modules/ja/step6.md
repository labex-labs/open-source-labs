# 仮想環境

パッケージのインストール問題の一般的な解決策は、自分用の「仮想環境」を作成することです。当然ながら、その方法は「一つの方法」ではありません。実際、いくつかの競合するツールや技術があります。ただし、標準的な Python インストールを使用している場合、次のように入力してみることができます。

```bash
$ sudo apt install python3-venv
$ python -m venv mypython
bash %
```

数分待つと、自分専用の小さな Python インストールである新しいディレクトリ `mypython` ができます。そのディレクトリ内には、`bin/` ディレクトリ（Unix）または `Scripts/` ディレクトリ（Windows）があります。そこにある `activate` スクリプトを実行すると、この Python のバージョンが「アクティブ」になり、シェルの既定の `python` コマンドになります。たとえば：

```bash
$ source mypython/bin/activate
(mypython) bash %
```

ここから、自分用に Python パッケージをインストールすることができます。たとえば：

    (mypython) $ python -m pip install pandas

...

実験やさまざまなパッケージの試用目的では、仮想環境で通常問題なく機能します。一方、アプリケーションを作成していて特定のパッケージ依存関係がある場合は、やや異なる問題です。
