# Visualizar Resultados

Neste passo, visualizaremos os resultados do processo de discretização de características. Plotaremos a precisão da classificação no conjunto de teste para cada classificador e conjunto de dados.

```python
plt.tight_layout()

# Ajustar o espaçamento acima da figura
plt.subplots_adjust(top=0.90)
suptitles = [
    "Classificadores Lineares",
    "Discretização de Características e Classificadores Lineares",
    "Classificadores Não-Lineares",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```
