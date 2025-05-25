# Caso de Teste: Esclarecimento de Unidades

Um método útil de conversões de unidades pode ser examinado implementando `Add` com um parâmetro de tipo fantasma. O traço `Add` é examinado abaixo:

```rust
// Esta construção imporia: `Self + RHS = Output`
// onde RHS assume o valor de Self se não especificado na implementação.
pub trait Add<RHS = Self> {
    type Output;

    fn add(self, rhs: RHS) -> Self::Output;
}

// `Output` deve ser `T<U>` para que `T<U> + T<U> = T<U>`.
impl<U> Add for T<U> {
    type Output = T<U>;
    ...
}
```

A implementação completa:

```rust
use std::ops::Add;
use std::marker::PhantomData;

/// Cria enumerações vazias para definir tipos de unidade.
#[derive(Debug, Clone, Copy)]
enum Inch {}
#[derive(Debug, Clone, Copy)]
enum Mm {}

/// `Length` é um tipo com parâmetro de tipo fantasma `Unit`,
/// e não é genérico em relação ao tipo de comprimento (ou seja, `f64`).
///
/// `f64` já implementa os traços `Clone` e `Copy`.
#[derive(Debug, Clone, Copy)]
struct Length<Unit>(f64, PhantomData<Unit>);

/// O traço `Add` define o comportamento do operador `+`.
impl<Unit> Add for Length<Unit> {
    type Output = Length<Unit>;

    // add() retorna uma nova estrutura `Length` contendo a soma.
    fn add(self, rhs: Length<Unit>) -> Length<Unit> {
        // `+` chama a implementação de `Add` para `f64`.
        Length(self.0 + rhs.0, PhantomData)
    }
}

fn main() {
    // Especifica `one_foot` para ter o parâmetro de tipo fantasma `Inch`.
    let one_foot:  Length<Inch> = Length(12.0, PhantomData);
    // `one_meter` tem o parâmetro de tipo fantasma `Mm`.
    let one_meter: Length<Mm>   = Length(1000.0, PhantomData);

    // `+` chama o método `add()` que implementamos para `Length<Unit>`.
    //
    // Como `Length` implementa `Copy`, `add()` não consome
    // `one_foot` e `one_meter`, mas os copia para `self` e `rhs`.
    let two_feet = one_foot + one_foot;
    let two_meters = one_meter + one_meter;

    // A adição funciona.
    println!("one foot + one_foot = {:?} in", two_feet.0);
    println!("one meter + one_meter = {:?} mm", two_meters.0);

    // Operações sem sentido falham como deveriam:
    // Erro em tempo de compilação: tipo incompatível.
    //let one_feter = one_foot + one_meter;
}
```
