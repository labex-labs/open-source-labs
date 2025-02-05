# 设置 PDF 文件的元数据

在这一步中，你将设置 PDF 文件的元数据。你可以设置 PDF 文件的标题、作者、主题、关键词以及创建/修改日期。

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Seppänen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
