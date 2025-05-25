# _String Slices_ como Parâmetros

Sabendo que você pode obter _slices_ de literais e valores `String`, isso nos leva a mais uma melhoria em `first_word`, e essa é sua assinatura:

```rust
fn first_word(s: &String) -> &str {
```

Um Rustacean mais experiente escreveria a assinatura mostrada na Listagem 4-9 em vez disso, porque ela nos permite usar a mesma função em valores `&String` e valores `&str`.

```rust
fn first_word(s: &str) -> &str {
```

Listagem 4-9: Melhorando a função `first_word` usando um _string slice_ para o tipo do parâmetro `s`

Se tivermos um _string slice_, podemos passá-lo diretamente. Se tivermos uma `String`, podemos passar um _slice_ da `String` ou uma referência à `String`. Essa flexibilidade aproveita as _coerções de deref_ (desreferência), um recurso que abordaremos em "Coerções de Deref Implícitas com Funções e Métodos".

Definir uma função para receber um _string slice_ em vez de uma referência a uma `String` torna nossa API mais geral e útil sem perder nenhuma funcionalidade:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let my_string = String::from("hello world");

    // `first_word` funciona em slices de `String`s, sejam parciais
    // ou inteiros
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // `first_word` também funciona em referências a `String`s, que
    // são equivalentes a slices inteiros de `String`s
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // `first_word` funciona em slices de literais de string,
    // sejam parciais ou inteiros
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Como os literais de string *já são* string slices,
    // isso também funciona, sem a sintaxe de slice!
    let word = first_word(my_string_literal);
}
```
