# Cargar y preprocesar la imagen

Comenzaremos cargando la imagen de monedas griegas y la preprocesaremos para que sea más fácil de trabajar. Redimensionaremos la imagen al 20% de su tamaño original y aplicaremos un filtro Gaussiano para suavizarla antes de reducir la escala para reducir artefactos de alias.

```python
# cargar las monedas como una matriz de numpy
monedas_orig = monedas()

# Redimensionarla al 20% de su tamaño original para acelerar el procesamiento
# Aplicando un filtro Gaussiano para suavizar antes de reducir la escala
# reduce los artefactos de alias.
monedas_suavizadas = filtro_gaussiano(monedas_orig, sigma=2)
monedas_redimensionadas = reescalar(monedas_suavizadas, 0.2, modo="reflect", anti_aliasing=False)
```
