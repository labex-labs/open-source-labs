# Onde o Operador `?` Pode Ser Usado

O operador `?` só pode ser usado em funções cujo tipo de retorno é compatível com o valor em que o `?` é usado. Isso ocorre porque o operador `?` é definido para realizar um retorno antecipado de um valor da função, da mesma maneira que a expressão `match` que definimos no Listing 9-6. No Listing 9-6, o `match` estava usando um valor `Result`, e o braço de retorno antecipado retornou um valor `Err(e)`. O tipo de retorno da função precisa ser um `Result` para que seja compatível com este `return`.

No Listing 9-10, vamos olhar para o erro que obteremos se usarmos o operador `?` em uma função `main` com um tipo de retorno que é incompatível com o tipo do valor em que usamos `?`.

Nome do arquivo: `src/main.rs`

```rust
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")?;
}
```

Listing 9-10: Tentar usar o `?` na função `main` que retorna `()` não compilará.

Este código abre um arquivo, o que pode falhar. O operador `?` segue o valor `Result` retornado por `File::open`, mas esta função `main` tem o tipo de retorno `()`, não `Result`. Quando compilamos este código, obtemos a seguinte mensagem de erro:

```bash
error[E0277]: the `?` operator can only be used in a function that returns
`Result` or `Option` (or another type that implements `FromResidual`)
 --> src/main.rs:4:48
  |
3 | / fn main() {
4 | |     let greeting_file = File::open("hello.txt")?;
  | |                                                ^ cannot use the `?`
operator in a function that returns `()`
5 | | }
  | |_- this function should return `Result` or `Option` to accept `?`
  |
  = help: the trait `FromResidual<Result<Infallible, std::io::Error>>` is not
implemented for `()`
```

Este erro aponta que só podemos usar o operador `?` em uma função que retorna `Result`, `Option` ou outro tipo que implementa `FromResidual`.

Para corrigir o erro, você tem duas opções. Uma opção é alterar o tipo de retorno da sua função para ser compatível com o valor em que você está usando o operador `?`, desde que você não tenha restrições que o impeçam. A outra opção é usar um `match` ou um dos métodos `Result<T, E>` para lidar com o `Result<T, E>` da maneira que for apropriada.

A mensagem de erro também mencionou que `?` pode ser usado com valores `Option<T>` também. Assim como usar `?` em `Result`, você só pode usar `?` em `Option` em uma função que retorna `Option`. O comportamento do operador `?` quando chamado em um `Option<T>` é semelhante ao seu comportamento quando chamado em um `Result<T, E>`: se o valor for `None`, o `None` será retornado antecipadamente da função naquele ponto. Se o valor for `Some`, o valor dentro do `Some` é o valor resultante da expressão, e a função continua. O Listing 9-11 tem um exemplo de uma função que encontra o último caractere da primeira linha no texto fornecido.

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
    text.lines().next()?.chars().last()
}
```

Listing 9-11: Usando o operador `?` em um valor `Option<T>`

Esta função retorna `Option<char>` porque é possível que haja um caractere lá, mas também é possível que não haja. Este código pega o argumento de fatia de string `text` e chama o método `lines` nele, que retorna um iterador sobre as linhas na string. Como esta função quer examinar a primeira linha, ela chama `next` no iterador para obter o primeiro valor do iterador. Se `text` for a string vazia, esta chamada para `next` retornará `None`, caso em que usamos `?` para parar e retornar `None` de `last_char_of_first_line`. Se `text` não for a string vazia, `next` retornará um valor `Some` contendo uma fatia de string da primeira linha em `text`.

O `?` extrai a fatia de string, e podemos chamar `chars` nessa fatia de string para obter um iterador de seus caracteres. Estamos interessados no último caractere desta primeira linha, então chamamos `last` para retornar o último item no iterador. Esta é uma `Option` porque é possível que a primeira linha seja a string vazia; por exemplo, se `text` começar com uma linha em branco, mas tiver caracteres em outras linhas, como em `"\nhi"`. No entanto, se houver um último caractere na primeira linha, ele será retornado na variante `Some`. O operador `?` no meio nos dá uma maneira concisa de expressar essa lógica, permitindo que implementemos a função em uma linha. Se não pudéssemos usar o operador `?` em `Option`, teríamos que implementar essa lógica usando mais chamadas de método ou uma expressão `match`.

Observe que você pode usar o operador `?` em um `Result` em uma função que retorna `Result`, e você pode usar o operador `?` em um `Option` em uma função que retorna `Option`, mas você não pode misturar e combinar. O operador `?` não converterá automaticamente um `Result` em um `Option` ou vice-versa; nesses casos, você pode usar métodos como o método `ok` em `Result` ou o método `ok_or` em `Option` para fazer a conversão explicitamente.

Até agora, todas as funções `main` que usamos retornam `()`. A função `main` é especial porque é o ponto de entrada e saída de um programa executável, e existem restrições sobre o que seu tipo de retorno pode ser para que o programa se comporte conforme o esperado.

Felizmente, `main` também pode retornar um `Result<(), E>`. O Listing 9-12 tem o código do Listing 9-10, mas alteramos o tipo de retorno de `main` para ser `Result<(), Box<dyn Error>>` e adicionamos um valor de retorno `Ok(())` ao final. Este código agora compilará.

Nome do arquivo: `src/main.rs`

```rust
use std::error::Error;
use std::fs::File;

fn main() -> Result<(), Box<dyn Error>> {
    let greeting_file = File::open("hello.txt")?;

    Ok(())
}
```

Listing 9-12: Alterar `main` para retornar `Result<(), E>` permite o uso do operador `?` em valores `Result`.

O tipo `Box<dyn Error>` é um _objeto de trait_, sobre o qual falaremos em "Usando Objetos de Trait que Permitem Valores de Diferentes Tipos". Por enquanto, você pode ler `Box<dyn Error>` para significar "qualquer tipo de erro". Usar `?` em um valor `Result` em uma função `main` com o tipo de erro `Box<dyn Error>` é permitido porque permite que qualquer valor `Err` seja retornado antecipadamente. Embora o corpo desta função `main` só retorne erros do tipo `std::io::Error`, ao especificar `Box<dyn Error>`, esta assinatura continuará correta mesmo que mais código que retorne outros erros seja adicionado ao corpo de `main`.

Quando uma função `main` retorna um `Result<(), E>`, o executável sairá com um valor de `0` se `main` retornar `Ok(())` e sairá com um valor diferente de zero se `main` retornar um valor `Err`. Executáveis escritos em C retornam inteiros quando saem: programas que saem com sucesso retornam o inteiro `0`, e programas que erram retornam algum inteiro diferente de `0`. Rust também retorna inteiros de executáveis para ser compatível com essa convenção.

A função `main` pode retornar qualquer tipo que implemente o trait `std::process::Termination`, que contém uma função `report` que retorna um `ExitCode`. Consulte a documentação da biblioteca padrão para obter mais informações sobre como implementar o trait `Termination` para seus próprios tipos.

Agora que discutimos os detalhes de chamar `panic!` ou retornar `Result`, vamos voltar ao tópico de como decidir qual é apropriado usar em quais casos.
