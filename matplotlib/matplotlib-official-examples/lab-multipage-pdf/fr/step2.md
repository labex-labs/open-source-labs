# Créer l'objet PdfPages

Ensuite, vous devez créer un objet PdfPages dans lequel vous enregistrerez les pages du fichier PDF. Vous pouvez utiliser l'instruction 'with' pour vous assurer que l'objet PdfPages est correctement fermé à la fin du bloc, même si une exception se produit.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
