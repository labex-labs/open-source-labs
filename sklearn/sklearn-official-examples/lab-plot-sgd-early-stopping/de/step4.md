# Zeichne die Ergebnisse

Der letzte Schritt besteht darin, die Ergebnisse zu zeichnen. Wir werden zwei Teilplots verwenden, um die Trainings- und Testscores sowie die Anzahl der Iterationen und die Fit-Zeit zu zeichnen. Wir werden verschiedene Linienstile für jeden Schätzer und jedes Stoppkriterium verwenden.

```python
# Definiere, was geplottet werden soll
lines = "Stoppkriterium"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# Erster Plot: Trainings- und Testscores
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["Trainingsscore", "Testscore"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# Zweiter Plot: n_iter und Fit-Zeit
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "Fit-Zeit (sec)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
