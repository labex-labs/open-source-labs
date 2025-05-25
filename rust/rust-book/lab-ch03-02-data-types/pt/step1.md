# Tipos de Dados

Cada valor em Rust é de um determinado **tipo de dado** (data type), que informa ao Rust que tipo de dado está sendo especificado, para que ele saiba como trabalhar com esses dados. Veremos dois subconjuntos de tipos de dados: escalares e compostos.

Tenha em mente que Rust é uma linguagem de **tipagem estática** (statically typed), o que significa que ela deve conhecer os tipos de todas as variáveis em tempo de compilação. O compilador geralmente pode inferir qual tipo queremos usar com base no valor e em como o usamos. Em casos onde muitos tipos são possíveis, como quando convertemos uma `String` para um tipo numérico usando `parse` em "Comparando o Palpite com o Número Secreto", devemos adicionar uma anotação de tipo, assim:

```rust
let guess: u32 = "42".parse().expect("Not a number!");
```

Se não adicionarmos a anotação de tipo `: u32` mostrada no código anterior, Rust exibirá o seguinte erro, o que significa que o compilador precisa de mais informações de nós para saber qual tipo queremos usar:

```bash
$ cargo build
   Compiling no_type_annotations v0.1.0 (file:///projects/no_type_annotations)
error[E0282]: type annotations needed
 --> src/main.rs:2:9
  |
2 |     let guess = "42".parse().expect("Not a number!");
  |         ^^^^^ consider giving `guess` a type
```

Você verá diferentes anotações de tipo para outros tipos de dados.
