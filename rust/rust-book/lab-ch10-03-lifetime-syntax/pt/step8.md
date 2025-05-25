# Anotações de _Lifetime_ em Definições de Structs

Até agora, as structs que definimos contêm todos os tipos _owned_. Podemos definir structs para conter referências, mas, nesse caso, precisaríamos adicionar uma anotação de _lifetime_ em cada referência na definição da struct. A Listagem 10-24 tem uma struct chamada `ImportantExcerpt` que contém um _string slice_.

Nome do arquivo: `src/main.rs`

```rust
1 struct ImportantExcerpt<'a> {
  2 part: &'a str,
}

fn main() {
  3 let novel = String::from(
        "Call me Ishmael. Some years ago..."
    );
  4 let first_sentence = novel
        .split('.')
        .next()
        .expect("Could not find a '.'");
  5 let i = ImportantExcerpt {
        part: first_sentence,
    };
}
```

Listagem 10-24: Uma struct que contém uma referência, exigindo uma anotação de _lifetime_

Esta struct tem o campo único `part` que contém um _string slice_, que é uma referência \[2]. Assim como com os tipos de dados genéricos, declaramos o nome do parâmetro genérico de _lifetime_ dentro de colchetes angulares após o nome da struct para que possamos usar o parâmetro de _lifetime_ no corpo da definição da struct \[1]. Esta anotação significa que uma instância de `ImportantExcerpt` não pode viver mais tempo do que a referência que ela contém em seu campo `part`.

A função `main` aqui cria uma instância da struct `ImportantExcerpt` \[5] que contém uma referência à primeira frase da `String` \[4] _owned_ pela variável `novel` \[3]. Os dados em `novel` existem antes que a instância `ImportantExcerpt` seja criada. Além disso, `novel` não sai do escopo até depois que `ImportantExcerpt` sai do escopo, então a referência na instância `ImportantExcerpt` é válida.
