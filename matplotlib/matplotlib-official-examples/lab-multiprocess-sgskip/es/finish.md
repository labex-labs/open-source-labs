# Resumen

En este laboratorio, aprendimos cómo usar la biblioteca `multiprocessing` y Matplotlib para graficar datos generados por un proceso separado. Creamos dos clases: `ProcessPlotter` y `NBPlot`, para manejar la graficación y la generación de datos, respectivamente. La clase `NBPlot` generó datos aleatorios y los envió a la clase `ProcessPlotter` a través de un tubo (pipe), que luego graficó los datos en tiempo real.
