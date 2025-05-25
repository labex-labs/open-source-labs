# arrays/slices

Assim como tuplas, arrays e slices podem ser desestruturados desta forma:

```rust
fn main() {
    // Tente alterar os valores no array, ou transformá-lo em um slice!
    let array = [1, -2, 6];

    match array {
        // Vincula o segundo e o terceiro elementos às respectivas variáveis
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // Valores únicos podem ser ignorados com _
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} e array[1] foi ignorado",
            third
        ),

        // Você também pode vincular alguns e ignorar o restante
        [-1, second, ..] => println!(
            "array[0] = -1, array[1] = {} e todos os outros foram ignorados",
            second
        ),
        // O código abaixo não seria compilado
        // [-1, second] => ...

        // Ou armazená-los em outro array/slice (o tipo depende do valor
        // que está sendo comparado)
        [3, second, tail @ ..] => println!(
            "array[0] = 3, array[1] = {} e os outros elementos foram {:?}",
            second, tail
        ),

        // Combinando esses padrões, podemos, por exemplo, vincular os primeiros e
        // últimos valores e armazenar o restante deles em um único array
        [first, middle @ .., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
