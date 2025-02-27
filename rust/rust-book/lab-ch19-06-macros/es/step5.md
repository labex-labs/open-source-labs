# Cómo Escribir una Macro derive Personalizada

Vamos a crear un crat llamado `hello_macro` que defina un trato llamado `HelloMacro` con una función asociada llamada `hello_macro`. En lugar de hacer que nuestros usuarios implementen el trato `HelloMacro` para cada uno de sus tipos, proporcionaremos una macro procedimental para que los usuarios puedan anotar su tipo con `#[derive(HelloMacro)]` para obtener una implementación predeterminada de la función `hello_macro`. La implementación predeterminada imprimirá `¡Hola, Macro! Me llamo` NombreTipo`!` donde NombreTipo es el nombre del tipo en el que se ha definido este trato. En otras palabras, escribiremos un crat que permita a otro programador escribir código como el de la Lista 19-30 usando nuestro crat.

Nombre del archivo: `src/main.rs`

```rust
use hello_macro::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Pancakes;

fn main() {
    Pancakes::hello_macro();
}
```

Lista 19-30: El código que un usuario de nuestro crat podrá escribir al usar nuestra macro procedimental

Este código imprimirá `¡Hola, Macro! Me llamo Pancakes!` cuando hayamos terminado. El primer paso es crear un nuevo crat de biblioteca, así:

```bash
cargo new hello_macro --lib
```

A continuación, definiremos el trato `HelloMacro` y su función asociada:

Nombre del archivo: `src/lib.rs`

```rust
pub trait HelloMacro {
    fn hello_macro();
}
```

Tenemos un trato y su función. En este momento, el usuario de nuestro crat podría implementar el trato para obtener la funcionalidad deseada, así:

```rust
use hello_macro::HelloMacro;

struct Pancakes;

impl HelloMacro for Pancakes {
    fn hello_macro() {
        println!("¡Hola, Macro! Me llamo Pancakes!");
    }
}

fn main() {
    Pancakes::hello_macro();
}
```

Sin embargo, tendrían que escribir el bloque de implementación para cada tipo que quisieran usar con `hello_macro`; queremos ahorrarlos esa labor.

Además, aún no podemos proporcionar a la función `hello_macro` una implementación predeterminada que imprima el nombre del tipo en el que se implementa el trato: Rust no tiene capacidades de reflexión, por lo que no puede buscar el nombre del tipo en tiempo de ejecución. Necesitamos una macro para generar código en tiempo de compilación.

El siguiente paso es definir la macro procedimental. En el momento de escribir esto, las macros procedimentales deben estar en su propio crat. Eventualmente, esta restricción podría ser levantada. La convención para estructurar crates y crates de macros es la siguiente: para un crat llamado foo, un crat de macro procedimental personalizado se llama foo`_derive`. Vamos a comenzar un nuevo crat llamado `hello_macro_derive` dentro de nuestro proyecto `hello_macro`:

```bash
cargo new hello_macro_derive --lib
```

Nuestros dos crates están estrechamente relacionados, por lo que creamos el crat de macro procedimental dentro del directorio de nuestro crat `hello_macro`. Si cambiamos la definición del trato en `hello_macro`, también tendremos que cambiar la implementación de la macro procedimental en `hello_macro_derive`. Los dos crates se tendrán que publicar por separado, y los programadores que usan estos crates tendrán que agregarlos ambos como dependencias y traerlos ambos al ámbito. En su lugar, podríamos hacer que el crat `hello_macro` use `hello_macro_derive` como dependencia y reexportar el código de la macro procedimental. Sin embargo, la forma en que hemos estructurado el proyecto permite a los programadores usar `hello_macro` incluso si no quieren la funcionalidad `derive`.

Necesitamos declarar el crat `hello_macro_derive` como un crat de macro procedimental. También necesitaremos funcionalidad de los crates `syn` y `quote`, como verás en un momento, por lo que debemos agregarlos como dependencias. Agregue lo siguiente al archivo `Cargo.toml` para `hello_macro_derive`:

Nombre del archivo: `hello_macro_derive/Cargo.toml`

```toml
[lib]
proc-macro = true

[dependencies]
syn = "1.0"
quote = "1.0"
```

Para comenzar a definir la macro procedimental, coloque el código de la Lista 19-31 en su archivo `src/lib.rs` para el crat `hello_macro_derive`. Tenga en cuenta que este código no se compilará hasta que agreguemos una definición para la función `impl_hello_macro`.

