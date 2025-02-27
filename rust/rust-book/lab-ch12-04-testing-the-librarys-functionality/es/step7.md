# Usando la función search en la función run

Ahora que la función `search` está funcionando y probada, necesitamos llamar a `search` desde nuestra función `run`. Necesitamos pasar el valor `config.query` y el `contents` que `run` lee del archivo a la función `search`. Luego, `run` imprimirá cada línea devuelta por `search`:

Nombre del archivo: `src/lib.rs`

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.file_path)?;

    for line in search(&config.query, &contents) {
        println!("{line}");
    }

    Ok(())
}
```

Todavía estamos usando un bucle `for` para devolver cada línea de `search` e imprimirla.

Ahora todo el programa debería funcionar. Probémoslo, primero con una palabra que debería devolver exactamente una línea del poema de Emily Dickinson: _frog_.

```bash
$ cargo run -- frog poem.txt
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.38s
     Running `target/debug/minigrep frog poem.txt`
How public, like a frog
```

Genial! Ahora probemos una palabra que coincida con múltiples líneas, como _body_:

```bash
$ cargo run -- body poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep body poem.txt`
I'm nobody! Who are you?
Are you nobody, too?
How dreary to be somebody!
```

Y finalmente, asegúrense de que no obtenemos ninguna línea cuando buscamos una palabra que no está en ningún lugar del poema, como _monomorphization_:

```bash
$ cargo run -- monomorphization poem.txt
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep monomorphization poem.txt`
```

Excelente! Hemos construido nuestra propia versión mini de una herramienta clásica y hemos aprendido mucho sobre cómo estructurar aplicaciones. También hemos aprendido un poco sobre la entrada y salida de archivos, los lifetimes, las pruebas y el análisis de la línea de comandos.

Para terminar este proyecto, demostraremos brevemente cómo trabajar con variables de entorno y cómo imprimir en el error estándar, ambos son útiles cuando se escribe un programa de línea de comandos.
