# Crear el objeto PdfPages

A continuación, debe crear un objeto PdfPages al que guardará las páginas del archivo PDF. Puede usar la instrucción 'with' para asegurarse de que el objeto PdfPages se cierre correctamente al final del bloque, incluso si se produce una excepción.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
