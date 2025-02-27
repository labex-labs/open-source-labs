# El tipo nunca que nunca devuelve

Rust tiene un tipo especial llamado `!` que en el vocabulario de la teoría de tipos se conoce como el _tipo vacío_ porque no tiene valores. Prefirimos llamarlo el _tipo nunca_ porque ocupa el lugar del tipo de retorno cuando una función nunca devuelve. Aquí hay un ejemplo:

```rust
fn bar() ->! {
    --snip--
}
```

Este código se lee como "la función `bar` devuelve nunca". Las funciones que devuelven nunca se llaman _funciones divergentes_. No podemos crear valores del tipo `!`, por lo que `bar` nunca puede devolver.

Pero ¿qué utilidad tiene un tipo para el que nunca se pueden crear valores? Recuerda el código de la Lista 2-5, parte del juego de adivinar el número; hemos reproducido un poco de él aquí en la Lista 19-26.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Lista 19-26: Un `match` con un brazo que termina en `continue`

En aquel momento, saltamos algunos detalles de este código. En "La construcción de flujo de control match", discutimos que los brazos de `match` deben todos devolver el mismo tipo. Entonces, por ejemplo, el siguiente código no funciona:

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

El tipo de `guess` en este código tendría que ser un entero _y_ una cadena, y Rust requiere que `guess` tenga solo un tipo. Entonces, ¿qué devuelve `continue`? ¿Cómo nos permitieron devolver un `u32` desde un brazo y tener otro brazo que termina con `continue` en la Lista 19-26?

Como probablemente hayas adivinado, `continue` tiene un valor de `!`. Es decir, cuando Rust calcula el tipo de `guess`, mira ambos brazos del `match`, el primero con un valor de `u32` y el segundo con un valor de `!`. Debido a que `!` nunca puede tener un valor, Rust decide que el tipo de `guess` es `u32`.

La forma formal de describir este comportamiento es que las expresiones de tipo `!` se pueden forzar a cualquier otro tipo. Estamos permitidos terminar este brazo de `match` con `continue` porque `continue` no devuelve un valor; en cambio, mueve el control de vuelta al principio del bucle, por lo que en el caso `Err`, nunca le asignamos un valor a `guess`.

El tipo nunca también es útil con la macro `panic!`. Recuerda la función `unwrap` que llamamos en valores de `Option<T>` para producir un valor o generar un error con esta definición:

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "llamado `Option::unwrap()` en un valor `None`"
            ),
        }
    }
}
```

En este código, sucede lo mismo que en el `match` de la Lista 19-26: Rust ve que `val` tiene el tipo `T` y `panic!` tiene el tipo `!`, por lo que el resultado de la expresión `match` en general es `T`. Este código funciona porque `panic!` no produce un valor; termina el programa. En el caso `None`, no devolveremos un valor desde `unwrap`, por lo que este código es válido.

Una última expresión que tiene el tipo `!` es un `loop`:

    print!("por siempre ");

    loop {
        print!("y para siempre ");
    }

Aquí, el bucle nunca termina, por lo que `!` es el valor de la expresión. Sin embargo, esto no sería cierto si incluyéramos un `break`, porque el bucle terminaría cuando llegara al `break`.
