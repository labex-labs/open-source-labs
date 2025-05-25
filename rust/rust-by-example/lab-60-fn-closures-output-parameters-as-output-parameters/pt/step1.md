# Como parâmetros de saída

Closures como parâmetros de entrada são possíveis, então retornar closures como parâmetros de saída também deve ser possível. No entanto, os tipos de closures anônimas são, por definição, desconhecidos, então precisamos usar `impl Trait` para retorná-los.

Os traits válidos para retornar uma closure são:

- `Fn`
- `FnMut`
- `FnOnce`

Além disso, a palavra-chave `move` deve ser usada, o que sinaliza que todas as capturas ocorrem por valor. Isso é necessário porque quaisquer capturas por referência seriam descartadas assim que a função terminasse, deixando referências inválidas na closure.

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
