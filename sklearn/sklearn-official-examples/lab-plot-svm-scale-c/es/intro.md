# Introducción

Esta práctica demuestra el efecto de la escala del parámetro de regularización al utilizar Máquinas de Vectores de Soporte (SVMs) para la clasificación. En la clasificación SVM, estamos interesados en la minimización del riesgo para la ecuación:

```math
C \sum_{i=1, n} \mathcal{L} (f(x_i), y_i) + \Omega (w)
```

donde:

- `C` se utiliza para establecer la cantidad de regularización
- `L` es una función de pérdida de nuestras muestras y nuestros parámetros del modelo.
- `Ω` es una función de penalización de nuestros parámetros del modelo

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
