# Установите метаданные PDF-файла

В этом шаге вы установите метаданные PDF-файла. Вы можете установить заголовок, автора, тему, ключевые слова и дату создания/изменения PDF-файла.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
