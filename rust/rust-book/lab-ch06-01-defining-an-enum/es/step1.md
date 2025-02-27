# Definiendo un Enum

Mientras que los structs te dan una forma de agrupar campos y datos relacionados, como un `Rectangle` con su `width` y `height`, los enums te dan una forma de decir que un valor es uno de un conjunto posible de valores. Por ejemplo, podríamos querer decir que `Rectangle` es uno de un conjunto posible de formas que también incluye `Circle` y `Triangle`. Para hacer esto, Rust nos permite codificar estas posibilidades como un enum.

Veamos una situación que podríamos querer expresar en código y veamos por qué los enums son útiles y más adecuados que los structs en este caso. Digamos que necesitamos trabajar con direcciones IP. Actualmente, se utilizan dos estándares principales para las direcciones IP: la versión cuatro y la versión seis. Debido a que estas son las únicas posibilidades para una dirección IP que nuestro programa encontrará, podemos _enumerar_ todas las variantes posibles, de ahí que el enumerado tenga su nombre.

Cualquier dirección IP puede ser una dirección de versión cuatro o una dirección de versión seis, pero no ambas al mismo tiempo. Esa propiedad de las direcciones IP hace que la estructura de datos enum sea adecuada porque un valor enum solo puede ser una de sus variantes. Tanto las direcciones de versión cuatro como las de versión seis todavía son fundamentalmente direcciones IP, por lo que deben tratarse como el mismo tipo cuando el código está manejando situaciones que se aplican a cualquier tipo de dirección IP.

Podemos expresar este concepto en código definiendo una enumeración `IpAddrKind` y listando los tipos posibles que puede tener una dirección IP, `V4` y `V6`. Estas son las variantes del enum:

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

`IpAddrKind` ahora es un tipo de datos personalizado que podemos utilizar en otros lugares de nuestro código.
