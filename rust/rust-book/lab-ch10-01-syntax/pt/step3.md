# Em Definições de Funções

Ao definir uma função que usa genéricos, colocamos os genéricos na assinatura da função, onde normalmente especificaríamos os tipos de dados dos parâmetros e do valor de retorno. Fazer isso torna nosso código mais flexível e oferece mais funcionalidade aos chamadores de nossa função, ao mesmo tempo em que evita a duplicação de código.

Continuando com nossa função `largest`, a Listagem 10-4 mostra duas funções que encontram o maior valor em uma fatia. Em seguida, combinaremos essas em uma única função que usa genéricos.

Nome do arquivo: `src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

Listagem 10-4: Duas funções que diferem apenas em seus nomes e nos tipos em suas assinaturas

A função `largest_i32` é aquela que extraímos na Listagem 10-3 que encontra o maior `i32` em uma fatia. A função `largest_char` encontra o maior `char` em uma fatia. Os corpos das funções têm o mesmo código, então vamos eliminar a duplicação introduzindo um parâmetro de tipo genérico em uma única função.

Para parametrizar os tipos em uma nova função única, precisamos nomear o parâmetro de tipo, assim como fazemos para os parâmetros de valor de uma função. Você pode usar qualquer identificador como um nome de parâmetro de tipo. Mas usaremos `T` porque, por convenção, os nomes de parâmetros de tipo em Rust são curtos, geralmente apenas uma letra, e a convenção de nomenclatura de tipos do Rust é CamelCase. Abreviação de _type_ (tipo), `T` é a escolha padrão da maioria dos programadores Rust.

Quando usamos um parâmetro no corpo da função, precisamos declarar o nome do parâmetro na assinatura para que o compilador saiba o que esse nome significa. Da mesma forma, quando usamos um nome de parâmetro de tipo em uma assinatura de função, precisamos declarar o nome do parâmetro de tipo antes de usá-lo. Para definir a função genérica `largest`, colocamos declarações de nome de tipo dentro de colchetes angulares, `<>`, entre o nome da função e a lista de parâmetros, assim:

```rust
fn largest<T>(list: &[T]) -> &T {
```

Lemos esta definição como: a função `largest` é genérica sobre algum tipo `T`. Esta função tem um parâmetro chamado `list`, que é uma fatia de valores do tipo `T`. A função `largest` retornará uma referência a um valor do mesmo tipo `T`.

A Listagem 10-5 mostra a definição da função `largest` combinada usando o tipo de dados genérico em sua assinatura. A listagem também mostra como podemos chamar a função com uma fatia de valores `i32` ou valores `char`. Observe que este código não compilará ainda, mas o corrigiremos mais tarde neste capítulo.

Nome do arquivo: `src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y', 'm', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

Listagem 10-5: A função `largest` usando parâmetros de tipo genéricos; isso não compila ainda

Se compilarmos este código agora, obteremos este erro:

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

O texto de ajuda menciona `std::cmp::PartialOrd`, que é um _trait_ (característica), e falaremos sobre traits na próxima seção. Por enquanto, saiba que este erro afirma que o corpo de `largest` não funcionará para todos os tipos possíveis que `T` poderia ser. Como queremos comparar valores do tipo `T` no corpo, só podemos usar tipos cujos valores podem ser ordenados. Para habilitar comparações, a biblioteca padrão tem o trait `std::cmp::PartialOrd` que você pode implementar em tipos (consulte o Apêndice C para obter mais informações sobre este trait). Seguindo a sugestão do texto de ajuda, restringimos os tipos válidos para `T` apenas àqueles que implementam `PartialOrd` e este exemplo compilará, porque a biblioteca padrão implementa `PartialOrd` em `i32` e `char`.
