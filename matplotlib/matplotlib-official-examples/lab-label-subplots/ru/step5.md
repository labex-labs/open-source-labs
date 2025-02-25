# Метка с заголовком

Если мы хотим, чтобы метка была выровнена с заголовком, мы можем включить ее в заголовок или использовать ключевой аргумент `loc`.

```python
for label, ax in axs.items():
    ax.set_title('Normal Title', fontstyle='italic')
    ax.set_title(label, fontfamily='serif', loc='left', fontsize='medium')
```
