# Módulos

O atributo `crate_type` pode ser usado para indicar ao compilador se um módulo é um binário ou uma biblioteca (e até que tipo de biblioteca), e o atributo `crate_name` pode ser usado para definir o nome do módulo.

No entanto, é importante notar que os atributos `crate_type` e `crate_name` não têm **nenhum** efeito quando se utiliza o Cargo, o gestor de pacotes Rust. Uma vez que o Cargo é usado na maioria dos projetos Rust, isto significa que os usos reais de `crate_type` e `crate_name` são relativamente limitados.

```rust
// Este módulo é uma biblioteca
#![crate_type = "lib"]
// A biblioteca é chamada "rary"
#![crate_name = "rary"]

pub fn public_function() {
    println!("chamada da função `public_function()` de rary");
}

fn private_function() {
    println!("chamada da função `private_function()` de rary");
}

pub fn indirect_access() {
    print!("chamada da função `indirect_access()` de rary, que\n> ");

    private_function();
}
```

Quando o atributo `crate_type` é usado, não precisamos mais de passar a flag `--crate-type` para o `rustc`.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
