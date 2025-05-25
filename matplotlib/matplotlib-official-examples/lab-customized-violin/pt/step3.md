# Personalizar a aparência do gráfico de violino

Agora, personalizaremos a aparência do gráfico de violino. Primeiro, limitaremos o que o Matplotlib desenha, definindo os argumentos `showmeans`, `showmedians` e `showextrema` como `False`. Em seguida, mudaremos a cor e a opacidade dos corpos do violino usando os métodos `set_facecolor` e `set_alpha`. Finalmente, adicionaremos uma representação simplificada de um box plot (gráfico de caixa) no topo do gráfico de violino, usando a função `percentile` do NumPy para calcular os quartis, medianas e whiskers (bigodes).

```python
# customize violin plot appearance
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# create violin plot
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# customize violin bodies
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# add box plot
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
