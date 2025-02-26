# 演習3.8：例外の送出

前節で書いた `parse_csv()` 関数は、ユーザー指定の列を選択できるようになっていますが、入力データファイルに列ヘッダーがある場合にのみ機能します。

コードを修正して、`select` と `has_headers=False` の両方の引数が渡された場合に例外が送出されるようにしましょう。たとえば：

```python
>>> parse_csv('/home/labex/project/prices.csv', select=['name','price'], has_headers=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 9, in parse_csv
    raise RuntimeError("select argument requires column headers")
RuntimeError: select argument requires column headers
>>>
```

この1つのチェックを追加したら、関数内で他の種類の妥当性チェックを行うべきかどうか尋ねるかもしれません。たとえば、ファイル名が文字列であること、`types` がリストであること、またはそのような性質のことをチェックするべきでしょうか？

一般的なルールとして、通常はそのようなテストを省略し、悪い入力でプログラムが失敗するようにするのがベストです。トレースバックメッセージが問題の原因を指摘し、デバッグに役立ちます。

上記のチェックを追加する主な理由は、無意味なモードでコードを実行しないようにすること（たとえば、列ヘッダーが必要な機能を使用する一方で、ヘッダーがないことを同時に指定すること）です。

これは、呼び出し元のコードのプログラミングエラーを示しています。「起こってはならない」ケースをチェックすることは、多くの場合、良い考えです。
