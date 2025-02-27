# if let

Pour certains cas d'utilisation, lors de la correspondance d'enumérations, `match` est gênant. Par exemple :

```rust
// Crée `optional` de type `Option<i32>`
let optional = Some(7);

match optional {
    Some(i) => {
        println!("Ceci est une chaîne de caractères vraiment longue et `{:?}`", i);
        // ^ Il a fallu 2 indentations juste pour pouvoir déstructurer
        // `i` de l'option.
    },
    _ => {},
    // ^ Nécessaire car `match` est exhaustif. Ne semble-t-il pas
    // que c'est de l'espace gaspillé?
};
```

`if let` est plus propre pour ce cas d'utilisation et permet en outre de spécifier diverses options de défaillance :

```rust
fn main() {
    // Tous ont le type `Option<i32>`
    let number = Some(7);
    let letter: Option<i32> = None;
    let emoticon: Option<i32> = None;

    // La construction `if let` se lit : "si `let` déstructure `number` en
    // `Some(i)`, évalue le bloc (`{}`).
    if let Some(i) = number {
        println!("Correspondance de {:?}!", i);
    }

    // Si vous devez spécifier une défaillance, utilisez un else :
    if let Some(i) = letter {
        println!("Correspondance de {:?}!", i);
    } else {
        // La déstructuration a échoué. Passons au cas de défaillance.
        println!("Pas de correspondance avec un nombre. Passons à une lettre!");
    }

    // Fournissez une condition de défaillance modifiée.
    let i_like_letters = false;

    if let Some(i) = emoticon {
        println!("Correspondance de {:?}!", i);
    // La déstructuration a échoué. Évaluez une condition `else if` pour voir si
    // la branche de défaillance alternative devrait être prise :
    } else if i_like_letters {
        println!("Pas de correspondance avec un nombre. Passons à une lettre!");
    } else {
        // La condition s'est avérée fausse. Cette branche est la valeur par défaut :
        println!("Je n'aime pas les lettres. Passons à un smiley :)!");
    }
}
```

De la même manière, `if let` peut être utilisé pour correspondre n'importe quelle valeur d'enumération :

```rust
// Notre enum d'exemple
enum Foo {
    Bar,
    Baz,
    Qux(u32)
}

fn main() {
    // Crée des variables d'exemple
    let a = Foo::Bar;
    let b = Foo::Baz;
    let c = Foo::Qux(100);

    // La variable a correspond à Foo::Bar
    if let Foo::Bar = a {
        println!("a est foobar");
    }

    // La variable b ne correspond pas à Foo::Bar
    // Donc cela n'affichera rien
    if let Foo::Bar = b {
        println!("b est foobar");
    }

    // La variable c correspond à Foo::Qux qui a une valeur
    // Similaire à Some() dans l'exemple précédent
    if let Foo::Qux(value) = c {
        println!("c est {}", value);
    }

    // Le binding fonctionne également avec `if let`
    if let Foo::Qux(value @ 100) = c {
        println!("c est cent");
    }
}
```

Un autre avantage est que `if let` nous permet de correspondre des variantes d'enumération non paramétrées. Cela est vrai même dans les cas où l'enum n'implémente pas ou n'hérite pas de `PartialEq`. Dans de tels cas, `if Foo::Bar == a` entraînerait une erreur de compilation, car les instances de l'enum ne peuvent pas être comparées, cependant `if let` continuera de fonctionner.

Voulez-vous un défi? Corrigez l'exemple suivant pour utiliser `if let` :

```rust
// Cet enum n'implémente et n'hérite pas intentionnellement de PartialEq.
// C'est pourquoi la comparaison Foo::Bar == a échoue ci-dessous.
enum Foo {Bar}

fn main() {
    let a = Foo::Bar;

    // La variable a correspond à Foo::Bar
    if Foo::Bar == a {
    // ^-- cela provoque une erreur de compilation. Utilisez `if let` à la place.
        println!("a est foobar");
    }
}
```
