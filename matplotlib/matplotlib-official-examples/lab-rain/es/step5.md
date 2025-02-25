# Crear la animación

Finalmente, crearemos la animación utilizando el objeto FuncAnimation, pasando la figura, la función de actualización, el intervalo entre cuadros en milisegundos y el número de cuadros a guardar.

```python
animation = FuncAnimation(fig, update, interval=10, save_count=100)
plt.show()
```
