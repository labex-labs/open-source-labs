# Como parámetros de entrada

Si bien Rust elige cómo capturar variables en la mayoría de los casos sin necesidad de anotación de tipo, esta ambigüedad no está permitida al escribir funciones. Cuando se toma una clausura como parámetro de entrada, el tipo completo de la clausura debe ser anotado utilizando uno de varios `trait`, y se determinan por lo que hace la clausura con el valor capturado. En orden decreciente de restricción, son:

- `Fn`: la clausura utiliza el valor capturado por referencia (`&T`)
- `FnMut`: la clausura utiliza el valor capturado por referencia mutable (`&mut T`)
- `FnOnce`: la clausura utiliza el valor capturado por valor (`T`)

En una base variable por variable, el compilador capturará las variables de la manera menos restrictiva posible.

Por ejemplo, considere un parámetro anotado como `FnOnce`. Esto especifica que la clausura _puede_ capturar por `&T`, `&mut T` o `T`, pero el compilador finalmente elegirá basado en cómo se utilizan las variables capturadas en la clausura.

Esto se debe a que si es posible hacer un movimiento, entonces cualquier tipo de préstamo también debería ser posible. Tenga en cuenta que lo contrario no es cierto. Si el parámetro está anotado como `Fn`, entonces no está permitido capturar variables por `&mut T` o `T`. Sin embargo, `&T` está permitido.

En el siguiente ejemplo, intente intercambiar el uso de `Fn`, `FnMut` y `FnOnce` para ver qué sucede:

```rust
// Una función que toma una clausura como argumento y la llama.
// <F> denota que F es un "parámetro de tipo genérico"
fn apply<F>(f: F) where
    // La clausura no toma entrada y no devuelve nada.
    F: FnOnce() {
    // ^ TODO: Intente cambiar esto a `Fn` o `FnMut`.

    f();
}

// Una función que toma una clausura y devuelve un `i32`.
fn apply_to_3<F>(f: F) -> i32 where
    // La clausura toma un `i32` y devuelve un `i32`.
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // Un tipo no copiable.
    // `to_owned` crea datos con propiedad a partir de uno prestado
    let mut farewell = "goodbye".to_owned();

    // Capture 2 variables: `greeting` por referencia y
    // `farewell` por valor.
    let diary = || {
        // `greeting` es por referencia: requiere `Fn`.
        println!("I said {}.", greeting);

        // La mutación fuerza a que `farewell` sea capturado por
        // referencia mutable. Ahora requiere `FnMut`.
        farewell.push_str("!!!");
        println!("Then I screamed {}.", farewell);
        println!("Now I can sleep. zzzzz");

        // Llamar manualmente a drop fuerza a que `farewell` sea
        // capturado por valor. Ahora requiere `FnOnce`.
        mem::drop(farewell);
    };

    // Llame a la función que aplica la clausura.
    apply(diary);

    // `double` satisface el límite de `trait` de `apply_to_3`
    let double = |x| 2 * x;

    println!("3 doubled: {}", apply_to_3(double));
}
```
