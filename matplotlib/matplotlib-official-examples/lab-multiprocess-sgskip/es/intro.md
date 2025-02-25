# Introducción

En este laboratorio, aprenderá a usar la biblioteca multiprocessing y Matplotlib para graficar datos generados por un proceso separado. Crearemos dos clases: `ProcessPlotter` y `NBPlot`, para manejar la graficación y la generación de datos, respectivamente. La clase `NBPlot` generará datos aleatorios y los enviará a la clase `ProcessPlotter` a través de un tubo (pipe), que luego graficará los datos en tiempo real.

## Consejos sobre la VM

Una vez que se haya iniciado la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Notebook** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar algunos segundos a que Jupyter Notebook termine de cargar. La validación de las operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje sus comentarios después de la sesión y lo resolveremos rápidamente para usted.
