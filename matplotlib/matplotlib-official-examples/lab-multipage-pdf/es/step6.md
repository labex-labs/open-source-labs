# Establecer los metadatos del archivo PDF

En este paso, establecerá los metadatos del archivo PDF. Puede establecer el título, el autor, el asunto, las palabras clave y la fecha de creación/modificación del archivo PDF.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
