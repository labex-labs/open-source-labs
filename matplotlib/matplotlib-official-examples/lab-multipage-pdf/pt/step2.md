# Criar o Objeto PdfPages

Em seguida, você precisa criar um objeto PdfPages no qual salvará as páginas do arquivo PDF. Você pode usar a instrução 'with' para garantir que o objeto PdfPages seja fechado corretamente no final do bloco, mesmo que ocorra uma exceção.

```python
with PdfPages('multipage_pdf.pdf') as pdf:
```
