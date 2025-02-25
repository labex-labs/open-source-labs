# Crear los recuadros

Primero creamos los recuadros a los que se asignarán los mensajes emergentes.

```python
rect1 = plt.Rectangle((10, -20), 10, 5, fc='blue')
rect2 = plt.Rectangle((-20, 15), 10, 5, fc='green')

shapes = [rect1, rect2]
labels = ['This is a blue rectangle.', 'This is a green rectangle']
```
