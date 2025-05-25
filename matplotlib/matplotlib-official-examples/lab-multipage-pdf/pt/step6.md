# Definir os Metadados do Arquivo PDF

Nesta etapa, você definirá os metadados do arquivo PDF. Você pode definir o título, autor, assunto, palavras-chave e data de criação/modificação do arquivo PDF.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
