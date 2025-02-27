# Paramètres de type génériques par défaut et surcharge d'opérateurs

Lorsque nous utilisons des paramètres de type génériques, nous pouvons spécifier un type concret par défaut pour le type générique. Cela élimine la nécessité pour les implémentateurs du trait de spécifier un type concret si le type par défaut convient. Vous spécifiez un type par défaut lors de la déclaration d'un type générique avec la syntaxe `<`TypeGénérique`=`TypeConcret`>`.

Un excellent exemple de situation où cette technique est utile est la _surcharge d'opérateurs_, dans laquelle vous personnalisez le comportement d'un opérateur (tel que `+`) dans des situations particulières.

Rust ne vous permet pas de créer vos propres opérateurs ou de surcharger des opérateurs arbitraires. Mais vous pouvez surcharger les opérations et les traits correspondants listés dans `std::ops` en implémentant les traits associés à l'opérateur. Par exemple, dans la Liste 19-14, nous surchargeons l'opérateur `+` pour additionner deux instances de `Point`. Nous le faisons en implémentant le trait `Add` sur une structure `Point`.

Nom de fichier : `src/main.rs`

```rust
use std::ops::Add;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
```

Liste 19-14 : Implémentation du trait `Add` pour surcharger l'opérateur `+` pour les instances de `Point`

La méthode `add` additionne les valeurs de `x` de deux instances de `Point` et les valeurs de `y` de deux instances de `Point` pour créer un nouveau `Point`. Le trait `Add` a un type associé nommé `Output` qui détermine le type renvoyé par la méthode `add`.

Le type générique par défaut dans ce code est dans le trait `Add`. Voici sa définition :

    trait Add<Rhs=Self> {
        type Output;

        fn add(self, rhs: Rhs) -> Self::Output;
    }

Ce code devrait vous paraître globalement familier : un trait avec une méthode et un type associé. La partie nouvelle est `Rhs=Self` : cette syntaxe est appelée _paramètres de type par défaut_. Le paramètre de type générique `Rhs` (abrégé de "right-hand side") définit le type du paramètre `rhs` dans la méthode `add`. Si nous ne spécifions pas un type concret pour `Rhs` lorsque nous implémentons le trait `Add`, le type de `Rhs` sera la valeur par défaut `Self`, qui sera le type sur lequel nous implémentons `Add`.

Lorsque nous avons implémenté `Add` pour `Point`, nous avons utilisé la valeur par défaut pour `Rhs` car nous voulions additionner deux instances de `Point`. Considérons un exemple d'implémentation du trait `Add` où nous voulons personnaliser le type `Rhs` plutôt que d'utiliser la valeur par défaut.

Nous avons deux structures, `Millimeters` et `Meters`, qui stockent des valeurs dans des unités différentes. Ce conditionnement mince d'un type existant dans une autre structure est connu sous le nom de _nouveau modèle de type_, que nous décrivons en détail dans "Utilisation du nouveau modèle de type pour implémenter des traits externes sur des types externes". Nous voulons ajouter des valeurs en millimètres à des valeurs en mètres et que l'implémentation de `Add` effectue correctement la conversion. Nous pouvons implémenter `Add` pour `Millimeters` avec `Meters` comme `Rhs`, comme montré dans la Liste 19-15.

Nom de fichier : `src/lib.rs`

```rust
use std::ops::Add;

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}
```

Liste 19-15 : Implémentation du trait `Add` sur `Millimeters` pour ajouter `Millimeters` et `Meters`

Pour ajouter `Millimeters` et `Meters`, nous spécifions `impl Add<Meters>` pour définir la valeur du paramètre de type `Rhs` au lieu d'utiliser la valeur par défaut `Self`.

Vous utiliserez les paramètres de type par défaut de deux manières principales :

1.  Pour étendre un type sans casser le code existant
2.  Pour permettre une personnalisation dans des cas spécifiques que la plupart des utilisateurs n'auront pas besoin

Le trait `Add` de la bibliothèque standard est un exemple du second but : généralement, vous additionnerez deux types similaires, mais le trait `Add` offre la possibilité de personnaliser au-delà de cela. L'utilisation d'un paramètre de type par défaut dans la définition du trait `Add` signifie que vous n'avez pas besoin de spécifier le paramètre supplémentaire la plupart du temps. En d'autres termes, un peu de boilerplate d'implémentation n'est pas nécessaire, ce qui facilite l'utilisation du trait.

Le premier but est similaire au second mais à l'envers : si vous voulez ajouter un paramètre de type à un trait existant, vous pouvez lui donner une valeur par défaut pour permettre l'extension de la fonctionnalité du trait sans casser le code d'implémentation existant.
