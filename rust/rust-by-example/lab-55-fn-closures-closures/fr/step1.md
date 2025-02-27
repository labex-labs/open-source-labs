# Closures

Les closures sont des fonctions qui peuvent capturer l'environnement entourant. Par exemple, une closure qui capture la variable `x` :

```rust
|val| val + x
```

La syntaxe et les capacités des closures les rendent très pratiques pour une utilisation immédiate. Appeler une closure est exactement comme appeler une fonction. Cependant, les types d'entrée et de retour _peuvent_ être inférés et les noms de variables d'entrée _doivent_ être spécifiés.

D'autres caractéristiques des closures sont les suivantes :

- utilisation de `||` au lieu de `()` autour des variables d'entrée.
- délimitation optionnelle du corps (`{}`) pour une seule expression (obligatoire sinon).
- capacité à capturer les variables de l'environnement extérieur.

```rust
fn main() {
    let outer_var = 42;

    // Une fonction normale ne peut pas faire référence à des variables dans l'environnement entourant
    //fn function(i: i32) -> i32 { i + outer_var }
    // TODO : décommenter la ligne ci-dessus et voir l'erreur du compilateur. Le compilateur
    // suggère de définir une closure à la place.

    // Les closures sont anonymes, ici nous les liions à des références
    // L'annotation est identique à l'annotation de fonction mais est optionnelle
    // tout comme les `{}` entourant le corps. Ces fonctions sans nom
    // sont assignées à des variables nommées de manière appropriée.
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred  = |i     |          i + outer_var  ;

    // Appelez les closures.
    println!("closure_annotated: {}", closure_annotated(1));
    println!("closure_inferred: {}", closure_inferred(1));
    // Une fois le type d'une closure inféré, il ne peut pas être inféré à nouveau avec un autre type.
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42i64));
    // TODO : décommenter la ligne ci-dessus et voir l'erreur du compilateur.

    // Une closure ne prenant aucun argument qui renvoie un `i32`.
    // Le type de retour est inféré.
    let one = || 1;
    println!("closure returning one: {}", one());

}
```
