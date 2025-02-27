# Defining Post and Creating a New Instance in the Draft State

Lassen Sie uns mit der Implementierung der Bibliothek beginnen! Wir wissen, dass wir eine öffentliche `Post`-Struktur benötigen, die etwas Inhalt enthält, daher werden wir mit der Definition der Struktur und einer zugehörigen öffentlichen `new`-Funktion beginnen, um eine Instanz von `Post` zu erstellen, wie in Listing 17-12 gezeigt. Wir werden auch ein privates `State`-Trait definieren, das das Verhalten definieren wird, das alle Zustandsobjekte für einen `Post` haben müssen.

Dann wird `Post` ein Trait-Objekt von `Box<dyn State>` in einem privaten Feld namens `state` innerhalb einer `Option<T>` enthalten, um das Zustandsobjekt zu halten. Sie werden gleich sehen, warum die `Option<T>` notwendig ist.

Dateiname: `src/lib.rs`

```rust
pub struct Post {
    state: Option<Box<dyn State>>,
    content: String,
}

impl Post {
    pub fn new() -> Post {
        Post {
          1 state: Some(Box::new(Draft {})),
          2 content: String::new(),
        }
    }
}

trait State {}

struct Draft {}

impl State for Draft {}
```

Listing 17-12: Definition einer `Post`-Struktur und einer `new`-Funktion, die eine neue `Post`-Instanz erstellt, eines `State`-Traits und einer `Draft`-Struktur

Das `State`-Trait definiert das von verschiedenen Post-Zuständen geteilte Verhalten. Die Zustandsobjekte sind `Draft`, `PendingReview` und `Published`, und alle werden das `State`-Trait implementieren. Momentan hat das Trait keine Methoden, und wir werden beginnen, nur den `Draft`-Zustand zu definieren, da das der Zustand ist, in dem wir einen Beitrag beginnen möchten.

Wenn wir eine neue `Post`-Instanz erstellen, legen wir ihr `state`-Feld auf einen `Some`-Wert fest, der eine `Box` enthält \[1\]. Diese `Box` verweist auf eine neue Instanz der `Draft`-Struktur. Dies gewährleistet, dass jedes Mal, wenn wir eine neue Instanz von `Post` erstellen, sie als Entwurf beginnen wird. Da das `state`-Feld von `Post` privat ist, gibt es keine Möglichkeit, eine `Post`-Instanz in einem anderen Zustand zu erstellen! In der `Post::new`-Funktion legen wir das `content`-Feld auf einen neuen, leeren `String` fest \[2\].
