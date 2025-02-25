# Introducción

Este tutorial te guiará sobre cómo dibujar una curva con una banda de error utilizando Python Matplotlib. Una banda de error se utiliza para indicar la incertidumbre de la curva. En este ejemplo, asumimos que el error puede ser dado como un escalar _err_ que describe la incertidumbre perpendicular a la curva en cada punto. Visualizamos este error como una banda coloreada alrededor de la trayectoria utilizando un `.PathPatch`. El parche se crea a partir de dos segmentos de trayectoria _(xp, yp)_ y _(xn, yn)_ que se desplazan por +/- _err_ perpendicular a la curva _(x, y)_.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haz clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tengas que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no puede automatizarse debido a las limitaciones de Jupyter Notebook.

Si tienes problemas durante el aprendizaje, no dudes en preguntar a Labby. Proporciona retroalimentación después de la sesión y resolveremos rápidamente el problema para ti.
