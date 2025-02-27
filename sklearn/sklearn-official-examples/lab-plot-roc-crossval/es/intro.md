# Introducción

En este laboratorio, aprenderemos a estimar y visualizar la varianza de la métrica Receiver Operating Characteristic (ROC) utilizando validación cruzada en Python. Las curvas ROC se utilizan en la clasificación binaria para medir el rendimiento de un modelo al trazar la tasa de verdaderos positivos (TPR) contra la tasa de falsos positivos (FPR). Utilizaremos la biblioteca Scikit-learn para cargar el conjunto de datos iris, crear características ruidosas y clasificar el conjunto de datos con Máquina de Vectores de Soporte (SVM). Luego graficaremos las curvas ROC con validación cruzada y calcularemos el área media debajo de la curva (AUC) para ver la variabilidad de la salida del clasificador cuando el conjunto de entrenamiento se divide en diferentes subconjuntos.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos el problema inmediatamente para usted.
