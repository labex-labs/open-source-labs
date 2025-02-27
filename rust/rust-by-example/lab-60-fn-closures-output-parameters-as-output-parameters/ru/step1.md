# В качестве выходных параметров

Так как замыкания могут быть использованы в качестве входных параметров, то возвращать их в качестве выходных параметров также должно быть возможно. Однако анонимные типы замыканий, по определению, неизвестны, поэтому мы должны использовать `impl Trait` для их возврата.

Допустимые трейты для возврата замыкания:

- `Fn`
- `FnMut`
- `FnOnce`

Кроме этого, необходимо использовать ключевое слово `move`, которое сигнализирует, что все захватываются по значению. Это необходимо, потому что любые захваты по ссылке будут уничтожены сразу после выхода из функции, оставляя в замыкании недействительные ссылки.

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
