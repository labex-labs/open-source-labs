# Paquetes y Cajas

Las primeras partes del sistema de módulos que cubriremos son los paquetes y las cajas.

Una _caja_ es la cantidad más pequeña de código que el compilador de Rust considera en un momento dado. Incluso si ejecutas `rustc` en lugar de `cargo` y le pasas un solo archivo de código fuente (como lo hicimos al principio en "Escribir y ejecutar un programa Rust"), el compilador considera que ese archivo es una caja. Las cajas pueden contener módulos, y los módulos pueden estar definidos en otros archivos que se compilan con la caja, como veremos en las secciones siguientes.

Una caja puede venir en una de dos formas: una caja binaria o una caja de biblioteca. Las _cajas binarias_ son programas que se pueden compilar en un ejecutable que se puede ejecutar, como un programa de línea de comandos o un servidor. Cada una debe tener una función llamada `main` que define lo que sucede cuando se ejecuta el ejecutable. Todas las cajas que hemos creado hasta ahora han sido cajas binarias.

Las _cajas de biblioteca_ no tienen una función `main` y no se compilan en un ejecutable. En cambio, definen funcionalidades destinadas a ser compartidas con múltiples proyectos. Por ejemplo, la caja `rand` que usamos en el Capítulo 2 proporciona funcionalidades para generar números aleatorios. En la mayoría de los casos, cuando los desarrolladores de Rust dicen "caja", se refieren a una caja de biblioteca, y usan "caja" de manera intercambiable con el concepto general de programación de una "biblioteca".

La _raíz de la caja_ es un archivo de código fuente a partir del cual el compilador de Rust comienza y que forma el módulo raíz de su caja (explicaremos los módulos en profundidad en "Definiendo módulos para controlar el alcance y la privacidad").

Un _paquete_ es un conjunto de una o más cajas que proporciona un conjunto de funcionalidades. Un paquete contiene un archivo `Cargo.toml` que describe cómo compilar esas cajas. Cargo en realidad es un paquete que contiene la caja binaria para la herramienta de línea de comandos que has estado usando para compilar tu código. El paquete de Cargo también contiene una caja de biblioteca en la que depende la caja binaria. Otros proyectos pueden depender de la caja de biblioteca de Cargo para usar la misma lógica que usa la herramienta de línea de comandos de Cargo.

Una caja puede venir en una de dos formas: una caja binaria o una caja de biblioteca. Un paquete puede contener tantas cajas binarias como desees, pero como máximo solo una caja de biblioteca. Un paquete debe contener al menos una caja, ya sea una caja de biblioteca o una caja binaria.

Veamos lo que sucede cuando creamos un paquete. Primero, escribimos el comando `cargo new my-project`:

```bash
$ cargo new my-project
     Created binary (application) `my-project` package
$ ls my-project
Cargo.toml
src
$ ls my-project/src
main.rs
```

Después de ejecutar `cargo new my-project`, usamos `ls` para ver lo que Cargo crea. En el directorio del proyecto, hay un archivo `Cargo.toml`, que nos da un paquete. También hay un directorio `src` que contiene `main.rs`. Abre `Cargo.toml` en tu editor de texto y observa que no se menciona `src/main.rs`. Cargo sigue una convención de que `src/main.rs` es la raíz de la caja de un crate binario con el mismo nombre que el paquete. Del mismo modo, Cargo sabe que si el directorio del paquete contiene `src/lib.rs`, el paquete contiene una caja de biblioteca con el mismo nombre que el paquete, y `src/lib.rs` es su raíz de la caja. Cargo pasa los archivos de raíz de la caja a `rustc` para compilar la biblioteca o el binario.

Aquí, tenemos un paquete que solo contiene `src/main.rs`, lo que significa que solo contiene una caja binaria llamada `my-project`. Si un paquete contiene `src/main.rs` y `src/lib.rs`, tiene dos cajas: una binaria y una de biblioteca, ambas con el mismo nombre que el paquete. Un paquete puede tener múltiples cajas binarias al colocar archivos en el directorio `src/bin`: cada archivo será una caja binaria separada.

