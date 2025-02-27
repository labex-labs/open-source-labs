# Création de synonymes de type avec des alias de type

Rust permet de déclarer un _alias de type_ pour donner un autre nom à un type existant. Pour ce faire, on utilise le mot clé `type`. Par exemple, on peut créer l'alias `Kilomètres` pour `i32` comme ceci :

```rust
type Kilomètres = i32;
```

Maintenant, l'alias `Kilomètres` est un _synonyme_ de `i32` ; contrairement aux types `Millimètres` et `Mètres` que nous avons créés dans la liste 19-15, `Kilomètres` n'est pas un type séparé et nouveau. Les valeurs qui ont le type `Kilomètres` seront traitées de la même manière que les valeurs de type `i32` :

    type Kilomètres = i32;

    let x: i32 = 5;
    let y: Kilomètres = 5;

    println!("x + y = {}", x + y);

Comme `Kilomètres` et `i32` sont le même type, on peut additionner les valeurs des deux types et on peut passer des valeurs de type `Kilomètres` à des fonctions qui prennent des paramètres de type `i32`. Cependant, avec cette méthode, on ne bénéficie pas des avantages de vérification de type que l'on obtient avec le motif newtype discuté précédemment. En d'autres termes, si on mélange des valeurs de type `Kilomètres` et `i32` quelque part, le compilateur ne nous donnera pas d'erreur.

Le principal cas d'utilisation des synonymes de type est de réduire la répétition. Par exemple, on pourrait avoir un type long comme celui-ci :

```rust
Box<dyn Fn() + Send + 'static>
```

Écrire ce type long dans les signatures de fonctions et comme annotations de type partout dans le code peut être fastidieux et propice à des erreurs. Imaginez avoir un projet plein de code comme celui de la liste 19-24.

```rust
let f: Box<dyn Fn() + Send + 'static> = Box::new(|| {
    println!("hi");
});

fn takes_long_type(f: Box<dyn Fn() + Send + 'static>) {
    --snip--
}

fn returns_long_type() -> Box<dyn Fn() + Send + 'static> {
    --snip--
}
```

Liste 19-24 : Utilisation d'un type long à de nombreux endroits

Un alias de type rend ce code plus facile à gérer en réduisant la répétition. Dans la liste 19-25, on a introduit un alias nommé `Thunk` pour le type verbeux et on peut remplacer toutes les utilisations du type par l'alias plus court `Thunk`.

    type Thunk = Box<dyn Fn() + Send + 'static>;

    let f: Thunk = Box::new(|| println!("hi"));

    fn takes_long_type(f: Thunk) {
        --snip--
    }

    fn returns_long_type() -> Thunk {
        --snip--
    }

Liste 19-25 : Introduction d'un alias de type `Thunk` pour réduire la répétition

Ce code est beaucoup plus facile à lire et à écrire! Choisir un nom significatif pour un alias de type peut également aider à communiquer votre intention (_thunk_ est un mot pour le code à évaluer plus tard, donc c'est un nom approprié pour une closure qui est stockée).

Les alias de type sont également couramment utilisés avec le type `Result<T, E>` pour réduire la répétition. Considérez le module `std::io` de la bibliothèque standard. Les opérations d'entrée/sortie renvoient souvent un `Result<T, E>` pour gérer les situations où les opérations échouent. Cette bibliothèque a une struct `std::io::Error` qui représente toutes les erreurs d'entrée/sortie possibles. Beaucoup des fonctions dans `std::io` renverront `Result<T, E>` où l'`E` est `std::io::Error`, comme ces fonctions dans le trait `Write` :

```rust
use std::fmt;
use std::io::Error;

pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize, Error>;
    fn flush(&mut self) -> Result<(), Error>;

    fn write_all(&mut self, buf: &[u8]) -> Result<(), Error>;
    fn write_fmt(
        &mut self,
        fmt: fmt::Arguments,
    ) -> Result<(), Error>;
}
```

Le `Result<..., Error>` est répété beaucoup. En conséquence, `std::io` a cette déclaration d'alias de type :

```rust
type Result<T> = std::result::Result<T, std::io::Error>;
```

Comme cette déclaration est dans le module `std::io`, on peut utiliser l'alias qualifié `std::io::Result<T>` ; c'est-à-dire un `Result<T, E>` avec l'`E` remplacé par `std::io::Error`. Les signatures de fonctions du trait `Write` finissent par ressembler à ceci :

```rust
pub trait Write {
    fn write(&mut self, buf: &[u8]) -> Result<usize>;
    fn flush(&mut self) -> Result<()>;

    fn write_all(&mut self, buf: &[u8]) -> Result<()>;
    fn write_fmt(&mut self, fmt: fmt::Arguments) -> Result<()>;
}
```

L'alias de type est utile de deux manières : il facilite l'écriture du code _et_ il nous donne une interface cohérente dans tout `std::io`. Comme c'est un alias, c'est juste un autre `Result<T, E>`, ce qui signifie que l'on peut utiliser toutes les méthodes qui fonctionnent sur `Result<T, E>` avec lui, ainsi que la syntaxe spéciale comme l'opérateur `?`.
