# Formatando o Gráfico

Agora, formataremos o gráfico adicionando rótulos para os eixos x e y, definindo o localizador e formatador principal do eixo x e removendo o eixo y e as spines. Aqui está o código para formatar o gráfico:

```python
# format x-axis with 4-month intervals
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
plt.setp(ax.get_xticklabels(), rotation=30, ha="right")

# remove y-axis and spines
ax.yaxis.set_visible(False)
ax.spines[["left", "top", "right"]].set_visible(False)

ax.margins(y=0.1)
plt.show()
```
