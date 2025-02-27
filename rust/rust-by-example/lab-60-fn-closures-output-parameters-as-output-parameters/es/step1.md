# Como parámetros de salida

Es posible utilizar closures como parámetros de entrada, por lo que también debería ser posible devolver closures como parámetros de salida. Sin embargo, los tipos de closures anónimos son, por definición, desconocidos, por lo que tenemos que utilizar `impl Trait` para devolverlos.

Los traits válidos para devolver una closure son:

- `Fn`
- `FnMut`
- `FnOnce`

Además de esto, se debe utilizar la palabra clave `move`, lo que indica que todas las capturas se realizan por valor. Esto es necesario porque cualquier captura por referencia se perdería tan pronto como la función saliera, dejando referencias inválidas en la closure.

```rust
fn create_fn() -> impl Fn() {
    let text = "Fn".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnmut() -> impl FnMut() {
    let text = "FnMut".to_owned();

    move || println!("This is a: {}", text)
}

fn create_fnonce() -> impl FnOnce() {
    let text = "FnOnce".to_owned();

    move || println!("This is a: {}", text)
}

fn main() {
    let fn_plain = create_fn();
    let mut fn_mut = create_fnmut();
    let fn_once = create_fnonce();

    fn_plain();
    fn_mut();
    fn_once();
}
```