> **Hoja de trucos de módulos**
>
> Antes de entrar en los detalles de los módulos y las rutas, aquí te proporcionamos una referencia rápida sobre cómo funcionan los módulos, las rutas, la palabra clave `use` y la palabra clave `pub` en el compilador, y cómo la mayoría de los desarrolladores organizan su código. Vamos a ver ejemplos de cada una de estas reglas a lo largo de este capítulo, pero este es un gran lugar para consultar como recordatorio de cómo funcionan los módulos.
>
> - **Comienza desde la raíz de la caja**: Al compilar una caja, el compilador primero busca en el archivo raíz de la caja (generalmente `src/lib.rs` para una caja de biblioteca o `src/main.rs` para una caja binaria) el código para compilar.
> - **Declarando módulos**: En el archivo raíz de la caja, puedes declarar nuevos módulos; digamos que declaras un módulo "jardín" con `mod garden;`. El compilador buscará el código del módulo en estos lugares:
> - Inline, dentro de llaves que reemplazan el punto y coma siguiente a `mod garden`
> - En el archivo `src/garden.rs`
> - En el archivo `src/garden/mod.rs`
> - **Declarando submódulos**: En cualquier archivo diferente al raíz de la caja, puedes declarar submódulos. Por ejemplo, podrías declarar `mod vegetables;` en `src/garden.rs`. El compilador buscará el código del submódulo dentro del directorio nombrado para el módulo padre en estos lugares:
> - Inline, directamente después de `mod vegetables`, dentro de llaves en lugar del punto y coma
> - En el archivo `src/garden/vegetables.rs`
> - En el archivo `src/garden/vegetables/mod.rs`
> - **Rutas al código en módulos**: Una vez que un módulo es parte de tu caja, puedes referirte al código en ese módulo desde cualquier otro lugar en la misma caja, siempre y cuando las reglas de privacidad lo permitan, usando la ruta al código. Por ejemplo, un tipo `Asparagus` en el módulo de verduras del jardín se encontraría en `crate::garden::vegetables::Asparagus`.
> - **Privado vs. público**: El código dentro de un módulo es privado para sus módulos padres por defecto. Para hacer que un módulo sea público, decláralo con `pub mod` en lugar de `mod`. Para hacer que los elementos dentro de un módulo público también sean públicos, usa `pub` antes de sus declaraciones.
> - **La palabra clave use**: Dentro de un ámbito, la palabra clave `use` crea atajos a elementos para reducir la repetición de rutas largas. En cualquier ámbito que pueda referirse a `crate::garden::vegetables::Asparagus`, puedes crear un atajo con `use crate::garden::vegetables::Asparagus;` y a partir de entonces solo necesitarás escribir `Asparagus` para usar ese tipo en el ámbito.
>
> Aquí, creamos una caja binaria llamada `backyard` que ilustra estas reglas. El directorio de la caja, también llamado `backyard`, contiene estos archivos y directorios:
>
> ```bash
> backyard
> ├── Cargo.lock
> ├── Cargo.toml
> └── src
> ├── garden
> │ └── vegetables.rs
> ├── garden.rs
> └── main.rs
> ```
>
> El archivo raíz de la caja en este caso es `src/main.rs`, y contiene:
>
> ```rust
> use crate::garden::vegetables::Asparagus;
>
> pub mod garden;
>
> fn main() {
>     let plant = Asparagus {};
>     println!("I'm growing {:?}!", plant);
> }
> ```
>
> La línea `pub mod garden;` le dice al compilador que incluya el código que encuentra en `src/garden.rs`, que es:
>
> ```rust
> pub mod vegetables;
> ```
>
> Aquí, `pub mod vegetables;` significa que también se incluye el código en `src/garden/vegetables.rs`. Ese código es:
>
> ```rust
> #[derive(Debug)]
> pub struct Asparagus {}
> ```
>
> Ahora, vamos a entrar en los detalles de estas reglas y demostrarlas en acción!
