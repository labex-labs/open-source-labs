# L'encapsulation qui cache les détails d'implémentation

Un autre aspect généralement associé à la programmation orientée objet est l'idée d'_encapsulation_, qui signifie que les détails d'implémentation d'un objet ne sont pas accessibles au code utilisant cet objet. Par conséquent, la seule manière d'interagir avec un objet est à travers son API publique; le code utilisant l'objet ne devrait pas être en mesure de pénétrer dans les internaux de l'objet et de modifier directement les données ou le comportement. Cela permet au programmeur de modifier et de refactoriser les internaux d'un objet sans avoir besoin de modifier le code qui utilise l'objet.

Nous avons discuté de la manière de contrôler l'encapsulation au chapitre 7 : nous pouvons utiliser le mot clé `pub` pour décider quels modules, types, fonctions et méthodes de notre code devraient être publiques, et par défaut tout le reste est privé. Par exemple, nous pouvons définir un struct `AveragedCollection` qui a un champ contenant un vecteur de valeurs de type `i32`. Le struct peut également avoir un champ qui contient la moyenne des valeurs dans le vecteur, ce qui signifie que la moyenne n'a pas besoin d'être calculée à la demande chaque fois que quelqu'un en a besoin. En d'autres termes, `AveragedCollection` va cacher la moyenne calculée pour nous. Le Listing 17-1 contient la définition du struct `AveragedCollection`.

Nom de fichier : `src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

Listing 17-1 : Un struct `AveragedCollection` qui maintient une liste d'entiers et la moyenne des éléments de la collection

Le struct est marqué `pub` afin que d'autres codes puissent l'utiliser, mais les champs à l'intérieur du struct restent privés. Cela est important dans ce cas car nous voulons nous assurer que chaque fois qu'une valeur est ajoutée ou supprimée de la liste, la moyenne est également mise à jour. Nous le faisons en implémentant les méthodes `add`, `remove` et `average` sur le struct, comme montré dans le Listing 17-2.

Nom de fichier : `src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

Listing 17-2 : Implémentations des méthodes publiques `add`, `remove` et `average` sur `AveragedCollection`

Les méthodes publiques `add`, `remove` et `average` sont les seules façons d'accéder ou de modifier les données dans une instance de `AveragedCollection`. Lorsqu'un élément est ajouté à `list` en utilisant la méthode `add` ou supprimé en utilisant la méthode `remove`, les implémentations de chaque appel appellent la méthode privée `update_average` qui s'occupe également de la mise à jour du champ `average`.

Nous laissons les champs `list` et `average` privés de sorte qu'il n'y ait aucun moyen pour le code externe d'ajouter ou de supprimer des éléments du champ `list` directement; sinon, le champ `average` pourrait être désynchronisé lorsque `list` change. La méthode `average` renvoie la valeur dans le champ `average`, permettant au code externe de lire `average` mais pas de le modifier.

Parce que nous avons encapsulé les détails d'implémentation du struct `AveragedCollection`, nous pouvons facilement modifier des aspects, tels que la structure de données, plus tard. Par exemple, nous pourrions utiliser un `HashSet<i32>` au lieu d'un `Vec<i32>` pour le champ `list`. Tant que les signatures des méthodes publiques `add`, `remove` et `average` restent les mêmes, le code utilisant `AveragedCollection` n'aura pas besoin de changer. Si nous avions rendu `list` public au lieu de cela, ce ne serait pas nécessairement le cas : `HashSet<i32>` et `Vec<i32>` ont des méthodes différentes pour ajouter et supprimer des éléments, donc le code externe devrait probablement changer s'il modifiait directement `list`.

Si l'encapsulation est un aspect requis pour qu'un langage soit considéré comme orienté objet, alors Rust répond à cette exigence. L'option d'utiliser ou non `pub` pour différentes parties du code permet d'encapsuler les détails d'implémentation.
