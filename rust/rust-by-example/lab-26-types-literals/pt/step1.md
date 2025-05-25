# Literais

Literais numéricos podem ser anotados com o tipo adicionando o tipo como sufixo. Por exemplo, para especificar que o literal `42` deve ter o tipo `i32`, escreva `42i32`.

O tipo de literais numéricos sem sufixo dependerá de como eles são usados. Se nenhuma restrição existir, o compilador usará `i32` para inteiros e `f64` para números de ponto flutuante.

```rust
fn main() {
    // Literais com sufixo, seus tipos são conhecidos na inicialização
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Literais sem sufixo, seus tipos dependem de como são usados
    let i = 1;
    let f = 1.0;

    // `size_of_val` retorna o tamanho de uma variável em bytes
    println!("tamanho de `x` em bytes: {}", std::mem::size_of_val(&x));
    println!("tamanho de `y` em bytes: {}", std::mem::size_of_val(&y));
    println!("tamanho de `z` em bytes: {}", std::mem::size_of_val(&z));
    println!("tamanho de `i` em bytes: {}", std::mem::size_of_val(&i));
    println!("tamanho de `f` em bytes: {}", std::mem::size_of_val(&f));
}
```

Há alguns conceitos usados no código anterior que ainda não foram explicados. Aqui está uma breve explicação para os leitores impacientes:

- `std::mem::size_of_val` é uma função, mas chamada com seu _caminho completo_. O código pode ser dividido em unidades lógicas chamadas _módulos_. Neste caso, a função `size_of_val` é definida no módulo `mem`, e o módulo `mem` é definido no _crate_ `std`. Para mais detalhes, consulte módulos e crates.
