# Testcase: List

Implémenter `fmt::Display` pour une structure dont les éléments doivent chacun être traités séquentiellement est difficile. Le problème est que chaque `write!` génère un `fmt::Result`. Pour gérer correctement ceci, il est nécessaire de traiter _tous_ les résultats. Rust fournit l'opérateur `?` précisément à cette fin.

Utiliser `?` sur `write!` ressemble à ceci :

```rust
// Essayez `write!` pour voir s'il y a une erreur. Si c'est le cas, renvoyez
// l'erreur. Sinon, continuez.
write!(f, "{}", value)?;
```

Avec `?` disponible, implémenter `fmt::Display` pour un `Vec` est simple :

```rust
use std::fmt; // Importez le module `fmt`.

// Définissez une structure nommée `List` contenant un `Vec`.
struct List(Vec<i32>);

impl fmt::Display for List {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        // Extrait la valeur en utilisant l'indexation de tuple,
        // et crée une référence à `vec`.
        let vec = &self.0;

        write!(f, "[")?;

        // Itérez sur `v` dans `vec` tout en énumérant le
        // compteur d'itération dans `count`.
        for (count, v) in vec.iter().enumerate() {
            // Pour chaque élément sauf le premier, ajoutez une virgule.
            // Utilisez l'opérateur? pour renvoyer en cas d'erreur.
            if count!= 0 { write!(f, ", ")?; }
            write!(f, "{}", v)?;
        }

        // Fermez la parenthèse ouvrante et renvoyez une valeur `fmt::Result`.
        write!(f, "]")
    }
}

fn main() {
    let v = List(vec![1, 2, 3]);
    println!("{}", v);
}
```

## Activité

Essayez de modifier le programme de manière à ce que l'index de chaque élément dans le vecteur soit également imprimé. La nouvelle sortie devrait ressembler à ceci :

```rust
[0: 1, 1: 2, 2: 3]
```
