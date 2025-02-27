# Dynamisch angepasste Typen und das Sized-Trait

Rust muss bestimmte Details über seine Typen kennen, wie viel Speicherplatz beispielsweise für einen Wert eines bestimmten Typs zuzuweisen ist. Dies lässt einen kleinen Winkel seines Typsystems zunächst etwas verwirrend: den Begriff der _dynamisch angepassten Typen_. Manchmal auch als _DSTs_ oder _unsized types_ bezeichnet, erlauben diese Typen es uns, Code mit Werten zu schreiben, deren Größe wir erst zur Laufzeit kennen können.

Lassen Sie uns die Details eines dynamisch angepassten Typs namens `str` untersuchen, den wir bereits im ganzen Buch verwendet haben. Richtig, nicht `&str`, sondern `str` allein ist ein DST. Wir können die Länge der Zeichenkette erst zur Laufzeit wissen, was bedeutet, dass wir keine Variable vom Typ `str` erstellen können, und wir können auch keinen Parameter vom Typ `str` akzeptieren. Betrachten Sie den folgenden Code, der nicht funktioniert:

```rust
let s1: str = "Hello there!";
let s2: str = "How's it going?";
```

Rust muss wissen, wie viel Speicherplatz für jeden Wert eines bestimmten Typs zuzuweisen ist, und alle Werte eines Typs müssen den gleichen Speicherplatz verwenden. Wenn Rust uns diesen Code schreiben würde, müssten diese beiden `str`-Werte den gleichen Speicherplatz beanspruchen. Aber sie haben unterschiedliche Längen: `s1` benötigt 12 Bytes Speicher und `s2` benötigt 15. Deshalb ist es nicht möglich, eine Variable zu erstellen, die einen dynamisch angepassten Typ enthält.

Was tun wir also? In diesem Fall kennen Sie bereits die Antwort: wir machen die Typen von `s1` und `s2` zu einem `&str` anstatt einem `str`. Erinnern Sie sich aus "String Slices", dass die Slicedatenstruktur nur die Startposition und die Länge des Slices speichert. Also, obwohl ein `&T` ein einzelner Wert ist, der die Speicheradresse des Ortes speichert, an dem der `T` gespeichert ist, ist ein `&str` _zwei_ Werte: die Adresse des `str` und seine Länge. Daher können wir die Größe eines `&str`-Werts zur Compilezeit bestimmen: es ist das Doppelte der Länge eines `usize`. Das heißt, wir wissen immer die Größe eines `&str`, unabhängig davon, wie lang die Zeichenkette ist, auf die er verweist. Im Allgemeinen ist dies die Art und Weise, wie dynamisch angepasste Typen in Rust verwendet werden: Sie haben ein zusätzliches Metadatenbit, das die Größe der dynamischen Informationen speichert. Die goldene Regel für dynamisch angepasste Typen ist, dass wir Werte von dynamisch angepassten Typen immer hinter einem Zeiger von irgendeiner Art platzieren müssen.

Wir können `str` mit allen möglichen Zeigern kombinieren: beispielsweise `Box<str>` oder `Rc<str>`. Tatsächlich haben Sie das bereits zuvor gesehen, aber mit einem anderen dynamisch angepassten Typ: Traits. Jeder Trait ist ein dynamisch angepasster Typ, auf den wir uns mit dem Namen des Traits beziehen können. Im Abschnitt "Verwendung von Trait-Objekten, die Werte unterschiedlicher Typen zulassen" haben wir erwähnt, dass wir Traits als Trait-Objekte verwenden müssen, indem wir sie hinter einem Zeiger platzieren, wie `&dyn Trait` oder `Box<dyn Trait>` (`Rc<dyn Trait>` würde ebenfalls funktionieren).

Um mit DSTs umzugehen, stellt Rust das `Sized`-Trait bereit, um zu bestimmen, ob die Größe eines Typs zur Compilezeit bekannt ist oder nicht. Dieses Trait wird automatisch für alles implementiert, dessen Größe zur Compilezeit bekannt ist. Darüber hinaus fügt Rust implizit eine Begrenzung auf `Sized` zu jeder generischen Funktion hinzu. Das heißt, eine generische Funktionsdefinition wie diese:

```rust
fn generic<T>(t: T) {
    --snip--
}
```

wird tatsächlich so behandelt, als hätten wir dies geschrieben:

```rust
fn generic<T: Sized>(t: T) {
    --snip--
}
```

Standardmäßig funktionieren generische Funktionen nur mit Typen, deren Größe zur Compilezeit bekannt ist. Sie können jedoch die folgende spezielle Syntax verwenden, um diese Einschränkung zu lockern:

```rust
fn generic<T:?Sized>(t: &T) {
    --snip--
}
```

Eine Trait-Begrenzung auf `?Sized` bedeutet "`T` kann `Sized` sein oder auch nicht", und diese Notation überschreibt die Standard-Einschränkung, dass generische Typen zur Compilezeit eine bekannte Größe haben müssen. Die `?Trait`-Syntax mit dieser Bedeutung ist nur für `Sized` verfügbar, nicht für andere Traits.

Beachten Sie auch, dass wir den Typ des `t`-Parameters von `T` auf `&T` umgeschaltet haben. Da der Typ möglicherweise nicht `Sized` ist, müssen wir ihn hinter einem Zeiger von irgendeiner Art verwenden. In diesem Fall haben wir eine Referenz gewählt.

Als nächstes werden wir über Funktionen und Closures sprechen!
