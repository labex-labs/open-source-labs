# Parâmetros de Tipo Genéricos, _Trait Bounds_ e _Lifetimes_ Juntos

Vamos dar uma olhada breve na sintaxe de como especificar parâmetros de tipo genéricos, _trait bounds_ e _lifetimes_ tudo em uma função!

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
```

Esta é a função `longest` da Listagem 10-21 que retorna a maior de duas _string slices_. Mas agora ela tem um parâmetro extra chamado `ann` do tipo genérico `T`, que pode ser preenchido por qualquer tipo que implemente o _trait_ `Display`, conforme especificado pela cláusula `where`. Este parâmetro extra será impresso usando `{}`, e é por isso que o _trait bound_ `Display` é necessário. Como os _lifetimes_ são um tipo de genérico, as declarações do parâmetro de _lifetime_ `'a` e do parâmetro de tipo genérico `T` vão na mesma lista dentro dos colchetes angulares após o nome da função.
