# El tipo String

Para ilustrar las reglas de propiedad, necesitamos un tipo de datos más complejo que los que cubrimos en "Tipos de datos". Los tipos cubiertos anteriormente son de tamaño conocido, pueden almacenarse en la pila y desapilarse de la pila cuando su ámbito finaliza, y pueden copiarse rápidamente y sin complejidad para crear una nueva instancia independiente si otra parte del código necesita usar el mismo valor en un ámbito diferente. Pero queremos ver datos que se almacenan en el montón y explorar cómo Rust sabe cuándo limpiar esos datos, y el tipo `String` es un gran ejemplo.

Nos concentraremos en las partes de `String` que se relacionan con la propiedad. Estos aspectos también se aplican a otros tipos de datos complejos, ya sea que estén proporcionados por la biblioteca estándar o creados por ti. Discutiremos `String` con más detalle en el Capítulo 8.

Ya hemos visto literales de cadena, donde un valor de cadena está codificado en nuestro programa. Los literales de cadena son convenientes, pero no son adecuados para todas las situaciones en las que podamos querer usar texto. Una razón es que son inmutables. Otra es que no todos los valores de cadena pueden conocerse cuando escribimos nuestro código: por ejemplo, ¿qué pasa si queremos tomar la entrada del usuario y almacenarla? Para estas situaciones, Rust tiene un segundo tipo de cadena, `String`. Este tipo gestiona datos asignados en el montón y, por lo tanto, es capaz de almacenar una cantidad de texto que es desconocida para nosotros en tiempo de compilación. Puedes crear un `String` a partir de un literal de cadena usando la función `from`, así:

```rust
let s = String::from("hello");
```

El operador de dos puntos `::` nos permite colocar este particular función `from` dentro del espacio de nombres del tipo `String` en lugar de usar algún tipo de nombre como `string_from`. Discutiremos esta sintaxis más en "Sintaxis de métodos", y cuando hablamos sobre el espacio de nombres con módulos en "Rutas para referirse a un elemento en el árbol de módulos".

Este tipo de cadena _puede_ ser mutada:

```rust
let mut s = String::from("hello");

s.push_str(", world!"); // push_str() agrega un literal a una String

println!("{s}"); // Esto imprimirá `hello, world!`
```

Entonces, ¿cuál es la diferencia aquí? ¿Por qué `String` puede ser mutado pero los literales no? La diferencia está en cómo estos dos tipos manejan la memoria.
