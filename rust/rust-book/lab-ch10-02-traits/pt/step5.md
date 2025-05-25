# Traits como Parâmetros

Agora que você sabe como definir e implementar traits, podemos explorar como usar traits para definir funções que aceitam muitos tipos diferentes. Usaremos a trait `Summary` que implementamos nos tipos `NewsArticle` e `Tweet` na Listagem 10-13 para definir uma função `notify` que chama o método `summarize` em seu parâmetro `item`, que é de algum tipo que implementa a trait `Summary`. Para fazer isso, usamos a sintaxe `impl Trait`, assim:

```rust
pub fn notify(item: &impl Summary) {
    println!("Breaking news! {}", item.summarize());
}
```

Em vez de um tipo concreto para o parâmetro `item`, especificamos a palavra-chave `impl` e o nome da trait. Este parâmetro aceita qualquer tipo que implemente a trait especificada. No corpo de `notify`, podemos chamar quaisquer métodos em `item` que venham da trait `Summary`, como `summarize`. Podemos chamar `notify` e passar qualquer instância de `NewsArticle` ou `Tweet`. O código que chama a função com qualquer outro tipo, como uma `String` ou um `i32`, não compilará porque esses tipos não implementam `Summary`.
