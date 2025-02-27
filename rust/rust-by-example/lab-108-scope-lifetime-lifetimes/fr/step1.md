# Durées de vie

Une **durée de vie** est une construction utilisée par le compilateur (plus précisément, son **vérificateur d'emprunts**) pour s'assurer que tous les emprunts sont valides. Plus précisément, la durée de vie d'une variable commence lorsqu'elle est créée et se termine lorsqu'elle est détruite. Bien que les durées de vie et les portées soient souvent mentionnées ensemble, elles ne sont pas les mêmes.

Prendons, par exemple, le cas où nous empruntons une variable via `&`. L'emprunt a une durée de vie qui est déterminée par où il est déclaré. En conséquence, l'emprunt est valide tant qu'il se termine avant que le prêteur ne soit détruit. Cependant, la portée de l'emprunt est déterminée par l'endroit où la référence est utilisée.

Dans l'exemple suivant et dans le reste de cette section, nous verrons comment les durées de vie sont liées aux portées, ainsi que comment les deux diffèrent.

```rust
// Les durées de vie sont annotées ci-dessous avec des lignes indiquant
// la création et la destruction de chaque variable.
// `i` a la plus longue durée de vie car sa portée entoure entièrement
// à la fois `borrow1` et `borrow2`. La durée de `borrow1` par rapport
// à `borrow2` est sans importance car elles sont disjointes.
fn main() {
    let i = 3; // La durée de vie de `i` commence. ────────────────┐
    //                                                     │
    { //                                                   │
        let borrow1 = &i; // La durée de vie de `borrow1` commence. ──┐│
        //                                                ││
        println!("borrow1: {}", borrow1); //              ││
    } // La durée de vie de `borrow1` se termine. ─────────────────────────────────┘│
    //                                                     │
    //                                                     │
    { //                                                   │
        let borrow2 = &i; // La durée de vie de `borrow2` commence. ──┐│
        //                                                ││
        println!("borrow2: {}", borrow2); //              ││
    } // La durée de vie de `borrow2` se termine. ─────────────────────────────────┘│
    //                                                     │
}   // La durée de vie se termine. ─────────────────────────────────────┘
```

Notez que aucun nom ou type n'est assigné pour étiqueter les durées de vie. Cela restreint la manière dont les durées de vie pourront être utilisées, comme nous le verrons.
