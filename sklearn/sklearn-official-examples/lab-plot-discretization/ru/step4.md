# Дискретизация входного признака

В этом шаге мы будем использовать класс KBinsDiscretizer для дискретизации входного признака. Мы создадим 10 групп (bins) и применим one-hot кодирование для преобразования данных.

```python
enc = KBinsDiscretizer(n_bins=10, encode="onehot")
X_binned = enc.fit_transform(X)
```
