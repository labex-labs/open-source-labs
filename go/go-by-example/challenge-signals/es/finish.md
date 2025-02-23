# Resumen

El desafío de Señales demuestra cómo manejar señales Unix en programas Go utilizando canales. Al crear un canal bufferizado para recibir notificaciones de `os.Signal` y registrar el canal para recibir notificaciones de señales específicas utilizando `signal.Notify`, podemos manejar las señales de manera adecuada y salir del programa cuando se recibe la señal esperada.
