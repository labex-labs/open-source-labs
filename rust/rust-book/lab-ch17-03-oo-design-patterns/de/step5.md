# Requesting a Review Changes the Post's State

Als nächstes müssen wir Funktionalität hinzufügen, um eine Überprüfung eines Beitrags anzufordern, was seinen Zustand von `Draft` in `PendingReview` ändern sollte. Listing 17-15 zeigt diesen Code.

Dateiname: `src/lib.rs`

```rust
impl Post {
    --snip--
  1 pub fn request_review(&mut self) {
      2 if let Some(s) = self.state.take() {
          3 self.state = Some(s.request_review())
        }
    }
}

trait State {
  4 fn request_review(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      5 Box::new(PendingReview {})
    }
}

struct PendingReview {}

impl State for PendingReview {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
      6 self
    }
}
```

Listing 17-15: Implementierung von `request_review`-Methoden auf `Post` und dem `State`-Trait

Wir geben `Post` eine öffentliche Methode namens `request_review`, die eine mutable Referenz auf `self` nimmt \[1\]. Dann rufen wir eine interne `request_review`-Methode auf dem aktuellen Zustand von `Post` auf \[3\], und diese zweite `request_review`-Methode konsumiert den aktuellen Zustand und gibt einen neuen Zustand zurück.

Wir fügen die `request_review`-Methode zum `State`-Trait hinzu \[4\]; alle Typen, die das Trait implementieren, müssen jetzt die `request_review`-Methode implementieren. Beachten Sie, dass anstatt `self`, `&self` oder `&mut self` als ersten Parameter der Methode wir `self: Box<Self>` haben. Diese Syntax bedeutet, dass die Methode nur gültig ist, wenn sie auf einer `Box` aufgerufen wird, die den Typ hält. Diese Syntax übernimmt die Eigentumsgewalt von `Box<Self>`, was den alten Zustand ungültig macht, sodass der Zustandswert von `Post` in einen neuen Zustand transformiert werden kann.

Um den alten Zustand zu konsumieren, muss die `request_review`-Methode die Eigentumsgewalt über den Zustandswert übernehmen. Hier kommt das `Option` im `state`-Feld von `Post` ins Spiel: wir rufen die `take`-Methode auf, um den `Some`-Wert aus dem `state`-Feld zu nehmen und an seiner Stelle ein `None` zu hinterlassen, weil Rust uns nicht erlaubt, unbesetzte Felder in Structs zu haben \[2\]. Dies ermöglicht es uns, den `state`-Wert aus `Post` zu bewegen, anstatt ihn zu entleihen. Dann werden wir den Zustandswert von `Post` auf das Ergebnis dieser Operation setzen.

Wir müssen `state` vorübergehend auf `None` setzen, anstatt es direkt mit Code wie `self.state = self.state.request_review();` zu setzen, um die Eigentumsgewalt über den `state`-Wert zu erhalten. Dies gewährleistet, dass `Post` den alten `state`-Wert nicht mehr verwenden kann, nachdem wir ihn in einen neuen Zustand transformiert haben.

Die `request_review`-Methode auf `Draft` gibt eine neue, in eine Box gepackte Instanz eines neuen `PendingReview`-Structs zurück \[5\], der den Zustand repräsentiert, wenn ein Beitrag auf eine Überprüfung wartet. Die `PendingReview`-Struktur implementiert auch die `request_review`-Methode, macht aber keine Transformationen. Stattdessen gibt sie sich selbst zurück \[6\], weil wenn wir eine Überprüfung für einen Beitrag in einem bereits im `PendingReview`-Zustand anfordern, er im `PendingReview`-Zustand bleiben sollte.

Jetzt können wir die Vorteile des State-Patterns beginnen zu sehen: Die `request_review`-Methode auf `Post` ist die gleiche, unabhängig von ihrem `state`-Wert. Jeder Zustand ist für seine eigenen Regeln verantwortlich.

Wir lassen die `content`-Methode auf `Post` so wie sie ist, und geben einen leeren String-Slice zurück. Wir können jetzt einen `Post` sowohl im `PendingReview`-Zustand als auch im `Draft`-Zustand haben, aber wir wollen das gleiche Verhalten im `PendingReview`-Zustand. Listing 17-11 funktioniert jetzt bis zur Zeile bei \[5\]!
