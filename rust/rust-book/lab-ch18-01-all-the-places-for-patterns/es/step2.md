# Brasos de `match`

Como se discutió en el Capítulo 6, usamos patrones en los brazos de las expresiones `match`. Formalmente, las expresiones `match` se definen como la palabra clave `match`, un valor sobre el que se hará la coincidencia, y uno o más brazos de coincidencia que constan de un patrón y una expresión que se ejecutará si el valor coincide con el patrón de ese brazo, como esto:

    match VALOR {
        PATRÓN => EXPRESIÓN,
        PATRÓN => EXPRESIÓN,
        PATRÓN => EXPRESIÓN,
    }

Por ejemplo, aquí está la expresión `match` del Listado 6-5 que coincide con un valor `Option<i32>` en la variable `x`:

    match x {
        None => None,
        Some(i) => Some(i + 1),
    }

Los patrones en esta expresión `match` son `None` y `Some(i)` a la izquierda de cada flecha.

Un requisito para las expresiones `match` es que deben ser _exhaustivas_ en el sentido de que se deben considerar todas las posibilidades para el valor en la expresión `match`. Una forma de asegurarse de haber cubierto todas las posibilidades es tener un patrón general para el último brazo: por ejemplo, un nombre de variable que coincida con cualquier valor nunca fallará y, por lo tanto, cubrirá todos los casos restantes.

El patrón particular `_` coincidirá con cualquier cosa, pero nunca se enlazará a una variable, por lo que a menudo se usa en el último brazo de coincidencia. El patrón `_` puede ser útil cuando se desea ignorar cualquier valor no especificado, por ejemplo. Cubriremos el patrón `_` con más detalle en "Ignorando valores en un patrón".
