# Padrões que se Vinculam a Valores

Outra característica útil dos braços match é que eles podem se vincular às partes dos valores que correspondem ao padrão. É assim que podemos extrair valores das variantes enum.

Como exemplo, vamos alterar uma de nossas variantes enum para conter dados dentro dela. De 1999 a 2008, os Estados Unidos cunharam moedas de 25 centavos com designs diferentes para cada um dos 50 estados em um lado. Nenhuma outra moeda recebeu designs estaduais, então apenas as moedas de 25 centavos têm esse valor extra. Podemos adicionar essa informação ao nosso `enum` alterando a variante `Quarter` para incluir um valor `UsState` armazenado dentro dela, o que fizemos na Listagem 6-4.

```rust
#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}
```

Listagem 6-4: Um enum `Coin` no qual a variante `Quarter` também contém um valor `UsState`

Vamos imaginar que um amigo está tentando colecionar todas as moedas de 25 centavos dos 50 estados. Enquanto classificamos nossa troco por tipo de moeda, também diremos o nome do estado associado a cada moeda de 25 centavos para que, se for uma que nosso amigo não tem, ele possa adicioná-la à sua coleção.

Na expressão match para este código, adicionamos uma variável chamada `state` ao padrão que corresponde aos valores da variante `Coin::Quarter`. Quando um `Coin::Quarter` corresponde, a variável `state` se vinculará ao valor do estado dessa moeda de 25 centavos. Então, podemos usar `state` no código para esse braço, assim:

```rust
fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

Se chamássemos `value_in_cents(Coin::Quarter(UsState::Alaska))`, `coin` seria `Coin::Quarter(UsState::Alaska)`. Quando comparamos esse valor com cada um dos braços match, nenhum deles corresponde até chegarmos a `Coin::Quarter(state)`. Nesse ponto, a ligação para `state` será o valor `UsState::Alaska`. Podemos então usar essa ligação na expressão `println!`, obtendo assim o valor do estado interno da variante enum `Coin` para `Quarter`.
