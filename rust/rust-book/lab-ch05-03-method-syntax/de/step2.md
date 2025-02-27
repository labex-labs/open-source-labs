# Methoden definieren

Ändern wir die `area`-Funktion, die eine `Rectangle`-Instanz als Parameter hat, und definieren stattdessen eine `area`-Methode für die `Rectangle`-Struktur, wie in Listing 5-13 gezeigt.

Dateiname: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

1 impl Rectangle {
  2 fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
      3 rect1.area()
    );
}
```

Listing 5-13: Definieren einer `area`-Methode für die `Rectangle`-Struktur

Um die Funktion innerhalb des Kontexts von `Rectangle` zu definieren, starten wir einen `impl` (Implementierungs)-Block für `Rectangle` \[1\]. Alles innerhalb dieses `impl`-Blocks wird mit dem `Rectangle`-Typ assoziiert. Dann bewegen wir die `area`-Funktion innerhalb der geschweiften Klammern des `impl` \[2\] und ändern den ersten (und in diesem Fall einzigen) Parameter in der Signatur und überall im Körper in `self`. In `main`, wo wir die `area`-Funktion aufgerufen und `rect1` als Argument übergeben haben, können wir stattdessen die _Methodensyntax_ verwenden, um die `area`-Methode auf unserer `Rectangle`-Instanz aufzurufen \[3\]. Die Methodensyntax folgt einer Instanz: Wir fügen einen Punkt hinzu, gefolgt vom Methodennamen, Klammern und beliebigen Argumenten.

In der Signatur für `area` verwenden wir `&self` anstelle von `rectangle: &Rectangle`. `&self` ist eigentlich die Abkürzung für `self: &Self`. Innerhalb eines `impl`-Blocks ist der Typ `Self` ein Alias für den Typ, für den der `impl`-Block bestimmt ist. Methoden müssen einen Parameter namens `self` vom Typ `Self` als ersten Parameter haben, daher lässt Rust Ihnen diese mit nur dem Namen `self` im ersten Parameterplatz abkürzen. Beachten Sie, dass wir immer noch das `&` vor der `self`-Abkürzung verwenden müssen, um anzuzeigen, dass diese Methode die `Self`-Instanz baut, genauso wie wir es in `rectangle: &Rectangle` getan haben. Methoden können die Eigentumsgewalt an `self` übernehmen, `self` unveränderlich bauen, wie wir hier getan haben, oder `self` veränderlich bauen, genauso wie sie auch jeden anderen Parameter können.

Wir haben hier `&self` gewählt, aus dem gleichen Grund, warum wir in der Funktionsversion `&Rectangle` verwendet haben: Wir möchten keine Eigentumsgewalt übernehmen und nur die Daten in der Struktur lesen, nicht darauf schreiben. Wenn wir die Instanz, auf der wir die Methode aufgerufen haben, als Teil dessen ändern möchten, was die Methode tut, würden wir `&mut self` als ersten Parameter verwenden. Es ist selten, dass eine Methode die Eigentumsgewalt an der Instanz übernimmt, indem sie nur `self` als ersten Parameter verwendet; diese Technik wird normalerweise verwendet, wenn die Methode `self` in etwas anderes umwandelt und Sie möchten, dass der Aufrufer die ursprüngliche Instanz nach der Transformation nicht mehr verwenden kann.

Der Hauptgrund für die Verwendung von Methoden statt Funktionen, neben der Bereitstellung der Methodensyntax und der Tatsache, dass man nicht den Typ von `self` in jeder Methodensignatur wiederholen muss, ist die Organisation. Wir haben alles, was wir mit einer Instanz eines Typs tun können, in einem `impl`-Block zusammengefasst, anstatt zukünftige Benutzer unseres Codes dazu zu bringen, in verschiedenen Teilen der Bibliothek, die wir zur Verfügung stellen, nach den Fähigkeiten von `Rectangle` zu suchen.

Beachten Sie, dass wir die Möglichkeit haben, einer Methode denselben Namen wie einem der Felder der Struktur zu geben. Beispielsweise können wir eine Methode auf `Rectangle` definieren, die auch `width` heißt:

Dateiname: `src/main.rs`

```rust
impl Rectangle {
    fn width(&self) -> bool {
        self.width > 0
    }
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    if rect1.width() {
        println!(
            "The rectangle has a nonzero width; it is {}",
            rect1.width
        );
    }
}
```

Hier wählen wir aus, dass die `width`-Methode `true` zurückgibt, wenn der Wert im `width`-Feld der Instanz größer als `0` ist, und `false`, wenn der Wert `0` ist: Wir können ein Feld innerhalb einer Methode mit demselben Namen zu jedem Zweck verwenden. In `main`, wenn wir `rect1.width` mit Klammern folgen, weiß Rust, dass wir die Methode `width` meinen. Wenn wir keine Klammern verwenden, weiß Rust, dass wir das Feld `width` meinen.

Oft, aber nicht immer, wenn wir Methoden mit demselben Namen wie einem Feld geben, möchten wir, dass sie nur den Wert im Feld zurückgeben und nichts anderes tun. Methoden wie diese werden _Getter_ genannt, und Rust implementiert sie nicht automatisch für Strukturfelder wie einige andere Sprachen. Getter sind nützlich, weil Sie das Feld privat und die Methode öffentlich machen können und so einen schreibgeschützten Zugang zu diesem Feld als Teil der öffentlichen API des Typs ermöglichen. Wir werden in Kapitel 7 diskutieren, was öffentlich und privat sind und wie man ein Feld oder eine Methode als öffentlich oder privat markiert.

> **Wo ist der -\> Operator?**
>
> In C und C++ werden zwei verschiedene Operatoren zum Aufrufen von Methoden verwendet: Sie verwenden `.`, wenn Sie direkt auf dem Objekt eine Methode aufrufen, und `->`, wenn Sie die Methode auf einem Zeiger auf das Objekt aufrufen und den Zeiger zuerst aufgelöst haben müssen. Mit anderen Worten, wenn `object` ein Zeiger ist, ist `object->`something`()` ähnlich zu `(*object).`something`()`.
>
> Rust hat keinen Äquivalent zum `->`-Operator; stattdessen hat Rust ein Feature namens _automatisches Referenzieren und Dereferenzieren_. Methodenaufrufe sind eine der wenigen Stellen in Rust, an denen dieses Verhalten existiert.
>
> So funktioniert es: Wenn Sie eine Methode mit `object.`something`()` aufrufen, fügt Rust automatisch `&`, `&mut` oder `*` hinzu, sodass `object` der Signatur der Methode entspricht. Mit anderen Worten, die folgenden beiden Zeilen sind gleichwertig:
>
>     p1.distance(&p2);
>     (&p1).distance(&p2);
>
> Die erste sieht viel sauberer aus. Dieses automatische Referenzieren funktioniert, weil Methoden einen eindeutigen Empfänger haben - den Typ von `self`. Ausgehend vom Empfänger und dem Namen einer Methode kann Rust eindeutig feststellen, ob die Methode das Objekt liest (`&self`), mutiert (`&mut self`) oder konsumiert (`self`). Die Tatsache, dass Rust das Entlehnung implizit für Methodenempfänger macht, ist ein wichtiger Teil der Tatsache, dass die Eigentumsgewalt in der Praxis komfortabel zu handhaben ist.
