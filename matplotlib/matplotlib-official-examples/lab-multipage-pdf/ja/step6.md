# PDFファイルのメタデータを設定する

このステップでは、PDFファイルのメタデータを設定します。PDFファイルのタイトル、著者、件名、キーワード、作成日/修正日を設定できます。

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
