# Resumen

Este desafío demostró cómo implementar un grupo de trabajadores utilizando goroutines y canales. El grupo de trabajadores recibe trabajos a través del canal `jobs` y envía los resultados correspondientes a través del canal `results`. Cada trabajador duerme durante un segundo por trabajo para simular una tarea costosa.
