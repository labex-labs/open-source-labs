# Desestructuración de structs

La Lista 18-12 muestra un struct `Point` con dos campos, `x` e `y`, que podemos descomponer usando un patrón con una declaración `let`.

Nombre de archivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    assert_eq!(0, a);
    assert_eq!(7, b);
}
```

Lista 18-12: Desestructuración de los campos de un struct en variables separadas

Este código crea las variables `a` y `b` que coinciden con los valores de los campos `x` e `y` del struct `p`. Este ejemplo muestra que los nombres de las variables en el patrón no tienen que coincidir con los nombres de los campos del struct. Sin embargo, es común hacer coincidir los nombres de las variables con los nombres de los campos para que sea más fácil recordar qué variables provienen de qué campos. Debido a este uso común, y porque escribir `let Point { x: x, y: y } = p;` contiene mucha duplicación, Rust tiene una forma abreviada para los patrones que coinciden con los campos de struct: solo es necesario listar el nombre del campo del struct, y las variables creadas a partir del patrón tendrán los mismos nombres. La Lista 18-13 se comporta de la misma manera que el código de la Lista 18-12, pero las variables creadas en el patrón `let` son `x` e `y` en lugar de `a` y `b`.

Nombre de archivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x, y } = p;
    assert_eq!(0, x);
    assert_eq!(7, y);
}
```

Lista 18-13: Desestructuración de campos de struct usando la forma abreviada de campo de struct

Este código crea las variables `x` e `y` que coinciden con los campos `x` e `y` de la variable `p`. El resultado es que las variables `x` e `y` contienen los valores del struct `p`.

También podemos desestructurar con valores literales como parte del patrón de struct en lugar de crear variables para todos los campos. Hacer esto nos permite probar algunos de los campos para valores particulares mientras creamos variables para desestructurar los otros campos.

En la Lista 18-14, tenemos una expresión `match` que separa los valores de `Point` en tres casos: puntos que se encuentran directamente sobre el eje `x` (lo que es cierto cuando `y = 0`), sobre el eje `y` (`x = 0`) o sobre ninguno de los ejes.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("Sobre el eje x en {x}"),
        Point { x: 0, y } => println!("Sobre el eje y en {y}"),
        Point { x, y } => {
            println!("Sobre ninguno de los ejes: ({x}, {y})");
        }
    }
}
```

Lista 18-14: Desestructuración y coincidencia de valores literales en un patrón

El primer brazo coincidirá con cualquier punto que se encuentre sobre el eje `x` al especificar que el campo `y` coincide si su valor coincide con el literal `0`. El patrón todavía crea una variable `x` que podemos usar en el código de este brazo.

Del mismo modo, el segundo brazo coincide con cualquier punto sobre el eje `y` al especificar que el campo `x` coincide si su valor es `0` y crea una variable `y` para el valor del campo `y`. El tercer brazo no especifica ningún literal, por lo que coincide con cualquier otro `Point` y crea variables para ambos campos `x` e `y`.

En este ejemplo, el valor `p` coincide con el segundo brazo por el hecho de que `x` contiene un `0`, por lo que este código imprimirá `Sobre el eje y en 7`.

Recuerda que una expresión `match` deja de comprobar los brazos una vez que ha encontrado el primer patrón que coincide, por lo que aunque `Point { x: 0, y: 0}` está sobre el eje `x` y el eje `y`, este código solo imprimirá `Sobre el eje x en 0`.
