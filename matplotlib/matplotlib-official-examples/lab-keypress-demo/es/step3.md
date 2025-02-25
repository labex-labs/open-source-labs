# Crear la gráfica y conectar el oyente de eventos de pulsación de tecla

Creamos una gráfica simple utilizando `np.random.rand()` para generar datos aleatorios. Luego, configuramos el oyente de eventos de pulsación de tecla utilizando `fig.canvas.mpl_connect()` y pasando el nombre del evento que queremos escuchar (`'key_press_event'`) y la función que queremos llamar cuando se produzca el evento (`on_press`).

```python
fig, ax = plt.subplots()

fig.canvas.mpl_connect('key_press_event', on_press)

ax.plot(np.random.rand(12), np.random.rand(12), 'go')
xl = ax.set_xlabel('easy come, easy go')
ax.set_title('Presiona una tecla')
plt.show()
```
