# Reexportando Nomes com `pub use`

Quando trazemos um nome para o escopo com a palavra-chave `use`, o nome disponível no novo escopo é privado. Para permitir que o código que chama nosso código se refira a esse nome como se ele tivesse sido definido no escopo desse código, podemos combinar `pub` e `use`. Essa técnica é chamada de _reexportação_ (re-exporting) porque estamos trazendo um item para o escopo, mas também tornando esse item disponível para que outros o tragam para seu escopo.

A Listagem 7-17 mostra o código na Listagem 7-11 com `use` no módulo raiz alterado para `pub use`.

Nome do arquivo: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_restaurant() {
    hosting::add_to_waitlist();
}
```

Listagem 7-17: Tornando um nome disponível para qualquer código usar de um novo escopo com `pub use`

Antes dessa alteração, o código externo teria que chamar a função `add_to_waitlist` usando o caminho `restaurant::front_of_house::hosting::add_to_waitlist()`. Agora que este `pub use` reexportou o módulo `hosting` do módulo raiz, o código externo pode usar o caminho `restaurant::hosting::add_to_waitlist()` em vez disso.

A reexportação é útil quando a estrutura interna do seu código é diferente de como os programadores que chamam seu código pensariam sobre o domínio. Por exemplo, nesta metáfora do restaurante, as pessoas que administram o restaurante pensam em "frente da casa" e "fundo da casa". Mas os clientes que visitam um restaurante provavelmente não pensarão nas partes do restaurante nesses termos. Com `pub use`, podemos escrever nosso código com uma estrutura, mas expor uma estrutura diferente. Fazer isso torna nossa biblioteca bem organizada para programadores que trabalham na biblioteca e programadores que chamam a biblioteca. Veremos outro exemplo de `pub use` e como ele afeta a documentação do seu crate em "Exportando uma API Pública Conveniente com pub use".
