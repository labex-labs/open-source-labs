# Resumen

En este laboratorio, aprendimos cómo implementar tiempos de espera en Go utilizando canales y `select`. Utilizamos un canal con búfer para evitar fugas de gorutinas en caso de que el canal nunca se lea, y `time.After` para esperar a que se envíe un valor después del tiempo de espera. También utilizamos `select` para continuar con la primera recepción lista.
