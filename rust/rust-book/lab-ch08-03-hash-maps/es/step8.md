# Actualizar un valor basado en el valor antiguo

Otro caso de uso común para los mapas hash es buscar el valor de una clave y luego actualizarlo en función del valor antiguo. Por ejemplo, la Lista 8-25 muestra un código que cuenta cuántas veces aparece cada palabra en un texto. Usamos un mapa hash con las palabras como claves e incrementamos el valor para llevar la cuenta de cuántas veces hemos visto esa palabra. Si es la primera vez que vemos una palabra, primero insertaremos el valor `0`.

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";

let mut map = HashMap::new();

for word in text.split_whitespace() {
    let count = map.entry(word).or_insert(0);
    *count += 1;
}

println!("{:?}", map);
```

Lista 8-25: Contando las ocurrencias de palabras usando un mapa hash que almacena palabras y recuentos

Este código imprimirá `{"world": 2, "hello": 1, "wonderful": 1}`. Puedes ver los mismos pares clave-valor impresos en un orden diferente: recuerda de "Accediendo a valores en un mapa hash" que iterar sobre un mapa hash ocurre en un orden arbitrario.

El método `split_whitespace` devuelve un iterador sobre subsecciones, separadas por espacios en blanco, del valor en `text`. El método `or_insert` devuelve una referencia mutable (`&mut V`) al valor de la clave especificada. Aquí, almacenamos esa referencia mutable en la variable `count`, así que para asignar a ese valor, primero debemos desreferenciar `count` usando el asterisco (`*`). La referencia mutable sale de alcance al final del bucle `for`, así que todos estos cambios son seguros y permitidos por las reglas de préstamo (borrowing rules).
