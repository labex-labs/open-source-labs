# Implementing Transitions as Transformations into Different Types

Wie bekommen wir dann einen veröffentlichten Beitrag? Wir möchten die Regel durchsetzen, dass ein Entwurfszustand eines Beitrags überprüft und genehmigt werden muss, bevor er veröffentlicht werden kann. Ein Beitrag im Zustand „Wartet auf Überprüfung“ sollte immer noch keinen Inhalt anzeigen. Lassen Sie uns diese Beschränkungen implementieren, indem wir eine weitere Struktur, `PendingReviewPost`, hinzufügen, die `request_review`-Methode auf `DraftPost` definieren, um eine `PendingReviewPost` zurückzugeben, und eine `approve`-Methode auf `PendingReviewPost` definieren, um eine `Post` zurückzugeben, wie in Listing 17-20 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl DraftPost {
    --snip--
    pub fn request_review(self) -> PendingReviewPost {
        PendingReviewPost {
            content: self.content,
        }
    }
}

pub struct PendingReviewPost {
    content: String,
}

impl PendingReviewPost {
    pub fn approve(self) -> Post {
        Post {
            content: self.content,
        }
    }
}
```

Listing 17-20: Eine `PendingReviewPost`, die durch Aufruf von `request_review` auf `DraftPost` erstellt wird, und eine `approve`-Methode, die eine `PendingReviewPost` in einen veröffentlichten `Post` umwandelt

Die `request_review`- und `approve`-Methoden übernehmen die Eigentumsgewalt von `self`, verbrauchen somit die `DraftPost`- und `PendingReviewPost`-Instanzen und wandeln sie jeweils in eine `PendingReviewPost` und einen veröffentlichten `Post` um. Auf diese Weise haben wir keine verbleibenden `DraftPost`-Instanzen mehr, nachdem wir `request_review` auf ihnen aufgerufen haben, und so weiter. Die `PendingReviewPost`-Struktur hat keine darauf definierte `content`-Methode, sodass das Versuchen, ihren Inhalt zu lesen, zu einem Compilerfehler führt, wie bei `DraftPost`. Da der einzige Weg, um eine veröffentlichte `Post`-Instanz zu erhalten, die eine definierte `content`-Methode hat, darin besteht, die `approve`-Methode auf einer `PendingReviewPost` aufzurufen, und der einzige Weg, um eine `PendingReviewPost` zu erhalten, darin besteht, die `request_review`-Methode auf einer `DraftPost` aufzurufen, haben wir jetzt den Blogbeitrags-Workflow in das Typsystem kodiert.

Wir müssen aber auch einige kleine Änderungen an `main` vornehmen. Die `request_review`- und `approve`-Methoden geben neue Instanzen zurück, anstatt die Struktur, auf der sie aufgerufen werden, zu modifizieren, sodass wir mehr `let post =`-Shadowing-Zuweisungen hinzufügen müssen, um die zurückgegebenen Instanzen zu speichern. Wir können auch keine Assertionen mehr haben, dass der Inhalt der Entwurfszustände und der Zustände, die auf Überprüfung warten, leere Strings sind, und wir brauchen sie auch nicht: Wir können den Code nicht mehr kompilieren, der versucht, den Inhalt von Beiträgen in diesen Zuständen zu verwenden. Der aktualisierte Code in `main` ist in Listing 17-21 gezeigt.

Dateiname: `src/main.rs`

```rust
use blog::Post;

fn main() {
    let mut post = Post::new();

    post.add_text("I ate a salad for lunch today");

    let post = post.request_review();

    let post = post.approve();

    assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-21: Änderungen an `main`, um die neue Implementierung des Blogbeitrags-Workflows zu verwenden

Die Änderungen, die wir an `main` vornehmen mussten, um `post` neu zuzuweisen, bedeuten, dass diese Implementierung nicht mehr ganz dem objektorientierten State-Pattern folgt: Die Transformationen zwischen den Zuständen werden nicht mehr vollständig innerhalb der `Post`-Implementierung kapselt. Unser Gewinn ist jedoch, dass ungültige Zustände jetzt aufgrund des Typsystems und der Typprüfsung, die zur Compile-Zeit erfolgt, unmöglich sind! Dies gewährleistet, dass bestimmte Fehler, wie die Anzeige des Inhalts eines nicht veröffentlichten Beitrags, vor der Produktion entdeckt werden.

Versuchen Sie die am Anfang dieses Abschnitts vorgeschlagenen Aufgaben auf dem `blog`-Kratzen, wie er nach Listing 17-21 ist, um zu sehen, was Sie über das Design dieser Version des Codes denken. Beachten Sie, dass einige der Aufgaben in diesem Design möglicherweise bereits abgeschlossen sind.

Wir haben gesehen, dass auch wenn Rust in der Lage ist, objektorientierte Entwurfsmuster zu implementieren, auch andere Muster, wie die Kodierung des Zustands in das Typsystem, in Rust verfügbar sind. Diese Muster haben unterschiedliche Vor- und Nachteile. Auch wenn Sie möglicherweise sehr vertraut mit objektorientierten Mustern sind, kann das Nachdenken über das Problem, um die Funktionen von Rust zu nutzen, Vorteile bringen, wie das Verhindern von bestimmten Fehlern zur Compile-Zeit. Objektorientierte Muster werden aufgrund bestimmter Eigenschaften, wie der Eigentumsverwaltung, die objektorientierten Sprachen nicht haben, nicht immer die beste Lösung in Rust sein.
