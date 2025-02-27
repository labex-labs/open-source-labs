# Sintaxis de Métodos

Los _métodos_ son similares a las funciones: los declaramos con la palabra clave `fn` y un nombre, pueden tener parámetros y un valor de retorno, y contienen un código que se ejecuta cuando se llama al método desde otro lugar. A diferencia de las funciones, los métodos se definen en el contexto de un struct (o un enum o un objeto de trato, que cubriremos en los Capítulos 6 y 17, respectivamente), y su primer parámetro siempre es `self`, que representa la instancia del struct en el que se está llamando al método.
