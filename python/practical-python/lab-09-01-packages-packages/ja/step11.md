# チャレンジ9.1：単純なパッケージの作成

`porty/` というディレクトリを作成し、上記のすべてのPythonファイルをその中に入れます。さらに空の `__init__.py` ファイルを作成し、それを同じディレクトリに置きます。以下のようなファイルのディレクトリができるはずです。

    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py

ディレクトリにある `__pycache__` ファイルを削除します。これには以前の事前コンパイル済みのPythonモジュールが含まれています。新しく始めましょう。

パッケージのいくつかのモジュールをインポートしてみましょう。

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

これらのインポートが失敗した場合は、適切なファイルに移動して、モジュールインポートを修正して、パッケージ相対インポートを含めます。たとえば、`import fileparse` のようなステートメントは、次のように変更される場合があります。

    # report.py
    from. import fileparse

...

`from fileparse import parse_csv` のようなステートメントがある場合は、コードを次のように変更します。

    # report.py
    from.fileparse import parse_csv

...
