# Encoding States and Behavior as Types

Wir werden Ihnen zeigen, wie Sie das State-Pattern neu denken, um eine andere Reihe von Vor- und Nachteilen zu erhalten. Anstatt die Zustände und Übergänge vollständig zu kapseln, sodass der externe Code nichts von ihnen weiß, werden wir die Zustände in verschiedene Typen kodieren. Folglich wird das Typprüfsystem von Rust Compilerfehler ausgeben, um Versuche zu verhindern, Entwurfsbeiträge zu verwenden, wo nur veröffentlichte Beiträge erlaubt sind.

Betrachten wir den ersten Teil von `main` in Listing 17-11:

Dateiname: `src/main.rs`

```rust
fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");
    assert_eq!("", post.content());
}
```

Wir ermöglichen immer noch die Erstellung neuer Beiträge im Entwurfszustand mithilfe von `Post::new` und die Möglichkeit, Text zum Inhalt des Beitrags hinzuzufügen. Anstatt jedoch eine `content`-Methode auf einem Entwurfszustand zu haben, die einen leeren String zurückgibt, werden wir es so gestalten, dass Entwurfszustände überhaupt keine `content`-Methode haben. Auf diese Weise erhalten wir einen Compilerfehler, wenn wir versuchen, den Inhalt eines Entwurfszustands zu erhalten, der uns mitteilt, dass die Methode nicht existiert. Folglich wird es uns unmöglich sein, versehentlich den Inhalt eines Entwurfszustands in der Produktion anzuzeigen, da dieser Code nicht einmal kompilieren wird. Listing 17-19 zeigt die Definition einer `Post`-Struktur und einer `DraftPost`-Struktur sowie die Methoden auf jeder.

Dateiname: `src/lib.rs`

```rust
pub struct Post {
    content: String,
}

pub struct DraftPost {
    content: String,
}

impl Post {
  1 pub fn new() -> DraftPost {
        DraftPost {
            content: String::new(),
        }
    }

  2 pub fn content(&self) -> &str {
        &self.content
    }
}

impl DraftPost {
  3 pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-19: Eine `Post`-Struktur mit einer `content`-Methode und eine `DraftPost`-Struktur ohne eine `content`-Methode

Sowohl die `Post`- als auch die `DraftPost`-Strukturen haben ein privates `content`-Feld, das den Blogbeitragstext speichert. Die Strukturen haben kein `state`-Feld mehr, da wir die Kodierung des Zustands in die Typen der Strukturen verschieben. Die `Post`-Struktur wird einen veröffentlichten Beitrag repräsentieren, und sie hat eine `content`-Methode, die den `content` zurückgibt \[2\].

Wir haben immer noch eine `Post::new`-Funktion, aber anstatt eine Instanz von `Post` zurückzugeben, gibt sie eine Instanz von `DraftPost` zurück \[1\]. Da `content` privat ist und es keine Funktionen gibt, die `Post` zurückgeben, ist es momentan nicht möglich, eine Instanz von `Post` zu erstellen.

Die `DraftPost`-Struktur hat eine `add_text`-Methode, sodass wir wie zuvor Text zu `content` hinzufügen können \[3\], beachten Sie jedoch, dass `DraftPost` keine definierte `content`-Methode hat! Somit stellt das Programm sicher, dass alle Beiträge als Entwurfszustände beginnen und dass der Inhalt von Entwurfszuständen nicht für die Anzeige verfügbar ist. Jeder Versuch, diesen Beschränkungen zu entgehen, führt zu einem Compilerfehler.
