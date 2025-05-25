# O Tipo Never (Nunca) que Nunca Retorna

O Rust tem um tipo especial chamado `!` que é conhecido na linguagem da teoria dos tipos como o _tipo vazio_ (empty type) porque não tem valores. Preferimos chamá-lo de _tipo never_ (nunca) porque ele fica no lugar do tipo de retorno quando uma função nunca retornará. Aqui está um exemplo:

```rust
fn bar() -> ! {
    --snip--
}
```

Este código é lido como "a função `bar` retorna nunca". Funções que retornam nunca são chamadas de _funções divergentes_ (diverging functions). Não podemos criar valores do tipo `!`, então `bar` nunca pode retornar.

Mas qual a utilidade de um tipo para o qual você nunca pode criar valores? Recorde o código da Listagem 2-5, parte do jogo de adivinhação de números; reproduzimos um pouco dele aqui na Listagem 19-26.

```rust
let guess: u32 = match guess.trim().parse() {
    Ok(num) => num,
    Err(_) => continue,
};
```

Listagem 19-26: Um `match` com um braço que termina em `continue`

Na época, ignoramos alguns detalhes neste código. Em "A Construção de Fluxo de Controle match", discutimos que os braços `match` devem todos retornar o mesmo tipo. Então, por exemplo, o código a seguir não funciona:

```rust
let guess = match guess.trim().parse() {
    Ok(_) => 5,
    Err(_) => "hello",
};
```

O tipo de `guess` neste código teria que ser um inteiro _e_ uma string, e o Rust exige que `guess` tenha apenas um tipo. Então, o que `continue` retorna? Como fomos autorizados a retornar um `u32` de um braço e ter outro braço que termina com `continue` na Listagem 19-26?

Como você pode ter adivinhado, `continue` tem um valor `!`. Ou seja, quando o Rust calcula o tipo de `guess`, ele olha para ambos os braços match, o primeiro com um valor de `u32` e o último com um valor `!`. Como `!` nunca pode ter um valor, o Rust decide que o tipo de `guess` é `u32`.

A forma formal de descrever este comportamento é que expressões do tipo `!` podem ser forçadas em qualquer outro tipo. Somos autorizados a terminar este braço `match` com `continue` porque `continue` não retorna um valor; em vez disso, ele move o controle de volta para o topo do loop, então no caso `Err`, nunca atribuímos um valor a `guess`.

O tipo never é útil com a macro `panic!` também. Recorde a função `unwrap` que chamamos em valores `Option<T>` para produzir um valor ou entrar em pânico com esta definição:

```rust
impl<T> Option<T> {
    pub fn unwrap(self) -> T {
        match self {
            Some(val) => val,
            None => panic!(
                "called `Option::unwrap()` on a `None` value"
            ),
        }
    }
}
```

Neste código, a mesma coisa acontece como no `match` na Listagem 19-26: Rust vê que `val` tem o tipo `T` e `panic!` tem o tipo `!`, então o resultado da expressão `match` geral é `T`. Este código funciona porque `panic!` não produz um valor; ele encerra o programa. No caso `None`, não estaremos retornando um valor de `unwrap`, então este código é válido.

Uma expressão final que tem o tipo `!` é um `loop`:

    print!("forever ");

    loop {
        print!("and ever ");
    }

Aqui, o loop nunca termina, então `!` é o valor da expressão. No entanto, isso não seria verdade se incluíssemos um `break`, porque o loop terminaria quando chegasse ao `break`.
