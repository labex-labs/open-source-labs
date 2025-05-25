# Definindo um Enum

Onde as structs fornecem uma maneira de agrupar campos e dados relacionados, como um `Rectangle` com sua `width` e `height`, os enums fornecem uma maneira de dizer que um valor é um de um conjunto possível de valores. Por exemplo, podemos querer dizer que `Rectangle` é uma de um conjunto de formas possíveis que também inclui `Circle` e `Triangle`. Para fazer isso, o Rust nos permite codificar essas possibilidades como um enum.

Vamos analisar uma situação que podemos querer expressar em código e ver por que os enums são úteis e mais apropriados do que as structs neste caso. Digamos que precisamos trabalhar com endereços IP. Atualmente, dois padrões principais são usados para endereços IP: versão quatro e versão seis. Como essas são as únicas possibilidades para um endereço IP que nosso programa encontrará, podemos _enumerar_ todas as variantes possíveis, que é de onde a enumeração recebe seu nome.

Qualquer endereço IP pode ser um endereço versão quatro ou versão seis, mas não ambos ao mesmo tempo. Essa propriedade dos endereços IP torna a estrutura de dados enum apropriada porque um valor enum pode ser apenas uma de suas variantes. Tanto os endereços versão quatro quanto os versão seis ainda são fundamentalmente endereços IP, portanto, devem ser tratados como o mesmo tipo quando o código está lidando com situações que se aplicam a qualquer tipo de endereço IP.

Podemos expressar esse conceito em código definindo uma enumeração `IpAddrKind` e listando os tipos possíveis que um endereço IP pode ser, `V4` e `V6`. Estas são as variantes do enum:

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

`IpAddrKind` é agora um tipo de dado personalizado que podemos usar em outras partes do nosso código.
