# Обучение словаря

Обучение словаря - это метод для нахождения разреженного представления входных данных в виде комбинации простых элементов, которые образуют словарь. Мы применяем MiniBatchDictionaryLearning, которая представляет собой более быструю версию DictionaryLearning, лучше подходящую для обработки больших наборов данных.

```python
# Dictionary learning
batch_dict_estimator = decomposition.MiniBatchDictionaryLearning(
    n_components=n_components, alpha=0.1, max_iter=50, batch_size=3, random_state=rng
)
batch_dict_estimator.fit(faces_centered)
plot_gallery("Dictionary learning", batch_dict_estimator.components_[:n_components])
```
