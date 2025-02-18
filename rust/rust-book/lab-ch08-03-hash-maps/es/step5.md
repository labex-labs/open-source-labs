# Actualizar un mapa hash

Aunque el número de pares clave-valor es creciente, cada clave única solo puede tener un valor asociado a la vez (pero no al revés: por ejemplo, tanto el equipo Azul como el equipo Amarillo podrían tener el valor `10` almacenado en el mapa hash `scores`).

Cuando quieres cambiar los datos en un mapa hash, debes decidir cómo manejar el caso en el que una clave ya tiene un valor asignado. Podrías reemplazar el valor antiguo con el nuevo valor, sin tener en cuenta en absoluto el valor antiguo. Podrías mantener el valor antiguo e ignorar el nuevo valor, agregando el nuevo valor solo si la clave _no_ tiene ya un valor. O podrías combinar el valor antiguo y el nuevo valor. ¡Veamos cómo hacer cada una de estas cosas!
