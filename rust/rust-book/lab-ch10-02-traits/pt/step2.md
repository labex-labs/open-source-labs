# Definindo uma Trait

O comportamento de um tipo consiste nos métodos que podemos chamar nesse tipo. Diferentes tipos compartilham o mesmo comportamento se pudermos chamar os mesmos métodos em todos esses tipos. Definições de trait são uma forma de agrupar assinaturas de métodos para definir um conjunto de comportamentos necessários para realizar algum propósito.

Por exemplo, digamos que temos múltiplas structs que armazenam vários tipos e quantidades de texto: uma struct `NewsArticle` que armazena uma notícia arquivada em um local específico e um `Tweet` que pode ter, no máximo, 280 caracteres, juntamente com metadados que indicam se foi um novo tweet, um retweet ou uma resposta a outro tweet.

Queremos criar uma crate de biblioteca agregadora de mídia chamada `aggregator` que pode exibir resumos de dados que podem ser armazenados em uma instância `NewsArticle` ou `Tweet`. Para fazer isso, precisamos de um resumo de cada tipo, e solicitaremos esse resumo chamando um método `summarize` em uma instância. A Listagem 10-12 mostra a definição de uma trait pública `Summary` que expressa esse comportamento.

Nome do arquivo: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

Listagem 10-12: Uma trait `Summary` que consiste no comportamento fornecido por um método `summarize`

Aqui, declaramos uma trait usando a palavra-chave `trait` e, em seguida, o nome da trait, que é `Summary` neste caso. Também declaramos a trait como `pub` para que as crates que dependem desta crate também possam usar esta trait, como veremos em alguns exemplos. Dentro das chaves, declaramos as assinaturas dos métodos que descrevem os comportamentos dos tipos que implementam esta trait, que neste caso é `fn summarize(&self) -> String`.

Após a assinatura do método, em vez de fornecer uma implementação dentro das chaves, usamos um ponto e vírgula. Cada tipo que implementa esta trait deve fornecer seu próprio comportamento personalizado para o corpo do método. O compilador irá garantir que qualquer tipo que tenha a trait `Summary` terá o método `summarize` definido exatamente com esta assinatura.

Uma trait pode ter múltiplos métodos em seu corpo: as assinaturas dos métodos são listadas uma por linha, e cada linha termina com um ponto e vírgula.
