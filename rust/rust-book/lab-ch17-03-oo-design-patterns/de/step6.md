# Adding approve to Change the Behavior of content

Die `approve`-Methode wird ähnlich zur `request_review`-Methode sein: Sie wird `state` auf den Wert setzen, den der aktuelle Zustand angibt, wenn dieser Zustand genehmigt wird, wie in Listing 17-16 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve())
        }
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dyn State>;
    fn approve(self: Box<Self>) -> Box<dyn State>;
}

struct Draft {}

impl State for Draft {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      1 self
    }
}

struct PendingReview {}

impl State for PendingReview {
    --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
      2 Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}
```

Listing 17-16: Implementierung der `approve`-Methode auf `Post` und dem `State`-Trait

Wir fügen die `approve`-Methode zum `State`-Trait hinzu und erstellen eine neue Struktur, die `State` implementiert, den `Published`-Zustand.

Ähnlich wie die `request_review`-Methode auf `PendingReview` funktioniert, hat der Aufruf der `approve`-Methode auf einem `Draft` keine Auswirkungen, da `approve` `self` zurückgibt \[1\]. Wenn wir `approve` auf `PendingReview` aufrufen, wird eine neue, in eine Box gepackte Instanz des `Published`-Structs zurückgegeben \[2\]. Die `Published`-Struktur implementiert das `State`-Trait, und für beide Methoden `request_review` und `approve` gibt sie sich selbst zurück, da der Beitrag in diesen Fällen im `Published`-Zustand bleiben sollte.

Jetzt müssen wir die `content`-Methode auf `Post` aktualisieren. Wir möchten, dass der von `content` zurückgegebene Wert von dem aktuellen Zustand von `Post` abhängt, daher wird `Post` an eine `content`-Methode delegieren, die auf seinem `state` definiert ist, wie in Listing 17-17 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(self)
    }
    --snip--
}
```

Listing 17-17: Aktualisierung der `content`-Methode auf `Post`, um an eine `content`-Methode auf `State` zu delegieren

Da das Ziel darin besteht, alle diese Regeln in den Structs zu halten, die `State` implementieren, rufen wir eine `content`-Methode auf dem Wert in `state` auf und übergeben die Beitragsinstanz (d.h. `self`) als Argument. Dann geben wir den Wert zurück, der von der Verwendung der `content`-Methode auf dem `state`-Wert zurückgegeben wird.

Wir rufen die `as_ref`-Methode auf der `Option` auf, weil wir einen Verweis auf den Wert innerhalb der `Option` möchten, anstatt die Eigentumsgewalt über den Wert zu erwerben. Da `state` eine `Option<Box<dyn State>>` ist, wird bei Aufruf von `as_ref` eine `Option<&Box<dyn State>>` zurückgegeben. Wenn wir `as_ref` nicht aufrufen würden, würden wir einen Fehler erhalten, da wir `state` nicht aus der entlehnten `&self` des Funktionsparameters heraus bewegen können.

Anschließend rufen wir die `unwrap`-Methode auf, von der wir wissen, dass sie niemals abstürzt, da wir wissen, dass die Methoden auf `Post` gewährleisten, dass `state` immer einen `Some`-Wert enthalten wird, wenn diese Methoden abgeschlossen sind. Dies ist einer der Fälle, über die wir in "Fälle, in denen Sie mehr Informationen haben als der Compiler" gesprochen haben, wenn wir wissen, dass ein `None`-Wert niemals möglich ist, auch wenn der Compiler dies nicht verstehen kann.

An diesem Punkt, wenn wir `content` auf der `&Box<dyn State>` aufrufen, wird die Deref-Zwangskonvertierung auf dem `&` und der `Box` wirken, sodass die `content`-Methode letztendlich auf dem Typ aufgerufen wird, der das `State`-Trait implementiert. Das bedeutet, dass wir `content` zur `State`-Trait-Definition hinzufügen müssen, und genau dort werden wir die Logik für den Inhalt ablegen, der zurückgegeben werden soll, je nachdem, welchen Zustand wir haben, wie in Listing 17-18 gezeigt.

Dateiname: `src/lib.rs`

```rust
trait State {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      1 ""
    }
}

--snip--
struct Published {}

impl State for Published {
    --snip--
    fn content<'a>(&self, post: &'a Post) -> &'a str {
      2 &post.content
    }
}
```

Listing 17-18: Hinzufügen der `content`-Methode zum `State`-Trait

Wir fügen eine Standardimplementierung für die `content`-Methode hinzu, die einen leeren String-Slice zurückgibt \[1\]. Das bedeutet, dass wir `content` auf den Structs `Draft` und `PendingReview` nicht implementieren müssen. Die `Published`-Struktur wird die `content`-Methode überschreiben und den Wert in `post.content` zurückgeben \[2\].

Beachten Sie, dass wir für diese Methode Lebenszeit-Anmerkungen benötigen, wie wir in Kapitel 10 diskutiert haben. Wir nehmen einen Verweis auf einen `post` als Argument und geben einen Verweis auf einen Teil dieses `post` zurück, daher ist die Lebenszeit des zurückgegebenen Verweises mit der Lebenszeit des `post`-Arguments verbunden.

Und fertig ist es - alles in Listing 17-11 funktioniert jetzt! Wir haben das State-Pattern mit den Regeln des Blog-Beitrags-Workflows implementiert. Die Logik, die mit den Regeln zusammenhängt, befindet sich in den Zustandsobjekten, anstatt durch `Post` verteilt zu sein.

> **Warum kein Enum?**
>
> Sie haben sich vielleicht gefragt, warum wir nicht ein `enum` mit den verschiedenen möglichen Beitragszuständen als Varianten verwendet haben. Das ist sicherlich eine mögliche Lösung; versuchen Sie es und vergleichen Sie die Endresultate, um zu sehen, was Ihnen besser gefällt! Ein Nachteil der Verwendung eines Enums ist, dass an jeder Stelle, an der der Wert des Enums überprüft wird, ein `match`-Ausdruck oder ähnliches erforderlich ist, um jede mögliche Variante zu behandeln. Dies kann repetitiver werden als diese Trait-Objekt-Lösung.
