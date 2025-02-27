# Als Ausgabeparameter

Es ist möglich, Closures als Eingabeparameter zu verwenden, daher sollte es auch möglich sein, Closures als Ausgabeparameter zurückzugeben. Da anonyme Closure-Typen per Definition unbekannt sind, müssen wir `impl Trait` verwenden, um sie zurückzugeben.

Die gültigen Traits für das Zurückgeben eines Closures sind:

- `Fn`
- `FnMut`
- `FnOnce`

Darüber hinaus muss das `move`-Schlüsselwort verwendet werden, was signalisiert, dass alle Captures per Wert erfolgen. Dies ist erforderlich, da alle Captures per Referenz sofort fallen würden, sobald die Funktion beendet wird, was zu ungültigen Referenzen im Closure führt.

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
