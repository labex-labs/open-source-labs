# Procurando em iteradores

`Iterator::find` é uma função que itera sobre um iterador e procura o primeiro valor que satisfaz alguma condição. Se nenhum dos valores satisfazer a condição, retorna `None`. Sua assinatura:

```rust
pub trait Iterator {
    // O tipo sendo iterado.
    type Item;

    // `find` recebe `&mut self`, significando que o chamador pode ser emprestado
    // e modificado, mas não consumido.
    fn find<P>(&mut self, predicate: P) -> Option<Self::Item> where
        // `FnMut` significando que qualquer variável capturada pode no máximo ser
        // modificada, não consumida. `&Self::Item` indica que recebe argumentos para o fechamento por referência.
        P: FnMut(&Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` para vetores retorna `&i32`.
    let mut iter = vec1.iter();
    // `into_iter()` para vetores retorna `i32`.
    let mut into_iter = vec2.into_iter();

    // `iter()` para vetores retorna `&i32`, e queremos referenciar um de seus
    // itens, então precisamos desestruturar `&&i32` para `i32`
    println!("Encontrar 2 em vec1: {:?}", iter     .find(|&&x| x == 2));
    // `into_iter()` para vetores retorna `i32`, e queremos referenciar um de seus
    // itens, então precisamos desestruturar `&i32` para `i32`
    println!("Encontrar 2 em vec2: {:?}", into_iter.find(| &x| x == 2));

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` para arrays retorna `&&i32`
    println!("Encontrar 2 em array1: {:?}", array1.iter()     .find(|&&x| x == 2));
    // `into_iter()` para arrays retorna `&i32`
    println!("Encontrar 2 em array2: {:?}", array2.into_iter().find(|&x| x == 2));
}
```

`Iterator::find` fornece uma referência ao item. Mas se você quiser o _índice_ do item, use `Iterator::position`.

```rust
fn main() {
    let vec = vec![1, 9, 3, 3, 13, 2];

    // `iter()` para vetores retorna `&i32` e `position()` não recebe uma referência, então
    // precisamos desestruturar `&i32` para `i32`
    let index_of_first_even_number = vec.iter().position(|&x| x % 2 == 0);
    assert_eq!(index_of_first_even_number, Some(5));

    // `into_iter()` para vetores retorna `i32` e `position()` não recebe uma referência, então
    // não precisamos desestruturar
    let index_of_first_negative_number = vec.into_iter().position(|x| x < 0);
    assert_eq!(index_of_first_negative_number, None);
}
```
