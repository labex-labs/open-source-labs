# Introducción

La detección de novedades y valores atípicos son técnicas utilizadas para identificar si una nueva observación pertenece a la misma distribución que las observaciones existentes o si debe considerarse diferente. Estas técnicas se utilizan comúnmente para limpiar conjuntos de datos reales identificando observaciones anormales o inusuales.

Hay dos distinciones importantes en este contexto:

1. Detección de valores atípicos: Los datos de entrenamiento contienen valores atípicos, que son observaciones que se alejan de las demás. Los estimadores de detección de valores atípicos tratan de ajustarse a las regiones donde los datos de entrenamiento están más concentrados, ignorando las observaciones aberrantes.
2. Detección de novedades: Los datos de entrenamiento no están contaminados por valores atípicos, y el objetivo es detectar si una nueva observación es un valor atípico. En este contexto, un valor atípico también se llama novedad.

El proyecto scikit-learn proporciona un conjunto de herramientas de aprendizaje automático que se pueden utilizar tanto para la detección de novedades como de valores atípicos. Estas herramientas se implementan utilizando algoritmos de aprendizaje no supervisado, lo que significa que aprenden patrones a partir de los datos sin necesidad de ejemplos etiquetados.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Notebook** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos rápidamente el problema para usted.
