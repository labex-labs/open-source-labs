# Definir los datos

En este paso, definiremos los datos que utilizaremos para crear el diagrama de tallos tridimensional. Crearemos una matriz `linspace` para el ángulo y utilizaremos las funciones seno y coseno para calcular las coordenadas x e y. También definiremos la coordenada z como el ángulo.

```python
theta = np.linspace(0, 2*np.pi)
x = np.cos(theta - np.pi/2)
y = np.sin(theta - np.pi/2)
z = theta
```
