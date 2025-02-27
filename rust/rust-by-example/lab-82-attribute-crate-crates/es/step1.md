# Cajas (Crates)

El atributo `crate_type` se puede utilizar para decirle al compilador si una caja es binaria o una biblioteca (e incluso qué tipo de biblioteca), y el atributo `crate_name` se puede utilizar para establecer el nombre de la caja.

Sin embargo, es importante tener en cuenta que ambos atributos `crate_type` y `crate_name` **no** tienen ningún efecto cuando se utiliza Cargo, el administrador de paquetes de Rust. Dado que Cargo se utiliza en la mayoría de los proyectos de Rust, esto significa que los usos reales de `crate_type` y `crate_name` son relativamente limitados.

```rust
// Esta caja es una biblioteca
#![crate_type = "lib"]
// La biblioteca se llama "rary"
#![crate_name = "rary"]

pub fn public_function() {
    println!("llamada a `public_function()` de rary");
}

fn private_function() {
    println!("llamada a `private_function()` de rary");
}

pub fn indirect_access() {
    print!("llamada a `indirect_access()` de rary, que\n> ");

    private_function();
}
```

Cuando se utiliza el atributo `crate_type`, ya no es necesario pasar la bandera `--crate-type` a `rustc`.

```shell
$ rustc lib.rs
$ ls lib*
library.rlib
```
