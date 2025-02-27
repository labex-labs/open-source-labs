# macro_rules!

Rust bietet ein leistungsstarkes Makrosystem, das Metaprogrammierung ermöglicht. Wie Sie in vorherigen Kapiteln gesehen haben, sehen Makros wie Funktionen aus, nur dass ihr Name mit einem Ausrufezeichen `!` endet. Anstatt jedoch einen Funktionsaufruf zu generieren, werden Makros in Quellcode expandiert, der zusammen mit dem Rest des Programms kompiliert wird. Anders als Makros in C und anderen Sprachen werden Rust-Makros jedoch in abstrakte Syntaxbäume expandiert, statt einer String-Vorverarbeitung, sodass Sie keine unerwarteten Prädenzfehler bekommen.

Makros werden mit dem `macro_rules!`-Makro erstellt.

```rust
// Dies ist ein einfaches Makro namens `say_hello`.
macro_rules! say_hello {
    // `()` gibt an, dass das Macro keine Argumente nimmt.
    () => {
        // Das Macro wird in den Inhalt dieses Blocks expandiert.
        println!("Hello!")
    };
}

fn main() {
    // Dieser Aufruf wird in `println!("Hello")` expandiert
    say_hello!()
}
```

Warum sind Makros nützlich?

1.  Vermeiden Sie Wiederholungen. Es gibt viele Fälle, in denen Sie möglicherweise in mehreren Stellen ähnliche Funktionalität benötigen, aber mit unterschiedlichen Typen. Oft ist das Schreiben eines Makros ein nützlicher Weg, um Codewiederholungen zu vermeiden. (Mehr dazu später)

2.  Domänenspezifische Sprachen. Makros ermöglichen es Ihnen, eine spezielle Syntax für einen bestimmten Zweck zu definieren. (Mehr dazu später)

3.  Variadische Schnittstellen. Manchmal möchten Sie eine Schnittstelle definieren, die eine variable Anzahl von Argumenten akzeptiert. Ein Beispiel ist `println!`, das je nach Formatzeichen beliebig viele Argumente akzeptieren kann. (Mehr dazu später)
