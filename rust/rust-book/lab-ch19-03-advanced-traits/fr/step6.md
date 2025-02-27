# Utilisation du nouveau modèle de type pour implémenter des traits externes

Dans "Implémentation d'un trait sur un type", nous avons mentionné la règle de l'orphelin qui stipule que nous ne sommes autorisés à implémenter un trait sur un type que si le trait ou le type, ou les deux, sont locaux à notre crate. Il est possible de contourner cette restriction en utilisant le _nouveau modèle de type_, qui consiste à créer un nouveau type dans une structure tuple. (Nous avons abordé les structures tuple dans "Utilisation de structures tuple sans champs nommés pour créer différents types".) La structure tuple aura un seul champ et sera une enveloppe mince autour du type pour lequel nous voulons implémenter un trait. Ensuite, le type d'enveloppe est local à notre crate, et nous pouvons implémenter le trait sur l'enveloppe. _Nouveau type_ est un terme qui vient du langage de programmation Haskell. Il n'y a pas de pénalité de performance à l'exécution pour utiliser ce modèle, et le type d'enveloppe est éliminé à la compilation.

Par exemple, disons que nous voulons implémenter `Display` sur `Vec<T>`, ce que la règle de l'orphelin nous empêche de faire directement car le trait `Display` et le type `Vec<T>` sont définis en dehors de notre crate. Nous pouvons créer une structure `Wrapper` qui contient une instance de `Vec<T>` ; puis nous pouvons implémenter `Display` sur `Wrapper` et utiliser la valeur de `Vec<T>`, comme montré dans la Liste 19-23.

Nom de fichier : `src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

Liste 19-23 : Création d'un type `Wrapper` autour de `Vec<String>` pour implémenter `Display`

L'implémentation de `Display` utilise `self.0` pour accéder au `Vec<T>` interne car `Wrapper` est une structure tuple et `Vec<T>` est l'élément à l'index 0 dans la tuple. Ensuite, nous pouvons utiliser la fonctionnalité du type `Display` sur `Wrapper`.

Le inconvénient d'utiliser cette technique est que `Wrapper` est un nouveau type, donc il n'a pas les méthodes de la valeur qu'il contient. Nous devrions implémenter toutes les méthodes de `Vec<T>` directement sur `Wrapper` de sorte que les méthodes déléguent à `self.0`, ce qui nous permettrait de traiter `Wrapper` exactement comme un `Vec<T>`. Si nous voulions que le nouveau type ait toutes les méthodes du type interne, implémenter le trait `Deref` sur `Wrapper` pour renvoyer le type interne serait une solution (nous avons discuté de l'implémentation du trait `Deref` dans "Traiter des pointeurs intelligents comme des références normales avec Deref"). Si nous ne voulions pas que le type `Wrapper` ait toutes les méthodes du type interne - par exemple, pour restreindre le comportement du type `Wrapper` - nous devrions implémenter seulement les méthodes que nous voulons manuellement.

Ce nouveau modèle de type est également utile même lorsqu'aucun trait n'est impliqué. Passons à la question et examinons certaines façons avancées d'interagir avec le système de types de Rust.
