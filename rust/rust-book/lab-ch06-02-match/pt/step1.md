# A Construção de Fluxo de Controle `match`

Rust possui uma construção de fluxo de controle extremamente poderosa chamada `match` que permite comparar um valor com uma série de padrões e, em seguida, executar código com base em qual padrão corresponde. Os padrões podem ser compostos por valores literais, nomes de variáveis, curingas e muitas outras coisas; o Capítulo 18 cobre todos os diferentes tipos de padrões e o que eles fazem. O poder do `match` vem da expressividade dos padrões e do fato de que o compilador confirma que todos os casos possíveis são tratados.

Pense em uma expressão `match` como uma máquina de classificação de moedas: as moedas deslizam por uma trilha com orifícios de vários tamanhos ao longo dela, e cada moeda cai pelo primeiro orifício que encontra e que cabe nela. Da mesma forma, os valores passam por cada padrão em um `match`, e no primeiro padrão em que o valor "se encaixa", o valor cai no bloco de código associado para ser usado durante a execução.

Falando em moedas, vamos usá-las como exemplo usando `match`! Podemos escrever uma função que recebe uma moeda dos EUA desconhecida e, de maneira semelhante à máquina de contagem, determina qual moeda é e retorna seu valor em centavos, conforme mostrado na Listagem 6-3.

```rust
1 enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
  2 match coin {
      3 Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```

Listagem 6-3: Um enum e uma expressão `match` que tem as variantes do enum como seus padrões

Vamos detalhar o `match` na função `value_in_cents`. Primeiro, listamos a palavra-chave `match` seguida por uma expressão, que neste caso é o valor `coin` \[2]. Isso parece muito semelhante a uma expressão usada com `if`, mas há uma grande diferença: com `if`, a expressão precisa retornar um valor booleano, mas aqui ela pode retornar qualquer tipo. O tipo de `coin` neste exemplo é o enum `Coin` que definimos em \[1].

Em seguida, vêm os braços `match`. Um braço tem duas partes: um padrão e algum código. O primeiro braço aqui tem um padrão que é o valor `Coin::Penny` e, em seguida, o operador `=>` que separa o padrão e o código a ser executado \[3]. O código neste caso é apenas o valor `1`. Cada braço é separado do próximo por uma vírgula.

Quando a expressão `match` é executada, ela compara o valor resultante com o padrão de cada braço, em ordem. Se um padrão corresponder ao valor, o código associado a esse padrão é executado. Se esse padrão não corresponder ao valor, a execução continua para o próximo braço, assim como em uma máquina de classificação de moedas. Podemos ter quantos braços precisarmos: na Listagem 6-3, nosso `match` tem quatro braços.

O código associado a cada braço é uma expressão, e o valor resultante da expressão no braço correspondente é o valor que é retornado para toda a expressão `match`.

Normalmente, não usamos chaves se o código do braço match for curto, como é na Listagem 6-3, onde cada braço apenas retorna um valor. Se você quiser executar várias linhas de código em um braço match, você deve usar chaves, e a vírgula após o braço é então opcional. Por exemplo, o código a seguir imprime "Lucky penny!" toda vez que o método é chamado com um `Coin::Penny`, mas ainda retorna o último valor do bloco, `1`:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        }
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}
```
