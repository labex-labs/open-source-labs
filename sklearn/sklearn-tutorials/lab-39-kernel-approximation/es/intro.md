# Introducción

Este tutorial lo guiará a través del proceso de uso de técnicas de aproximación de kernel en scikit-learn.

Los métodos de kernel, como las máquinas de vectores de soporte (SVM), son técnicas poderosas para la clasificación no lineal. Estos métodos se basan en el concepto de una función de kernel que mapea los datos de entrada a un espacio de características de alta dimensión. Sin embargo, trabajar con mapeos de características explícitos puede ser computacionalmente costoso, especialmente para conjuntos de datos grandes. Los métodos de aproximación de kernel proporcionan una solución al generar aproximaciones de baja dimensión del espacio de características de kernel.

En este tutorial, exploraremos varias técnicas de aproximación de kernel disponibles en scikit-learn, incluyendo el método de Nystroem, la aproximación del kernel de función radial básica (RBF), la aproximación del kernel de chi cuadrado aditivo (ACS), la aproximación del kernel de chi cuadrado sesgado (SCS) y la aproximación del kernel polinomial usando Tensor Sketch. Demonstraremos cómo usar estas técnicas y discutiremos sus ventajas y limitaciones.

## Consejos sobre la VM

Una vez que se haya completado la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y lo resolveremos rápidamente para usted.
