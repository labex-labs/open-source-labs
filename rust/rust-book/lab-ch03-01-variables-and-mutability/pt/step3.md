# Shadowing (Sombreamento)

Como você viu no tutorial do jogo de adivinhação no Capítulo 2, você pode declarar uma nova variável com o mesmo nome de uma variável anterior. Os Rustaceans dizem que a primeira variável é _shadowed_ (sombreada) pela segunda, o que significa que a segunda variável é o que o compilador verá quando você usar o nome da variável. Na prática, a segunda variável ofusca a primeira, assumindo qualquer uso do nome da variável até que ela própria seja sombreada ou o escopo termine. Podemos sombrear uma variável usando o nome da mesma variável e repetindo o uso da palavra-chave `let`, da seguinte forma:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x = 5;

    let x = x + 1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");
}
```

Este programa primeiro vincula `x` a um valor de `5`. Em seguida, ele cria uma nova variável `x` repetindo `let x =`, pegando o valor original e adicionando `1`, de modo que o valor de `x` seja então `6`. Em seguida, dentro de um escopo interno criado com as chaves, a terceira instrução `let` também sombreia `x` e cria uma nova variável, multiplicando o valor anterior por `2` para dar a `x` um valor de `12`. Quando esse escopo termina, o sombreamento interno termina e `x` volta a ser `6`. Quando executamos este programa, ele exibirá o seguinte:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
    Finished dev [unoptimized + debuginfo] target(s) in 0.31s
     Running `target/debug/variables`
The value of x in the inner scope is: 12
The value of x is: 6
```

O sombreamento é diferente de marcar uma variável como `mut` porque receberemos um erro em tempo de compilação se tentarmos, acidentalmente, reatribuir a esta variável sem usar a palavra-chave `let`. Usando `let`, podemos realizar algumas transformações em um valor, mas fazer com que a variável seja imutável após a conclusão dessas transformações.

A outra diferença entre `mut` e sombreamento é que, como estamos efetivamente criando uma nova variável quando usamos a palavra-chave `let` novamente, podemos alterar o tipo do valor, mas reutilizar o mesmo nome. Por exemplo, digamos que nosso programa peça a um usuário para mostrar quantos espaços ele deseja entre algum texto, inserindo caracteres de espaço, e então queremos armazenar essa entrada como um número:

```rust
let spaces = "   ";
let spaces = spaces.len();
```

A primeira variável `spaces` é do tipo string e a segunda variável `spaces` é do tipo número. O sombreamento, portanto, nos poupa de ter que inventar nomes diferentes, como `spaces_str` e `spaces_num`; em vez disso, podemos reutilizar o nome mais simples `spaces`. No entanto, se tentarmos usar `mut` para isso, como mostrado aqui, receberemos um erro em tempo de compilação:

```rust
let mut spaces = "   ";
spaces = spaces.len();
```

O erro diz que não podemos mutar o tipo de uma variável:

```bash
$ cargo run
   Compiling variables v0.1.0 (file:///projects/variables)
error[E0308]: mismatched types
 --> src/main.rs:3:14
  |
2 |     let mut spaces = "   ";
  |                      ----- expected due to this value
3 |     spaces = spaces.len();
  |              ^^^^^^^^^^^^ expected `&str`, found `usize`
```

Agora que exploramos como as variáveis funcionam, vamos analisar mais tipos de dados que elas podem ter.
