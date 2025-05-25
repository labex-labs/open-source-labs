# Rotular a figura

Nesta etapa, rotularemos a figura. Adicionaremos um título, linhas de grade e rótulos para os eixos x e y.

```python
fig.suptitle("Cumulative Distributions")
for ax in axs:
    ax.grid(True)
    ax.legend()
    ax.set_xlabel("Annual rainfall (mm)")
    ax.set_ylabel("Probability of occurrence")
    ax.label_outer()

plt.show()
```
