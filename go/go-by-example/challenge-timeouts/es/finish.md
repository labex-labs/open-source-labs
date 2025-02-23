# Resumen

En este desafío, aprendimos cómo implementar timeouts en Go utilizando canales y `select`. Utilizamos un canal con búfer para evitar fugas de goroutine en caso de que el canal nunca sea leído, y `time.After` para esperar a que se envíe un valor después del timeout. También utilizamos `select` para continuar con la primera recepción lista.
