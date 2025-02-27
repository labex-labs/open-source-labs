# Introducción

Este tutorial demostrará cómo realizar una regresión cuantílica utilizando scikit-learn. Generaremos dos conjuntos de datos sintéticos para ilustrar cómo la regresión cuantílica puede predecir cuantiles condicionales no triviales. Utilizaremos la clase `QuantileRegressor` para estimar la mediana, así como un cuantil bajo y alto fijados en el 5% y 95%, respectivamente. Compararemos `QuantileRegressor` con `LinearRegression` y evaluaremos su rendimiento utilizando el error absoluto medio (MAE) y el error cuadrático medio (MSE).

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
