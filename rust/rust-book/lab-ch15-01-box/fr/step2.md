# Utiliser Box`<T>` pour stocker des données sur le tas

Avant de discuter du cas d'utilisation de stockage sur le tas pour `Box<T>`, nous allons aborder la syntaxe et la manière d'interagir avec les valeurs stockées dans un `Box<T>`.

Le Listing 15-1 montre comment utiliser une boîte pour stocker une valeur `i32` sur le tas.

Nom de fichier : `src/main.rs`

```rust
fn main() {
    let b = Box::new(5);
    println!("b = {b}");
}
```

Listing 15-1 : Stockage d'une valeur `i32` sur le tas à l'aide d'une boîte

Nous définissons la variable `b` pour avoir la valeur d'une `Box` qui pointe vers la valeur `5`, qui est allouée sur le tas. Ce programme affichera `b = 5` ; dans ce cas, nous pouvons accéder aux données dans la boîte de la même manière que si ces données étaient sur la pile. Tout comme toute valeur possédée, lorsqu'une boîte sort de portée, comme `b` le fait à la fin de `main`, elle sera désallouée. La désallocation se produit à la fois pour la boîte (stockée sur la pile) et les données qu'elle pointe (stockées sur le tas).

Mettre une seule valeur sur le tas n'est pas très utile, donc vous n'utiliserez pas souvent les boîtes seules de cette manière. Avoir des valeurs comme un simple `i32` sur la pile, où elles sont stockées par défaut, est plus approprié dans la majorité des situations. Regardons un cas où les boîtes nous permettent de définir des types que nous ne serions pas autorisés à définir si nous n'avions pas de boîtes.
