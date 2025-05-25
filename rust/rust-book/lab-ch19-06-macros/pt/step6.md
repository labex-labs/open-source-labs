# Macros do Tipo Atributo

Macros do tipo atributo são semelhantes às macros `derive` customizadas, mas, em vez de gerar código para o atributo `derive`, elas permitem que você crie novos atributos. Elas também são mais flexíveis: `derive` só funciona para structs e enums; os atributos podem ser aplicados a outros itens também, como funções. Aqui está um exemplo de como usar uma macro do tipo atributo. Digamos que você tenha um atributo chamado `route` que anota funções ao usar um framework de aplicação web:

```rust
#[route(GET, "/")]
fn index() {
```

Este atributo `#[route]` seria definido pelo framework como uma macro procedural. A assinatura da função de definição da macro seria assim:

    #[proc_macro_attribute]
    pub fn route(
        attr: TokenStream,
        item: TokenStream
    ) -> TokenStream {

Aqui, temos dois parâmetros do tipo `TokenStream`. O primeiro é para o conteúdo do atributo: a parte `GET, "/"`. O segundo é o corpo do item ao qual o atributo está anexado: neste caso, `fn index() {}` e o restante do corpo da função.

Fora isso, as macros do tipo atributo funcionam da mesma forma que as macros `derive` customizadas: você cria um crate com o tipo de crate `proc-macro` e implementa uma função que gera o código que você deseja!
