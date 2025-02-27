# Separando Módulos en Diferentes Archivos

Hasta ahora, todos los ejemplos de este capítulo han definido múltiples módulos en un solo archivo. Cuando los módulos se vuelven grandes, es posible que desees mover sus definiciones a un archivo separado para facilitar la navegación en el código.

Por ejemplo, comenzaremos con el código de la Lista 7-17 que tenía múltiples módulos de restaurante. Extraeremos los módulos a archivos en lugar de tener todos los módulos definidos en el archivo raíz del crat. En este caso, el archivo raíz del crat es `src/lib.rs`, pero este procedimiento también funciona con crates binarios cuyo archivo raíz del crat es `src/main.rs`.

Primero, extraeremos el módulo `front_of_house` a su propio archivo. Quite el código dentro de los corchetes del módulo `front_of_house`, dejando solo la declaración `mod front_of_house;`, de modo que `src/lib.rs` contenga el código mostrado en la Lista 7-21. Tenga en cuenta que esto no se compilará hasta que cree el archivo `src/front_of_house.rs` de la Lista 7-22.

Nombre de archivo: `src/lib.rs`

```rust
mod front_of_house;

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Lista 7-21: Declarando el módulo `front_of_house` cuyo cuerpo estará en `src/front_of_house.rs`

A continuación, coloque el código que estaba dentro de los corchetes en un nuevo archivo llamado `src/front_of_house.rs`, como se muestra en la Lista 7-22. El compilador sabe que debe buscar en este archivo porque encontró la declaración del módulo en la raíz del crat con el nombre `front_of_house`.

Nombre de archivo: `src/front_of_house.rs`

```rust
pub mod hosting {
    pub fn add_to_waitlist() {}
}
```

Lista 7-22: Definiciones dentro del módulo `front_of_house` en `src/front_of_house.rs`

Tenga en cuenta que solo necesita cargar un archivo usando una declaración `mod` _una vez_ en su árbol de módulos. Una vez que el compilador sabe que el archivo es parte del proyecto (y sabe dónde en el árbol de módulos reside el código debido a donde ha colocado la declaración `mod`), los otros archivos de su proyecto deben referirse al código del archivo cargado usando una ruta a donde se declaró, como se describe en "Rutas para Referirse a un Elemento en el Árbol de Módulos". En otras palabras, `mod` no es una operación de "incluir" que puede haber visto en otros lenguajes de programación.

A continuación, extraeremos el módulo `hosting` a su propio archivo. El proceso es un poco diferente porque `hosting` es un módulo hijo de `front_of_house`, no del módulo raíz. Colocaremos el archivo para `hosting` en un nuevo directorio que tendrá el nombre de sus ancestros en el árbol de módulos, en este caso _src/front_of_house_.

Para comenzar a mover `hosting`, cambiamos `src/front_of_house.rs` para que contenga solo la declaración del módulo `hosting`:

Nombre de archivo: `src/front_of_house.rs`

```rust
pub mod hosting;
```

Luego creamos un directorio `src/front_of_house` y un archivo `hosting.rs` para contener las definiciones hechas en el módulo `hosting`:

Nombre de archivo: `src/front_of_house/hosting.rs`

```rust
pub fn add_to_waitlist() {}
```

Si en lugar de eso ponemos `hosting.rs` en el directorio `src`, el compilador esperaría que el código de `hosting.rs` estuviera en un módulo `hosting` declarado en la raíz del crat, y no declarado como hijo del módulo `front_of_house`. Las reglas del compilador para determinar qué archivos buscar para el código de qué módulos significan que los directorios y archivos coinciden más estrechamente con el árbol de módulos.

> **Rutas de Archivo Alternativas**
>
> Hasta ahora hemos cubierto las rutas de archivo más idiómáticas que utiliza el compilador de Rust, pero Rust también admite un estilo más antiguo de ruta de archivo. Para un módulo llamado `front_of_house` declarado en la raíz del crat, el compilador buscará el código del módulo en:
>
> - `src/front_of_house.rs` (lo que hemos cubierto)
> - `src/front_of_house/mod.rs` (estilo antiguo, ruta todavía admitida)
>
> Para un módulo llamado `hosting` que es un submódulo de `front_of_house`, el compilador buscará el código del módulo en:
>
> - `src/front_of_house/hosting.rs` (lo que hemos cubierto)
> - `src/front_of_house/hosting/mod.rs` (estilo antiguo, ruta todavía admitida)
>
> Si utiliza ambos estilos para el mismo módulo, obtendrá un error del compilador. Se permite usar una mezcla de ambos estilos para diferentes módulos en el mismo proyecto, pero puede resultar confuso para las personas que navegan por su proyecto.
>
> La principal desventaja del estilo que utiliza archivos con el nombre `mod.rs` es que su proyecto puede terminar con muchos archivos con el nombre `mod.rs`, lo que puede resultar confuso cuando los tiene abiertos en su editor al mismo tiempo.

Hemos movido el código de cada módulo a un archivo separado, y el árbol de módulos permanece el mismo. Las llamadas a funciones en `eat_at_restaurant` funcionarán sin ninguna modificación, aunque las definiciones se encuentran en archivos diferentes. Esta técnica le permite mover los módulos a nuevos archivos a medida que crecen en tamaño.

Tenga en cuenta que la declaración `pub use crate::front_of_house::hosting` en `src/lib.rs` también no ha cambiado, ni `use` tiene ningún impacto en qué archivos se compilan como parte del crat. La palabra clave `mod` declara módulos, y Rust busca en un archivo con el mismo nombre que el módulo para el código que entra en ese módulo.
