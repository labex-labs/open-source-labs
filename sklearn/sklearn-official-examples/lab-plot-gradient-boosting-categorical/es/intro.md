# Introducción

En este laboratorio, usaremos el conjunto de datos de viviendas de Ames para comparar diferentes métodos de manejo de características categóricas en estimadores de Gradient Boosting. El conjunto de datos contiene características numéricas y categóricas, y la variable objetivo es el precio de venta de las casas. Compararemos el rendimiento de cuatro tuberías diferentes:

- Eliminando las características categóricas
- Codificación one-hot de las características categóricas
- Tratando las características categóricas como valores ordinales
- Usando el soporte nativo para características categóricas en el estimador de Gradient Boosting

Evaluaremos las tuberías en términos de sus tiempos de ajuste y rendimientos de predicción usando validación cruzada.

## Consejos sobre la VM

Una vez finalizada la inicialización de la VM, haga clic en la esquina superior izquierda para cambiar a la pestaña **Cuaderno** y acceder a Jupyter Notebook para practicar.

A veces, es posible que tenga que esperar unos segundos a que Jupyter Notebook termine de cargarse. La validación de operaciones no se puede automatizar debido a las limitaciones de Jupyter Notebook.

Si tiene problemas durante el aprendizaje, no dude en preguntar a Labby. Deje comentarios después de la sesión y resolveremos rápidamente el problema para usted.
