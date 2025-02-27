# Генерация данных

Мы сгенерируем некоторые данные для обучения, тестирования и обнаружения выбросов с использованием numpy. Мы сгенерируем 100 нормальных наблюдений для обучения, 20 нормальных наблюдений для тестирования и 20 аномальных новых наблюдений.

```python
np.random.seed(42)

xx, yy = np.meshgrid(np.linspace(-5, 5, 500), np.linspace(-5, 5, 500))
X = 0.3 * np.random.randn(100, 2)
X_train = np.r_[X + 2, X - 2]
X = 0.3 * np.random.randn(20, 2)
X_test = np.r_[X + 2, X - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20, 2))
```
