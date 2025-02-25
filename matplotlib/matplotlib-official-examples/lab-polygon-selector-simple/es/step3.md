# Crear un polígono de manera interactiva

Para crear un polígono de manera interactiva, necesitamos crear un objeto `Figure` y un objeto `Axes`. Luego, podemos crear un objeto `PolygonSelector` y agregar vértices a él haciendo clic en la gráfica. También podemos usar las teclas `shift` y `ctrl` para mover los vértices.

```python
fig, ax = plt.subplots()
selector = PolygonSelector(ax, lambda *args: None)

print("Haga clic en la figura para crear un polígono.")
print("Presione la tecla 'esc' para comenzar un nuevo polígono.")
print("Intente mantener presionada la tecla 'shift' para mover todos los vértices.")
print("Intente mantener presionada la tecla 'ctrl' para mover un solo vértice.")

plt.show()
```
