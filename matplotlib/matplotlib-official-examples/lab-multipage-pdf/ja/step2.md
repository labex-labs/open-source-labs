# PdfPagesオブジェクトの作成

次に、PDFファイルのページを保存するためのPdfPagesオブジェクトを作成する必要があります。例外が発生した場合でも、ブロックの終了時にPdfPagesオブジェクトが正常にクローズされるようにするために、'with'文を使用できます。

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
