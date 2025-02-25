# Создаем сеть

Мы создаем сеть в пространстве параметрических переменных `u` и `v`. Это делается с использованием функции `np.meshgrid()` для создания сетки точек `u` и `v`.

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
