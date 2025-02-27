# Parámetros de tipo fantasma

Un parámetro de tipo fantasma es aquel que no aparece en tiempo de ejecución, pero se comprueba en tiempo de compilación (y solo) de manera estática.

Los tipos de datos pueden usar parámetros de tipo genéricos adicionales para actuar como marcadores o para realizar comprobaciones de tipo en tiempo de compilación. Estos parámetros adicionales no tienen valores de almacenamiento y no tienen comportamiento en tiempo de ejecución.

En el siguiente ejemplo, combinamos \[std::marker::PhantomData\] con el concepto de parámetro de tipo fantasma para crear tuplas que contengan diferentes tipos de datos.

```rust
use std::marker::PhantomData;

// Una struct de tupla fantasma que es genérica sobre `A` con parámetro oculto `B`.
#[derive(PartialEq)] // Permite la prueba de igualdad para este tipo.
struct PhantomTuple<A, B>(A, PhantomData<B>);

// Una struct de tipo fantasma que es genérica sobre `A` con parámetro oculto `B`.
#[derive(PartialEq)] // Permite la prueba de igualdad para este tipo.
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// Nota: Se asigna almacenamiento para el tipo genérico `A`, pero no para `B`.
//       Por lo tanto, `B` no se puede usar en cálculos.

fn main() {
    // Aquí, `f32` y `f64` son los parámetros ocultos.
    // Tipo PhantomTuple especificado como `<char, f32>`.
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // Tipo PhantomTuple especificado como `<char, f64>`.
    let _tuple2: PhantomTuple<char, f64> = PhantomTuple('Q', PhantomData);

    // Tipo especificado como `<char, f32>`.
    let _struct1: PhantomStruct<char, f32> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };
    // Tipo especificado como `<char, f64>`.
    let _struct2: PhantomStruct<char, f64> = PhantomStruct {
        first: 'Q',
        phantom: PhantomData,
    };

    // ¡Error de compilación! Hay un desajuste de tipos, por lo que no se pueden comparar:
    // println!("_tuple1 == _tuple2 produce: {}",
    //           _tuple1 == _tuple2);

    // ¡Error de compilación! Hay un desajuste de tipos, por lo que no se pueden comparar:
    // println!("_struct1 == _struct2 produce: {}",
    //           _struct1 == _struct2);
}
```
