# `read_lines`

## Un enfoque sencillo

Este podría ser un primer intento razonable para la primera implementación de un principiante para leer líneas de un archivo.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

Dado que el método `lines()` devuelve un iterador sobre las líneas del archivo, también podemos realizar un mapeo en línea y recopilar los resultados, lo que produce una expresión más concisa y fluida.

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // genera un panic en posibles errores de lectura de archivo
     .lines()  // divide la cadena en un iterador de rebanadas de cadena
     .map(String::from)  // convierte cada rebanada en una cadena
     .collect()  // los agrupa en un vector
}
```

Tenga en cuenta que en ambos ejemplos anteriores, debemos convertir la referencia `&str` devuelta por `lines()` al tipo `String` con propiedad, usando `.to_string()` y `String::from` respectivamente.

## Un enfoque más eficiente

Aquí pasamos la propiedad del `File` abierto a una estructura `BufReader`. `BufReader` utiliza un búfer interno para reducir las asignaciones intermedias.

También actualizamos `read_lines` para devolver un iterador en lugar de asignar nuevos objetos `String` en memoria para cada línea.

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // El archivo hosts.txt debe existir en el directorio actual
    if let Ok(lines) = read_lines("./hosts.txt") {
        // Consume el iterador, devuelve una (Opcional) String
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// La salida está envuelta en un Result para permitir coincidir con errores
// Devuelve un Iterador al lector de las líneas del archivo.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

Ejecutar este programa simplemente imprime las líneas por separado.

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(Tenga en cuenta que dado que `File::open` espera un `AsRef<Path>` genérico como argumento, definimos nuestro método genérico `read_lines()` con la misma restricción genérica, usando la palabra clave `where`.)

Este proceso es más eficiente que crear una `String` en memoria con todo el contenido del archivo. Esto puede causar problemas de rendimiento especialmente al trabajar con archivos más grandes.
