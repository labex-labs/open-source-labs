# arrays/slices

Al igual que las tuplas, los arrays y los slices se pueden desestructurar de la siguiente manera:

```rust
fn main() {
    // Intenta cambiar los valores en el array, ¡o conviértelo en un slice!
    let array = [1, -2, 6];

    match array {
        // Vincula el segundo y el tercer elementos a las variables respectivas
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // Los valores individuales se pueden ignorar con _
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} y array[1] fue ignorado",
            third
        ),

        // También puedes vincular algunos y ignorar el resto
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} y todos los demás fueron ignorados",
            second
        ),
        // El código siguiente no se compilaría
        // [-1, second] =>...

        // O almacenarlos en otro array/slice (el tipo depende
        // del del valor contra el que se está coincidiendo)
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} y los otros elementos fueron {:?}",
            second, tail
        ),

        // Combinando estos patrones, podemos, por ejemplo, vincular el primer y
        // el último valor, y almacenar el resto de ellos en un solo array
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
