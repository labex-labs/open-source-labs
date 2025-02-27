# Implementing an Object-Oriented Design Pattern

Das _State-Pattern_ ist ein objektorientiertes Entwurfsmuster. Der Kern des Musters ist, dass wir intern eine Menge von Zuständen definieren, die ein Wert annehmen kann. Die Zustände werden durch eine Menge von _Zustandsobjekten_ repräsentiert, und das Verhalten des Werts ändert sich basierend auf seinem Zustand. Wir werden anhand eines Beispiels eines Blog-Beitrags-Structs arbeiten, das ein Feld hat, um seinen Zustand zu speichern, der ein Zustandsobjekt aus der Menge "Entwurf", "Überprüfung" oder "veröffentlicht" sein wird.

Die Zustandsobjekte teilen Funktionalität: Natürlich verwenden wir in Rust Structs und Traits anstelle von Objekten und Vererbung. Jedes Zustandsobjekt ist für sein eigenes Verhalten verantwortlich und dafür, zu bestimmen, wann es in einen anderen Zustand gewechselt werden sollte. Der Wert, der ein Zustandsobjekt hält, weiß nichts über das unterschiedliche Verhalten der Zustände oder wann zwischen den Zuständen gewechselt werden sollte.

Der Vorteil des Einsatzes des State-Patterns ist, dass wir, wenn sich die geschäftlichen Anforderungen des Programms ändern, nicht die Code des Werts, der den Zustand hält, oder den Code ändern müssen, der den Wert verwendet. Wir müssen nur den Code innerhalb eines der Zustandsobjekte aktualisieren, um seine Regeln zu ändern oder vielleicht weitere Zustandsobjekte hinzuzufügen.

Zuerst werden wir das State-Pattern auf eine traditionellere objektorientierte Weise implementieren, und dann werden wir einen Ansatz verwenden, der in Rust etwas natürlicher ist. Lassen Sie uns eintauchen, um mithilfe des State-Patterns einen Blog-Beitrags-Workflow schrittweise zu implementieren.

Die endgültige Funktionalität wird wie folgt aussehen:

1. Ein Blog-Beitrag beginnt als leerer Entwurf.
2. Wenn der Entwurf fertig ist, wird eine Überprüfung des Beitrags angefordert.
3. Wenn der Beitrag genehmigt wird, wird er veröffentlicht.
4. Nur veröffentlichte Blog-Beiträge geben Inhalte zurück, um gedruckt zu werden, sodass ungenehmigte Beiträge nicht versehentlich veröffentlicht werden können.

Jede andere Änderung, die an einem Beitrag versucht wird, sollte keinen Effekt haben. Beispielsweise sollte der Beitrag, wenn wir versuchen, einen Entwurf eines Blog-Beitrags zu genehmigen, bevor wir eine Überprüfung angefordert haben, weiterhin ein unveröffentlichter Entwurf bleiben.

Listing 17-11 zeigt diesen Workflow in Codeform: Dies ist ein Beispiel für die Verwendung der API, die wir in einem Bibliothekskasten namens `blog` implementieren werden. Dies wird noch nicht kompilieren, da wir den `blog`-Kasten noch nicht implementiert haben.

Dateiname: `src/main.rs`

```rust
use blog::Post;

fn main() {
  1 let mut post = Post::new();

  2 post.add_text("I ate a salad for lunch today");
  3 assert_eq!("", post.content());

  4 post.request_review();
  5 assert_eq!("", post.content());

  6 post.approve();
  7 assert_eq!("I ate a salad for lunch today", post.content());
}
```

Listing 17-11: Code, der das gewünschte Verhalten zeigt, das wir von unserem `blog`-Kasten haben möchten

Wir möchten es dem Benutzer ermöglichen, einen neuen Entwurf eines Blog-Beitrags mit `Post::new` zu erstellen \[1\]. Wir möchten es ermöglichen, Text zum Blog-Beitrag hinzuzufügen \[2\]. Wenn wir versuchen, den Inhalt des Beitrags sofort zu erhalten, bevor die Genehmigung erfolgt, sollten wir keinen Text erhalten, da der Beitrag noch ein Entwurf ist. Wir haben `assert_eq!` im Code zu Demonstrationszwecken hinzugefügt \[3\]. Ein ausgezeichneter Unit-Test hierfür wäre, zu prüfen, dass ein Entwurf eines Blog-Beitrags aus der `content`-Methode einen leeren String zurückgibt, aber wir werden für dieses Beispiel keine Tests schreiben.

Als nächstes möchten wir eine Anfrage an die Überprüfung des Beitrags ermöglichen \[4\], und wir möchten, dass `content` einen leeren String zurückgibt, während wir auf die Überprüfung warten \[5\]. Wenn der Beitrag Genehmigung erhält \[6\], sollte er veröffentlicht werden, was bedeutet, dass der Text des Beitrags zurückgegeben wird, wenn `content` aufgerufen wird \[7\].

Beachten Sie, dass der einzige Typ, mit dem wir aus dem Kasten interagieren, der `Post`-Typ ist. Dieser Typ wird das State-Pattern verwenden und wird einen Wert halten, der eines von drei Zustandsobjekten sein wird, die die verschiedenen Zustände darstellen, in denen ein Beitrag sein kann - Entwurf, Überprüfung oder veröffentlicht. Das Wechseln von einem Zustand in einen anderen wird intern innerhalb des `Post`-Typs verwaltet. Die Zustände ändern sich als Reaktion auf die Methoden, die von den Benutzern unserer Bibliothek auf der `Post`-Instanz aufgerufen werden, aber sie müssen die Zustandsänderungen nicht direkt verwalten. Auch können die Benutzer keine Fehler bei den Zuständen machen, wie beispielsweise einen Beitrag veröffentlichen, bevor er überprüft wurde.
