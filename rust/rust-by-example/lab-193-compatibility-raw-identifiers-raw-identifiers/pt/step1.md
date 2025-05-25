# Identificadores Brutos

Rust, como muitas linguagens de programação, possui o conceito de "palavras-chave". Esses identificadores têm um significado para a linguagem, e por isso não podem ser usados em locais como nomes de variáveis, nomes de funções e outros. Identificadores brutos permitem que você use palavras-chave onde normalmente não seriam permitidas. Isso é particularmente útil quando o Rust introduz novas palavras-chave e uma biblioteca usando uma edição mais antiga do Rust possui uma variável ou função com o mesmo nome de uma palavra-chave introduzida em uma edição mais recente.

Por exemplo, considere um pacote `foo` compilado com a edição 2015 do Rust que exporta uma função chamada `try`. Essa palavra-chave é reservada para um novo recurso na edição 2018, então, sem identificadores brutos, não teríamos como nomear a função.

```rust
extern crate foo;

fn main() {
    foo::try();
}
```

Você receberá este erro:

```plaintext
error: expected identifier, found keyword `try`
 --> src/main.rs:4:4
  |
4 | foo::try();
  |      ^^^ expected identifier, found keyword
```

Você pode escrever isso com um identificador bruto:

```rust
extern crate foo;

fn main() {
    foo::r#try();
}
```
