# Introducción

Esta práctica proporciona un ejemplo de cómo utilizar scikit-learn para la clasificación de texto mediante aprendizaje fuera de núcleo. El objetivo es aprender a partir de datos que no caben en la memoria principal. Para lograr esto, utilizamos un clasificador en línea que admite el método partial_fit, al que se alimentarán lotes de ejemplos. Para garantizar que el espacio de características permanezca constante con el tiempo, aprovechamos un HashingVectorizer que proyectará cada ejemplo al mismo espacio de características. Esto es especialmente útil en el caso de la clasificación de texto donde pueden aparecer nuevas características (palabras) en cada lote.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje su retroalimentación después de la sesión y resolveremos rápidamente el problema para usted.
