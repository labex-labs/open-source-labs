# 出力パラメータとして

クロージャを入力パラメータとして使用できるので、クロージャを出力パラメータとして返すこともできるはずです。ただし、匿名クロージャ型は定義上不明なので、返すには `impl Trait` を使用しなければなりません。

クロージャを返すための有効なトレイトは以下の通りです。

- `Fn`
- `FnMut`
- `FnOnce`

これに加えて、`move` キーワードを使用する必要があります。これは、すべてのキャプチャが値によって行われることを示します。これは必要です。なぜなら、関数が終了するとすぐに参照によるキャプチャは破棄され、クロージャ内に無効な参照が残ってしまうからです。

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
