# Создание второго пакета в рабочем пространстве

Далее, давайте создадим еще один пакет-член в рабочем пространстве и назовем его `add_one`. Измените верхнеуровневый `Cargo.toml`, чтобы указать путь к _add_one_ в списке `members`:

Имя файла: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

Затем сгенерируйте новый библиотечный ящик под названием `add_one`:

```bash
$ cargo new add_one --lib
Created library $(add_one) package
```

Теперь в директории `add` должны быть следующие директории и файлы:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

В файле `add_one/src/lib.rs` давайте добавим функцию `add_one`:

Имя файла: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Теперь в пакете `adder` с нашим бинарным файлом можно сделать его зависящим от пакета `add_one`, в котором находится наша библиотека. Во - первых, нам нужно добавить зависимость по пути на `add_one` в _adder/Cargo.toml_:

Имя файла: `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo не предполагает, что ящики в рабочем пространстве будут зависеть друг от друга, поэтому мы должны явно указывать зависимости.

Далее, давайте используем функцию `add_one` (из ящика `add_one`) в ящике `adder`. Откройте файл `adder/src/main.rs` и добавьте строку `use` в начале, чтобы включить новый библиотечный ящик `add_one` в область видимости. Затем измените функцию `main`, чтобы вызвать функцию `add_one`, как показано в Листинге 14-7.

Имя файла: `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Листинг 14-7: Использование библиотеки `add_one` из ящика `adder`

Построим рабочее пространство, выполнив `cargo build` в верхнеуровневой директории _add_!

```bash
$ cargo build
   Compiling add_one v0.1.0 (file:///projects/add/add_one)
   Compiling adder v0.1.0 (file:///projects/add/adder)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68s
```

Чтобы запустить бинарный ящик из директории `add`, мы можем указать, какой пакет в рабочем пространстве мы хотим запустить, используя аргумент `-p` и имя пакета с `cargo run`:

```bash
$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/adder`
Hello, world! 10 plus one is 11!
```

Это запускает код в `adder/src/main.rs`, который зависит от ящика `add_one`.
