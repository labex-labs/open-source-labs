# Creando un proyecto con Cargo

Vamos a crear un nuevo proyecto usando Cargo y ver cómo difiere de nuestro original proyecto "Hello, world!". Navega de vuelta a tu directorio `project` (o dondequiera que hayas decidido almacenar tu código). Luego, en cualquier sistema operativo, ejecuta lo siguiente:

```bash
cd ~/project
cargo new hello_cargo
cd hello_cargo
```

El primer comando crea un nuevo directorio y proyecto llamado _hello_cargo_. Hemos nombrado nuestro proyecto _hello_cargo_, y Cargo crea sus archivos en un directorio con el mismo nombre.

Ingresa al directorio `hello_cargo` y lista los archivos. Verás que Cargo ha generado dos archivos y un directorio para nosotros: un archivo `Cargo.toml` y un directorio `src` con un archivo `main.rs` dentro.

También ha inicializado un nuevo repositorio Git junto con un archivo _.gitignore_. Los archivos de Git no se generarán si ejecutas `cargo new` dentro de un repositorio Git existente; puedes anular este comportamiento usando `cargo new --vcs=git`.

> Nota: Git es un sistema de control de versiones común. Puedes cambiar `cargo new` para usar un sistema de control de versiones diferente o ningún sistema de control de versiones usando la bandera `--vcs`. Ejecuta `cargo new --help` para ver las opciones disponibles.

Abre `Cargo.toml` en tu editor de texto preferido. Debería verse similar al código de la Lista 1-2.

Nombre de archivo: `Cargo.toml`

```toml
[package]
name = "hello_cargo"
version = "0.1.0"
edition = "2021"

[dependencies]
```

Lista 1-2: Contenido de `Cargo.toml` generado por `cargo new`

Este archivo está en el formato _TOML_ (_Tom's Obvious, Minimal Language_), que es el formato de configuración de Cargo.

La primera línea, `[package]`, es un encabezado de sección que indica que las siguientes declaraciones están configurando un paquete. A medida que agregamos más información a este archivo, agregaremos otras secciones.

Las siguientes tres líneas establecen la información de configuración que Cargo necesita para compilar tu programa: el nombre, la versión y la edición de Rust a usar. Hablaremos de la clave `edition` en el Apéndice E.

La última línea, `[dependencies]`, es el comienzo de una sección para que puedas listar cualquier dependencia de tu proyecto. En Rust, los paquetes de código se denominan _crates_. No necesitaremos ningún otro crate para este proyecto, pero sí en el primer proyecto del Capítulo 2, así que usaremos esta sección de dependencias entonces.

Ahora abre `src/main.rs` y echa un vistazo:

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    println!("Hello, world!");
}
```

Cargo ha generado un programa "Hello, world!" para ti, ¡al igual que el que escribimos en la Lista 1-1! Hasta ahora, las diferencias entre nuestro proyecto y el proyecto generado por Cargo son que Cargo colocó el código en el directorio `src` y tenemos un archivo de configuración `Cargo.toml` en el directorio principal.

Cargo espera que tus archivos fuente estén dentro del directorio `src`. El directorio principal del proyecto es solo para archivos README, información de licencia, archivos de configuración y cualquier otra cosa no relacionada con tu código. Usar Cargo te ayuda a organizar tus proyectos. Hay un lugar para todo, y todo está en su lugar.

Si comenzaste un proyecto que no usa Cargo, como lo hicimos con el proyecto "Hello, world!", puedes convertirlo en un proyecto que sí use Cargo. Mueve el código del proyecto al directorio `src` y crea un archivo `Cargo.toml` adecuado.
