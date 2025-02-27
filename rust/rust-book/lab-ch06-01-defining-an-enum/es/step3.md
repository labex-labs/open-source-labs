# El enum `Option` y sus ventajas sobre los valores nulos

Esta sección explora un estudio de caso de `Option`, que es otro enum definido por la biblioteca estándar. El tipo `Option` codifica el escenario muy común en el que un valor puede ser algo o puede ser nada.

Por ejemplo, si solicita el primer elemento de una lista que contiene múltiples elementos, obtendrá un valor. Si solicita el primer elemento de una lista vacía, no obtendrá nada. Expresar este concepto en términos del sistema de tipos significa que el compilador puede comprobar si ha manejado todos los casos que debe manejar; esta funcionalidad puede prevenir errores que son extremadamente comunes en otros lenguajes de programación.

El diseño de los lenguajes de programación a menudo se piensa en términos de las características que se incluyen, pero las características que se excluyen también son importantes. Rust no tiene la característica de null que tienen muchos otros lenguajes. _Null_ es un valor que significa que no hay un valor allí. En los lenguajes con null, las variables siempre pueden estar en uno de dos estados: null o no-null.

En su presentación de 2009 "Null References: The Billion Dollar Mistake", Tony Hoare, el inventor de null, dice lo siguiente:

> Lo llamo mi error de mil millones de dólares. En aquel momento, estaba diseñando el primer sistema de tipos integral para referencias en un lenguaje orientado a objetos. Mi objetivo era garantizar que todo uso de referencias fuera absolutamente seguro, con comprobaciones realizadas automáticamente por el compilador. Pero no pude resistir la tentación de incluir una referencia nula, simplemente porque era tan fácil de implementar. Esto ha dado lugar a innumerables errores, vulnerabilidades y errores del sistema, que probablemente han causado mil millones de dólares de dolor y daño en los últimos cuarenta años. El problema con los valores nulos es que si intenta usar un valor nulo como un valor no nulo, obtendrá algún tipo de error. Debido a que esta propiedad de null o no-null es generalizada, es extremadamente fácil cometer este tipo de error.

Sin embargo, el concepto que intenta expresar null todavía es útil: un null es un valor que actualmente es inválido o ausente por alguna razón.

El problema no es realmente el concepto sino la implementación particular. Por lo tanto, Rust no tiene nulls, pero tiene un enum que puede codificar el concepto de que un valor está presente o ausente. Este enum es `Option<T>`, y está definido por la biblioteca estándar de la siguiente manera:

```rust
enum Option<T> {
    None,
    Some(T),
}
```

El enum `Option<T>` es tan útil que incluso está incluido en el preludio; no es necesario traerlo al ámbito explícitamente. Sus variantes también están incluidas en el preludio: se puede usar `Some` y `None` directamente sin el prefijo `Option::`. El enum `Option<T>` todavía es solo un enum regular, y `Some(T)` y `None` todavía son variantes del tipo `Option<T>`.

La sintaxis `<T>` es una característica de Rust que todavía no hemos mencionado. Es un parámetro de tipo genérico, y cubriremos los genéricos en más detalle en el Capítulo 10. Por ahora, todo lo que necesita saber es que `<T>` significa que la variante `Some` del enum `Option` puede contener un dato de cualquier tipo, y que cada tipo concrete que se utiliza en lugar de `T` hace que el tipo `Option<T>` en general sea un tipo diferente. Aquí hay algunos ejemplos de uso de valores `Option` para contener tipos numéricos y tipos de cadena:

```rust
let some_number = Some(5);
let some_char = Some('e');

let absent_number: Option<i32> = None;
```

El tipo de `some_number` es `Option<i32>`. El tipo de `some_char` es `Option<char>`, que es un tipo diferente. Rust puede inferir estos tipos porque hemos especificado un valor dentro de la variante `Some`. Para `absent_number`, Rust requiere que anote el tipo `Option` en general: el compilador no puede inferir el tipo que contendrá la variante `Some` correspondiente solo al ver un valor `None`. Aquí, le decimos a Rust que queremos que `absent_number` sea del tipo `Option<i32>`.

Cuando tenemos un valor `Some`, sabemos que un valor está presente y el valor se encuentra dentro de `Some`. Cuando tenemos un valor `None`, en cierto sentido significa lo mismo que null: no tenemos un valor válido. Entonces, ¿por qué tener `Option<T>` es mejor que tener null?

En resumen, porque `Option<T>` y `T` (donde `T` puede ser cualquier tipo) son tipos diferentes, el compilador no nos permitirá usar un valor `Option<T>` como si fuera definitivamente un valor válido. Por ejemplo, este código no se compilará, porque está intentando sumar un `i8` a un `Option<i8>`:

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

let sum = x + y;
```

Si ejecutamos este código, obtenemos un mensaje de error como este:

```bash
error[E0277]: cannot add `Option<i8>` to `i8`
 --> src/main.rs:5:17
  |
5 |     let sum = x + y;
  |                 ^ no implementation for `i8 + Option<i8>`
  |
  = help: the trait `Add<Option<i8>>` is not implemented for `i8`
```

¡Intenso! En efecto, este mensaje de error significa que Rust no entiende cómo sumar un `i8` y un `Option<i8>`, porque son tipos diferentes. Cuando tenemos un valor de un tipo como `i8` en Rust, el compilador asegurará de que siempre tengamos un valor válido. Podemos continuar con confianza sin tener que comprobar si es null antes de usar ese valor. Solo cuando tenemos un `Option<i8>` (o cualquier tipo de valor con el que estemos trabajando) tenemos que preocuparnos por no tener un valor, y el compilador se asegurará de que manejemos ese caso antes de usar el valor.

En otras palabras, tiene que convertir un `Option<T>` en un `T` antes de poder realizar operaciones de `T` con él. En general, esto ayuda a detectar uno de los problemas más comunes con null: suponer que algo no es null cuando en realidad lo es.

Eliminar el riesgo de suponer incorrectamente un valor no nulo lo ayuda a tener más confianza en su código. Para tener un valor que posiblemente sea null, debe optar explícitamente haciéndolo del tipo `Option<T>`. Luego, cuando use ese valor, se le exige manejar explícitamente el caso en el que el valor sea null. En todas partes donde un valor tiene un tipo que no es `Option<T>`, _puede_ suponer con seguridad que el valor no es null. Esta fue una decisión de diseño deliberada de Rust para limitar la generalización de null y aumentar la seguridad del código de Rust.

Entonces, ¿cómo se obtiene el valor `T` de una variante `Some` cuando se tiene un valor del tipo `Option<T>` para poder usar ese valor? El enum `Option<T>` tiene una gran cantidad de métodos que son útiles en una variedad de situaciones; puede consultarlos en su documentación. Volverse familiarizado con los métodos en `Option<T>` será extremadamente útil en su viaje con Rust.

En general, para usar un valor `Option<T>`, se desea tener código que manejará cada variante. Se desea tener algún código que solo se ejecutará cuando se tiene un valor `Some(T)`, y este código puede usar el `T` interno. Se desea que otro código solo se ejecute si se tiene un valor `None`, y ese código no tiene un valor `T` disponible. La expresión `match` es una construcción de flujo de control que hace exactamente esto cuando se utiliza con enums: ejecutará código diferente dependiendo de qué variante del enum tenga, y ese código puede usar los datos dentro del valor coincidente.
