# Festlegen der Metadaten der PDF-Datei

In diesem Schritt wirst du die Metadaten der PDF-Datei festlegen. Du kannst den Titel, den Autor, das Thema, die Schlüsselwörter sowie das Erstellungs- und Änderungsdatum der PDF-Datei festlegen.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
