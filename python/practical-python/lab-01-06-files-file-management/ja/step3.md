# ファイルに書き込むための一般的な慣用句

文字列を書き込む。

```python
with open('outfile', 'wt') as out:
    out.write('Hello World\n')
 ...
```

print 関数をリダイレクトする。

```python
with open('outfile', 'wt') as out:
    print('Hello World', file=out)
 ...
```

これらのエクササイズは、`portfolio.csv` というファイルに依存しています。このファイルには、株式のポートフォリオに関する情報が含まれた行のリストがあります。あなたが `~/project/` ディレクトリで作業していることが前提となっています。もしあなたが確信できない場合、このようにして Python がどこを実行していると考えているかを調べることができます。

```python
>>> import os
>>> os.getcwd()
'/home/labex/project' # 出力は異なります
>>>
```
