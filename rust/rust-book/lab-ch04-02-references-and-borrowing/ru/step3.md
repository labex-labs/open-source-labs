# Dangling References

В языках с указателями легко ошибочно создать _промазывающий указатель_ (dangling pointer) - указатель, который ссылается на место в памяти, которое может быть передано кому-то другому - освободив память, сохранив при этом указатель на эту память. В Rust наоборот, компилятор гарантирует, что ссылки никогда не будут промазывающими ссылками: если у вас есть ссылка на какие-то данные, компилятор обеспечит то, что данные не выйдут за пределы области видимости раньше, чем ссылка на эти данные.

Попробуем создать промазывающую ссылку, чтобы увидеть, как Rust предотвращает их с помощью ошибки компиляции:

Filename: `src/main.rs`

```rust
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");

    &s
}
```

Вот ошибка:

```bash
error[E0106]: missing lifetime specifier
 --> src/main.rs:5:16
  |
5 | fn dangle() -> &String {
  |                ^ expected named lifetime parameter
  |
  = help: this function's return type contains a borrowed value,
but there is no value for it to be borrowed from
help: consider using the `'static` lifetime
  |
5 | fn dangle() -> &'static String {
  |                ~~~~~~~~
```

Это сообщение об ошибке ссылается на функцию, которую мы еще не рассматривали: lifetimes. Мы обсудим lifetimes подробно в главе 10. Однако, если проигнорировать части о lifetimes, сообщение содержит ключ к тому, почему этот код является проблемой:

```rust
this function's return type contains a borrowed value, but there
is no value for it to be borrowed from
```

Давайте более внимательно рассмотрим, что именно происходит на каждом этапе нашего кода `dangle`:

    // src/main.rs
    fn dangle() -> &String { // dangle возвращает ссылку на String

        let s = String::from("hello"); // s - это новый String

        &s // мы возвращаем ссылку на String, s
    } // Здесь s выходит из области видимости и уничтожается, поэтому ее память исчезает
      // Опасность!

Поскольку `s` создается внутри `dangle`, когда код `dangle` завершен, `s` будет освобождено. Но мы пытались вернуть ссылку на него. Это означает, что эта ссылка будет ссылаться на недействительный `String`. Это не хорошо! Rust не позволит нам сделать это.

Решением здесь будет возвращение `String` напрямую:

```rust
fn no_dangle() -> String {
    let s = String::from("hello");

    s
}
```

Это работает без каких-либо проблем. Владение передается, и ничего не освобождается.
