# Настройка Gaussian Mixture Model

Теперь мы можем настроить Gaussian Mixture Model на наших данных с использованием класса `GaussianMixture` из модуля `sklearn.mixture`. Укажите желаемое количество компонентов и любые другие параметры, которые вы хотите использовать.

```python
# Fit a Gaussian Mixture Model
gmm = GaussianMixture(n_components=3)
gmm.fit(X_train)
```
