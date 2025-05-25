# Correspondência de Variáveis Nomeadas (Matching Named Variables)

Variáveis nomeadas são padrões irrefutáveis que correspondem a qualquer valor, e as usamos muitas vezes neste livro. No entanto, há uma complicação quando você usa variáveis nomeadas em expressões `match`. Como `match` inicia um novo escopo, as variáveis declaradas como parte de um padrão dentro da expressão `match` sombrearão aquelas com o mesmo nome fora da construção `match`, como é o caso com todas as variáveis. Na Listagem 18-11, declaramos uma variável chamada `x` com o valor `Some(5)` e uma variável `y` com o valor `10`. Em seguida, criamos uma expressão `match` no valor `x`. Observe os padrões nos braços do match e o `println!` no final, e tente descobrir o que o código imprimirá antes de executar este código ou ler mais.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
  1 let x = Some(5);
  2 let y = 10;

    match x {
      3 Some(50) => println!("Got 50"),
      4 Some(y) => println!("Matched, y = {y}"),
      5 _ => println!("Default case, x = {:?}", x),
    }

  6 println!("at the end: x = {:?}, y = {y}", x);
}
```

Listagem 18-11: Uma expressão `match` com um braço que introduz uma variável sombreada `y`

Vamos analisar o que acontece quando a expressão `match` é executada. O padrão no primeiro braço do match \[3] não corresponde ao valor definido de `x` \[1], então o código continua.

O padrão no segundo braço do match \[4] introduz uma nova variável chamada `y` que corresponderá a qualquer valor dentro de um valor `Some`. Como estamos em um novo escopo dentro da expressão `match`, esta é uma nova variável `y`, não a `y` que declaramos no início com o valor `10` \[2]. Esta nova ligação `y` corresponderá a qualquer valor dentro de um `Some`, que é o que temos em `x`. Portanto, este novo `y` se liga ao valor interno do `Some` em `x`. Esse valor é `5`, então a expressão para esse braço é executada e imprime `Matched, y = 5`.

Se `x` tivesse sido um valor `None` em vez de `Some(5)`, os padrões nos dois primeiros braços não teriam correspondido, então o valor teria correspondido ao sublinhado \[5]. Não introduzimos a variável `x` no padrão do braço do sublinhado, então o `x` na expressão ainda é o `x` externo que não foi sombreado. Nesse caso hipotético, o `match` imprimiria `Default case, x = None`.

Quando a expressão `match` termina, seu escopo termina, e também o escopo do `y` interno. O último `println!` \[6] produz `at the end: x = Some(5), y = 10`.

Para criar uma expressão `match` que compare os valores de `x` e `y` externos, em vez de introduzir uma variável sombreada, precisaríamos usar uma condição de guarda (match guard) em vez disso. Falaremos sobre guardas de correspondência em "Condicionais Extras com Guardas de Correspondência".
