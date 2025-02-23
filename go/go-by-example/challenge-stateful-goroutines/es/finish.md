# Resumen

Este desafío demostró cómo utilizar canales y gorutinas para sincronizar el acceso a un estado compartido. Al tener una sola gorutina que posea el estado y utilizar canales para emitir solicitudes de lectura y escritura, podemos evitar condiciones de carrera y corrupción de datos.
