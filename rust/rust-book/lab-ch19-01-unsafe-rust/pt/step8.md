# Implementando uma Trait Unsafe

Podemos usar `unsafe` para implementar uma trait unsafe. Uma trait é unsafe quando pelo menos um de seus métodos tem algum invariante que o compilador não pode verificar. Declaramos que uma trait é `unsafe` adicionando a palavra-chave `unsafe` antes de `trait` e marcando a implementação da trait como `unsafe` também, conforme mostrado na Listagem 19-11.

    unsafe trait Foo {
        // methods go here
    }

    unsafe impl Foo for i32 {
        // method implementations go here
    }

Listagem 19-11: Definindo e implementando uma trait unsafe

Ao usar `unsafe impl`, estamos prometendo que manteremos os invariantes que o compilador não pode verificar.

Como exemplo, lembre-se das traits marcadoras `Send` e `Sync` que discutimos em "Concorrência Extensível com as Traits Send e Sync": o compilador implementa essas traits automaticamente se nossos tipos forem compostos inteiramente de tipos `Send` e `Sync`. Se implementarmos um tipo que contém um tipo que não é `Send` ou `Sync`, como ponteiros brutos, e quisermos marcar esse tipo como `Send` ou `Sync`, devemos usar `unsafe`. O Rust não pode verificar se nosso tipo mantém as garantias de que ele pode ser enviado com segurança entre threads ou acessado de várias threads; portanto, precisamos fazer essas verificações manualmente e indicar isso com `unsafe`.
