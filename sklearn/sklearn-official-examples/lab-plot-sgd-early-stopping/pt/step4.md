# Plotar os resultados

O passo final é plotar os resultados. Usaremos dois subplots para plotar as pontuações de treinamento e teste, e o número de iterações e o tempo de ajuste. Usaremos estilos de linha diferentes para cada estimador e critério de parada.

```python
# Definir o que plotar
lines = "Critério de parada"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# Primeiro gráfico: pontuações de treinamento e teste
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["Pontuação de treinamento", "Pontuação de teste"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# Segundo gráfico: n_iter e tempo de ajuste
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "Tempo de ajuste (seg)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
