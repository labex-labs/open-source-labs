# Usando Box`<T>` para Armazenar Dados no Heap

Antes de discutirmos o caso de uso de armazenamento no heap para `Box<T>`, abordaremos a sintaxe e como interagir com valores armazenados dentro de um `Box<T>`.

A Listagem 15-1 mostra como usar uma box para armazenar um valor `i32` no heap.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let b = Box::new(5);
    println!("b = {b}");
}
```

Listagem 15-1: Armazenando um valor `i32` no heap usando uma box

Definimos a variável `b` para ter o valor de um `Box` que aponta para o valor `5`, que é alocado no heap. Este programa imprimirá `b = 5`; neste caso, podemos acessar os dados na box de forma semelhante a como faríamos se esses dados estivessem na stack. Assim como qualquer valor próprio, quando uma box sai do escopo, como `b` faz no final de `main`, ela será desalocada. A desalocação acontece tanto para a box (armazenada na stack) quanto para os dados aos quais ela aponta (armazenados no heap).

Colocar um único valor no heap não é muito útil, então você não usará boxes por si só dessa maneira com muita frequência. Ter valores como um único `i32` na stack, onde eles são armazenados por padrão, é mais apropriado na maioria das situações. Vamos analisar um caso em que as boxes nos permitem definir tipos que não poderíamos definir se não tivéssemos boxes.
