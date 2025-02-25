# Генерация диаграммы Хинтона

Теперь мы сгенерируем случайную матрицу весов с использованием numpy, а затем используем функцию `hinton` для генерации диаграммы Хинтона.

```python
if __name__ == '__main__':
    # Fixing random state for reproducibility
    np.random.seed(19680801)

    hinton(np.random.rand(20, 20) - 0.5)
    plt.show()
```
