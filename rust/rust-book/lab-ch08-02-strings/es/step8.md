# Representación interna

Una `String` es una envolvente sobre un `Vec<u8>`. Echemos un vistazo a algunos de nuestros ejemplos de cadenas codificadas correctamente en UTF-8 de la Lista 8-14. Primero, este:

```rust
let hello = String::from("Hola");
```

En este caso, `len` será `4`, lo que significa que el vector que almacena la cadena `"Hola"` tiene 4 bytes de longitud. Cada una de estas letras ocupa un byte cuando se codifica en UTF-8. La siguiente línea, sin embargo, puede sorprenderte (ten en cuenta que esta cadena empieza con la letra cyrílica mayúscula _Ze_, no el número árabe 3):

```rust
let hello = String::from("Здравствуйте");
```

Si te preguntasen cuánto es la longitud de la cadena, es posible que dijeras 12. De hecho, la respuesta de Rust es 24: ese es el número de bytes que se necesitan para codificar "Здравствуйте" en UTF-8, porque cada valor escalar Unicode en esa cadena ocupa 2 bytes de almacenamiento. Por lo tanto, un índice en los bytes de la cadena no siempre se correlacionará con un valor escalar Unicode válido. Para demostrarlo, considera este código de Rust no válido:

```rust
let hello = "Здравствуйте";
let answer = &hello[0];
```

Ya sabes que `answer` no será `З`, la primera letra. Cuando se codifica en UTF-8, el primer byte de `З` es `208` y el segundo es `151`, así que parece que `answer` en realidad debería ser `208`, pero `208` no es un carácter válido por sí solo. Devolver `208` probablemente no sea lo que un usuario querría si pidiera la primera letra de esta cadena; sin embargo, ese es el único dato que Rust tiene en el índice de byte 0. Generalmente, los usuarios no quieren que se les devuelva el valor del byte, incluso si la cadena contiene solo letras latinas: si `&"hello"[0]` fuera código válido que devolviera el valor del byte, devolvería `104`, no `h`.

La respuesta, entonces, es que para evitar devolver un valor inesperado y causar errores que quizás no se descubran inmediatamente, Rust no compila este código en absoluto y evita los malentendidos al principio del proceso de desarrollo.
