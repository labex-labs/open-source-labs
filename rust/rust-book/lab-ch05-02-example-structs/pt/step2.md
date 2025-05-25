# Refatorando com Tuplas

A Listagem 5-9 mostra outra versão do nosso programa que usa tuplas.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "The area of the rectangle is {} square pixels.",
      1 area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
  2 dimensions.0 * dimensions.1
}
```

Listagem 5-9: Especificando a largura e a altura do retângulo com uma tupla

De certa forma, este programa é melhor. As tuplas nos permitem adicionar um pouco de estrutura, e agora estamos passando apenas um argumento \[1]. Mas, de outra forma, esta versão é menos clara: as tuplas não nomeiam seus elementos, então temos que indexar as partes da tupla \[2], tornando nosso cálculo menos óbvio.

Trocar a largura e a altura não faria diferença para o cálculo da área, mas se quisermos desenhar o retângulo na tela, faria! Teríamos que ter em mente que `largura` é o índice da tupla `0` e `altura` é o índice da tupla `1`. Isso seria ainda mais difícil para outra pessoa descobrir e ter em mente se fosse usar nosso código. Como não transmitimos o significado de nossos dados em nosso código, agora é mais fácil introduzir erros.
