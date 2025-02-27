# Ignorar valores en un patrón

Has visto que a veces es útil ignorar valores en un patrón, como en el último brazo de una `match`, para obtener un caso general que en realidad no hace nada pero abarca todos los valores posibles restantes. Hay varias maneras de ignorar valores enteros o partes de valores en un patrón: usando el patrón `_` (que ya has visto), usando el patrón `_` dentro de otro patrón, usando un nombre que empieza con un guion bajo o usando `..` para ignorar las partes restantes de un valor. Vamos a explorar cómo y por qué usar cada uno de estos patrones.
