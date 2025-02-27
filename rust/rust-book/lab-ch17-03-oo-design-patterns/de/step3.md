# Storing the Text of the Post Content

Wir haben in Listing 17-11 gesehen, dass wir eine Methode namens `add_text` aufrufen können und ihr einen `&str` übergeben, der dann als Textinhalt des Blog-Beitrags hinzugefügt wird. Wir implementieren dies als Methode, anstatt das `content`-Feld als `pub` zu exponieren, damit wir später eine Methode implementieren können, die steuert, wie die Daten des `content`-Felds gelesen werden. Die `add_text`-Methode ist ziemlich einfach, daher fügen wir in Listing 17-13 die Implementierung zum `impl Post`-Block hinzu.

Dateiname: `src/lib.rs`

```rust
impl Post {
    --snip--
    pub fn add_text(&mut self, text: &str) {
        self.content.push_str(text);
    }
}
```

Listing 17-13: Implementierung der `add_text`-Methode, um Text zum `content` eines Beitrags hinzuzufügen

Die `add_text`-Methode nimmt eine mutable Referenz auf `self`, weil wir die `Post`-Instanz ändern, auf der wir `add_text` aufrufen. Anschließend rufen wir `push_str` auf der `String` in `content` auf und übergeben das `text`-Argument, um es zum gespeicherten `content` hinzuzufügen. Dieses Verhalten hängt nicht vom Zustand des Beitrags ab, daher ist es kein Teil des State-Patterns. Die `add_text`-Methode interagiert überhaupt nicht mit dem `state`-Feld, gehört aber zu dem Verhalten, das wir unterstützen möchten.
