# arrays/slices

Wie Tupel können Arrays und Slices auch so dekonstruiert werden:

```rust
fn main() {
    // Versuchen Sie, die Werte im Array zu ändern oder es zu einem Slice zu machen!
    let array = [1, -2, 6];

    match array {
        // Bindet das zweite und das dritte Element an die entsprechenden Variablen
        [0, second, third] =>
            println!("array[0] = 0, array[1] = {}, array[2] = {}", second, third),

        // Einzelwerte können mit _ ignoriert werden
        [1, _, third] => println!(
            "array[0] = 1, array[2] = {} und array[1] wurde ignoriert",
            third
        ),

        // Sie können auch einige binden und den Rest ignorieren
        [-1, second,..] => println!(
            "array[0] = -1, array[1] = {} und alle anderen wurden ignoriert",
            second
        ),
        // Der folgende Code würde nicht kompilieren
        // [-1, second] =>...

        // Oder speichern Sie sie in einem anderen Array/Slice (der Typ hängt davon ab,
        // welchem Typ der Wert entspricht, gegen den abgeglichen wird)
        [3, second, tail @..] => println!(
            "array[0] = 3, array[1] = {} und die anderen Elemente waren {:?}",
            second, tail
        ),

        // Indem wir diese Muster kombinieren, können wir beispielsweise das erste und
        // das letzte Element binden und den Rest in einem einzelnen Array speichern
        [first, middle @.., last] => println!(
            "array[0] = {}, middle = {:?}, array[2] = {}",
            first, middle, last
        ),
    }
}
```
