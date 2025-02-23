# Resumen

En este laboratorio, creó sus primeros contenedores de Ubuntu, Nginx y MongoDB.

Conclusiones Clave

- Los contenedores están compuestos por espacios de nombres de Linux y grupos de control que proporcionan aislamiento de otros contenedores y del host.
- Debido a las propiedades de aislamiento de los contenedores, puede programar muchos contenedores en un solo host sin preocuparse por dependencias en conflicto. Esto facilita la ejecución de múltiples contenedores en un solo host: aprovechando al máximo los recursos asignados a ese host y, en última instancia, ahorrando dinero en los costos del servidor.
- Evite usar contenido no verificado de la Tienda de Docker al desarrollar sus propias imágenes, ya que estas imágenes pueden contener vulnerabilidades de seguridad o incluso software malicioso.
- Los contenedores incluyen todo lo necesario para ejecutar los procesos dentro de ellos, por lo que no es necesario instalar dependencias adicionales directamente en su host.
