# Plotando resultados

Agora, reorganizamos os dados com base nas etiquetas de linha e coluna atribuídas pelo modelo `SpectralBiclustering` em ordem crescente e plotamos novamente. Os `row_labels_` variam de 0 a 3, enquanto os `column_labels_` variam de 0 a 2, representando um total de 4 clusters por linha e 3 clusters por coluna.

```python
# Reordenando primeiro as linhas e depois as colunas.
reordered_rows = data[np.argsort(model.row_labels_)]
reordered_data = reordered_rows[:, np.argsort(model.column_labels_)]

plt.matshow(reordered_data, cmap=plt.cm.Blues)
plt.title("Após o biclustering; reorganizado para mostrar os biclusters")
_ = plt.show()
```

Como último passo, queremos demonstrar as relações entre as etiquetas de linha e coluna atribuídas pelo modelo. Portanto, criamos uma grade com `numpy.outer`, que recebe os `row_labels_` e `column_labels_` ordenados e adiciona 1 a cada um para garantir que as etiquetas comecem em 1 em vez de 0, para uma melhor visualização.

```python
plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)
plt.title("Estrutura de xadrez dos dados reorganizados")
plt.show()
```
