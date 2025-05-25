# Mascarando Pontos de Dados e Criando o Gráfico de Dispersão

Nós mascaramos os pontos de dados com base em sua distância da origem. Pontos de dados com uma distância menor que `r0` são mascarados em `area1`, e aqueles com uma distância maior ou igual a `r0` são mascarados em `area2`. Em seguida, criamos um gráfico de dispersão dos pontos de dados mascarados com `marker='^'` e `marker='o'` para `area1` e `area2`, respectivamente.

```python
r = np.sqrt(x ** 2 + y ** 2)
area1 = np.ma.masked_where(r < r0, area)
area2 = np.ma.masked_where(r >= r0, area)
plt.scatter(x, y, s=area1, marker='^', c=c)
plt.scatter(x, y, s=area2, marker='o', c=c)
```
