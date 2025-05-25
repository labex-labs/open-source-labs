# Desestruturando Structs (Destructuring Structs)

A Listagem 18-12 mostra uma struct `Point` com dois campos, `x` e `y`, que podemos desmembrar usando um padrão com uma declaração `let`.

Nome do arquivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    assert_eq!(0, a);
    assert_eq!(7, b);
}
```

Listagem 18-12: Desestruturando os campos de uma struct em variáveis separadas

Este código cria as variáveis `a` e `b` que correspondem aos valores dos campos `x` e `y` da struct `p`. Este exemplo mostra que os nomes das variáveis no padrão não precisam corresponder aos nomes dos campos da struct. No entanto, é comum corresponder os nomes das variáveis aos nomes dos campos para facilitar a lembrança de quais variáveis vieram de quais campos. Devido a esse uso comum, e porque escrever `let Point { x: x, y: y } = p;` contém muita duplicação, o Rust tem uma abreviação para padrões que correspondem aos campos da struct: você só precisa listar o nome do campo da struct, e as variáveis criadas a partir do padrão terão os mesmos nomes. A Listagem 18-13 se comporta da mesma maneira que o código na Listagem 18-12, mas as variáveis criadas no padrão `let` são `x` e `y` em vez de `a` e `b`.

Nome do arquivo: `src/main.rs`

```rust
struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let p = Point { x: 0, y: 7 };

    let Point { x, y } = p;
    assert_eq!(0, x);
    assert_eq!(7, y);
}
```

Listagem 18-13: Desestruturando campos de struct usando a abreviação de campo de struct

Este código cria as variáveis `x` e `y` que correspondem aos campos `x` e `y` da variável `p`. O resultado é que as variáveis `x` e `y` contêm os valores da struct `p`.

Também podemos desestruturar com valores literais como parte do padrão da struct, em vez de criar variáveis para todos os campos. Fazer isso nos permite testar alguns dos campos para valores específicos enquanto criamos variáveis para desestruturar os outros campos.

Na Listagem 18-14, temos uma expressão `match` que separa os valores `Point` em três casos: pontos que estão diretamente no eixo `x` (o que é verdade quando `y = 0`), no eixo `y` (`x = 0`), ou em nenhum dos eixos.

Nome do arquivo: `src/main.rs`

```rust
fn main() {
    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 } => println!("On the x axis at {x}"),
        Point { x: 0, y } => println!("On the y axis at {y}"),
        Point { x, y } => {
            println!("On neither axis: ({x}, {y})");
        }
    }
}
```

Listagem 18-14: Desestruturando e correspondendo valores literais em um padrão

O primeiro braço corresponderá a qualquer ponto que esteja no eixo `x` especificando que o campo `y` corresponde se seu valor corresponder ao literal `0`. O padrão ainda cria uma variável `x` que podemos usar no código para este braço.

Da mesma forma, o segundo braço corresponde a qualquer ponto no eixo `y` especificando que o campo `x` corresponde se seu valor for `0` e cria uma variável `y` para o valor do campo `y`. O terceiro braço não especifica nenhum literal, então ele corresponde a qualquer outro `Point` e cria variáveis para os campos `x` e `y`.

Neste exemplo, o valor `p` corresponde ao segundo braço em virtude de `x` conter um `0`, então este código imprimirá `On the y axis at 7`.

Lembre-se que uma expressão `match` para de verificar os braços assim que encontra o primeiro padrão correspondente, então, embora `Point { x: 0, y: 0}` esteja no eixo `x` e no eixo `y`, este código só imprimirá `On the x axis at 0`.
