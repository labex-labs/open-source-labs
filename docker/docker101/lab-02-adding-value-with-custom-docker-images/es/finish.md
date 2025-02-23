# Resumen

En este laboratorio, comenzaste a agregar valor creando tus propios contenedores de Docker personalizados.

Conclusiones clave:

- El Dockerfile es cómo creas compilaciones reproducibles para tu aplicación y cómo integras tu aplicación con Docker en la canalización de CI/CD.
- Las imágenes de Docker pueden estar disponibles en todos tus entornos a través de un registro central. Docker Hub es un ejemplo de registro, pero puedes desplegar tu propio registro en servidores que controlas.
- Las imágenes de Docker contienen todas las dependencias que necesita para ejecutar una aplicación dentro de la imagen. Esto es útil porque ya no tenemos que preocuparnos por la deriva del entorno (diferencias de versión) cuando dependemos de dependencias que se instalan en cada entorno al que desplegamos.
- Docker utiliza el sistema de archivos union y "copiar al escribir" para reutilizar capas de imágenes. Esto reduce la huella de almacenamiento de las imágenes y aumenta significativamente el rendimiento al iniciar contenedores.
- Las capas de imágenes se almacenan en caché por el sistema de compilación y subida de Docker. No es necesario reconstruir o volver a subir capas de imágenes que ya están presentes en el sistema deseado.
- Cada línea en un Dockerfile crea una nueva capa, y debido a la memoria caché de capas, las líneas que cambian con más frecuencia (por ejemplo, agregar código fuente a una imagen) deben estar listadas cerca del final del archivo.
