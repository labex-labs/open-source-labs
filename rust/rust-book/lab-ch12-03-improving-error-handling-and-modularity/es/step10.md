# Extracción de la Lógica de main

Ahora que hemos terminado de refactorizar el análisis de la configuración, pasemos a la lógica del programa. Como dijimos en "Separation of Concerns for Binary Projects" (Separación de Preocupaciones para Proyectos Binarios), extraeremos una función llamada `run` que contendrá toda la lógica que actualmente está en la función `main` y que no está involucrada en la configuración o el manejo de errores. Cuando hayamos terminado, `main` será concisa y fácil de verificar por inspección, y podremos escribir pruebas para toda la otra lógica.

La Lista 12-11 muestra la función `run` extraída. Por ahora, solo estamos realizando la pequeña mejora incremental de extraer la función. Todavía estamos definiendo la función en `src/main.rs`.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    --snip--

    println!("Buscando {}", config.query);
    println!("En el archivo {}", config.file_path);

    run(config);
}

fn run(config: Config) {
    let contents = fs::read_to_string(config.file_path)
     .expect("Debería haber sido posible leer el archivo");

    println!("Con el texto:\n{contents}");
}

--snip--
```

Lista 12-11: Extracción de una función `run` que contiene el resto de la lógica del programa

La función `run` ahora contiene toda la lógica restante de `main`, comenzando desde la lectura del archivo. La función `run` toma la instancia de `Config` como argumento.
