# Itérateurs

Le trait `Iterator` est utilisé pour implémenter des itérateurs sur des collections telles que les tableaux.

Le trait ne nécessite qu'une méthode à être définie pour l'élément `next`, qui peut être définie manuellement dans un bloc `impl` ou automatiquement définie (comme dans les tableaux et les plages).

Pour faciliter les situations courantes, la construction `for` transforme certaines collections en itérateurs en utilisant la méthode `.into_iter()`.

```rust
struct Fibonacci {
    curr: u32,
    next: u32,
}

// Implémente `Iterator` pour `Fibonacci`.
// Le trait `Iterator` ne nécessite qu'une méthode à être définie pour l'élément `next`.
impl Iterator for Fibonacci {
    // Nous pouvons faire référence à ce type en utilisant Self::Item
    type Item = u32;

    // Ici, nous définissons la séquence en utilisant `.curr` et `.next`.
    // Le type de retour est `Option<T>` :
    //     * Lorsque l'`Iterator` est terminé, `None` est renvoyé.
    //     * Sinon, la valeur suivante est encapsulée dans `Some` et renvoyée.
    // Nous utilisons Self::Item dans le type de retour, de sorte que nous puissions
    // changer le type sans avoir à mettre à jour les signatures de fonction.
    fn next(&mut self) -> Option<Self::Item> {
        let current = self.curr;

        self.curr = self.next;
        self.next = current + self.next;

        // Étant donné qu'il n'y a pas de point d'arrêt pour une séquence de Fibonacci, l'`Iterator`
        // ne renverra jamais `None`, et `Some` est toujours renvoyé.
        Some(current)
    }
}

// Retourne un générateur de séquence de Fibonacci
fn fibonacci() -> Fibonacci {
    Fibonacci { curr: 0, next: 1 }
}

fn main() {
    // `0..3` est un `Iterator` qui génère : 0, 1 et 2.
    let mut sequence = 0..3;

    println!("Quatre appels consécutifs de `next` sur 0..3");
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());
    println!("> {:?}", sequence.next());

    // `for` fonctionne sur un `Iterator` jusqu'à ce qu'il renvoie `None`.
    // Chaque valeur `Some` est déballée et liée à une variable (ici, `i`).
    println!("Itérer sur 0..3 en utilisant `for`");
    for i in 0..3 {
        println!("> {}", i);
    }

    // La méthode `take(n)` réduit un `Iterator` à ses premiers `n` termes.
    println!("Les quatre premiers termes de la séquence de Fibonacci sont : ");
    for i in fibonacci().take(4) {
        println!("> {}", i);
    }

    // La méthode `skip(n)` raccourcit un `Iterator` en éliminant ses premiers `n` termes.
    println!("Les quatre termes suivants de la séquence de Fibonacci sont : ");
    for i in fibonacci().skip(4).take(4) {
        println!("> {}", i);
    }

    let array = [1u32, 3, 3, 7];

    // La méthode `iter` produit un `Iterator` sur un tableau/slice.
    println!("Itérer le tableau suivant {:?}", &array);
    for i in array.iter() {
        println!("> {}", i);
    }
}
```
