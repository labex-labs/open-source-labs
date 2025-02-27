# Anonimidad de tipos

Las closures capturan de manera concisa variables de los ámbitos envolventes. ¿Esto tiene alguna consecuencia? Seguro que sí. Observe cómo el uso de una closure como parámetro de función requiere \[genéricos\], lo cual es necesario debido a cómo se definen:

```rust
// `F` debe ser genérico.
fn apply<F>(f: F) where
    F: FnOnce() {
    f();
}
```

Cuando se define una closure, el compilador crea implícitamente una nueva estructura anónima para almacenar las variables capturadas dentro, mientras implementa la funcionalidad a través de uno de los `traits`: `Fn`, `FnMut` o `FnOnce` para este tipo desconocido. Este tipo se asigna a la variable que se almacena hasta la llamada.

Dado que este nuevo tipo es de tipo desconocido, cualquier uso en una función requerirá genéricos. Sin embargo, un parámetro de tipo sin límite `<T>` todavía sería ambiguo y no se permitiría. Por lo tanto, limitar por uno de los `traits`: `Fn`, `FnMut` o `FnOnce` (que implementa) es suficiente para especificar su tipo.

```rust
// `F` debe implementar `Fn` para una closure que no
// toma entradas y no devuelve nada - exactamente lo que se
// requiere para `print`.
fn apply<F>(f: F) where
    F: Fn() {
    f();
}

fn main() {
    let x = 7;

    // Captura `x` en un tipo anónimo e implementa
    // `Fn` para él. Guárdalo en `print`.
    let print = || println!("{}", x);

    apply(print);
}
```
