# Pruebas

Como sabemos, las pruebas son esenciales para cualquier software. Rust tiene un soporte de primera clase para las pruebas unitarias e integrales ([ver este capítulo](https://doc.rust-lang.org/book/ch11-00-testing.html) en TRPL).

A partir de los capítulos de pruebas vinculados anteriormente, vemos cómo escribir pruebas unitarias e integrales. Organizacionalmente, podemos colocar las pruebas unitarias en los módulos que se prueban y las pruebas integrales en su propio directorio `tests/`:

```txt
foo
├── Cargo.toml
├── src
│   └── main.rs
│   └── lib.rs
└── tests
    ├── my_test.rs
    └── my_other_test.rs
```

Cada archivo en `tests` es una [prueba integral](https://doc.rust-lang.org/book/ch11-03-test-organization.html#integration-tests) independiente, es decir, una prueba que está destinada a probar su biblioteca como si se estuviera llamando desde una caja dependiente.

El capítulo de Pruebas se detalla sobre los tres diferentes estilos de pruebas: Unitarias, Documentación y Integrales.

`cargo` naturalmente proporciona una forma fácil de ejecutar todas sus pruebas:

```shell
$ cargo test
```

Debería ver una salida como esta:

```shell
$ cargo test
   Compiling blah v0.1.0 (file:///nobackup/blah)
    Finished dev [unoptimized + debuginfo] target(s) in 0.89 secs
     Running target/debug/deps/blah-d3b32b97275ec472

running 3 tests
test test_bar... ok
test test_baz... ok
test test_foo_bar... ok
test test_foo... ok

test result: ok. 3 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

También puede ejecutar las pruebas cuyo nombre coincide con un patrón:

```shell
$ cargo test test_foo
```

```shell
$ cargo test test_foo
   Compiling blah v0.1.0 (file:///nobackup/blah)
    Finished dev [unoptimized + debuginfo] target(s) in 0.35 secs
     Running target/debug/deps/blah-d3b32b97275ec472

running 2 tests
test test_foo... ok
test test_foo_bar... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 2 filtered out
```

Una advertencia: Cargo puede ejecutar múltiples pruebas concurrentemente, así que asegúrese de que no se interrumpen mutuamente.

Un ejemplo de cómo esta concurrencia puede causar problemas es si dos pruebas escriben a un archivo, como a continuación:

```rust
#[cfg(test)]
mod tests {
    // Importa los módulos necesarios
    use std::fs::OpenOptions;
    use std::io::Write;

    // Esta prueba escribe en un archivo
    #[test]
    fn test_file() {
        // Abre el archivo ferris.txt o lo crea si no existe.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // Imprime "Ferris" 5 veces.
        for _ in 0..5 {
            file.write_all("Ferris\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }

    // Esta prueba intenta escribir en el mismo archivo
    #[test]
    fn test_file_also() {
        // Abre el archivo ferris.txt o lo crea si no existe.
        let mut file = OpenOptions::new()
         .append(true)
         .create(true)
         .open("ferris.txt")
         .expect("Failed to open ferris.txt");

        // Imprime "Corro" 5 veces.
        for _ in 0..5 {
            file.write_all("Corro\n".as_bytes())
             .expect("Could not write to ferris.txt");
        }
    }
}
```

Aunque la intención es obtener lo siguiente:

```shell
$ cat ferris.txt
Ferris
Ferris
Ferris
Ferris
Ferris
Corro
Corro
Corro
Corro
Corro
```

Lo que realmente se coloca en `ferris.txt` es esto:

```shell
$ cargo test test_foo
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
Corro
Ferris
```
