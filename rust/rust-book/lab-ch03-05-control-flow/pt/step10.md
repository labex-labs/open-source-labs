# Iterando por uma Coleção com `for`

Você pode optar por usar a construção `while` para iterar sobre os elementos de uma coleção, como um array. Por exemplo, o loop na Listagem 3-4 imprime cada elemento no array `a`.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;

    while index < 5 {
        println!("the value is: {}", a[index]);

        index += 1;
    }
}
```

Listagem 3-4: Iterando por cada elemento de uma coleção usando um loop `while`

Aqui, o código conta até os elementos no array. Ele começa no índice `0` e, em seguida, itera até atingir o índice final no array (ou seja, quando `index < 5` não é mais `true`). Executar este código imprimirá cada elemento no array:

```bash
$ cargo run
   Compiling loops v0.1.0 (file:///projects/loops)
    Finished dev [unoptimized + debuginfo] target(s) in 0.32s
     Running `target/debug/loops`
the value is: 10
the value is: 20
the value is: 30
the value is: 40
the value is: 50
```

Todos os cinco valores do array aparecem no terminal, como esperado. Embora `index` atinja um valor de `5` em algum momento, o loop para de executar antes de tentar buscar um sexto valor do array.

No entanto, essa abordagem é propensa a erros; poderíamos fazer com que o programa entrasse em pânico se o valor do índice ou a condição de teste estiverem incorretos. Por exemplo, se você alterasse a definição do array `a` para ter quatro elementos, mas esquecesse de atualizar a condição para `while index < 4`, o código entraria em pânico. Também é lento, porque o compilador adiciona código em tempo de execução para realizar a verificação condicional de se o índice está dentro dos limites do array em cada iteração do loop.

Como uma alternativa mais concisa, você pode usar um loop `for` e executar algum código para cada item em uma coleção. Um loop `for` se parece com o código na Listagem 3-5.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let a = [10, 20, 30, 40, 50];

    for element in a {
        println!("the value is: {element}");
    }
}
```

Listagem 3-5: Iterando por cada elemento de uma coleção usando um loop `for`

Quando executamos este código, veremos a mesma saída que na Listagem 3-4. Mais importante, agora aumentamos a segurança do código e eliminamos a chance de bugs que podem resultar de ir além do final do array ou não ir longe o suficiente e perder alguns itens.

Usando o loop `for`, você não precisaria se lembrar de alterar nenhum outro código se alterasse o número de valores no array, como faria com o método usado na Listagem 3-4.

A segurança e a concisão dos loops `for` os tornam a construção de loop mais comumente usada em Rust. Mesmo em situações em que você deseja executar algum código um certo número de vezes, como no exemplo de contagem regressiva que usou um loop `while` na Listagem 3-3, a maioria dos Rustaceans usaria um loop `for`. A maneira de fazer isso seria usar um `Range`, fornecido pela biblioteca padrão, que gera todos os números em sequência, começando de um número e terminando antes de outro número.

Aqui está como a contagem regressiva ficaria usando um loop `for` e outro método que ainda não discutimos, `rev`, para reverter o intervalo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");
}
```

Este código é um pouco melhor, não é?
