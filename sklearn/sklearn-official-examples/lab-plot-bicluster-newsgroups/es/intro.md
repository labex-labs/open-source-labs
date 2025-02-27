# Introducción

En este laboratorio, usaremos el algoritmo de co-agrupamiento espectral en el conjunto de datos de veinte grupos de noticias para agrupar bicuadrados los documentos. El conjunto de datos tiene 20 categorías de documentos y excluiremos la categoría "comp.os.ms-windows.misc" ya que contiene publicaciones sin datos. Las publicaciones vectorizadas TF-IDF forman una matriz de frecuencia de palabras que luego se agrupan bicuadrados utilizando el algoritmo de co-agrupamiento espectral de Dhillon. Los co-agrupamientos de documentos-palabras resultantes indican subconjuntos de palabras usadas con más frecuencia en esos subconjuntos de documentos. También agruparemos los documentos utilizando MiniBatchKMeans para comparación.

## Consejos sobre la VM

Después de que se inicie la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** para acceder a Jupyter Notebook y practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos rápidamente el problema para usted.
