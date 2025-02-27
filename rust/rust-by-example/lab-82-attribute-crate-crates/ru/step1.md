# Крейты

Атрибут `crate_type` можно использовать, чтобы сообщить компилятору, является ли крейт бинарным файлом или библиотекой (и даже какого типа библиотека), а атрибут `crate_name` можно использовать для установки имени крейта.

Однако важно отметить, что ни атрибут `crate_type`, ни атрибут `crate_name` не оказывают никакого эффекта при использовании Cargo - менеджера пакетов для Rust. Поскольку Cargo используется для большинства проектов на Rust, это означает, что практическое применение `crate_type` и `crate_name` относительно ограничено.

```rust
// Этот крейт - библиотека
#![crate_type = "lib"]
// Библиотека называется "rary"
#![crate_name = "rary"]

pub fn public_function() {
    println!("called rary's `public_function()`");
}

fn private_function() {
    println!("called rary's `private_function()`");
}

pub fn indirect_access() {
    print!("called rary's `indirect_access()`, that\n> ");

    private_function();
}
```

Когда используется атрибут `crate_type`, нам больше не нужно передавать флаг `--crate-type` в `rustc`.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
