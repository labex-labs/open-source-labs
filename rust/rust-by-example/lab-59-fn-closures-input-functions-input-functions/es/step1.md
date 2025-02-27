# Funciones de entrada

Dado que los closures pueden usarse como argumentos, es posible que te preguntes si lo mismo se puede decir de las funciones. ¡Y, de hecho, sí! Si declaras una función que tome un closure como parámetro, entonces cualquier función que cumpla con el límite de trato de ese closure puede pasarse como parámetro.

```rust
// Define una función que toma un argumento genérico `F`
// acotado por `Fn`, y lo llama
fn call_me<F: Fn()>(f: F) {
    f();
}

// Define una función envolvente que satisface el límite `Fn`
fn function() {
    println!("Soy una función!");
}

fn main() {
    // Define un closure que satisface el límite `Fn`
    let closure = || println!("Soy un closure!");

    call_me(closure);
    call_me(function);
}
```

Como nota adicional, los rasgos `Fn`, `FnMut` y `FnOnce` dictan cómo un closure captura variables del ámbito envolvente.
