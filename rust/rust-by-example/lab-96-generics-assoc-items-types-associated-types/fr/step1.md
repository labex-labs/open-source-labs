# Types associés

L'utilisation de "types associés" améliore la lisibilité globale du code en déplaçant les types internes localement dans un trait en tant que types de _sortie_. La syntaxe de la définition du `trait` est la suivante :

```rust
// `A` et `B` sont définis dans le trait via le mot clé `type`.
// (Remarque : `type` dans ce contexte est différent de `type` lorsqu'il est utilisé pour
// les alias).
trait Contains {
    type A;
    type B;

    // Syntaxe mise à jour pour faire référence à ces nouveaux types de manière générique.
    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
}
```

Remarquez que les fonctions qui utilisent le `trait` `Contains` n'ont plus besoin d'exprimer `A` ou `B` du tout :

```rust
// Sans utiliser des types associés
fn difference<A, B, C>(container: &C) -> i32 where
    C: Contains<A, B> {... }

// En utilisant des types associés
fn difference<C: Contains>(container: &C) -> i32 {... }
```

Réécrivons l'exemple de la section précédente en utilisant des types associés :

```rust
struct Container(i32, i32);

// Un trait qui vérifie si 2 éléments sont stockés dans le conteneur.
// Récupère également la première ou la dernière valeur.
trait Contains {
    // Définissez ici des types génériques que les méthodes pourront utiliser.
    type A;
    type B;

    fn contains(&self, _: &Self::A, _: &Self::B) -> bool;
    fn first(&self) -> i32;
    fn last(&self) -> i32;
}

impl Contains for Container {
    // Spécifiez quels types sont `A` et `B`. Si le type `input`
    // est `Container(i32, i32)`, les types `output` sont déterminés
    // comme étant `i32` et `i32`.
    type A = i32;
    type B = i32;

    // `&Self::A` et `&Self::B` sont également valides ici.
    fn contains(&self, number_1: &i32, number_2: &i32) -> bool {
        (&self.0 == number_1) && (&self.1 == number_2)
    }
    // Récupérez le premier nombre.
    fn first(&self) -> i32 { self.0 }

    // Récupérez le dernier nombre.
    fn last(&self) -> i32 { self.1 }
}

fn difference<C: Contains>(container: &C) -> i32 {
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