Nombre del archivo: `hello_macro_derive/src/lib.rs`

```rust
use proc_macro::TokenStream;
use quote::quote;
use syn;

#[proc_macro_derive(HelloMacro)]
pub fn hello_macro_derive(input: TokenStream) -> TokenStream {
    // Construya una representación del código de Rust como un árbol de sintaxis
    // que podemos manipular
    let ast = syn::parse(input).unwrap();

    // Construya la implementación del trato
    impl_hello_macro(&ast)
}
```

Lista 19-31: Código que la mayoría de los crates de macros procedimentales requerirá para procesar el código de Rust

Tenga en cuenta que hemos dividido el código en la función `hello_macro_derive`, que se encarga de analizar el `TokenStream`, y la función `impl_hello_macro`, que se encarga de transformar el árbol de sintaxis: esto hace que escribir una macro procedimental sea más conveniente. El código en la función externa (`hello_macro_derive` en este caso) será el mismo para casi todos los crates de macros procedimentales que vea o cree. El código que especifique en el cuerpo de la función interna (`impl_hello_macro` en este caso) será diferente según el propósito de su macro procedimental.

Hemos introducido tres nuevos crates: `proc_macro`, `syn` (disponible en *https://crates.io/crates/syn*) y `quote` (disponible en *https://crates.io/crates/quote*). El crat `proc_macro` viene con Rust, por lo que no tuvimos que agregarlo a las dependencias en `Cargo.toml`. El crat `proc_macro` es la API del compilador que nos permite leer y manipular el código de Rust a partir de nuestro código.

El crat `syn` analiza el código de Rust de una cadena en una estructura de datos en la que podemos realizar operaciones. El crat `quote` convierte las estructuras de datos de `syn` de vuelta en código de Rust. Estos crates hacen que sea mucho más sencillo analizar cualquier tipo de código de Rust que podamos querer manejar: escribir un analizador completo para el código de Rust no es una tarea sencilla.

La función `hello_macro_derive` se llamará cuando un usuario de nuestra biblioteca especifique `#[derive(HelloMacro)]` en un tipo. Esto es posible porque hemos anotado la función `hello_macro_derive` aquí con `proc_macro_derive` y hemos especificado el nombre `HelloMacro`, que coincide con el nombre de nuestro trato; esta es la convención que siguen la mayoría de las macros procedimentales.

La función `hello_macro_derive` primero convierte el `input` de un `TokenStream` a una estructura de datos que luego podemos interpretar y realizar operaciones. Aquí es donde entra en juego `syn`. La función `parse` en `syn` toma un `TokenStream` y devuelve una estructura `DeriveInput` que representa el código de Rust analizado. La Lista 19-32 muestra las partes relevantes de la estructura `DeriveInput` que obtenemos al analizar la cadena `struct Pancakes;`.

    DeriveInput {
        --snip--

        ident: Ident {
            ident: "Pancakes",
            span: #0 bytes(95..103)
        },
        data: Struct(
            DataStruct {
                struct_token: Struct,
                fields: Unit,
                semi_token: Some(
                    Semi
                )
            }
        )
    }

Lista 19-32: La instancia `DeriveInput` que obtenemos al analizar el código que tiene el atributo de la macro en la Lista 19-30

Los campos de esta estructura muestran que el código de Rust que hemos analizado es un struct unitario con el `ident` (_identificador_, es decir, el nombre) de `Pancakes`. Hay más campos en esta estructura para describir todo tipo de código de Rust; consulte la documentación de `syn` para `DeriveInput` en *https://docs.rs/syn/1.0/syn/struct.DeriveInput.html* para obtener más información.

Pronto definiremos la función `impl_hello_macro`, que es donde construiremos el nuevo código de Rust que queremos incluir. Pero antes de hacerlo, tenga en cuenta que la salida de nuestra macro `derive` también es un `TokenStream`. El `TokenStream` devuelto se agrega al código que escriben los usuarios de nuestro crat, por lo que cuando compilan su crat, obtendrán la funcionalidad adicional que proporcionamos en el `TokenStream` modificado.

Es posible que hayas notado que estamos llamando a `unwrap` para hacer que la función `hello_macro_derive` se detenga con un error si la llamada a la función `syn::parse` falla aquí. Es necesario que nuestra macro procedimental se detenga con errores porque las funciones `proc_macro_derive` deben devolver `TokenStream` en lugar de `Result` para conformarse a la API de la macro procedimental. Hemos simplificado este ejemplo usando `unwrap`; en el código de producción, deberías proporcionar mensajes de error más específicos sobre lo que salió mal usando `panic!` o `expect`.

Ahora que tenemos el código para convertir el código de Rust anotado de un `TokenStream` en una instancia `DeriveInput`, generemos el código que implementa el trato `HelloMacro` en el tipo anotado, como se muestra en la Lista 19-33.

Nombre del archivo: `hello_macro_derive/src/lib.rs`

```rust
fn impl_hello_macro(ast: &syn::DeriveInput) -> TokenStream {
    let name = &ast.ident;
    let gen = quote! {
        impl HelloMacro for #name {
            fn hello_macro() {
                println!(
                    "¡Hola, Macro! Me llamo {}!",
                    stringify!(#name)
                );
            }
        }
    };
    gen.into()
}
```

Lista 19-33: Implementando el trato `HelloMacro` usando el código de Rust analizado

Obtenemos una instancia de la estructura `Ident` que contiene el nombre (identificador) del tipo anotado usando `ast.ident`. La estructura en la Lista 19-32 muestra que cuando ejecutamos la función `impl_hello_macro` en el código de la Lista 19-30, el `ident` que obtenemos tendrá el campo `ident` con un valor de `"Pancakes"`. Por lo tanto, la variable `name` en la Lista 19-33 contendrá una instancia de la estructura `Ident` que, cuando se imprima, será la cadena `"Pancakes"`, el nombre del struct en la Lista 19-30.

La macro `quote!` nos permite definir el código de Rust que queremos devolver. El compilador espera algo diferente al resultado directo de la ejecución de la macro `quote!`, por lo que necesitamos convertirla a un `TokenStream`. Hacemos esto llamando al método `into`, que consume esta representación intermedia y devuelve un valor del tipo `TokenStream` requerido.

La macro `quote!` también proporciona algunos mecanismos de plantilla muy geniales: podemos escribir `#name`, y `quote!` lo reemplazará con el valor de la variable `name`. Incluso puedes hacer algo de repetición similar a la forma en que funcionan las macros regulares. Consulte la documentación del crat `quote` en *https://docs.rs/quote* para una introducción exhaustiva.

Queremos que nuestra macro procedimental genere una implementación de nuestro trato `HelloMacro` para el tipo que el usuario anotó, que podemos obtener usando `#name`. La implementación del trato tiene la función `hello_macro`, cuyo cuerpo contiene la funcionalidad que queremos proporcionar: imprimir `¡Hola, Macro! Me llamo` y luego el nombre del tipo anotado.

La macro `stringify!` usada aquí está integrada en Rust. Toma una expresión de Rust, como `1 + 2`, y en tiempo de compilación convierte la expresión en un literal de cadena, como `"1 + 2"`. Esto es diferente de `format!` o `println!`, macros que evalúan la expresión y luego convierten el resultado en un `String`. Es posible que la entrada `#name` sea una expresión para imprimir literalmente, por lo que usamos `stringify!`. Usar `stringify!` también ahorra una asignación convirtiendo `#name` en un literal de cadena en tiempo de compilación.

En este momento, `cargo build` debería completarse con éxito tanto en `hello_macro` como en `hello_macro_derive`. Vamos a conectar estos crates al código de la Lista 19-30 para ver la macro procedimental en acción! Cree un nuevo proyecto binario en su directorio `project` usando `cargo new pancakes`. Necesitamos agregar `hello_macro` y `hello_macro_derive` como dependencias en el `Cargo.toml` del crat `pancakes`. Si publicas tus versiones de `hello_macro` y `hello_macro_derive` en *https://crates.io*, serían dependencias normales; si no, puedes especificarlas como dependencias de `path` de la siguiente manera:

    [dependencies]
    hello_macro = { path = "../hello_macro" }
    hello_macro_derive = { path = "../hello_macro/hello_macro_derive" }

Coloque el código de la Lista 19-30 en `src/main.rs`, y ejecute `cargo run`: debería imprimir `¡Hola, Macro! Me llamo Pancakes!` La implementación del trato `HelloMacro` de la macro procedimental se incluyó sin que el crat `pancakes` tuviera que implementarla; el `#[derive(HelloMacro)]` agregó la implementación del trato.

A continuación, exploremos cómo las otras clases de macros procedimentales difieren de las macros `derive` personalizadas.
