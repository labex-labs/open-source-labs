# Movendo Valores Capturados de Closures e os Traits Fn

Uma vez que uma closure capturou uma referência ou capturou a propriedade de um valor do ambiente onde a closure é definida (afetando, portanto, o que, se algo, é movido _para_ a closure), o código no corpo da closure define o que acontece com as referências ou valores quando a closure é avaliada posteriormente (afetando, portanto, o que, se algo, é movido _para fora_ da closure).

Um corpo de closure pode fazer qualquer uma das seguintes coisas: mover um valor capturado para fora da closure, mutar o valor capturado, nem mover nem mutar o valor, ou não capturar nada do ambiente para começar.

A maneira como uma closure captura e lida com valores do ambiente afeta quais traits a closure implementa, e os traits são como funções e structs podem especificar que tipos de closures podem usar. Closures implementarão automaticamente um, dois ou todos os três desses traits `Fn`, de forma aditiva, dependendo de como o corpo da closure lida com os valores:

- `FnOnce` se aplica a closures que podem ser chamadas uma vez. Todas as closures implementam pelo menos este trait porque todas as closures podem ser chamadas. Uma closure que move valores capturados para fora de seu corpo implementará apenas `FnOnce` e nenhum dos outros traits `Fn` porque só pode ser chamada uma vez.
- `FnMut` se aplica a closures que não movem valores capturados para fora de seu corpo, mas que podem mutar os valores capturados. Essas closures podem ser chamadas mais de uma vez.
- `Fn` se aplica a closures que não movem valores capturados para fora de seu corpo e que não mutam valores capturados, bem como closures que não capturam nada de seu ambiente. Essas closures podem ser chamadas mais de uma vez sem mutar seu ambiente, o que é importante em casos como chamar uma closure várias vezes simultaneamente.

Vamos analisar a definição do método `unwrap_or_else` em `Option<T>` que usamos na Listagem 13-1:

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

Lembre-se que `T` é o tipo genérico que representa o tipo do valor na variante `Some` de um `Option`. Esse tipo `T` também é o tipo de retorno da função `unwrap_or_else`: o código que chama `unwrap_or_else` em um `Option<String>`, por exemplo, obterá um `String`.

Em seguida, observe que a função `unwrap_or_else` tem o parâmetro de tipo genérico adicional `F`. O tipo `F` é o tipo do parâmetro chamado `f`, que é a closure que fornecemos ao chamar `unwrap_or_else`.

A restrição de trait especificada no tipo genérico `F` é `FnOnce() -> T`, o que significa que `F` deve ser capaz de ser chamada uma vez, não receber argumentos e retornar um `T`. Usar `FnOnce` na restrição de trait expressa a restrição de que `unwrap_or_else` só vai chamar `f` uma vez, no máximo. No corpo de `unwrap_or_else`, podemos ver que se o `Option` for `Some`, `f` não será chamado. Se o `Option` for `None`, `f` será chamado uma vez. Como todas as closures implementam `FnOnce`, `unwrap_or_else` aceita a maior variedade de closures e é tão flexível quanto pode ser.

> Nota: Funções também podem implementar todos os três traits `Fn`. Se o que queremos fazer não exigir a captura de um valor do ambiente, podemos usar o nome de uma função em vez de uma closure onde precisamos de algo que implemente um dos traits `Fn`. Por exemplo, em um valor `Option<Vec<T>>`, poderíamos chamar `unwrap_or_else(Vec::new)` para obter um novo vetor vazio se o valor for `None`.

Agora, vamos analisar o método da biblioteca padrão `sort_by_key`, definido em fatias, para ver como ele difere de `unwrap_or_else` e por que `sort_by_key` usa `FnMut` em vez de `FnOnce` para a restrição de trait. A closure recebe um argumento na forma de uma referência ao item atual na fatia que está sendo considerada e retorna um valor do tipo `K` que pode ser ordenado. Essa função é útil quando você deseja classificar uma fatia por um atributo específico de cada item. Na Listagem 13-7, temos uma lista de instâncias `Rectangle` e usamos `sort_by_key` para ordená-las por seu atributo `width` de baixo para cima.

Nome do arquivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Listagem 13-7: Usando `sort_by_key` para ordenar retângulos por largura

Este código imprime:

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

A razão pela qual `sort_by_key` é definido para receber uma closure `FnMut` é que ele chama a closure várias vezes: uma vez para cada item na fatia. A closure `|r| r.width` não captura, muta ou move nada de seu ambiente, então ela atende aos requisitos da restrição de trait.

Em contraste, a Listagem 13-8 mostra um exemplo de uma closure que implementa apenas o trait `FnOnce`, porque ela move um valor para fora do ambiente. O compilador não nos permitirá usar essa closure com `sort_by_key`.

Nome do arquivo: `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

Listagem 13-8: Tentando usar uma closure `FnOnce` com `sort_by_key`

Esta é uma maneira forçada e convoluta (que não funciona) de tentar contar o número de vezes que `sort_by_key` é chamado ao classificar `list`. Este código tenta fazer essa contagem empurrando `value`---um `String` do ambiente da closure---para o vetor `sort_operations`. A closure captura `value` e, em seguida, move `value` para fora da closure transferindo a propriedade de `value` para o vetor `sort_operations`. Essa closure pode ser chamada uma vez; tentar chamá-la uma segunda vez não funcionaria porque `value` não estaria mais no ambiente para ser empurrado para `sort_operations` novamente! Portanto, essa closure implementa apenas `FnOnce`. Quando tentamos compilar este código, recebemos este erro de que `value` não pode ser movido para fora da closure porque a closure deve implementar `FnMut`:

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

O erro aponta para a linha no corpo da closure que move `value` para fora do ambiente. Para corrigir isso, precisamos alterar o corpo da closure para que ele não mova valores para fora do ambiente. Manter um contador no ambiente e incrementar seu valor no corpo da closure é uma maneira mais direta de contar o número de vezes que `sort_by_key` é chamado. A closure na Listagem 13-9 funciona com `sort_by_key` porque está apenas capturando uma referência mutável ao contador `num_sort_operations` e, portanto, pode ser chamada mais de uma vez.

Nome do arquivo: `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

Listagem 13-9: Usar uma closure `FnMut` com `sort_by_key` é permitido.

Os traits `Fn` são importantes ao definir ou usar funções ou tipos que fazem uso de closures. Na próxima seção, discutiremos iteradores. Muitos métodos de iterador recebem argumentos de closure, então tenha esses detalhes de closure em mente enquanto continuamos!
