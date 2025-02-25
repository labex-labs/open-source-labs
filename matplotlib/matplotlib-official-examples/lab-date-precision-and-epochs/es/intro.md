# Introducción

Este es un laboratorio paso a paso que demuestra cómo manejar la precisión de fechas y los épocas en Matplotlib. Matplotlib puede trabajar con objetos `.datetime` y objetos `numpy.datetime64` utilizando un conversor de unidades que reconoce estas fechas y las convierte en números de punto flotante. Antes de Matplotlib 3.3, el valor predeterminado para esta conversión devolvía un flotante que era el número de días desde "0000-12-31T00:00:00". A partir de Matplotlib 3.3, el valor predeterminado es el número de días a partir de "1970-01-01T00:00:00". Esto permite una mayor resolución para fechas modernas.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
