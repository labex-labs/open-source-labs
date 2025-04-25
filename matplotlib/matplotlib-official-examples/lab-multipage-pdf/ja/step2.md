# PdfPages オブジェクトの作成

次に、PDF ファイルのページを保存するための PdfPages オブジェクトを作成する必要があります。例外が発生した場合でも、ブロックの終了時に PdfPages オブジェクトが正常にクローズされるようにするために、'with'文を使用できます。

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
