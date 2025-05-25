# Utilizando uma Biblioteca

Para ligar um _crate_ a esta nova biblioteca, pode utilizar o sinalizador `--extern` do `rustc`. Todos os seus itens serão então importados num módulo com o mesmo nome da biblioteca. Este módulo geralmente comporta-se da mesma forma que qualquer outro módulo.

```rust
// extern crate rary; // Pode ser necessário para a edição de Rust 2015 ou anterior

fn main() {
    rary::public_function();

    // Erro! `private_function` é privado
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# Onde library.rlib é o caminho para a biblioteca compilada, assumindo que está
# no mesmo diretório aqui:
$ rustc executable.rs --extern rary=library.rlib && ./executable
chamou `public_function()` da biblioteca rary
chamou `indirect_access()` da biblioteca rary, que
> chamou `private_function()` da biblioteca rary
```
