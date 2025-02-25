# Interpolar hacia arriba la imagen con interpolación 'nearest'

Ahora, interpolaremos hacia arriba la imagen de 500 píxeles de datos a 530 píxeles renderizados utilizando interpolación 'nearest'. Esto demostrará cómo los patrones de Moiré todavía pueden ocurrir incluso cuando la imagen se interpola hacia arriba si el factor de interpolación hacia arriba no es un número entero.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='nearest', cmap='gray')
ax.set_title("interpolado por un factor de 1.048, interpolación='nearest'")
plt.show()
```
