# Calculando o Tamanho de um Tipo Não Recursivo

Recorde o enum `Message` que definimos na Listagem 6-2 quando discutimos definições de enum no Capítulo 6:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Para determinar quanto espaço alocar para um valor `Message`, o Rust percorre cada uma das variantes para ver qual variante precisa de mais espaço. O Rust vê que `Message::Quit` não precisa de nenhum espaço, `Message::Move` precisa de espaço suficiente para armazenar dois valores `i32` e assim por diante. Como apenas uma variante será usada, o máximo de espaço que um valor `Message` precisará é o espaço que seria necessário para armazenar a maior de suas variantes.

Compare isso com o que acontece quando o Rust tenta determinar quanto espaço um tipo recursivo como o enum `List` na Listagem 15-2 precisa. O compilador começa olhando para a variante `Cons`, que contém um valor do tipo `i32` e um valor do tipo `List`. Portanto, `Cons` precisa de uma quantidade de espaço igual ao tamanho de um `i32` mais o tamanho de um `List`. Para descobrir quanta memória o tipo `List` precisa, o compilador olha para as variantes, começando com a variante `Cons`. A variante `Cons` contém um valor do tipo `i32` e um valor do tipo `List`, e esse processo continua infinitamente, como mostrado na Figura 15-1.

Figura 15-1: Uma `List` infinita consistindo em variantes `Cons` infinitas
