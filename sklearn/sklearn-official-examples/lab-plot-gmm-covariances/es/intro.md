# Introducción

Este tutorial demuestra el uso de diferentes tipos de covarianza para los modelos mixtos gaussianos (GMMs). Los GMMs se utilizan a menudo para agrupamiento, y podemos comparar los clusters obtenidos con las clases reales del conjunto de datos. Inicializamos las medias de las gaussianas con las medias de las clases del conjunto de entrenamiento para que esta comparación sea válida. Graficamos las etiquetas predichas en los datos de entrenamiento y de prueba utilizando una variedad de tipos de covarianza de GMM en el conjunto de datos iris. Comparamos GMMs con matrices de covarianza esférica, diagonal, completa y atada en orden creciente de rendimiento.

Aunque se esperaría que la covarianza completa tuviera el mejor rendimiento en general, es propensa a sobreajustarse en conjuntos de datos pequeños y no se generaliza bien a los datos de prueba.

En las gráficas, los datos de entrenamiento se muestran como puntos, mientras que los datos de prueba se muestran como cruces. El conjunto de datos iris es de cuatro dimensiones. Aquí se muestran solo las dos primeras dimensiones, y por lo tanto algunos puntos se separan en otras dimensiones.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y lo resolveremos rápidamente para usted.
