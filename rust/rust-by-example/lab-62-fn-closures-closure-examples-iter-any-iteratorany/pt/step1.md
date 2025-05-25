# Iterator::any

`Iterator::any` é uma função que, quando recebe um iterador, retorna `true` se algum elemento satisfazer o predicado. Caso contrário, retorna `false`. Sua assinatura:

```rust
pub trait Iterator {
    // O tipo sendo iterado.
    type Item;

    // `any` recebe `&mut self`, significando que o chamador pode ser emprestado
    // e modificado, mas não consumido.
    fn any<F>(&mut self, f: F) -> bool where
        // `FnMut`, significando que qualquer variável capturada pode, no máximo, ser
        // modificada, não consumida. `Self::Item` indica que a função recebe
        // argumentos para a closure por valor.
        F: FnMut(Self::Item) -> bool;
}
```

```rust
fn main() {
    let vec1 = vec![1, 2, 3];
    let vec2 = vec![4, 5, 6];

    // `iter()` para vetores retorna `&i32`. Desestruture para `i32`.
    println!("2 em vec1: {}", vec1.iter()     .any(|&x| x == 2));
    // `into_iter()` para vetores retorna `i32`. Nenhuma desestruturação necessária.
    println!("2 em vec2: {}", vec2.into_iter().any(|x| x == 2));

    // `iter()` apenas empresta `vec1` e seus elementos, então eles podem ser usados novamente
    println!("tamanho de vec1: {}", vec1.len());
    println!("Primeiro elemento de vec1 é: {}", vec1[0]);
    // `into_iter()` move `vec2` e seus elementos, então eles não podem ser usados novamente
    // println!("Primeiro elemento de vec2 é: {}", vec2[0]);
    // println!("tamanho de vec2: {}", vec2.len());
    // TODO: descomente as duas linhas acima e veja os erros do compilador.

    let array1 = [1, 2, 3];
    let array2 = [4, 5, 6];

    // `iter()` para arrays retorna `&i32`.
    println!("2 em array1: {}", array1.iter()     .any(|&x| x == 2));
    // `into_iter()` para arrays retorna `i32`.
    println!("2 em array2: {}", array2.into_iter().any(|x| x == 2));
}
```
