# Rotular com Título

Se quisermos que o rótulo seja alinhado com o título, podemos incorporá-lo no título ou usar o argumento de palavra-chave `loc`.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
