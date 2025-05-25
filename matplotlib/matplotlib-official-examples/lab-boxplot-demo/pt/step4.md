# Personalizar o boxplot

Podemos personalizar o boxplot alterando a aparência da caixa, dos _whiskers_ (arestas) e dos _outliers_ (valores discrepantes). Também podemos criar múltiplos boxplots no mesmo gráfico para comparar diferentes grupos de dados. Aqui estão alguns exemplos de como personalizar o boxplot:

```python
# Criar um boxplot entalhado (notched)
plt.boxplot(data, notch=True)
plt.show()

# Mudar os símbolos dos pontos outliers para diamantes verdes
plt.boxplot(data, flierprops=dict(marker='D', markerfacecolor='g', markersize=8))
plt.show()

# Criar boxplots horizontais
plt.boxplot(data, vert=False)
plt.show()

# Criar múltiplos boxplots em um gráfico
data1 = np.random.normal(0, 1, 50)
data2 = np.random.normal(1, 1, 50)
data3 = np.random.normal(2, 1, 50)

plt.boxplot([data1, data2, data3])
plt.show()
```
