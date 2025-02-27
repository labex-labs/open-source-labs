# Apprentissage de dictionnaire

L'apprentissage de dictionnaire est une méthode pour trouver une représentation sparse des données d'entrée sous forme d'une combinaison d'éléments simples, qui forment un dictionnaire. Nous appliquons MiniBatchDictionaryLearning, qui est une version plus rapide de DictionaryLearning qui est mieux adaptée aux grands jeux de données.

```python
# Apprentissage de dictionnaire
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Apprentissage de dictionnaire", batch_dict_estimator.components_[:n_components])
```
