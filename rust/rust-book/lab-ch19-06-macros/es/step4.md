# Macros Procedimentales para Generar Código a Partir de Atributos

La segunda forma de macros es la macro procedimental, que actúa más como una función (y es un tipo de procedimiento). Las _macros procedimentales_ aceptan algún código como entrada, operan sobre ese código y producen algún código como salida, en lugar de coincidir con patrones y reemplazar el código con otro código como lo hacen las macros declarativas. Los tres tipos de macros procedimentales son personalizadas `derive`, similares a atributos y similares a funciones, y todos funcionan de manera similar.

Al crear macros procedimentales, las definiciones deben residir en su propio crat con un tipo de crat especial. Esto es por razones técnicas complejas que esperamos eliminar en el futuro. En la Lista 19-29, mostramos cómo definir una macro procedimental, donde `some_attribute` es un marcador de posición para usar una variedad específica de macro.

Nombre del archivo: `src/lib.rs`

```rust
use proc_macro::TokenStream;

#[some_attribute]
pub fn some_name(input: TokenStream) -> TokenStream {
}
```

Lista 19-29: Un ejemplo de definición de una macro procedimental

La función que define una macro procedimental toma un `TokenStream` como entrada y produce un `TokenStream` como salida. El tipo `TokenStream` está definido por el crat `proc_macro` que viene incluido con Rust y representa una secuencia de tokens. Esta es la esencia de la macro: el código fuente sobre el que opera la macro forma el `TokenStream` de entrada, y el código que produce la macro es el `TokenStream` de salida. La función también tiene un atributo adjunto que especifica qué tipo de macro procedimental estamos creando. Podemos tener múltiples tipos de macros procedimentales en el mismo crat.

Echemos un vistazo a los diferentes tipos de macros procedimentales. Empezaremos con una macro personalizada `derive` y luego explicaremos las pequeñas diferencias que hacen que las otras formas sean diferentes.
