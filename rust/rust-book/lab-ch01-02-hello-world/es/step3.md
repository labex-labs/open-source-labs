# Escribiendo y ejecutando un programa Rust

A continuación, crea un nuevo archivo fuente y dile `main.rs`. Los archivos Rust siempre terminan con la extensión `.rs`. Si estás usando más de una palabra en el nombre de tu archivo, la convención es usar un subrayado para separarlas. Por ejemplo, utiliza `hello_world.rs` en lugar de `helloworld.rs`.

Ahora abre el archivo `main.rs` que acabas de crear y escribe el código de la Lista 1-1.

Nombre del archivo: `main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Lista 1-1: Un programa que imprime `¡Hola, mundo!`

Guarda el archivo y vuelve a tu ventana de terminal en el directorio `~/project/hello_world`. En Linux o macOS, escribe los siguientes comandos para compilar y ejecutar el archivo:

```bash
$ rustc main.rs
$./main
Hello, world!
```

Independientemente de tu sistema operativo, la cadena `¡Hola, mundo!` debería imprimirse en la terminal. Si no ves esta salida, consulta "Solución de problemas" para obtener formas de obtener ayuda.

Si se imprimió `¡Hola, mundo!`, ¡felicitaciones! Has escrito oficialmente un programa Rust. Eso te convierte en un programador Rust: ¡bienvenido!
