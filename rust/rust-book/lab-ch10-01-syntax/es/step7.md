# Rendimiento del código que utiliza genéricos

Es posible que te estés preguntando si hay un costo de tiempo de ejecución al usar parámetros de tipo genérico. La buena noticia es que usar tipos genéricos no hará que tu programa se ejecute más lentamente que con tipos concretos.

Rust logra esto mediante la monomorfización del código que utiliza genéricos en tiempo de compilación. La _monomorfización_ es el proceso de convertir el código genérico en código específico rellenando los tipos concretos que se usan durante la compilación. En este proceso, el compilador hace lo contrario de los pasos que usamos para crear la función genérica en la Lista 10-5: el compilador examina todos los lugares donde se llama al código genérico y genera código para los tipos concretos con los que se llama al código genérico.

Veamos cómo funciona esto usando el enum genérico `Option<T>` de la biblioteca estándar:

```rust
let integer = Some(5);
let float = Some(5.0);
```

Cuando Rust compila este código, realiza la monomorfización. Durante ese proceso, el compilador lee los valores que se han usado en las instancias de `Option<T>` e identifica dos tipos de `Option<T>`: uno es `i32` y el otro es `f64`. En consecuencia, expande la definición genérica de `Option<T>` en dos definiciones especializadas para `i32` y `f64`, reemplazando así la definición genérica con las específicas.

La versión monomorfizada del código se ve similar a la siguiente (el compilador usa nombres diferentes a los que estamos usando aquí para fines de ilustración):

Nombre de archivo: `src/main.rs`

```rust
enum Option_i32 {
    Some(i32),
    None,
}

enum Option_f64 {
    Some(f64),
    None,
}

fn main() {
    let integer = Option_i32::Some(5);
    let float = Option_f64::Some(5.0);
}
```

El genérico `Option<T>` se reemplaza con las definiciones específicas creadas por el compilador. Debido a que Rust compila el código genérico en código que especifica el tipo en cada instancia, no pagamos ningún costo de tiempo de ejecución por usar genéricos. Cuando el código se ejecuta, funciona exactamente igual que si hubiéramos duplicado cada definición a mano. El proceso de monomorfización hace que los genéricos de Rust sean extremadamente eficientes en tiempo de ejecución.
