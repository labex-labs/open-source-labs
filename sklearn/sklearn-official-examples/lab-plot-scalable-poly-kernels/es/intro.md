# Introducción

Esta práctica demostrará cómo utilizar la aproximación del kernel polinomial en scikit-learn para generar eficientemente aproximaciones del espacio de características del kernel polinomial. Esto se utiliza para entrenar clasificadores lineales que se aproximan a la precisión de los clasificadores kernelizados. Utilizaremos el conjunto de datos Covtype, que contiene 581.012 muestras con 54 características cada una, distribuidas entre 6 clases. El objetivo de este conjunto de datos es predecir el tipo de cobertura forestal a partir solo de variables cartográficas (sin datos de teleobservación). Después de cargarlo, lo transformamos en un problema de clasificación binaria para coincidir con la versión del conjunto de datos en la página web de LIBSVM, que fue la utilizada en el artículo original.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Notebook** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos rápidamente el problema para usted.
