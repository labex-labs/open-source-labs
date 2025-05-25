# Plotar Etiquetas Aprendidas

Finalmente, plotamos as etiquetas aprendidas para visualizar a precisão do LabelPropagation.

```python
output_labels = label_spread.transduction_
output_label_array = np.asarray(output_labels)
outer_numbers = np.where(output_label_array == outer)[0]
inner_numbers = np.where(output_label_array == inner)[0]

plt.figure(figsize=(4, 4))
plt.scatter(
    X[outer_numbers, 0],
    X[outer_numbers, 1],
    color="navy",
    marker="s",
    lw=0,
    s=10,
    label="externo aprendido",
)
plt.scatter(
    X[inner_numbers, 0],
    X[inner_numbers, 1],
    color="c",
    marker="s",
    lw=0,
    s=10,
    label="interno aprendido",
)
plt.legend(scatterpoints=1, shadow=False, loc="center")
plt.title("Etiquetas aprendidas com Label Spreading (KNN)")
plt.show()
```
