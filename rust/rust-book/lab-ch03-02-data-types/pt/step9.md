# O Tipo Tupla

Uma _tupla_ é uma forma geral de agrupar um número de valores com uma variedade de tipos em um tipo composto. Tuplas têm um comprimento fixo: uma vez declaradas, elas não podem crescer ou diminuir de tamanho.

Criamos uma tupla escrevendo uma lista de valores separados por vírgulas dentro de parênteses. Cada posição na tupla tem um tipo, e os tipos dos diferentes valores na tupla não precisam ser os mesmos. Adicionamos anotações de tipo opcionais neste exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let tup: (i32, f64, u8) = (500, 6.4, 1);
}
```

A variável `tup` se vincula à tupla inteira porque uma tupla é considerada um único elemento composto. Para obter os valores individuais de uma tupla, podemos usar correspondência de padrões (pattern matching) para desestruturar um valor de tupla, assim:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let tup = (500, 6.4, 1);

    let (x, y, z) = tup;

    println!("The value of y is: {y}");
}
```

Este programa primeiro cria uma tupla e a vincula à variável `tup`. Em seguida, usa um padrão com `let` para pegar `tup` e transformá-la em três variáveis separadas, `x`, `y` e `z`. Isso é chamado de _desestruturação_ (destructuring) porque quebra a tupla única em três partes. Finalmente, o programa imprime o valor de `y`, que é `6.4`.

Também podemos acessar um elemento da tupla diretamente usando um ponto (`.`) seguido pelo índice do valor que queremos acessar. Por exemplo:

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let x: (i32, f64, u8) = (500, 6.4, 1);

    let five_hundred = x.0;

    let six_point_four = x.1;

    let one = x.2;
}
```

Este programa cria a tupla `x` e, em seguida, acessa cada elemento da tupla usando seus respectivos índices. Como na maioria das linguagens de programação, o primeiro índice em uma tupla é 0.

A tupla sem nenhum valor tem um nome especial, _unit_ (unidade). Este valor e seu tipo correspondente são ambos escritos `()` e representam um valor vazio ou um tipo de retorno vazio. Expressões implicitamente retornam o valor unitário se não retornarem nenhum outro valor.
