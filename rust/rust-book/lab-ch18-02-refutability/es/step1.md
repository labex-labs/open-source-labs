# Refutabilidad: ¿Es posible que un patrón no coincida?

Los patrones pueden ser de dos tipos: refutables e irrefutables. Los patrones que coincidirán con cualquier valor posible que se les pase son _irrefutables_. Un ejemplo sería `x` en la declaración `let x = 5;` porque `x` coincide con cualquier cosa y, por lo tanto, no puede fallar en la coincidencia. Los patrones que pueden fallar en la coincidencia para algunos valores posibles son _refutables_. Un ejemplo sería `Some(x)` en la expresión `if let Some(x) = a_value` porque si el valor en la variable `a_value` es `None` en lugar de `Some`, el patrón `Some(x)` no coincidirá.

Los parámetros de función, las declaraciones `let` y los bucles `for` solo pueden aceptar patrones irrefutables porque el programa no puede hacer nada significativo cuando los valores no coinciden. Las expresiones `if let` y `while let` aceptan patrones refutables e irrefutables, pero el compilador advierte sobre los patrones irrefutables porque, por definición, están destinados a manejar posibles errores: la funcionalidad de una condición está en su capacidad de comportarse de manera diferente dependiendo de si tiene éxito o fracaso.

En general, no deberías preocuparte por la distinción entre patrones refutables e irrefutables; sin embargo, es necesario que estés familiarizado con el concepto de refutabilidad para que puedas responder cuando lo veas en un mensaje de error. En esos casos, tendrás que cambiar ya sea el patrón o la construcción en la que estás usando el patrón, dependiendo del comportamiento deseado del código.

Veamos un ejemplo de lo que sucede cuando intentamos usar un patrón refutable donde Rust requiere un patrón irrefutable y viceversa. La Lista 18-8 muestra una declaración `let`, pero para el patrón, hemos especificado `Some(x)`, un patrón refutable. Como cabría esperar, este código no se compilará.

```rust
let Some(x) = some_option_value;
```

Lista 18-8: Intentando usar un patrón refutable con `let`

Si `some_option_value` fuera un valor `None`, no coincidiría con el patrón `Some(x)`, lo que significa que el patrón es refutable. Sin embargo, la declaración `let` solo puede aceptar un patrón irrefutable porque no hay nada válido que el código pueda hacer con un valor `None`. En tiempo de compilación, Rust se quejará de que hemos intentado usar un patrón refutable donde se requiere un patrón irrefutable:

```bash
error[E0005]: refutable pattern in local binding: `None` not covered
   --> src/main.rs:3:9
    |
3   |     let Some(x) = some_option_value;
    |         ^^^^^^^ pattern `None` not covered
    |
    = note: `let` bindings require an "irrefutable pattern", like a `struct` or
an `enum` with only one variant
    = note: for more information, visit
https://doc.rust-lang.org/book/ch18-02-refutability.html
    = note: the matched value is of type `Option<i32>`
help: you might want to use `if let` to ignore the variant that isn't matched
    |
3   |     let x = if let Some(x) = some_option_value { x } else { todo!() };
    |     ++++++++++                                 ++++++++++++++++++++++
```

Debido a que no cubrimos (y no podíamos cubrir!) todos los valores válidos con el patrón `Some(x)`, Rust correctamente produce un error del compilador.

Si tenemos un patrón refutable donde se necesita un patrón irrefutable, podemos corregirlo cambiando el código que usa el patrón: en lugar de usar `let`, podemos usar `if let`. Entonces, si el patrón no coincide, el código simplemente omitirá el código entre llaves, lo que le da una forma de continuar de manera válida. La Lista 18-9 muestra cómo corregir el código de la Lista 18-8.

    if let Some(x) = some_option_value {
        println!("{x}");
    }

Lista 18-9: Usando `if let` y un bloque con patrones refutables en lugar de `let`

¡Le hemos dado una salida al código! Este código es perfectamente válido, aunque significa que no podemos usar un patrón irrefutable sin recibir un error. Si le damos a `if let` un patrón que siempre coincidirá, como `x`, como se muestra en la Lista 18-10, el compilador emitirá una advertencia.

    if let x = 5 {
        println!("{x}");
    };

Lista 18-10: Intentando usar un patrón irrefutable con `if let`

Rust se queja de que no tiene sentido usar `if let` con un patrón irrefutable:

    warning: irrefutable `if let` pattern
     --> src/main.rs:2:8
      |
    2 |     if let x = 5 {
      |        ^^^^^^^^^
      |
      = note: `#[warn(irrefutable_let_patterns)]` on by default
      = note: this pattern will always match, so the `if let` is
    useless
      = help: consider replacing the `if let` with a `let`

Por esta razón, los brazos de coincidencia deben usar patrones refutables, excepto el último brazo, que debe coincidir con cualquier valor restante con un patrón irrefutable. Rust nos permite usar un patrón irrefutable en un `match` con solo un brazo, pero esta sintaxis no es particularmente útil y podría reemplazarse con una declaración `let` más simple.

Ahora que sabes dónde usar patrones y la diferencia entre patrones refutables e irrefutables, cubramos toda la sintaxis que podemos usar para crear patrones.
