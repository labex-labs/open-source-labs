# Criando uma Biblioteca

Vamos criar uma biblioteca e, em seguida, ver como ligá-la a outro projeto.

Em `rary.rs`:

```rust
pub fn public_function() {
    println!("chamada da função `public_function()` da biblioteca rary");
}

fn private_function() {
    println!("chamada da função `private_function()` da biblioteca rary");
}

pub fn indirect_access() {
    print!("chamada da função `indirect_access()` da biblioteca rary, que\n> ");

    private_function();
}
```

```shell
$ rustc --crate-type=lib rary.rs
$ ls lib*
library.rlib
```

As bibliotecas são prefixadas com "lib" e, por padrão, recebem o nome do seu ficheiro de projeto, mas este nome padrão pode ser alterado passando a opção `--crate-name` para `rustc` ou usando o atributo `#[crate_name]`.
