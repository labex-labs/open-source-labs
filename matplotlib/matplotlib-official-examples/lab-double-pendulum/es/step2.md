# Establecer parámetros

A continuación, definiremos los parámetros para nuestra simulación. Estos parámetros incluyen la aceleración debida a la gravedad, la longitud y la masa de cada péndulo, y el intervalo de tiempo para la simulación.

```python
G = 9.8  # aceleración debida a la gravedad, en m/s^2
L1 = 1.0  # longitud del péndulo 1 en m
L2 = 1.0  # longitud del péndulo 2 en m
L = L1 + L2  # longitud máxima del péndulo combinado
M1 = 1.0  # masa del péndulo 1 en kg
M2 = 1.0  # masa del péndulo 2 en kg
t_stop = 2.5  # cuántos segundos simular
history_len = 500  # cuántos puntos de trayectoria mostrar
```
