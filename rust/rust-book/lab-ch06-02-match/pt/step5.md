# Padrões Catch-all e o Placeholder \_

Usando enums, também podemos tomar ações especiais para alguns valores particulares, mas para todos os outros valores tomar uma ação padrão. Imagine que estamos implementando um jogo onde, se você rolar um 3 em uma jogada de dados, seu jogador não se move, mas em vez disso ganha um novo chapéu chique. Se você rolar um 7, seu jogador perde um chapéu chique. Para todos os outros valores, seu jogador se move aquele número de espaços no tabuleiro do jogo. Aqui está um `match` que implementa essa lógica, com o resultado da jogada de dados hardcoded em vez de um valor aleatório, e toda a outra lógica representada por funções sem corpos porque implementá-las realmente está fora do escopo deste exemplo:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
  1 other => move_player(other),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn move_player(num_spaces: u8) {}
```

Para os dois primeiros braços, os padrões são os valores literais `3` e `7`. Para o último braço que cobre todos os outros valores possíveis, o padrão é a variável que escolhemos nomear `other` \[1]. O código que é executado para o braço `other` usa a variável passando-a para a função `move_player`.

Este código compila, mesmo que não tenhamos listado todos os valores possíveis que um `u8` pode ter, porque o último padrão corresponderá a todos os valores não listados especificamente. Este padrão catch-all atende ao requisito de que `match` deve ser exaustivo. Observe que temos que colocar o braço catch-all por último porque os padrões são avaliados em ordem. Se colocarmos o braço catch-all antes, os outros braços nunca serão executados, então o Rust nos avisará se adicionarmos braços após um catch-all!

O Rust também tem um padrão que podemos usar quando queremos um catch-all, mas não queremos _usar_ o valor no padrão catch-all: `_` é um padrão especial que corresponde a qualquer valor e não se vincula a esse valor. Isso diz ao Rust que não vamos usar o valor, então o Rust não nos avisará sobre uma variável não utilizada.

Vamos mudar as regras do jogo: agora, se você rolar qualquer coisa diferente de 3 ou 7, você deve rolar novamente. Não precisamos mais usar o valor catch-all, então podemos mudar nosso código para usar `_` em vez da variável chamada `other`:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
fn reroll() {}
```

Este exemplo também atende ao requisito de exaustividade porque estamos explicitamente ignorando todos os outros valores no último braço; não esquecemos nada.

Finalmente, mudaremos as regras do jogo mais uma vez para que nada mais aconteça na sua vez se você rolar qualquer coisa diferente de 3 ou 7. Podemos expressar isso usando o valor unitário (o tipo de tupla vazio que mencionamos em "O Tipo de Tupla") como o código que acompanha o braço `_`:

```rust
let dice_roll = 9;
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}

fn add_fancy_hat() {}
fn remove_fancy_hat() {}
```

Aqui, estamos dizendo ao Rust explicitamente que não vamos usar nenhum outro valor que não corresponda a um padrão em um braço anterior, e não queremos executar nenhum código neste caso.

Há mais sobre padrões e correspondência que abordaremos no Capítulo 18. Por enquanto, vamos passar para a sintaxe `if let`, que pode ser útil em situações em que a expressão `match` é um pouco prolixa.
