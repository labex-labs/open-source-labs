# Defining a Trait

Ein Typverhalten besteht aus den Methoden, die wir auf diesem Typ aufrufen können. Verschiedene Typen teilen das gleiche Verhalten, wenn wir auf allen diesen Typen die gleichen Methoden aufrufen können. Trait-Definitionen sind eine Möglichkeit, Methodensignaturen zusammenzufassen, um eine Menge an Verhaltensweisen zu definieren, die erforderlich sind, um einen bestimmten Zweck zu erreichen.

Nehmen wir beispielsweise an, dass wir mehrere Structs haben, die verschiedene Arten und Mengen von Text enthalten: ein `NewsArticle`-Struct, der eine Nachrichtengeschichte in einem bestimmten Ort speichert, und ein `Tweet`, der maximal 280 Zeichen haben kann, zusammen mit Metadaten, die angeben, ob es ein neuer Tweet, ein Retweet oder eine Antwort auf einen anderen Tweet war.

Wir möchten eine Medienaggregator-Bibliothekskiste namens `aggregator` erstellen, die Zusammenfassungen von Daten anzeigen kann, die in einer `NewsArticle`- oder `Tweet`-Instanz gespeichert sein könnten. Dazu benötigen wir eine Zusammenfassung von jedem Typ und werden diese Zusammenfassung durch Aufruf einer `summarize`-Methode auf einer Instanz anfordern. Listing 10-12 zeigt die Definition eines öffentlichen `Summary`-Traits, das dieses Verhalten ausdrückt.

Dateiname: `src/lib.rs`

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

Listing 10-12: Ein `Summary`-Trait, das aus dem Verhalten besteht, das von einer `summarize`-Methode bereitgestellt wird

Hier deklarieren wir ein Trait mit dem Schlüsselwort `trait` und dann dem Namen des Traits, was in diesem Fall `Summary` ist. Wir deklarieren das Trait auch als `pub`, damit Kisten, die von dieser Kiste abhängen, auch dieses Trait verwenden können, wie wir in ein paar Beispielen sehen werden. Innerhalb der geschweiften Klammern deklarieren wir die Methodensignaturen, die das Verhalten der Typen beschreiben, die dieses Trait implementieren, was in diesem Fall `fn summarize(&self) -> String` ist.

Nach der Methodensignatur geben wir statt einer Implementierung innerhalb von geschweiften Klammern ein Semikolon ein. Jeder Typ, der dieses Trait implementiert, muss sein eigenes benutzerdefiniertes Verhalten für den Methodenkörper angeben. Der Compiler wird sicherstellen, dass jeder Typ, der das `Summary`-Trait hat, die Methode `summarize` mit genau dieser Signatur definiert hat.

Ein Trait kann mehrere Methoden in seinem Körper haben: Die Methodensignaturen werden pro Zeile aufgelistet und jede Zeile endet mit einem Semikolon.
