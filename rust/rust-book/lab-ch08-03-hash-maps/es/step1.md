# Almacenar claves con valores asociados en mapas hash

La última de nuestras colecciones comunes es el _mapa hash_. El tipo `HashMap<K, V>` almacena una asignación de claves de tipo `K` a valores de tipo `V` utilizando una _función hash_, que determina cómo coloca estas claves y valores en la memoria. Muchos lenguajes de programación admiten este tipo de estructura de datos, pero a menudo la llaman de diferentes maneras, como _hash_, _mapa_, _objeto_, _tabla hash_, _diccionario_ o _matriz asociativa_, por nombrar solo algunas.

Los mapas hash son útiles cuando quieres buscar datos no mediante un índice, como se puede hacer con los vectores, sino mediante una clave que puede ser de cualquier tipo. Por ejemplo, en un juego, podrías llevar un registro de la puntuación de cada equipo en un mapa hash en el que cada clave es el nombre de un equipo y los valores son las puntuaciones de cada equipo. Dado el nombre de un equipo, puedes recuperar su puntuación.

Repasaremos la API básica de los mapas hash en esta sección, pero muchas más funcionalidades se encuentran en las funciones definidas en `HashMap<K, V>` por la biblioteca estándar. Como siempre, consulta la documentación de la biblioteca estándar para obtener más información.
