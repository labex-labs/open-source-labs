# Создание библиотеки

Создадим библиотеку, а затем посмотрим, как связать ее с другой коробкой (crate).

В `rary.rs`:

```rust
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

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

Библиотеки именуются с префиксом "lib", и по умолчанию они именуются по имени файла их коробки, но это имя по умолчанию можно переопределить, передав опцию `--crate-name` в `rustc` или используя атрибут \[`crate_name`\]\[crate-name\].
