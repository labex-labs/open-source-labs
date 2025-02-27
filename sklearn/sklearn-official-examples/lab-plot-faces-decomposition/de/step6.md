# Wörterbuchlern (Dictionary learning)

Das Wörterbuchlern ist eine Methode, um eine spärliche Darstellung der Eingabedaten als eine Kombination einfacher Elemente zu finden, die ein Wörterbuch bilden. Wir wenden MiniBatchDictionaryLearning an, was eine schnellere Version von DictionaryLearning ist und für große Datensätze besser geeignet ist.

```python
# Dictionary learning
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Dictionary learning", batch_dict_estimator.components_[:n_components])
```
