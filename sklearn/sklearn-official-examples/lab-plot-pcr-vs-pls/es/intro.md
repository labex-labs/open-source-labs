# Introducción

La Regresión por Componentes Principales (PCR, por sus siglas en inglés) y la Regresión por Mínimos Cuadrados Parciales (PLS, por sus siglas en inglés) son dos métodos utilizados en el análisis de regresión. La PCR implica aplicar el Análisis de Componentes Principales (PCA, por sus siglas en inglés) a los datos de entrenamiento, seguido del entrenamiento de un regresor en las muestras transformadas. La transformación PCA es no supervisada, lo que significa que no se utiliza ninguna información sobre las variables objetivo. Como resultado, la PCR puede funcionar mal en algunos conjuntos de datos donde la variable objetivo está fuertemente correlacionada con direcciones que tienen una baja varianza.

La PLS es tanto un transformador como un regresor, y es bastante similar a la PCR. También aplica una reducción de dimensionalidad a las muestras antes de aplicar un regresor lineal a los datos transformados. La principal diferencia con la PCR es que la transformación PLS es supervisada. Por lo tanto, no sufre del problema mencionado anteriormente.

En este laboratorio, compararemos la PCR y la PLS en un conjunto de datos de ejemplo.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
