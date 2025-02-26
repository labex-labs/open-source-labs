# コンテキストマネージャ

演習3.5では、ユーザーが見やすい形式のテーブルを作成できるようにしました。たとえば：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```

コードの1つの問題は、すべてのテーブルが標準出力（`sys.stdout`）に出力されることです。出力をファイルや他の場所にリダイレクトしたい場合があります。全体的に見ると、すべてのテーブル形式のコードを変更して、異なる出力ファイルを許可することができます。ただし、緊急の場合には、コンテキストマネージャを使ってこれを解決することもできます。

次のコンテキストマネージャを定義します。

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

このコンテキストマネージャは、`sys.stdout`に一時的なパッチを当てて、すべての出力を異なるファイルにリダイレクトすることで機能します。終了時には、パッチが元に戻されます。試してみましょう。

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # ファイルを確認する
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
