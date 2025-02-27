# Creando una biblioteca

Vamos a crear una biblioteca y luego ver cómo vincularla a otra caja (crate).

En `rary.rs`:

```rust
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

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

Las bibliotecas se prefijan con "lib" y, por defecto, se nombran con el nombre de su archivo de caja (crate), pero este nombre predeterminado se puede anular pasando la opción `--crate-name` a `rustc` o utilizando el atributo \[`crate_name`\]\[crate-name\].
