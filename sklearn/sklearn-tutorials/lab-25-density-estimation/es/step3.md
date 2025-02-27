# Ajustar un estimador de densidad con núcleo

Ahora, crearemos una instancia del estimador `KernelDensity` y la ajustaremos a nuestros datos. Podemos elegir el tipo de núcleo y el ancho de banda para el estimador. Por ejemplo, podemos usar un núcleo gaussiano y establecer el ancho de banda en 0,2.

```python
kde = KernelDensity(kernel='gaussian', bandwidth=0.2).fit(X)
```
