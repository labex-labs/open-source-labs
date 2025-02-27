# Refactoring avec des tuples

La liste 5-9 montre une autre version de notre programme qui utilise des tuples.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let rect1 = (30, 50);

    println!(
        "L'aire du rectangle est {} pixels carrés.",
      1 area(rect1)
    );
}

fn area(dimensions: (u32, u32)) -> u32 {
  2 dimensions.0 * dimensions.1
}
```

Liste 5-9 : Spécification de la largeur et de la hauteur du rectangle avec un tuple

D'une certaine manière, ce programme est meilleur. Les tuples nous permettent d'ajouter une certaine structure, et nous passons maintenant un seul argument \[1\]. Mais d'une autre manière, cette version est moins claire : les tuples ne nomment pas leurs éléments, donc nous devons accéder aux parties du tuple par index \[2\], ce qui rend notre calcul moins évident.

Mélanger la largeur et la hauteur n'aurait pas d'importance pour le calcul de l'aire, mais si nous voulons dessiner le rectangle sur l'écran, cela compterait! Nous devrions garder à l'esprit que `width` est l'index du tuple `0` et `height` est l'index du tuple `1`. Cela serait encore plus difficile pour autrui de comprendre et de garder à l'esprit s'ils devaient utiliser notre code. Parce que nous n'avons pas transmis la signification de nos données dans notre code, il est maintenant plus facile d'introduire des erreurs.
