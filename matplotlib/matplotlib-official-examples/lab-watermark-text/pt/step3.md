# Adicionar Marca d'Água de Texto

Para adicionar uma marca d'água de texto, podemos usar o método `text()` do objeto `Figure`. Precisamos fornecer a posição, o texto e outras propriedades como tamanho da fonte, cor e transparência.

```python
ax.text(0.5, 0.5, 'created with matplotlib', transform=ax.transAxes,
        fontsize=40, color='gray', alpha=0.5,
        ha='center', va='center', rotation=30)
```
