# Anotações de _Lifetime_ em Definições de Métodos

Quando implementamos métodos em uma struct com _lifetimes_, usamos a mesma sintaxe que a dos parâmetros de tipo genéricos mostrados na Listagem 10-11. Onde declaramos e usamos os parâmetros de _lifetime_ depende se eles estão relacionados aos campos da struct ou aos parâmetros e valores de retorno do método.

Os nomes de _lifetime_ para campos de struct sempre precisam ser declarados após a palavra-chave `impl` e, em seguida, usados após o nome da struct, porque esses _lifetimes_ fazem parte do tipo da struct.

Nas assinaturas de métodos dentro do bloco `impl`, as referências podem estar vinculadas ao _lifetime_ das referências nos campos da struct, ou podem ser independentes. Além disso, as regras de elisão de _lifetime_ geralmente fazem com que as anotações de _lifetime_ não sejam necessárias nas assinaturas de métodos. Vamos analisar alguns exemplos usando a struct chamada `ImportantExcerpt` que definimos na Listagem 10-24.

Primeiro, usaremos um método chamado `level` cujo único parâmetro é uma referência a `self` e cujo valor de retorno é um `i32`, que não é uma referência a nada:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn level(&self) -> i32 {
        3
    }
}
```

A declaração do parâmetro de _lifetime_ após `impl` e seu uso após o nome do tipo são necessários, mas não somos obrigados a anotar o _lifetime_ da referência a `self` por causa da primeira regra de elisão.

Aqui está um exemplo onde a terceira regra de elisão de _lifetime_ se aplica:

```rust
impl<'a> ImportantExcerpt<'a> {
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

Existem dois _lifetimes_ de entrada, então o Rust aplica a primeira regra de elisão de _lifetime_ e dá a `&self` e `announcement` seus próprios _lifetimes_. Então, como um dos parâmetros é `&self`, o tipo de retorno recebe o _lifetime_ de `&self`, e todos os _lifetimes_ foram contabilizados.
