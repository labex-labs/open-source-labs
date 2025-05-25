# Visibilidade de Structs

Structs possuem um nível extra de visibilidade em relação aos seus campos. A visibilidade padrão é privada, e pode ser alterada com o modificador `pub`. Essa visibilidade só importa quando um struct é acessado de fora do módulo onde é definido, e tem o objetivo de esconder informações (encapsulamento).

```rust
mod my {
    // Um struct público com um campo público de tipo genérico `T`
    pub struct OpenBox<T> {
        pub contents: T,
    }

    // Um struct público com um campo privado de tipo genérico `T`
    pub struct ClosedBox<T> {
        contents: T,
    }

    impl<T> ClosedBox<T> {
        // Um método construtor público
        pub fn new(contents: T) -> ClosedBox<T> {
            ClosedBox {
                contents: contents,
            }
        }
    }
}

fn main() {
    // Structs públicos com campos públicos podem ser criados normalmente
    let open_box = my::OpenBox { contents: "informação pública" };

    // e seus campos podem ser acessados normalmente.
    println!("A caixa aberta contém: {}", open_box.contents);

    // Structs públicos com campos privados não podem ser criados usando nomes de campos.
    // Erro! `ClosedBox` possui campos privados
    //let closed_box = my::ClosedBox { contents: "informação classificada" };
    // TODO ^ Tente descomentar esta linha

    // No entanto, structs com campos privados podem ser criados usando
    // construtores públicos
    let _closed_box = my::ClosedBox::new("informação classificada");

    // e os campos privados de um struct público não podem ser acessados.
    // Erro! O campo `contents` é privado
    //println!("A caixa fechada contém: {}", _closed_box.contents);
    // TODO ^ Tente descomentar esta linha
}
```
