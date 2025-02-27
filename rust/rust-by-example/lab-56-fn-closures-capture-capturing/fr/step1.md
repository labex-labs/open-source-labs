# Capturing

Les closures sont intrinsèquement flexibles et feront ce que la fonctionnalité nécessite pour que la closure fonctionne sans annotation. Cela permet à la capture d'adapter flexiblement au cas d'utilisation, empruntant parfois et parfois enlevant la propriété. Les closures peuvent capturer des variables :

- par référence : `&T`
- par référence mutable : `&mut T`
- par valeur : `T`

Elles capturent les variables par référence de manière préférentielle et ne descendent qu'en-dessous si nécessaire.

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // Une closure pour afficher `color` qui emprunte immédiatement (`&`) `color` et
    // stocke l'emprunt et la closure dans la variable `print`. Elle restera
    // empruntée jusqu'à ce que `print` soit utilisée la dernière fois.
    //
    // `println!` ne nécessite que des arguments par référence immuable, donc
    // elle n'impose rien de plus restrictif.
    let print = || println!("`color`: {}", color);

    // Appelez la closure en utilisant l'emprunt.
    print();

    // `color` peut être à nouveau emprunté de manière immuable, car la closure ne conserve
    // qu'une référence immuable à `color`.
    let _reborrow = &color;
    print();

    // Un déplacement ou un nouvel emprunt est autorisé après l'utilisation finale de `print`
    let _color_moved = color;


    let mut count = 0;
    // Une closure pour incrémenter `count` pourrait prendre soit `&mut count` soit `count`
    // mais `&mut count` est moins restrictif, donc elle le prend. Elle emprunte immédiatement
    // `count`.
    //
    // Un `mut` est requis sur `inc` car un `&mut` est stocké à l'intérieur. Ainsi,
    // appeler la closure modifie la closure, ce qui nécessite un `mut`.
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // Appelez la closure en utilisant un emprunt mutable.
    inc();

    // La closure emprunte toujours mutuellement `count` car elle est appelée plus tard.
    // Une tentative de nouvel emprunt entraînera une erreur.
    // let _reborrow = &count;
    // ^ TODO: essayez de décommenter cette ligne.
    inc();

    // La closure n'a plus besoin d'emprunter `&mut count`. Par conséquent, il est
    // possible de faire un nouvel emprunt sans erreur
    let _count_reborrowed = &mut count;


    // Un type non copiable.
    let movable = Box::new(3);

    // `mem::drop` nécessite `T`, donc cela doit prendre par valeur. Un type copiable
    // serait copié dans la closure, laissant l'original inchangé.
    // Un type non copiable doit être déplacé, donc `movable` est immédiatement déplacé dans
    // la closure.
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` consomme la variable, donc cela ne peut être appelé qu'une fois.
    consume();
    // consume();
    // ^ TODO: Essayez de décommenter cette ligne.
}
```

En utilisant `move` avant les pipes verticaux, on force la closure à prendre la propriété des variables capturées :

```rust
fn main() {
    // `Vec` a des sémantiques non copiables.
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ Déccommenter la ligne ci-dessus entraînera une erreur de compilation
    // car le vérificateur d'emprunt ne permet pas de réutiliser une variable après qu'elle
    // ait été déplacée.

    // En supprimant `move` de la signature de la closure, la closure
    // empruntera la variable _haystack_ de manière immuable, donc _haystack_ est toujours
    // disponible et décommenter la ligne ci-dessus ne causera pas d'erreur.
}
```
