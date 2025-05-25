# if let

Para alguns casos de uso, ao corresponder a enumerações, `match` é pouco prático. Por exemplo:

```rust
// Crie `optional` do tipo `Option<i32>`
let optional = Some(7);

match optional {
    Some(i) => {
        println!("Esta é uma string longa e `{:?}`", i);
        // ^ Necessário 2 níveis de indentação apenas para desestruturar
        // `i` da opção.
    },
    _ => {},
    // ^ Necessário porque `match` é exaustivo. Não parece
    // espaço desperdiçado?
};
```

`if let` é mais limpo para este caso de uso e, além disso, permite especificar várias opções de falha:

```rust
fn main() {
    // Todos têm o tipo `Option<i32>`
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // A construção `if let` lê: "se `let` desestruturar `number` em
    // `Some(i)`, avalie o bloco (`{}`).
    if let Some(i) = number {
        println!("Correspondência {:?}!", i);
    }

    // Se precisar especificar uma falha, use um else:
    if let Some(i) = letter {
        println!("Correspondência {:?}!", i);
    } else {
        // Desestruturação falhou. Mude para o caso de falha.
        println!("Não correspondeu a um número. Vamos com uma letra!");
    }

    // Forneça uma condição de falha alterada.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Correspondência {:?}!", i);
    // Desestruturação falhou. Avalie uma condição `else if` para ver se o
    // ramo alternativo de falha deve ser tomado:
    } else if i_like_letters {
        println!("Não correspondeu a um número. Vamos com uma letra!");
    } else {
        // A condição avaliou falso. Este ramo é o padrão:
        println!("Não gosto de letras. Vamos com um emoticon :)!");
    }
}
```

Da mesma forma, `if let` pode ser usado para corresponder a qualquer valor de enumeração:

```rust
// Nossa enumeração de exemplo
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // Crie variáveis de exemplo
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // A variável a corresponde a Foo::Bar
    if let Foo::Bar = a {
        println!("a é foobar");
    }

    // A variável b não corresponde a Foo::Bar
    // Portanto, isso não imprimirá nada
    if let Foo::Bar = b {
        println!("b é foobar");
    }

    // A variável c corresponde a Foo::Qux que tem um valor
    // Similar a Some() no exemplo anterior
    if let Foo::Qux(value) = c {
        println!("c é {}", value);
    }

    // O vínculo também funciona com `if let`
    if let Foo::Qux(value @ 100) = c {
        println!("c é cem");
    }
}
```

Outro benefício é que `if let` permite corresponder a variantes de enumeração não parametrizadas. Isso é verdade mesmo em casos onde a enumeração não implementa ou deriva `PartialEq`. Nesses casos, `if Foo::Bar == a` falharia na compilação, porque as instâncias da enumeração não podem ser igualadas, no entanto, `if let` continuará funcionando.

Você gostaria de um desafio? Corrija o exemplo a seguir para usar `if let`:

```rust
// Esta enumeração propositalmente não implementa nem deriva PartialEq.
// É por isso que comparar Foo::Bar == a falha abaixo.
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // A variável a corresponde a Foo::Bar
    if Foo::Bar == a {
    // ^-- isso causa um erro de tempo de compilação. Use `if let` em vez disso.
        println!("a é foobar");
    }
}
```
