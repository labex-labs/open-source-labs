# Jerarquía de archivos

Los módulos se pueden mapear a una jerarquía de archivos/directorios. Analicemos el ejemplo de visibilidad en archivos:

```shell
$ tree.
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

En `split.rs`:

```rust
// Esta declaración buscará un archivo llamado `my.rs` y
// insertará su contenido dentro de un módulo llamado `my` en este ámbito
mod my;

fn function() {
    println!("llamado `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

En `my.rs`:

```rust
// Del mismo modo, `mod inaccessible` y `mod nested` localizarán los archivos `nested.rs`
// y `inaccessible.rs` e insertarán aquí bajo sus respectivos
// módulos
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("llamado `my::function()`");
}

fn private_function() {
    println!("llamado `my::private_function()`");
}

pub fn indirect_access() {
    print!("llamado `my::indirect_access()`, que\n> ");

    private_function();
}
```

En `my/nested.rs`:

```rust
pub fn function() {
    println!("llamado `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("llamado `my::nested::private_function()`");
}
```

En `my/inaccessible.rs`:

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("llamado `my::inaccessible::public_function()`");
}
```

Veamos si las cosas siguen funcionando como antes:

```shell
$ rustc split.rs &&./split
llamado `my::function()`
llamado `function()`
llamado `my::indirect_access()`, que
> llamado `my::private_function()`
llamado `my::nested::function()`
```
