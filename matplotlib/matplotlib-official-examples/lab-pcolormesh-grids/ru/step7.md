# Оттенкование Гуро

Можно также указать `оттенкование Гуро (Gouraud shading)`, при котором цвет в четырехугольниках линейно интерполируется между точками сетки. Формы `X`, `Y`, `Z` должны быть одинаковыми. Мы можем визуализировать сеть с помощью следующего кодового блока:

```python
fig, ax = plt.subplots()
ax.pcolormesh(X, Y, Z, shading='gouraud', cmap='viridis')
ax.set_title('Gouraud Shading')
plt.show()
```
