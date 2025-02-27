# Ensuring the Content of a Draft Post Is Empty

Auch nachdem wir `add_text` aufgerufen und etwas Inhalt zu unserem Beitrag hinzugefügt haben, möchten wir, dass die `content`-Methode einen leeren String-Slice zurückgibt, da der Beitrag immer noch im Entwurfszustand ist, wie in \[3\] in Listing 17-11 gezeigt. Momentan implementieren wir die `content`-Methode mit dem einfachsten Ding, das diese Anforderung erfüllt: indem wir immer einen leeren String-Slice zurückgeben. Wir werden dies später ändern, wenn wir die Möglichkeit implementieren, einen Beitragsstatus zu ändern, sodass er veröffentlicht werden kann. Bisher können Beiträge nur im Entwurfszustand sein, daher sollte der Beitragsinhalt immer leer sein. Listing 17-14 zeigt diese Platzhalter-Implementierung.

Dateiname: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn content(&self) -> &str {
        ""
    }
}
```

Listing 17-14: Hinzufügen einer Platzhalter-Implementierung für die `content`-Methode auf `Post`, die immer einen leeren String-Slice zurückgibt

Mit dieser hinzugefügten `content`-Methode funktioniert alles in Listing 17-11 bis zur Zeile bei \[3\] wie gewünscht.
