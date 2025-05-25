# Repetir

Repetiremos o processo de seleção dos cinco pontos mais incertos, adicionando seus rótulos aos pontos de dados rotulados e treinando o modelo até termos 30 pontos de dados rotulados.

```python
max_iterations = 3

for i in range(max_iterations):
    if len(unlabeled_indices) == 0:
        print("Não há mais itens não rotulados para serem rotulados.")
        break

    # selecionar os cinco pontos mais incertos
    pred_entropies = stats.distributions.entropy(lp_model.label_distributions_.T)
    uncertainty_index = np.argsort(pred_entropies)[::-1]
    uncertainty_index = uncertainty_index[np.in1d(uncertainty_index, unlabeled_indices)][:5]

    # adicionar rótulos aos pontos de dados rotulados
    y_train[uncertainty_index] = y[uncertainty_index]

    # treinar o modelo
    lp_model.fit(X, y_train)

    # remover pontos de dados rotulados do conjunto não rotulado
    delete_indices = np.array([], dtype=int)
    for index, image_index in enumerate(uncertainty_index):
        (delete_index,) = np.where(unlabeled_indices == image_index)
        delete_indices = np.concatenate((delete_indices, delete_index))
    unlabeled_indices = np.delete(unlabeled_indices, delete_indices)
    n_labeled_points += len(uncertainty_index)
```
