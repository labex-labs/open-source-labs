# Caso de prueba: aclaración de unidades

Un método útil de conversiones de unidades puede ser examinado implementando `Add` con un parámetro de tipo fantasma. El trato `Add` se examina a continuación:

```rust
// Esta construcción impondría: `Self + RHS = Output`
// donde RHS tiene como valor predeterminado Self si no se especifica en la implementación.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` debe ser `T<U>` para que `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
  ...
}
```

La implementación completa:

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// Crea enumeraciones vacías para definir tipos de unidad.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` es un tipo con parámetro de tipo fantasma `Unit`,
/// y no es genérico sobre el tipo de longitud (es decir `f64`).
///
/// `f64` ya implementa los tratados `Clone` y `Copy`.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// El trato `Add` define el comportamiento del operador `+`.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() devuelve un nuevo struct `Length` que contiene la suma.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` llama a la implementación de `Add` para `f64`.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // Especifica que `one_foot` tiene el parámetro de tipo fantasma `Inch`.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` tiene el parámetro de tipo fantasma `Mm`.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` llama al método `add()` que implementamos para `Length<Unit>`.
    //
    // Dado que `Length` implementa `Copy`, `add()` no consume
    // `one_foot` y `one_meter` sino que los copia en `self` y `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // La adición funciona.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Las operaciones absurdas fallan como deben:
    // Error de compilación: error de tipo de desajuste.
    //let one_feter = one_foot + one_meter;
}
```
