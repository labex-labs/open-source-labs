# Resumen

Esta práctica demuestra cómo manejar la precisión de fechas y las épocas en Matplotlib. Podemos establecer la época al valor predeterminado antiguo o al nuevo valor predeterminado utilizando el método `mdates.set_epoch`. Luego, podemos convertir objetos `datetime` o `numpy.datetime64` a fechas de Matplotlib utilizando la función `mdates.date2num`, y dar la vuelta a las fechas utilizando la función `mdates.num2date` para asegurarnos de que la conversión sea exacta. También podemos graficar datos con diferentes épocas para observar las diferencias en la gráfica.
