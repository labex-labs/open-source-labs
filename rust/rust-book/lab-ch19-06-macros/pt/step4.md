# Macros Procedurais para Geração de Código a partir de Atributos

A segunda forma de macros é a macro procedural, que age mais como uma função (e é um tipo de procedimento). As _macros procedurais_ aceitam algum código como entrada, operam nesse código e produzem algum código como saída, em vez de corresponder a padrões e substituir o código por outro código, como as macros declarativas fazem. Os três tipos de macros procedurais são `derive` customizado, tipo atributo e tipo função, e todos funcionam de maneira semelhante.

Ao criar macros procedurais, as definições devem residir em seu próprio crate com um tipo de crate especial. Isso se deve a razões técnicas complexas que esperamos eliminar no futuro. Na Listagem 19-29, mostramos como definir uma macro procedural, onde `some_attribute` é um espaço reservado para usar uma variedade específica de macro.

Nome do arquivo: `src/lib.rs`

```rust
use proc_macro::TokenStream;

#[some_attribute]
pub fn some_name(input: TokenStream) -> TokenStream {
}
```

Listagem 19-29: Um exemplo de definição de uma macro procedural

A função que define uma macro procedural recebe um `TokenStream` como entrada e produz um `TokenStream` como saída. O tipo `TokenStream` é definido pelo crate `proc_macro` que está incluído com Rust e representa uma sequência de tokens. Este é o núcleo da macro: o código-fonte em que a macro está operando constitui o `TokenStream` de entrada, e o código que a macro produz é o `TokenStream` de saída. A função também tem um atributo anexado a ela que especifica qual tipo de macro procedural estamos criando. Podemos ter vários tipos de macros procedurais no mesmo crate.

Vamos analisar os diferentes tipos de macros procedurais. Começaremos com uma macro `derive` customizada e, em seguida, explicaremos as pequenas diferenças que tornam as outras formas diferentes.
