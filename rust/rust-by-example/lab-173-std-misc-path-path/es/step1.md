# Path

La estructura `Path` representa rutas de archivos en el sistema de archivos subyacente. Hay dos variantes de `Path`: `posix::Path`, para sistemas UNIX-like, y `windows::Path`, para Windows. El preludio exporta la variante de `Path` adecuada para la plataforma.

Una `Path` se puede crear a partir de un `OsStr`, y proporciona varios métodos para obtener información del archivo/directorio al que apunta la ruta.

Una `Path` es inmutable. La versión con propiedad de `Path` es `PathBuf`. La relación entre `Path` y `PathBuf` es similar a la de `str` y `String`: un `PathBuf` se puede mutar in situ, y se puede desreferenciar a una `Path`.

Tenga en cuenta que una `Path` no se representa internamente como una cadena UTF-8, sino que se almacena como un `OsString`. Por lo tanto, convertir una `Path` en un `&str` no es gratis y puede fallar (se devuelve una `Option`). Sin embargo, una `Path` se puede convertir libremente en un `OsString` o `&OsStr` usando `into_os_string` y `as_os_str`, respectivamente.

```rust
use std::path::Path;

fn main() {
    // Crea una `Path` a partir de un `&'static str`
    let path = Path::new(".");

    // El método `display` devuelve una estructura `Display`able
    let _display = path.display();

    // `join` combina una ruta con un contenedor de bytes usando el separador
    // específico de la plataforma, y devuelve un `PathBuf`
    let mut new_path = path.join("a").join("b");

    // `push` extiende el `PathBuf` con una `&Path`
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // `set_file_name` actualiza el nombre de archivo del `PathBuf`
    new_path.set_file_name("package.tgz");

    // Convierte el `PathBuf` en una porción de cadena
    match new_path.to_str() {
        None => panic!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}
```

Asegúrese de revisar otros métodos de `Path` (`posix::Path` o `windows::Path`) y la estructura `Metadata`.
