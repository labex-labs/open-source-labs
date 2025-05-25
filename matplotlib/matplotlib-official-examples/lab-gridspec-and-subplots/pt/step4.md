# Removendo os Axes Subjacentes

Removemos os axes subjacentes que são cobertos pelos axes maiores que criaremos no próximo passo.

```python
for ax in axs[1:, -1]:
    ax.remove()
```
