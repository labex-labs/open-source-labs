# Implementando uma Trait em um Tipo

Agora que definimos as assinaturas desejadas dos métodos da trait `Summary`, podemos implementá-la nos tipos em nosso agregador de mídia. A Listagem 10-13 mostra uma implementação da trait `Summary` na struct `NewsArticle` que usa o título, o autor e a localização para criar o valor de retorno de `summarize`. Para a struct `Tweet`, definimos `summarize` como o nome de usuário seguido por todo o texto do tweet, assumindo que o conteúdo do tweet já está limitado a 280 caracteres.

Nome do arquivo: `src/lib.rs`

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!(
            "{}, by {} ({})",
            self.headline,
            self.author,
            self.location
        )
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

Listagem 10-13: Implementando a trait `Summary` nos tipos `NewsArticle` e `Tweet`

Implementar uma trait em um tipo é semelhante a implementar métodos regulares. A diferença é que, após `impl`, colocamos o nome da trait que queremos implementar, então usamos a palavra-chave `for` e, em seguida, especificamos o nome do tipo para o qual queremos implementar a trait. Dentro do bloco `impl`, colocamos as assinaturas dos métodos que a definição da trait definiu. Em vez de adicionar um ponto e vírgula após cada assinatura, usamos chaves e preenchemos o corpo do método com o comportamento específico que queremos que os métodos da trait tenham para o tipo específico.

Agora que a biblioteca implementou a trait `Summary` em `NewsArticle` e `Tweet`, os usuários da crate podem chamar os métodos da trait em instâncias de `NewsArticle` e `Tweet` da mesma forma que chamamos métodos regulares. A única diferença é que o usuário deve trazer a trait para o escopo, bem como os tipos. Aqui está um exemplo de como uma crate binária pode usar nossa crate de biblioteca `aggregator`:

```rust
use aggregator::{Summary, Tweet};

fn main() {
    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}
```

Este código imprime `1 new tweet: horse_ebooks: of course, as you probably already know, people`.

Outras crates que dependem da crate `aggregator` também podem trazer a trait `Summary` para o escopo para implementar `Summary` em seus próprios tipos. Uma restrição a ser observada é que podemos implementar uma trait em um tipo somente se a trait ou o tipo, ou ambos, forem locais para nossa crate. Por exemplo, podemos implementar traits da biblioteca padrão como `Display` em um tipo personalizado como `Tweet` como parte da funcionalidade de nossa crate `aggregator` porque o tipo `Tweet` é local para nossa crate `aggregator`. Também podemos implementar `Summary` em `Vec<T>` em nossa crate `aggregator` porque a trait `Summary` é local para nossa crate `aggregator`.

Mas não podemos implementar traits externas em tipos externos. Por exemplo, não podemos implementar a trait `Display` em `Vec<T>` dentro de nossa crate `aggregator` porque `Display` e `Vec<T>` são ambos definidos na biblioteca padrão e não são locais para nossa crate `aggregator`. Essa restrição faz parte de uma propriedade chamada _coerência_ (coherence), e mais especificamente a _regra do órfão_ (orphan rule), assim chamada porque o tipo pai não está presente. Essa regra garante que o código de outras pessoas não possa quebrar seu código e vice-versa. Sem a regra, duas crates poderiam implementar a mesma trait para o mesmo tipo, e o Rust não saberia qual implementação usar.
