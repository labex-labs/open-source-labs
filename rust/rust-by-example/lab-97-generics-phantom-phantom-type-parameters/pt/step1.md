# Parâmetros de Tipo Fantasma

Um parâmetro de tipo fantasma é aquele que não aparece em tempo de execução, mas é verificado estaticamente (e apenas) em tempo de compilação.

Tipos de dados podem usar parâmetros genéricos extras para atuar como marcadores ou para realizar verificações de tipo em tempo de compilação. Esses parâmetros extras não armazenam valores e não têm comportamento em tempo de execução.

No exemplo a seguir, combinamos `std::marker::PhantomData` com o conceito de parâmetro de tipo fantasma para criar tuplas contendo diferentes tipos de dados.

```rust
use std::marker::PhantomData;

// Uma estrutura de tupla fantasma genérica em `A` com parâmetro oculto `B`.
#[derive(PartialEq)] // Permite teste de igualdade para este tipo.
struct PhantomTuple<A, B>(A, PhantomData<B>);

// Uma estrutura de tipo fantasma genérica em `A` com parâmetro oculto `B`.
#[derive(PartialEq)] // Permite teste de igualdade para este tipo.
struct PhantomStruct<A, B> { first: A, phantom: PhantomData<B> }

// Nota: Armazenamento é alocado para o tipo genérico `A`, mas não para `B`.
//       Portanto, `B` não pode ser usado em cálculos.

fn main() {
    // Aqui, `f32` e `f64` são os parâmetros ocultos.
    // Tipo `PhantomTuple` especificado como `<char, f32>`.
    let _tuple1: PhantomTuple<char, f32> = PhantomTuple('Q', PhantomData);
    // Tipo `PhantomTuple` especificado como `<char, f64>`.
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

    // Erro em tempo de compilação! Incompatibilidade de tipos, portanto, não podem ser comparados:
    // println!("_tuple1 == _tuple2 yields: {}",
    //           _tuple1 == _tuple2);

    // Erro em tempo de compilação! Incompatibilidade de tipos, portanto, não podem ser comparados:
    // println!("_struct1 == _struct2 yields: {}",
    //           _struct1 == _struct2);
}
```
