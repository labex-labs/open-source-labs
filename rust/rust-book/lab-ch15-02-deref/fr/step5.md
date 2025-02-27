# Implementing the Deref Trait

Comme discuté dans "Implementing a Trait on a Type", pour implémenter un trait, nous devons fournir des implémentations pour les méthodes requises du trait. Le trait `Deref`, fourni par la bibliothèque standard, nous oblige à implémenter une méthode nommée `deref` qui emprunte `self` et renvoie une référence à la donnée interne. La Liste 15-10 contient une implémentation de `Deref` à ajouter à la définition de `MyBox``<T>`.

Nom du fichier : `src/main.rs`

```rust
use std::ops::Deref;

impl<T> Deref for MyBox<T> {
  1 type Target = T;

    fn deref(&self) -> &Self::Target {
      2 &self.0
    }
}
```

Liste 15-10 : Implémentation de `Deref` sur `MyBox<T>`

La syntaxe `type Target = T;` \[1\] définit un type associé pour le trait `Deref` à utiliser. Les types associés sont une manière légèrement différente de déclarer un paramètre générique, mais vous n'avez pas besoin de vous en soucier pour l'instant ; nous en aborderons les détails plus en détail au Chapitre 19.

Nous remplissons le corps de la méthode `deref` avec `&self.0` de sorte que `deref` renvoie une référence à la valeur que nous voulons accéder avec l'opérateur `*` \[2\] ; rappelez-vous de "Using Tuple Structs Without Named Fields to Create Different Types" que `.0` accède à la première valeur dans une struct tuple. La fonction `main` de la Liste 15-9 qui appelle `*` sur la valeur `MyBox<T>` compile désormais, et les assertions sont validées!

Sans le trait `Deref`, le compilateur ne peut déréférencer que les références `&`. La méthode `deref` donne au compilateur la capacité de prendre une valeur de tout type qui implémente `Deref` et d'appeler la méthode `deref` pour obtenir une référence `&` qu'il sait déréférencer.

Lorsque nous avons entré `*y` dans la Liste 15-9, en coulisse, Rust a effectivement exécuté ce code :

```rust
*(y.deref())
```

Rust remplace l'opérateur `*` par un appel à la méthode `deref` puis un simple déréférencement, de sorte que nous n'ayons pas besoin de nous demander si nous devons appeler la méthode `deref` ou non. Cette fonctionnalité de Rust nous permet d'écrire du code qui fonctionne de manière identique que nous ayons une référence normale ou un type qui implémente `Deref`.

La raison pour laquelle la méthode `deref` renvoie une référence à une valeur et que le déréférencement simple en dehors des parenthèses dans `*(y.deref())` est toujours nécessaire est liée au système de propriété. Si la méthode `deref` renvoyait directement la valeur au lieu d'une référence à la valeur, la valeur serait déplacée hors de `self`. Nous ne voulons pas prendre la propriété de la valeur interne dans `MyBox<T>` dans ce cas ou dans la plupart des cas où nous utilisons l'opérateur de déréférence.

Notez que l'opérateur `*` est remplacé par un appel à la méthode `deref` puis un appel à l'opérateur `*` une seule fois, chaque fois que nous utilisons un `*` dans notre code. Étant donné que la substitution de l'opérateur `*` ne se poursuit pas indéfiniment, nous obtenons finalement des données de type `i32`, qui correspondent à `5` dans `assert_eq!` de la Liste 15-9.
