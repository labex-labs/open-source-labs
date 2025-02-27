# tableaux/slices

Comme les tuples, les tableaux et les slices peuvent être décomposés de cette manière :

```rust
fn main() {
    // Essayez de modifier les valeurs dans le tableau, ou en faire un slice!
    let array = [1, -2, 6];

    match array {
        // Lie le deuxième et le troisième éléments aux variables respectives
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // Les valeurs individuelles peuvent être ignorées avec _
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} et array[1] a été ignoré",
            third
        ),

        // Vous pouvez également lier certains et ignorer le reste
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} et toutes les autres ont été ignorées",
            second
        ),
        // Le code ci-dessous ne compilerait pas
        // [-1, second] =>...

        // Ou les stocker dans un autre tableau/slice (le type dépend
        // de celui de la valeur contre laquelle on est en train de matcher)
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} et les autres éléments étaient {:?}",
            second, tail
        ),

        // En combinant ces modèles, nous pouvons, par exemple, lier la première et
        // la dernière valeur, et stocker le reste d'entre elles dans un seul tableau
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
