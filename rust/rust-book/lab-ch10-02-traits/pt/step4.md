# Implementações Padrão

Às vezes, é útil ter um comportamento padrão para alguns ou todos os métodos em uma trait, em vez de exigir implementações para todos os métodos em cada tipo. Então, ao implementarmos a trait em um tipo específico, podemos manter ou substituir o comportamento padrão de cada método.

Na Listagem 10-14, especificamos uma string padrão para o método `summarize` da trait `Summary`, em vez de apenas definir a assinatura do método, como fizemos na Listagem 10-12.

Nome do arquivo: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String {
        String::from("(Leia mais...)")
    }
}
```

Listagem 10-14: Definindo uma trait `Summary` com uma implementação padrão do método `summarize`

Para usar uma implementação padrão para resumir instâncias de `NewsArticle`, especificamos um bloco `impl` vazio com `impl Summary for NewsArticle {}`.

Embora não estejamos mais definindo o método `summarize` em `NewsArticle` diretamente, fornecemos uma implementação padrão e especificamos que `NewsArticle` implementa a trait `Summary`. Como resultado, ainda podemos chamar o método `summarize` em uma instância de `NewsArticle`, assim:

```rust
let article = NewsArticle {
    headline: String::from(
        "Penguins win the Stanley Cup Championship!"
    ),
    location: String::from("Pittsburgh, PA, USA"),
    author: String::from("Iceburgh"),
    content: String::from(
        "The Pittsburgh Penguins once again are the best \
         hockey team in the NHL.",
    ),
};

println!("New article available! {}", article.summarize());
```

Este código imprime `New article available! (Leia mais...)`.

Criar uma implementação padrão não exige que mudemos nada sobre a implementação de `Summary` em `Tweet` na Listagem 10-13. A razão é que a sintaxe para substituir uma implementação padrão é a mesma da sintaxe para implementar um método de trait que não tem uma implementação padrão.

Implementações padrão podem chamar outros métodos na mesma trait, mesmo que esses outros métodos não tenham uma implementação padrão. Dessa forma, uma trait pode fornecer muita funcionalidade útil e exigir que os implementadores especifiquem apenas uma pequena parte dela. Por exemplo, poderíamos definir a trait `Summary` para ter um método `summarize_author` cuja implementação é obrigatória e, em seguida, definir um método `summarize` que tenha uma implementação padrão que chama o método `summarize_author`:

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!(
            "(Leia mais de {}...)",
            self.summarize_author()
        )
    }
}
```

Para usar esta versão de `Summary`, só precisamos definir `summarize_author` quando implementamos a trait em um tipo:

```rust
impl Summary for Tweet {
    fn summarize_author(&self) -> String {
        format!("@{}", self.username)
    }
}
```

Depois de definirmos `summarize_author`, podemos chamar `summarize` em instâncias da struct `Tweet`, e a implementação padrão de `summarize` chamará a definição de `summarize_author` que fornecemos. Como implementamos `summarize_author`, a trait `Summary` nos deu o comportamento do método `summarize` sem exigir que escrevêssemos mais nenhum código. Veja como isso se parece:

```rust
let tweet = Tweet {
    username: String::from("horse_ebooks"),
    content: String::from(
        "of course, as you probably already know, people",
    ),
    reply: false,
    retweet: false,
};

println!("1 new tweet: {}", tweet.summarize());
```

Este código imprime `1 new tweet: (Leia mais de @horse_ebooks...)`.

Observe que não é possível chamar a implementação padrão de uma implementação de substituição desse mesmo método.
