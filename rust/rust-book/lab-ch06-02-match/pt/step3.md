# Correspondência com Option`<T>`{=html}

Na seção anterior, queríamos obter o valor interno `T` do caso `Some` ao usar `Option<T>`; também podemos lidar com `Option<T>` usando `match`, como fizemos com o enum `Coin`! Em vez de comparar moedas, compararemos as variantes de `Option<T>`, mas a maneira como a expressão `match` funciona permanece a mesma.

Digamos que queremos escrever uma função que recebe um `Option<i32>` e, se houver um valor dentro, adiciona 1 a esse valor. Se não houver um valor dentro, a função deve retornar o valor `None` e não tentar realizar nenhuma operação.

Esta função é muito fácil de escrever, graças ao `match`, e se parecerá com a Listagem 6-5.

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
      1 None => None,
      2 Some(i) => Some(i + 1),
    }
}

let five = Some(5);
let six = plus_one(five); 3
let none = plus_one(None); 4
```

Listagem 6-5: Uma função que usa uma expressão `match` em um `Option<i32>`

Vamos examinar a primeira execução de `plus_one` em mais detalhes. Quando chamamos `plus_one(five)` \[3], a variável `x` no corpo de `plus_one` terá o valor `Some(5)`. Em seguida, comparamos isso com cada braço match:

```rust
None => None,
```

O valor `Some(5)` não corresponde ao padrão `None` \[1], então continuamos para o próximo braço:

```rust
Some(i) => Some(i + 1),
```

`Some(5)` corresponde a `Some(i)` \[2]? Sim, corresponde! Temos a mesma variante. O `i` se vincula ao valor contido em `Some`, então `i` assume o valor `5`. O código no braço match é então executado, então adicionamos 1 ao valor de `i` e criamos um novo valor `Some` com nosso total `6` dentro.

Agora, vamos considerar a segunda chamada de `plus_one` na Listagem 6-5, onde `x` é `None` \[4]. Entramos no `match` e comparamos com o primeiro braço \[1].

Corresponde! Não há valor para adicionar, então o programa para e retorna o valor `None` no lado direito de `=>`. Como o primeiro braço correspondeu, nenhum outro braço é comparado.

Combinar `match` e enums é útil em muitas situações. Você verá esse padrão muito no código Rust: `match` contra um enum, vincular uma variável aos dados internos e, em seguida, executar o código com base nele. É um pouco complicado no início, mas assim que você se acostumar, desejará tê-lo em todas as linguagens. É consistentemente o favorito dos usuários.
