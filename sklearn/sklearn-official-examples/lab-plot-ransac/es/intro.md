# Introducción

En este laboratorio, demostraremos cómo ajustar robustamente un modelo lineal a datos defectuosos utilizando el algoritmo RANSAC en scikit-learn. El regresor lineal ordinario es sensible a los valores atípicos, y la línea ajustada puede desviarse fácilmente de la verdadera relación subyacente de los datos. El regresor RANSAC automaticamente divide los datos en valores internos y valores atípicos, y la línea ajustada se determina solo por los valores internos identificados. Utilizaremos el conjunto de datos make_regression de scikit-learn para generar datos aleatorios con valores atípicos, y luego ajustaremos tanto un modelo lineal como un regresor RANSAC a los datos.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
