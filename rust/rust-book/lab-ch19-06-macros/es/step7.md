# Macros Similares a Funciones

Las macros similares a funciones definen macros que se ven como llamadas a funciones. Al igual que las macros `macro_rules!`, son más flexibles que las funciones; por ejemplo, pueden tomar un número desconocido de argumentos. Sin embargo, las macros `macro_rules!` solo se pueden definir usando la sintaxis similar a `match` que discutimos en "Macros Declarativas con macro_rules! para Metaprogramación General". Las macros similares a funciones toman un parámetro `TokenStream`, y su definición manipula ese `TokenStream` usando código de Rust como lo hacen las otras dos clases de macros procedimentales. Un ejemplo de una macro similar a una función es una macro `sql!` que podría ser llamada así:

```rust
let sql = sql!(SELECT * FROM posts WHERE id=1);
```

Esta macro analizaría la declaración SQL dentro de ella y comprobaría que es sintácticamente correcta, lo que es un procesamiento mucho más complejo que lo que puede hacer una macro `macro_rules!`. La macro `sql!` se definiría así:

```rust
#[proc_macro]
pub fn sql(input: TokenStream) -> TokenStream {
```

Esta definición es similar a la firma de la macro `derive` personalizada: recibimos los tokens que están dentro de los paréntesis y devolvemos el código que queríamos generar.
