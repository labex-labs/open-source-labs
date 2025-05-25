# Tuplas

Uma tupla é uma coleção de valores de diferentes tipos. Tuplas são construídas usando parênteses `()`, e cada tupla em si é um valor com a assinatura de tipo `(T1, T2, ...)`, onde `T1`, `T2` são os tipos de seus membros. Funções podem usar tuplas para retornar múltiplos valores, pois tuplas podem conter qualquer número de valores.

```rust
// Tuplas podem ser usadas como argumentos de função e como valores de retorno.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` pode ser usado para ligar os membros de uma tupla a variáveis.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// A struct a seguir é para a atividade.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // Uma tupla com um monte de tipos diferentes.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Valores podem ser extraídos da tupla usando indexação de tupla.
    println!("Long tuple first value: {}", long_tuple.0);
    println!("Long tuple second value: {}", long_tuple.1);

    // Tuplas podem ser membros de tuplas.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Tuplas são imprimíveis.
    println!("tuple of tuples: {:?}", tuple_of_tuples);

    // Mas Tuplas longas (mais de 12 elementos) não podem ser impressas.
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Too long tuple: {:?}", too_long_tuple);
    // TODO ^ Uncomment the above 2 lines to see the compiler error

    let pair = (1, true);
    println!("Pair is {:?}", pair);

    println!("The reversed pair is {:?}", reverse(pair));

    // Para criar tuplas de um elemento, a vírgula é necessária para diferenciá-las
    // de um literal cercado por parênteses.
    println!("One element tuple: {:?}", (5u32,));
    println!("Just an integer: {:?}", (5u32));

    // Tuplas podem ser desestruturadas para criar ligações (bindings).
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## Atividade

1.  _Recapitulação_: Adicione o trait `fmt::Display` à struct `Matrix` no exemplo acima, de modo que, se você mudar de imprimir o formato de debug `{:?}` para o formato de exibição `{}` , você veja a seguinte saída:

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    Você pode querer consultar o exemplo para exibição de impressão.

2.  Adicione uma função `transpose` usando a função `reverse` como um modelo, que aceita uma matriz como argumento e retorna uma matriz na qual dois elementos foram trocados. Por exemplo:

    ```rust
    println!("Matrix:\n{}", matrix);
    println!("Transpose:\n{}", transpose(matrix));
    ```

    Resulta na saída:

    ```plaintext
    Matrix:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transpose:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
