# Иерархия файлов

Модули могут быть сопоставлены иерархии файлов/директорий. Рассмотрим пример видимости в файлах:

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

В `split.rs`:

```rust
// Эта декларация будет искать файл с именем `my.rs` и
// вставлять его содержимое внутри модуля с именем `my` в этом контексте
mod my;

fn function() {
    println!("called `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

В `my.rs`:

```rust
// Аналогично `mod inaccessible` и `mod nested` будут искать файлы `nested.rs`
// и `inaccessible.rs` и вставлять их здесь под соответствующими
// модулями
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("called `my::function()`");
}

fn private_function() {
    println!("called `my::private_function()`");
}

pub fn indirect_access() {
    print!("called `my::indirect_access()`, that\n> ");

    private_function();
}
```

В `my/nested.rs`:

```rust
pub fn function() {
    println!("called `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("called `my::nested::private_function()`");
}
```

В `my/inaccessible.rs`:

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("called `my::inaccessible::public_function()`");
}
```

Проверим, что все по-прежнему работает как прежде:

```shell
$ rustc split.rs &&./split
called `my::function()`
called `function()`
called `my::indirect_access()`, that
> called `my::private_function()`
called `my::nested::function()`
```
