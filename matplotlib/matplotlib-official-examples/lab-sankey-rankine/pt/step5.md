# Adicionar Rótulos e Formatação

Adicionaremos rótulos aos patches no diagrama de Sankey usando o atributo `text` de cada patch. Também formataremos o texto para ser negrito e aumentaremos o tamanho da fonte.

```python
diagrams = sankey.finish()
for diagram in diagrams:
    diagram.text.set_fontweight('bold')
    diagram.text.set_fontsize('10')
    for text in diagram.texts:
        text.set_fontsize('10')
```
