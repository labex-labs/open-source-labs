# Enums

Le mot clé `enum` permet de créer un type qui peut être l'un de plusieurs variants différents. Tout variant valide en tant que `struct` est également valide dans un `enum`.

```rust
// Crée un `enum` pour classifier un événement web. Notez comment à la fois
// les noms et les informations de type spécifient le variant :
// `PageLoad!= PageUnload` et `KeyPress(char)!= Paste(String)`.
// Chacun est différent et indépendant.
enum WebEvent {
    // Un variant d'`enum` peut être soit `unit-like`,
    PageLoad,
    PageUnload,
    // soit comme des structs tuple,
    KeyPress(char),
    Paste(String),
    // soit des structures du type C.
    Click { x: i64, y: i64 },
}

// Une fonction qui prend un `enum` WebEvent en argument et
// ne renvoie rien.
fn inspect(event: WebEvent) {
    match event {
        WebEvent::PageLoad => println!("page chargée"),
        WebEvent::PageUnload => println!("page déchargée"),
        // Déstructure `c` à l'intérieur du variant d'`enum`.
        WebEvent::KeyPress(c) => println!("appuyé sur '{}'.", c),
        WebEvent::Paste(s) => println!("collé \"{}\".", s),
        // Déstructure `Click` en `x` et `y`.
        WebEvent::Click { x, y } => {
            println!("cliqué à x={}, y={}.", x, y);
        },
    }
}

fn main() {
    let pressed = WebEvent::KeyPress('x');
    // `to_owned()` crée une `String` propriétaire à partir d'un slice de chaîne.
    let pasted  = WebEvent::Paste("my text".to_owned());
    let click   = WebEvent::Click { x: 20, y: 80 };
    let load    = WebEvent::PageLoad;
    let unload  = WebEvent::PageUnload;

    inspect(pressed);
    inspect(pasted);
    inspect(click);
    inspect(load);
    inspect(unload);
}
```

## Alias de type

Si vous utilisez un alias de type, vous pouvez faire référence à chaque variant d'énumération via son alias. Cela peut être utile si le nom de l'énumération est trop long ou trop générique et que vous voulez le renommer.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

// Crée un alias de type
type Operations = VeryVerboseEnumOfThingsToDoWithNumbers;

fn main() {
    // Nous pouvons faire référence à chaque variant via son alias, et non son nom long et inconvénient.
    let x = Operations::Add;
}
```

Le lieu où vous le verrez le plus couramment est dans les blocs `impl` utilisant l'alias `Self`.

```rust
enum VeryVerboseEnumOfThingsToDoWithNumbers {
    Add,
    Subtract,
}

impl VeryVerboseEnumOfThingsToDoWithNumbers {
    fn run(&self, x: i32, y: i32) -> i32 {
        match self {
            Self::Add => x + y,
            Self::Subtract => x - y,
        }
    }
}
```

Pour en savoir plus sur les énumérations et les alias de type, vous pouvez lire le rapport de stabilisation à partir du moment où cette fonctionnalité est devenue stable dans Rust.
