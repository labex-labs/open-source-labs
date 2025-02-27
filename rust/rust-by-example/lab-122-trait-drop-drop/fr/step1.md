# Drop

Le trait `Drop` n'a qu'une seule méthode : `drop`, qui est appelée automatiquement lorsqu'un objet sort de portée. L'utilisation principale du trait `Drop` est de libérer les ressources que possède l'instance de l'implémentation.

`Box`, `Vec`, `String`, `File` et `Process` sont quelques exemples de types qui implémentent le trait `Drop` pour libérer des ressources. Le trait `Drop` peut également être implémenté manuellement pour n'importe quel type de données personnalisé.

L'exemple suivant ajoute une impression à la console à la fonction `drop` pour annoncer lorsqu'elle est appelée.

```rust
struct Droppable {
    name: &'static str,
}

// Cette implémentation triviale de `drop` ajoute une impression à la console.
impl Drop for Droppable {
    fn drop(&mut self) {
        println!("> Dropping {}", self.name);
    }
}

fn main() {
    let _a = Droppable { name: "a" };

    // bloc A
    {
        let _b = Droppable { name: "b" };

        // bloc B
        {
            let _c = Droppable { name: "c" };
            let _d = Droppable { name: "d" };

            println!("Exiting block B");
        }
        println!("Just exited block B");

        println!("Exiting block A");
    }
    println!("Just exited block A");

    // La variable peut être supprimée manuellement en utilisant la fonction `drop`
    drop(_a);
    // TODO ^ Essayez de commenter cette ligne

    println!("fin de la fonction principale");

    // `_a` *ne sera pas* supprimé à nouveau ici, car il a déjà été
    // (manuellement) supprimé
}
```
