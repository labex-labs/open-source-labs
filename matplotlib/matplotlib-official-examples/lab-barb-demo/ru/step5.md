# Создаем график ветровых стрелок с замаскированными данными

Мы также можем создать график ветровых стрелок с замаскированными данными, используя замаскированный массив. В этом случае мы изменим значение одного вектора на недопустимое значение и замаскируем его.

```python
masked_u = np.ma.masked_array(U)
masked_u[4] = 1000  # Bad value that should not be plotted when masked
masked_u[4] = np.ma.masked

plt.barbs(X, Y, masked_u, V, length=8, pivot='middle')
plt.show()
```
