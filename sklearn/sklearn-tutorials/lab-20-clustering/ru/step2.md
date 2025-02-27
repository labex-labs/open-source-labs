# Генерируем примерные данные

Далее давайте сгенерируем некоторые примерные данные для работы. Мы будем использовать функцию `make_blobs` из модуля `sklearn.datasets`, чтобы создать синтетический набор данных с кластерами.

```python
# Generate sample data
X, y = make_blobs(n_samples=100, centers=4, random_state=0, cluster_std=1.0)
```
