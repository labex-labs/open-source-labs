# Macros do Tipo Função

Macros do tipo função definem macros que se parecem com chamadas de função. Semelhantes às macros `macro_rules!`, elas são mais flexíveis do que funções; por exemplo, elas podem receber um número desconhecido de argumentos. No entanto, as macros `macro_rules!` só podem ser definidas usando a sintaxe semelhante a correspondência que discutimos em "Macros Declarativas com macro_rules! para Metaprogramação Geral". Macros do tipo função recebem um parâmetro `TokenStream`, e sua definição manipula esse `TokenStream` usando código Rust, como os outros dois tipos de macros procedurais fazem. Um exemplo de uma macro do tipo função é uma macro `sql!` que pode ser chamada assim:

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

Esta macro analisaria a instrução SQL dentro dela e verificaria se ela está sintaticamente correta, o que é um processamento muito mais complexo do que uma macro `macro_rules!` pode fazer. A macro `sql!` seria definida assim:

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

Esta definição é semelhante à assinatura da macro `derive` customizada: recebemos os tokens que estão dentro dos parênteses e retornamos o código que queríamos gerar.
