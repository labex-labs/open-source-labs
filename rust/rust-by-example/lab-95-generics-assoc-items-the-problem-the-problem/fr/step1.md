# Le problème

Un `trait` qui est générique sur son type de conteneur a des exigences de spécification de type - les utilisateurs du `trait` _doivent_ spécifier tous ses types génériques.

Dans l'exemple ci-dessous, le `trait` `Contains` autorise l'utilisation des types génériques `A` et `B`. Le trait est ensuite implémenté pour le type `Container`, en spécifiant `i32` pour `A` et `B` de manière à ce qu'il puisse être utilisé avec `fn difference()`.

Étant donné que `Contains` est générique, nous sommes contraints d'explicitement spécifier _tous_ les types génériques pour `fn difference()`. En pratique, nous souhaitons trouver un moyen d'exprimer que `A` et `B` sont déterminés par l'`entrée` `C`. Comme vous le verrez dans la section suivante, les types associés offrent exactement cette capacité.

```rust
struct Container(i32, i32);

// Un trait qui vérifie si 2 éléments sont stockés dans le conteneur.
// Récupère également la première ou la dernière valeur.
trait Contains<A, B> {
    fn contains(&self, _: &A, _: &B) -> bool; // Exige explicitement `A` et `B`.
    fn first(&self) -> i32; // N'exige pas explicitement `A` ou `B`.
    fn last(&self) -> i32;  // N'exige pas explicitement `A` ou `B`.
}

impl Contains<i32, i32> for Container {
    // Vrai si les nombres stockés sont égaux.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }

    // Récupère le premier nombre.
    fn first(&self) -> i32 { self.0 }

    // Récupère le dernier nombre.
    fn last(&self) -> i32 { self.1 }
}

// `C` contient `A` et `B`. Compte tenu de cela, devoir exprimer `A` et
// `B` à nouveau est gênant.
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {
    container.last() - container.first()
}

fn main() {
    let number_1 = 3;
    let number_2 = 10;

    let container = Container(number_1, number_2);

    println!("Le conteneur contient-il {} et {} : {}",
        &number_1, &number_2,
        container.contains(&number_1, &number_2));
    println!("Premier nombre : {}", container.first());
    println!("Dernier nombre : {}", container.last());

    println!("La différence est : {}", difference(&container));
}
```
