# Propriété et mouvements

Étant donné que les variables sont chargées de libérer leurs propres ressources, **une ressource ne peut avoir qu'un seul propriétaire**. Cela empêche également les ressources d'être libérées plus d'une fois. Notez que non toutes les variables possèdent des ressources (par exemple, les [références]).

Lorsque l'on effectue des affectations (`let x = y`) ou que l'on passe des arguments de fonction par valeur (`foo(x)`), la _propriété_ des ressources est transférée. En langage Rust, on appelle cela un _move_.

Après avoir transféré les ressources, l'ancien propriétaire ne peut plus être utilisé. Cela évite de créer des pointeurs faussaires.

```rust
// Cette fonction prend la propriété de la mémoire allouée sur le tas
fn destroy_box(c: Box<i32>) {
    println!("Destroying a box that contains {}", c);

    // `c` est détruit et la mémoire est libérée
}

fn main() {
    // Entier alloué sur la _pile_
    let x = 5u32;

    // *Copie* `x` dans `y` - aucune ressource n'est déplacée
    let y = x;

    // Les deux valeurs peuvent être utilisées indépendamment
    println!("x is {}, and y is {}", x, y);

    // `a` est un pointeur vers un entier alloué sur le _tas_
    let a = Box::new(5i32);

    println!("a contains: {}", a);

    // *Déplace* `a` dans `b`
    let b = a;
    // L'adresse du pointeur de `a` est copiée (pas les données) dans `b`.
    // Les deux sont maintenant des pointeurs vers les mêmes données allouées sur le tas, mais
    // `b` en est maintenant le propriétaire.

    // Erreur! `a` ne peut plus accéder aux données, car il ne possède plus
    // la mémoire du tas
    //println!("a contains: {}", a);
    // TODO ^ Essayez de décommenter cette ligne

    // Cette fonction prend la propriété de la mémoire allouée sur le tas à partir de `b`
    destroy_box(b);

    // Étant donné que la mémoire du tas a été libérée à ce stade, cette action entraînerait
    // une déréférencement de mémoire libérée, mais le compilateur l'interdit
    // Erreur! Même raison que l'erreur précédente
    //println!("b contains: {}", b);
    // TODO ^ Essayez de décommenter cette ligne
}
```
