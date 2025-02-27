# Creación del segundo paquete en el espacio de trabajo

A continuación, creemos otro paquete miembro en el espacio de trabajo y lo llamemos `add_one`. Cambiemos el `Cargo.toml` de nivel superior para especificar la ruta _add_one_ en la lista `members`:

Nombre del archivo: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
    "add_one",
]
```

Luego genere un nuevo crate de biblioteca llamado `add_one`:

```bash
$ cargo new add_one --lib
Creado el paquete de biblioteca $(add_one)
```

Su directorio `add` ahora debería tener estos directorios y archivos:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── add_one
    │   ├── Cargo.toml
    │   └── src
    │       └── lib.rs
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

En el archivo `add_one/src/lib.rs`, agreguemos una función `add_one`:

Nombre del archivo: `add_one/src/lib.rs`

```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

Ahora podemos hacer que el paquete `adder` con nuestro binario dependa del paquete `add_one` que tiene nuestra biblioteca. Primero necesitaremos agregar una dependencia de ruta en `add_one` a _adder/Cargo.toml_:

Nombre del archivo: `adder/Cargo.toml`

```tomlrust
[dependencies]
add_one = { path = "../add_one" }
```

Cargo no asume que los crates en un espacio de trabajo dependerán unos de otros, por lo que debemos ser explícitos sobre las relaciones de dependencia.

A continuación, usemos la función `add_one` (del crate `add_one`) en el crate `adder`. Abra el archivo `adder/src/main.rs` y agregue una línea `use` en la parte superior para traer el nuevo crate de biblioteca `add_one` al ámbito. Luego cambie la función `main` para llamar a la función `add_one`, como en la Lista 14-7.

Nombre del archivo: `adder/src/main.rs`

```rust
use add_one;

fn main() {
    let num = 10;
    println!(
        "Hello, world! {num} plus one is {}!",
        add_one::add_one(num)
    );
}
```

Lista 14-7: Usando el crate de biblioteca `add_one` desde el crate `adder`

¡Compilamos el espacio de trabajo ejecutando `cargo build` en el directorio _add_ de nivel superior!

```bash
$ cargo build
   Compilando add_one v0.1.0 (file:///projects/add/add_one)
   Compilando adder v0.1.0 (file:///projects/add/adder)
    Compilación finalizada [no optimizada + información de depuración] en 0.68s
```

Para ejecutar el crate binario desde el directorio `add`, podemos especificar qué paquete del espacio de trabajo queremos ejecutar usando el argumento `-p` y el nombre del paquete con `cargo run`:

```bash
$ cargo run -p adder
Compilación finalizada [no optimizada + información de depuración] en 0.0s
Ejecutando $(target/debug/adder)
Hello, world! 10 más uno es 11!
```

Esto ejecuta el código en `adder/src/main.rs`, que depende del crate `add_one`.
