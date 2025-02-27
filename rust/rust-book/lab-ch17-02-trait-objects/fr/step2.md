# Définition d'un trait pour un comportement commun

Pour implémenter le comportement que nous voulons que `gui` ait, nous allons définir un trait nommé `Draw` qui aura une méthode nommée `draw`. Ensuite, nous pouvons définir un vecteur qui prend un _objet de trait_. Un objet de trait pointe vers à la fois une instance d'un type implémentant notre trait spécifié et une table utilisée pour rechercher les méthodes de trait sur ce type à l'exécution. Nous créons un objet de trait en spécifiant un certain type de pointeur, tel qu'une référence `&` ou un pointeur intelligent `Box<T>`, puis le mot clé `dyn`, puis en spécifiant le trait pertinent. (Nous parlerons des raisons pour lesquelles les objets de trait doivent utiliser un pointeur dans "Types de taille dynamique et le trait Sized".) Nous pouvons utiliser des objets de trait à la place d'un type générique ou concret. Partout où nous utilisons un objet de trait, le système de types de Rust assurera à la compilation que toute valeur utilisée dans ce contexte implémentera le trait de l'objet de trait. En conséquence, nous n'avons pas besoin de connaître tous les types possibles à la compilation.

Nous avons mentionné que, en Rust, nous évitons d'appeler les structs et les enums "objets" pour les distinguer des objets des autres langages. Dans un struct ou un enum, les données dans les champs du struct et le comportement dans les blocs `impl` sont séparés, tandis que dans les autres langages, les données et le comportement combinés en un seul concept sont souvent étiquetés comme un objet. Cependant, les objets de trait _sont_ plus semblables aux objets dans les autres langages dans le sens où ils combinent données et comportement. Mais les objets de trait diffèrent des objets traditionnels en ce que nous ne pouvons pas ajouter de données à un objet de trait. Les objets de trait ne sont pas aussi généralement utiles que les objets dans les autres langages : leur but spécifique est d'autoriser l'abstraction sur un comportement commun.

La liste 17-3 montre comment définir un trait nommé `Draw` avec une méthode nommée `draw`.

Nom de fichier : `src/lib.rs`

```rust
pub trait Draw {
    fn draw(&self);
}
```

Liste 17-3 : Définition du trait `Draw`

Cette syntaxe devrait vous paraître familière d'après nos discussions sur la manière de définir des traits au chapitre 10. Ensuite vient une nouvelle syntaxe : la liste 17-4 définit une struct nommée `Screen` qui contient un vecteur nommé `components`. Ce vecteur est de type `Box<dyn Draw>`, qui est un objet de trait ; c'est un substitut pour tout type à l'intérieur d'un `Box` qui implémente le trait `Draw`.

Nom de fichier : `src/lib.rs`

```rust
pub struct Screen {
    pub components: Vec<Box<dyn Draw>>,
}
```

Liste 17-4 : Définition de la struct `Screen` avec un champ `components` contenant un vecteur d'objets de trait qui implémentent le trait `Draw`

Sur la struct `Screen`, nous allons définir une méthode nommée `run` qui appellera la méthode `draw` sur chacun de ses `components`, comme montré dans la liste 17-5.

Nom de fichier : `src/lib.rs`

```rust
impl Screen {
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Liste 17-5 : Une méthode `run` sur `Screen` qui appelle la méthode `draw` sur chaque composant

Cela fonctionne différemment de la définition d'une struct qui utilise un paramètre de type générique avec des contraintes de trait. Un paramètre de type générique ne peut être remplacé qu'avec un type concret à la fois, tandis que les objets de trait permettent de multiples types concret de remplir le rôle de l'objet de trait à l'exécution. Par exemple, nous aurions pu définir la struct `Screen` en utilisant un type générique et une contrainte de trait, comme dans la liste 17-6.

Nom de fichier : `src/lib.rs`

```rust
pub struct Screen<T: Draw> {
    pub components: Vec<T>,
}

impl<T> Screen<T>
where
    T: Draw,
{
    pub fn run(&self) {
        for component in self.components.iter() {
            component.draw();
        }
    }
}
```

Liste 17-6 : Une implémentation alternative de la struct `Screen` et de sa méthode `run` utilisant des types génériques et des contraintes de trait

Cela nous restreint à une instance de `Screen` qui a une liste de composants tous de type `Button` ou tous de type `TextField`. Si vous n'aurez jamais que des collections homogènes, utiliser des types génériques et des contraintes de trait est préférable car les définitions seront monomorphisées à la compilation pour utiliser les types concret.

D'un autre côté, avec la méthode utilisant des objets de trait, une instance de `Screen` peut contenir un `Vec<T>` qui contient un `Box<Button>` ainsi qu'un `Box<TextField>`. Voyons comment cela fonctionne, puis nous parlerons des implications de performance à l'exécution.
