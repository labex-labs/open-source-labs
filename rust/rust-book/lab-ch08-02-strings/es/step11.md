# Métodos para iterar sobre cadenas

La mejor manera de operar sobre partes de cadenas es ser explícito sobre si deseas caracteres o bytes. Para valores escalares Unicode individuales, utiliza el método `chars`. Llamar a `chars` en "Зд" separa y devuelve dos valores de tipo `char`, y puedes iterar sobre el resultado para acceder a cada elemento:

    for c in "Зд".chars() {
        println!("{c}");
    }

Este código imprimirá lo siguiente:

```rust
З
д
```

En alternativa, el método `bytes` devuelve cada byte crudo, lo que puede ser adecuado para tu dominio:

    for b in "Зд".bytes() {
        println!("{b}");
    }

Este código imprimirá los cuatro bytes que forman esta cadena:

    208
    151
    208
    180

Pero asegúrate de recordar que los valores escalares Unicode válidos pueden estar formados por más de un byte.

Obtener clusters de grafemas de cadenas, como con el alfabeto devanagari, es complejo, por lo que esta funcionalidad no está disponible en la biblioteca estándar. Hay cajas disponibles en *https://crates.io* si esta es la funcionalidad que necesitas.
