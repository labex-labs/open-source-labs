# Построение точек обучения

Теперь мы построим точки обучения на поверхности решения. Мы будем использовать метод scatter() для построения точек обучения с разными цветами для разных значений целевых переменных.

```python
for i, color in zip(clf.classes_, colors):
    idx = np.where(y == i)
    plt.scatter(
        X[idx, 0],
        X[idx, 1],
        c=color,
        label=iris.target_names[i],
        cmap=plt.cm.Paired,
        edgecolor="black",
        s=20,
    )
plt.title("Decision surface of multi-class SGD")
plt.axis("tight")
```
