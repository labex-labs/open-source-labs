# Clone

Lorsque l'on traite des ressources, le comportement par défaut est de les transférer lors d'affectations ou d'appels de fonction. Cependant, parfois, nous avons également besoin de créer une copie de la ressource.

Le trait `Clone` nous aide à faire exactement cela. Le plus souvent, nous pouvons utiliser la méthode `.clone()` définie par le trait `Clone`.

```rust
// Une struct unit sans ressources
#[derive(Debug, Clone, Copy)]
struct Unit;

// Une struct tuple avec des ressources qui implémente le trait `Clone`
#[derive(Clone, Debug)]
struct Pair(Box<i32>, Box<i32>);

fn main() {
    // Instancie `Unit`
    let unit = Unit;
    // Copie `Unit`, il n'y a pas de ressources à déplacer
    let copied_unit = unit;

    // Les deux `Unit` peuvent être utilisés indépendamment
    println!("original: {:?}", unit);
    println!("copie: {:?}", copied_unit);

    // Instancie `Pair`
    let pair = Pair(Box::new(1), Box::new(2));
    println!("original: {:?}", pair);

    // Déplace `pair` dans `moved_pair`, déplace les ressources
    let moved_pair = pair;
    println!("déplacé: {:?}", moved_pair);

    // Erreur! `pair` a perdu ses ressources
    //println!("original: {:?}", pair);
    // TODO ^ Essayez de décommenter cette ligne

    // Clone `moved_pair` dans `cloned_pair` (les ressources sont incluses)
    let cloned_pair = moved_pair.clone();
    // Supprime la paire d'origine en utilisant std::mem::drop
    drop(moved_pair);

    // Erreur! `moved_pair` a été supprimé
    //println!("copie: {:?}", moved_pair);
    // TODO ^ Essayez de décommenter cette ligne

    // Le résultat de.clone() peut toujours être utilisé!
    println!("clone: {:?}", cloned_pair);
}
```
