# Создание нового проекта

Для создания нового проекта перейдите в директорию `project`, которую вы создали в главе 1, и создайте новый проект с помощью Cargo, как показано ниже:

```bash
cargo new guessing_game
cd guessing_game
```

Первая команда, `cargo new`, принимает имя проекта (`guessing_game`) в качестве первого аргумента. Вторая команда переходит в директорию нового проекта.

Посмотрите на сгенерированный файл `Cargo.toml`:

Имя файла: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# См. дополнительные ключи и их определения по адресу
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Как вы видели в главе 1, `cargo new` генерирует для вас программу "Hello, world!". Посмотрите на файл `src/main.rs`:

Имя файла: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Теперь скомпилируем эту программу "Hello, world!" и запустим ее в одном и том же шаге с помощью команды `cargo run`:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

Команда `run` удобна, когда вам нужно быстро перебирать варианты в проекте, как мы будем делать в этой игре, быстро тестируя каждый вариант перед переходом к следующему.

Откройте снова файл `src/main.rs`. В этом файле вы будете писать весь код.
