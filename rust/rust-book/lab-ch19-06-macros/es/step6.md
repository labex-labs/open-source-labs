# Macros Similares a Atributos

Las macros similares a atributos son similares a las macros `derive` personalizadas, pero en lugar de generar código para el atributo `derive`, te permiten crear nuevos atributos. También son más flexibles: `derive` solo funciona para structs y enums; los atributos se pueden aplicar a otros elementos también, como funciones. Aquí hay un ejemplo de uso de una macro similar a un atributo. Digamos que tienes un atributo llamado `route` que anota funciones cuando se usa un marco de aplicación web:

```rust
#[route(GET, "/")]
fn index() {
```

Este atributo `#[route]` sería definido por el marco como una macro procedimental. La firma de la función de definición de la macro se vería así:

    #[proc_macro_attribute]
    pub fn route(
        attr: TokenStream,
        item: TokenStream
    ) -> TokenStream {

Aquí, tenemos dos parámetros de tipo `TokenStream`. El primero es para el contenido del atributo: la parte `GET, "/"`. El segundo es el cuerpo del elemento al que se adjunta el atributo: en este caso, `fn index() {}` y el resto del cuerpo de la función.

Excepto por eso, las macros similares a atributos funcionan de la misma manera que las macros `derive` personalizadas: creas un crat con el tipo de crat `proc-macro` e implementas una función que genere el código que quieres!
