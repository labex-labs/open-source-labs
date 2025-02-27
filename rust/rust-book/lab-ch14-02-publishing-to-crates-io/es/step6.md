# Exportando una API Pública Conveniente con `pub use`

La estructura de tu API pública es una consideración importante al publicar una caja. Las personas que usan tu caja son menos familiarizadas con la estructura que tú y pueden tener dificultades para encontrar los componentes que desean usar si tu caja tiene una gran jerarquía de módulos.

En el Capítulo 7, cubrimos cómo hacer que los elementos sean públicos utilizando la palabra clave `pub` y cómo traer elementos a un ámbito con la palabra clave `use`. Sin embargo, la estructura que tiene sentido para ti mientras desarrollas una caja puede no ser muy conveniente para tus usuarios. Puedes querer organizar tus structs en una jerarquía que contenga varios niveles, pero luego las personas que quieran usar un tipo que has definido profundamente en la jerarquía pueden tener problemas para descubrir que existe ese tipo. También pueden molestarles tener que escribir `use` `my_crate::`algún_módulo`::`otro_módulo`::`TipoÚtil`;` en lugar de `use` `my_crate::`TipoÚtil`;`.

La buena noticia es que si la estructura _no_ es conveniente para que otros la usen desde otra biblioteca, no tienes que reorganizar tu organización interna: en cambio, puedes re-exportar elementos para crear una estructura pública diferente a tu estructura privada utilizando `pub use`. _Re-exportar_ toma un elemento público en un lugar y lo hace público en otro lugar, como si estuviera definido en el otro lugar en lugar de aquí.

Por ejemplo, digamos que creamos una biblioteca llamada `art` para modelar conceptos artísticos. Dentro de esta biblioteca hay dos módulos: un módulo `kinds` que contiene dos enum denominados `PrimaryColor` y `SecondaryColor` y un módulo `utils` que contiene una función llamada `mix`, como se muestra en la Lista 14-3.

Nombre del archivo: `src/lib.rs`

```rust
//! # Arte
//!
//! Una biblioteca para modelar conceptos artísticos.

pub mod kinds {
    /// Los colores primarios de acuerdo con el modelo de color RYB.
    pub enum PrimaryColor {
        Red,
        Yellow,
        Blue,
    }

    /// Los colores secundarios de acuerdo con el modelo de color RYB.
    pub enum SecondaryColor {
        Orange,
        Green,
        Purple,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// Combina dos colores primarios en cantidades iguales para crear
    /// un color secundario.
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

Lista 14-3: Una biblioteca `art` con elementos organizados en los módulos `kinds` y `utils`

La Figura 14-3 muestra cómo se vería la página principal de la documentación de esta caja generada por `cargo doc`.

Figura 14-3: Página principal de la documentación de `art` que lista los módulos `kinds` y `utils`

Observa que los tipos `PrimaryColor` y `SecondaryColor` no se listan en la página principal, ni tampoco la función `mix`. Tenemos que hacer clic en `kinds` y `utils` para verlos.

Otra caja que depende de esta biblioteca necesitaría declaraciones `use` que traigan los elementos de `art` al ámbito, especificando la estructura de módulos que se define actualmente. La Lista 14-4 muestra un ejemplo de una caja que utiliza los elementos `PrimaryColor` y `mix` de la caja `art`.

Nombre del archivo: `src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}
```

Lista 14-4: Una caja que utiliza los elementos de la caja `art` con su estructura interna exportada

El autor del código de la Lista 14-4, que utiliza la caja `art`, tuvo que averiguar que `PrimaryColor` está en el módulo `kinds` y `mix` está en el módulo `utils`. La estructura de módulos de la caja `art` es más relevante para los desarrolladores que trabajan en la caja `art` que para aquellos que la usan. La estructura interna no contiene ninguna información útil para alguien que intenta entender cómo usar la caja `art`, sino que más bien causa confusión porque los desarrolladores que la usan tienen que averiguar dónde buscar y deben especificar los nombres de los módulos en las declaraciones `use`.

Para eliminar la organización interna de la API pública, podemos modificar el código de la caja `art` de la Lista 14-3 para agregar declaraciones `pub use` para re-exportar los elementos en el nivel superior, como se muestra en la Lista 14-5.

Nombre del archivo: `src/lib.rs`

```rust
//! # Arte
//!
//! Una biblioteca para modelar conceptos artísticos.

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

Lista 14-5: Agregando declaraciones `pub use` para re-exportar elementos

La documentación de API que `cargo doc` genera para esta caja ahora listará y enlazará los re-exports en la página principal, como se muestra en la Figura 14-4, lo que hace que los tipos `PrimaryColor` y `SecondaryColor` y la función `mix` sean más fáciles de encontrar.

Figura 14-4: La página principal de la documentación de `art` que lista los re-exports

Los usuarios de la caja `art` todavía pueden ver y usar la estructura interna de la Lista 14-3 como se demuestra en la Lista 14-4, o pueden usar la estructura más conveniente de la Lista 14-5, como se muestra en la Lista 14-6.

Nombre del archivo: `src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

Lista 14-6: Un programa que utiliza los elementos re-exportados de la caja `art`

En casos donde hay muchos módulos anidados, re-exportar los tipos en el nivel superior con `pub use` puede marcar una gran diferencia en la experiencia de las personas que usan la caja. Otro uso común de `pub use` es re-exportar definiciones de una dependencia en la caja actual para que las definiciones de esa caja formen parte de la API pública de tu caja.

Crear una estructura de API pública útil es más un arte que una ciencia, y puedes iterar para encontrar la API que funcione mejor para tus usuarios. Elegir `pub use` te da flexibilidad en cómo estructuras tu caja internamente y desacopla esa estructura interna de lo que presentas a tus usuarios. Echa un vistazo al código de algunas de las cajas que has instalado para ver si su estructura interna difiere de su API pública.
