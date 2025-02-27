# Parámetros de Tipo Genéricos Predeterminados y Sobrecarga de Operadores

Cuando usamos parámetros de tipo genéricos, podemos especificar un tipo concrete predeterminado para el tipo genérico. Esto elimina la necesidad de que los implementadores del trait especifiquen un tipo concrete si el tipo predeterminado funciona. Se especifica un tipo predeterminado al declarar un tipo genérico con la sintaxis `<`TipoMarcador`=`TipoConcreto`>`.

Un gran ejemplo de una situación en la que esta técnica es útil es con la _sobrecarga de operadores_, en la que se personaliza el comportamiento de un operador (como `+`) en situaciones particulares.

Rust no te permite crear tus propios operadores o sobrecargar operadores arbitrarios. Pero puedes sobrecargar las operaciones y los traits correspondientes enumerados en `std::ops` al implementar los traits asociados al operador. Por ejemplo, en la Lista 19-14 sobrecargamos el operador `+` para sumar dos instancias de `Point`. Hacemos esto al implementar el trait `Add` en una struct `Point`.

Nombre de archivo: `src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Lista 19-14: Implementando el trait `Add` para sobrecargar el operador `+` para instancias de `Point`

El método `add` suma los valores de `x` de dos instancias de `Point` y los valores de `y` de dos instancias de `Point` para crear un nuevo `Point`. El trait `Add` tiene un tipo asociado llamado `Output` que determina el tipo devuelto por el método `add`.

El tipo genérico predeterminado en este código está dentro del trait `Add`. Aquí está su definición:

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

Este código debería parecer generalmente familiar: un trait con un método y un tipo asociado. La parte nueva es `Rhs=Self`: esta sintaxis se llama _parámetros de tipo predeterminados_. El parámetro de tipo genérico `Rhs` (abreviatura de "lado derecho") define el tipo del parámetro `rhs` en el método `add`. Si no especificamos un tipo concrete para `Rhs` cuando implementamos el trait `Add`, el tipo de `Rhs` tendrá como valor predeterminado `Self`, que será el tipo en el que estamos implementando `Add`.

Cuando implementamos `Add` para `Point`, usamos el valor predeterminado para `Rhs` porque queríamos sumar dos instancias de `Point`. Veamos un ejemplo de implementación del trait `Add` donde queremos personalizar el tipo `Rhs` en lugar de usar el valor predeterminado.

Tenemos dos structs, `Millimeters` y `Meters`, que almacenan valores en diferentes unidades. Este envoltorio delgado de un tipo existente en otra struct se conoce como el _patrón newtype_, que describiremos con más detalle en "Usando el Patrón newtype para Implementar Traits Externos en Tipos Externos". Queremos sumar valores en milímetros a valores en metros y que la implementación de `Add` haga la conversión correctamente. Podemos implementar `Add` para `Millimeters` con `Meters` como `Rhs`, como se muestra en la Lista 19-15.

Nombre de archivo: `src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

Lista 19-15: Implementando el trait `Add` en `Millimeters` para sumar `Millimeters` y `Meters`

Para sumar `Millimeters` y `Meters`, especificamos `impl Add<Meters>` para establecer el valor del parámetro de tipo `Rhs` en lugar de usar el valor predeterminado de `Self`.

Usarás los parámetros de tipo predeterminados de dos maneras principales:

1.  Para extender un tipo sin romper el código existente
2.  Para permitir la personalización en casos específicos que la mayoría de los usuarios no necesitarán

El trait `Add` de la biblioteca estándar es un ejemplo del segundo propósito: por lo general, sumarás dos tipos similares, pero el trait `Add` proporciona la capacidad de personalizar más allá de eso. Usar un parámetro de tipo predeterminado en la definición del trait `Add` significa que no tienes que especificar el parámetro extra la mayor parte del tiempo. En otras palabras, no se necesita un poco de código de implementación repetitivo, lo que hace que sea más fácil usar el trait.

El primer propósito es similar al segundo pero al revés: si quieres agregar un parámetro de tipo a un trait existente, puedes darle un valor predeterminado para permitir la extensión de la funcionalidad del trait sin romper el código de implementación existente.
