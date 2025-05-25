# Arrays e Slices

Um array é uma coleção de objetos do mesmo tipo `T`, armazenados em memória contígua. Arrays são criados usando colchetes `[]`, e seu comprimento, que é conhecido em tempo de compilação, faz parte de sua assinatura de tipo `[T; length]`.

Slices são semelhantes a arrays, mas seu comprimento não é conhecido em tempo de compilação. Em vez disso, um slice é um objeto de duas palavras; a primeira palavra é um ponteiro para os dados, a segunda palavra é o comprimento do slice. O tamanho da palavra é o mesmo que usize, determinado pela arquitetura do processador, por exemplo, 64 bits em um x86-64. Slices podem ser usados para emprestar (borrow) uma seção de um array e têm a assinatura de tipo `&[T]`.

```rust
use std::mem;

// Esta função empresta um slice.
fn analyze_slice(slice: &[i32]) {
    println!("Primeiro elemento do slice: {}", slice[0]);
    println!("O slice tem {} elementos", slice.len());
}

fn main() {
    // Array de tamanho fixo (assinatura de tipo é supérflua).
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // Todos os elementos podem ser inicializados com o mesmo valor.
    let ys: [i32; 500] = [0; 500];

    // Indexação começa em 0.
    println!("Primeiro elemento do array: {}", xs[0]);
    println!("Segundo elemento do array: {}", xs[1]);

    // `len` retorna a contagem de elementos no array.
    println!("Número de elementos no array: {}", xs.len());

    // Arrays são alocados na pilha (stack).
    println!("Array ocupa {} bytes", mem::size_of_val(&xs));

    // Arrays podem ser automaticamente emprestados como slices.
    println!("Emprestar o array inteiro como um slice.");
    analyze_slice(&xs);

    // Slices podem apontar para uma seção de um array.
    // Eles têm a forma [índice_inicial..índice_final].
    // `índice_inicial` é a primeira posição no slice.
    // `índice_final` é um a mais que a última posição no slice.
    println!("Emprestar uma seção do array como um slice.");
    analyze_slice(&ys[1 .. 4]);

    // Exemplo de slice vazio `&[]`:
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // Mesmo, mas mais verboso

    // Arrays podem ser acessados com segurança usando `.get`, que retorna um
    // `Option`. Isso pode ser combinado como mostrado abaixo, ou usado com
    // `.expect()` se você quiser que o programa saia com uma boa
    // mensagem em vez de continuar alegremente.
    for i in 0..xs.len() + 1 { // Oops, um elemento muito longe!
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("Devagar! {} está muito longe!", i),
        }
    }

    // Indexação fora dos limites no array causa erro em tempo de compilação.
    //println!("{}", xs[5]);
    // Indexação fora dos limites no slice causa erro em tempo de execução.
    //println!("{}", xs[..][5]);
}
```
