# Em Definições de Structs

Também podemos definir structs para usar um parâmetro de tipo genérico em um ou mais campos usando a sintaxe `<>`. A Listagem 10-6 define uma struct `Point<T>` para armazenar os valores das coordenadas `x` e `y` de qualquer tipo.

Nome do arquivo: `src/main.rs`

```rust
1 struct Point<T> {
  2 x: T,
  3 y: T,
}

fn main() {
    let integer = Point { x: 5, y: 10 };
    let float = Point { x: 1.0, y: 4.0 };
}
```

Listagem 10-6: Uma struct `Point<T>` que armazena valores `x` e `y` do tipo `T`

A sintaxe para usar genéricos em definições de struct é semelhante à usada em definições de funções. Primeiro, declaramos o nome do parâmetro de tipo dentro de colchetes angulares logo após o nome da struct \[1]. Em seguida, usamos o tipo genérico na definição da struct onde, de outra forma, especificaríamos tipos de dados concretos \[23].

Observe que, como usamos apenas um tipo genérico para definir `Point<T>`, esta definição diz que a struct `Point<T>` é genérica sobre algum tipo `T`, e os campos `x` e `y` são _ambos_ do mesmo tipo, seja qual for esse tipo. Se criarmos uma instância de um `Point<T>` que tenha valores de tipos diferentes, como na Listagem 10-7, nosso código não compilará.

Nome do arquivo: `src/main.rs`

```rust
struct Point<T> {
    x: T,
    y: T,
}

fn main() {
    let wont_work = Point { x: 5, y: 4.0 };
}
```

Listagem 10-7: Os campos `x` e `y` devem ser do mesmo tipo porque ambos têm o mesmo tipo de dados genérico `T`.

Neste exemplo, quando atribuímos o valor inteiro `5` a `x`, informamos ao compilador que o tipo genérico `T` será um inteiro para esta instância de `Point<T>`. Então, quando especificamos `4.0` para `y`, que definimos para ter o mesmo tipo que `x`, obteremos um erro de incompatibilidade de tipo como este:

```bash
error[E0308]: mismatched types
 --> src/main.rs:7:38
  |
7 |     let wont_work = Point { x: 5, y: 4.0 };
  |                                      ^^^ expected integer, found floating-
point number
```

Para definir uma struct `Point` onde `x` e `y` são ambos genéricos, mas podem ter tipos diferentes, podemos usar vários parâmetros de tipo genérico. Por exemplo, na Listagem 10-8, alteramos a definição de `Point` para ser genérica sobre os tipos `T` e `U`, onde `x` é do tipo `T` e `y` é do tipo `U`.

Nome do arquivo: `src/main.rs`

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

fn main() {
    let both_integer = Point { x: 5, y: 10 };
    let both_float = Point { x: 1.0, y: 4.0 };
    let integer_and_float = Point { x: 5, y: 4.0 };
}
```

Listagem 10-8: Um genérico `Point<T, U>` sobre dois tipos para que `x` e `y` possam ser valores de tipos diferentes

Agora, todas as instâncias de `Point` mostradas são permitidas! Você pode usar quantos parâmetros de tipo genérico quiser em uma definição, mas usar mais do que alguns torna seu código difícil de ler. Se você estiver descobrindo que precisa de muitos tipos genéricos em seu código, isso pode indicar que seu código precisa ser reestruturado em pedaços menores.
