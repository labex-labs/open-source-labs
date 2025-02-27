# Tracer les résultats

La dernière étape consiste à tracer les résultats. Nous utiliserons deux sous-graphiques pour tracer les scores d'entraînement et de test, ainsi que le nombre d'itérations et le temps d'ajustement. Nous utiliserons différents styles de lignes pour chaque estimateur et critère d'arrêt.

```python
# Définir ce qui doit être tracé
lines = "Critère d'arrêt"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# Premier graphique : scores d'entraînement et de test
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["Score d'entraînement", "Score de test"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# Second graphique : n_iter et temps d'ajustement
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "Temps d'ajustement (sec)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
