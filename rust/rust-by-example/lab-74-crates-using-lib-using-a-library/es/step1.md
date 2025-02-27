# Usando una biblioteca

Para vincular una caja a esta nueva biblioteca, puede usar la bandera `--extern` de `rustc`. Todos sus elementos se importarán entonces en un módulo con el mismo nombre que la biblioteca. Este módulo generalmente se comporta de la misma manera que cualquier otro módulo.

```rust
// extern crate rary; // Puede ser necesario para la edición Rust 2015 o anterior

fn main() {
    rary::public_function();

    // Error! `private_function` es privada
    //rary::private_function();

    rary::indirect_access();
}
```

```txt
# Donde library.rlib es la ruta a la biblioteca compilada, suponiendo que está
# en el mismo directorio aquí:
$ rustc executable.rs --extern rary=library.rlib &&./executable
llamó a la `public_function()` de rary
llamó a la `indirect_access()` de rary, que
> llamó a la `private_function()` de rary
```
