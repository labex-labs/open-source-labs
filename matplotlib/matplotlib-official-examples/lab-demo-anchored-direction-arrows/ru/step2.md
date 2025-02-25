# Создаем график

Далее мы создадим простой график с использованием NumPy. Этот график будет служить фоном для направленных стрелок с привязкой.

```python
# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.imshow(np.random.random((10, 10)))
```
