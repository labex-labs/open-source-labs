# Introducción

En este laboratorio, aprenderemos cómo transformar una señal como una combinación esparsa de ondas de Ricker utilizando métodos de codificación esparsa. El Ricker (también conocido como sombrero mexicano o la segunda derivada de una función Gaussiana) no es un kernel particularmente bueno para representar señales piecewise constantes como esta. Por lo tanto, se puede ver cuánto importa agregar átomos de diferentes anchos y, por lo tanto, se justifica aprender el diccionario para ajustarse mejor al tipo de señales que se tienen.

Visualizaremos diferentes métodos de codificación esparsa utilizando el estimador `SparseCoder`. El diccionario más rico de la derecha no es más grande en tamaño, se realiza una submuestreo más agresivo para mantenerse en el mismo orden de magnitud.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos para que Jupyter Notebook termine de cargarse. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos el problema inmediatamente para usted.
