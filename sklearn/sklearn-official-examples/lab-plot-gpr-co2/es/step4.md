# Interpretación de los hiperparámetros del kernel

Ahora, podemos echar un vistazo a los hiperparámetros del kernel.

```python
gaussian_process.kernel_
```

Por lo tanto, la mayor parte de la señal objetivo, con la media restada, está explicada por una tendencia ascendente a largo plazo de ~45 ppm y una escala de longitud de ~52 años. El componente periódico tiene una amplitud de ~2,6 ppm, un tiempo de decaimiento de ~90 años y una escala de longitud de ~1,5. El largo tiempo de decaimiento indica que tenemos un componente muy cercano a una periodicidad estacional. El ruido correlacionado tiene una amplitud de ~0,2 ppm con una escala de longitud de ~0,12 años y una contribución de ruido blanco de ~0,04 ppm. Por lo tanto, el nivel general de ruido es muy pequeño, lo que indica que los datos pueden ser muy bien explicados por el modelo.
