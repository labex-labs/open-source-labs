# Vetores

Vetores são _arrays_ redimensionáveis. Assim como as _slices_, seu tamanho não é conhecido em tempo de compilação, mas eles podem crescer ou diminuir a qualquer momento. Um vetor é representado usando 3 parâmetros:

- ponteiro para os dados
- comprimento
- capacidade

A capacidade indica quanta memória é reservada para o vetor. O vetor pode crescer enquanto o comprimento for menor que a capacidade. Quando esse limite precisa ser ultrapassado, o vetor é realocado com uma capacidade maior.

```rust
fn main() {
    // Iteradores podem ser coletados em vetores
    let collected_iterator: Vec<i32> = (0..10).collect();
    println!("Coletado (0..10) em: {:?}", collected_iterator);

    // A macro `vec!` pode ser usada para inicializar um vetor
    let mut xs = vec![1i32, 2, 3];
    println!("Vetor inicial: {:?}", xs);

    // Insere um novo elemento no final do vetor
    println!("Push 4 no vetor");
    xs.push(4);
    println!("Vetor: {:?}", xs);

    // Erro! Vetores imutáveis não podem crescer
    collected_iterator.push(0);
    // FIXME ^ Comente esta linha

    // O método `len` retorna o número de elementos atualmente armazenados em um vetor
    println!("Comprimento do vetor: {}", xs.len());

    // Indexação é feita usando colchetes (a indexação começa em 0)
    println!("Segundo elemento: {}", xs[1]);

    // `pop` remove o último elemento do vetor e o retorna
    println!("Pop último elemento: {:?}", xs.pop());

    // Indexação fora dos limites resulta em um pânico
    println!("Quarto elemento: {}", xs[3]);
    // FIXME ^ Comente esta linha

    // Vetores podem ser facilmente iterados
    println!("Conteúdo de xs:");
    for x in xs.iter() {
        println!("> {}", x);
    }

    // Um `Vector` também pode ser iterado enquanto a contagem da iteração
    // é enumerada em uma variável separada (`i`)
    for (i, x) in xs.iter().enumerate() {
        println!("Na posição {} temos o valor {}", i, x);
    }

    // Graças ao `iter_mut`, `Vector`s mutáveis também podem ser iterados
    // de uma forma que permite modificar cada valor
    for x in xs.iter_mut() {
        *x *= 3;
    }
    println!("Vetor atualizado: {:?}", xs);
}
```

Mais métodos `Vec` podem ser encontrados no módulo `std::vec`
