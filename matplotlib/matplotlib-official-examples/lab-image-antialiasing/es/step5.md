# Interpolar hacia arriba la imagen con interpolación 'antialiased'

Finalmente, interpolaremos hacia arriba la imagen de 500 píxeles de datos a 530 píxeles renderizados utilizando interpolación 'antialiased'. Esto demostrará cómo utilizar algoritmos de anti-aliasing mejores puede reducir los patrones de Moiré.

```python
fig, ax = plt.subplots(figsize=(6.8, 6.8))
ax.imshow(a, interpolation='antialiased', cmap='gray')
ax.set_title("interpolado por un factor de 1.048, interpolación='antialiased'")
plt.show()
```
