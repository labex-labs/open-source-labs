# Expressões condicionais `if let`

No Capítulo 6, discutimos como usar expressões `if let` principalmente como uma maneira mais curta de escrever o equivalente a um `match` que corresponde apenas a um caso. Opcionalmente, `if let` pode ter um `else` correspondente contendo código para executar se o padrão no `if let` não corresponder.

A Listagem 18-1 mostra que também é possível misturar e combinar expressões `if let`, `else if` e `else if let`. Fazer isso nos dá mais flexibilidade do que uma expressão `match` na qual podemos expressar apenas um valor para comparar com os padrões. Além disso, o Rust não exige que as condições em uma série de ramos `if let`, `else if` e `else if let` se relacionem entre si.

O código na Listagem 18-1 determina qual cor usar para o seu plano de fundo com base em uma série de verificações para várias condições. Para este exemplo, criamos variáveis com valores codificados que um programa real pode receber da entrada do usuário.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listagem 18-1: Misturando `if let`, `else if`, `else if let` e `else`

Se o usuário especificar uma cor favorita \[1], essa cor é usada como plano de fundo \[2]. Se nenhuma cor favorita for especificada e hoje for terça-feira \[3], a cor do plano de fundo é verde \[4]. Caso contrário, se o usuário especificar sua idade como uma string e pudermos analisá-la com sucesso como um número \[5], a cor será roxa \[7] ou laranja \[8], dependendo do valor do número \[6]. Se nenhuma dessas condições se aplicar \[9], a cor do plano de fundo será azul \[10].

Essa estrutura condicional nos permite suportar requisitos complexos. Com os valores codificados que temos aqui, este exemplo imprimirá `Using purple as the background color`.

Você pode ver que `if let` também pode introduzir variáveis sombreadas da mesma forma que os ramos `match` podem: a linha `if let Ok(age) = age` \[5] introduz uma nova variável `age` sombreada que contém o valor dentro da variante `Ok`. Isso significa que precisamos colocar a condição `if age > 30` \[6] dentro desse bloco: não podemos combinar essas duas condições em `if let Ok(age) = age && age > 30`. O `age` sombreado que queremos comparar com 30 não é válido até que o novo escopo comece com a chave.

A desvantagem de usar expressões `if let` é que o compilador não verifica a exaustividade, enquanto com expressões `match` ele o faz. Se omitíssemos o último bloco `else` \[9] e, portanto, deixássemos de lidar com alguns casos, o compilador não nos alertaria sobre o possível bug de lógica.
