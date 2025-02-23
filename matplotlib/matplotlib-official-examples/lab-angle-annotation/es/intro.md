# Introducción

En este tutorial, aprenderá a crear una etiqueta de ángulo invariante a la escala utilizando Matplotlib. La anotación de ángulos se utiliza a menudo para marcar los ángulos entre líneas o dentro de formas con un arco circular. Si bien Matplotlib proporciona un `~.patches.Arc`, un problema inherente al usarlo directamente para este propósito es que un arco circular en el espacio de datos no necesariamente es circular en el espacio de visualización. Además, el radio del arco a menudo se define mejor en un sistema de coordenadas que es independiente de las coordenadas de datos reales - al menos si desea poder hacer un zoom libremente en su gráfico sin que la anotación crezca hasta el infinito. Esto requiere una solución donde el centro del arco se defina en el espacio de datos, pero su radio en una unidad física como puntos o píxeles, o como una proporción de la dimensión de los Ejes.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
