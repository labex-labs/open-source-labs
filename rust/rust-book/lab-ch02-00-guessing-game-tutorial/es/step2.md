# Configurando un nuevo proyecto

Para configurar un nuevo proyecto, ve al directorio `proyecto` que creaste en el Capítulo 1 y crea un nuevo proyecto usando Cargo, así:

```bash
cargo new guessing_game
cd guessing_game
```

El primer comando, `cargo new`, toma el nombre del proyecto (`guessing_game`) como primer argumento. El segundo comando cambia al directorio del nuevo proyecto.

Echa un vistazo al archivo `Cargo.toml` generado:

Nombre del archivo: `Cargo.toml`

```toml
[package]
name = "guessing_game"
version = "0.1.0"
edition = "2021"

# Ver más claves y sus definiciones en
https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Como viste en el Capítulo 1, `cargo new` genera un programa "Hola, mundo!" para ti. Echa un vistazo al archivo `src/main.rs`:

Nombre del archivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Ahora vamos a compilar este programa "Hola, mundo!" y ejecutarlo en un solo paso usando el comando `cargo run`:

```bash
$ cargo run
   Compiling guessing_game v0.1.0 (file:///projects/guessing_game)
    Finished dev [unoptimized + debuginfo] target(s) in 1.50s
     Running `target/debug/guessing_game`
Hello, world!
```

El comando `run` es muy útil cuando necesitas iterar rápidamente en un proyecto, como lo haremos en este juego, probando rápidamente cada iteración antes de pasar a la siguiente.

Vuelve a abrir el archivo `src/main.rs`. Escribirás todo el código en este archivo.
