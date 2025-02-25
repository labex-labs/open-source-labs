# Définir les métadonnées du fichier PDF

Dans cette étape, vous allez définir les métadonnées du fichier PDF. Vous pouvez définir le titre, l'auteur, le sujet, les mots-clés et la date de création/modification du fichier PDF.

```python
d = pdf.infodict()
d['Title'] = 'Multipage PDF Example'
d['Author'] = 'Jouni K. Sepp\xe4nen'
d['Subject'] = 'How to create a multipage pdf file and set its metadata'
d['Keywords'] = 'PdfPages multipage keywords author title subject'
d['CreationDate'] = datetime.datetime(2009, 11, 13)
d['ModDate'] = datetime.datetime.today()
```
