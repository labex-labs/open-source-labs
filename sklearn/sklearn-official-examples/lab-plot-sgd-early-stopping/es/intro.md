# Introducción

El Descenso de Gradiente Estocástico es una técnica de optimización popular utilizada para minimizar una función de pérdida. La técnica realiza pasos de descenso de gradiente de manera estocástica, es decir, seleccionando aleatoriamente muestras para cada iteración. El método es eficiente, especialmente para ajustar modelos lineales. Sin embargo, no está garantizada la convergencia en cada iteración, y la función de pérdida no necesariamente disminuye en cada iteración. En este caso, puede ser difícil monitorear la convergencia en la función de pérdida. En este laboratorio, exploraremos la estrategia de parada temprana, que es un enfoque para monitorear la convergencia en una puntuación de validación. Utilizaremos el modelo `SGDClassifier` de la biblioteca scikit-learn y el conjunto de datos MNIST para ilustrar cómo la parada temprana se puede utilizar para lograr una precisión casi igual a la de un modelo construido sin parada temprana, y reducir significativamente el tiempo de entrenamiento.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos rápidamente el problema para usted.
