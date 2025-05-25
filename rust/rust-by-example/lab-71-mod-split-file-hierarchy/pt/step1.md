# Hierarquia de Arquivos

Módulos podem ser mapeados para uma hierarquia de arquivos/diretórios. Vamos decompor o exemplo de visibilidade em arquivos:

```shell
$ tree .
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

Em `split.rs`:

```rust
// Esta declaração procurará um arquivo chamado `my.rs` e
// inserirá seu conteúdo dentro de um módulo chamado `my` sob este escopo
mod my;

fn function() {
    println!("chamada `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

Em `my.rs`:

```rust
// Similarmente, `mod inaccessible` e `mod nested` localizarão os arquivos
// `nested.rs` e `inaccessible.rs` e os inserirão aqui sob seus respectivos
// módulos
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("chamada `my::function()`");
}

fn private_function() {
    println!("chamada `my::private_function()`");
}

pub fn indirect_access() {
    print!("chamada `my::indirect_access()`, que\n> ");

    private_function();
}
```

Em `my/nested.rs`:

```rust
pub fn function() {
    println!("chamada `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("chamada `my::nested::private_function()`");
}
```

Em `my/inaccessible.rs`:

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("chamada `my::inaccessible::public_function()`");
}
```

Vamos verificar se as coisas ainda funcionam como antes:

```shell
$ rustc split.rs && ./split
chamada `my::function()`
chamada `function()`
chamada `my::indirect_access()`, que
> chamada `my::private_function()`
chamada `my::nested::function()`
```
