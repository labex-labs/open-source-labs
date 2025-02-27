# Enum-Werte

Wir können Instanzen von den beiden Varianten von `IpAddrKind` wie folgt erstellen:

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

Beachte, dass die Varianten der Enum unter ihrem Bezeichner benannt sind, und wir verwenden einen Doppelpunkt, um die beiden zu trennen. Dies ist nützlich, da jetzt beide Werte `IpAddrKind::V4` und `IpAddrKind::V6` vom gleichen Typ sind: `IpAddrKind`. Wir können dann beispielsweise eine Funktion definieren, die einen beliebigen `IpAddrKind` annimmt:

```rust
fn route(ip_kind: IpAddrKind) {}
```

Und wir können diese Funktion mit jeder Variante aufrufen:

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

Das Verwenden von Enums hat noch weitere Vorteile. Wenn wir uns mehr über unseren IP-Adressentyp Gedanken machen, haben wir momentan keine Möglichkeit, die tatsächlichen IP-Adress-_Daten_ zu speichern; wir wissen nur, von welcher _Art_ es handelt. Da Sie gerade in Kapitel 5 über Structs gelernt haben, könnten Sie versucht sein, dieses Problem mit Structs wie in Listing 6-1 anzugehen.

```rust
1 enum IpAddrKind {
    V4,
    V6,
}

2 struct IpAddr {
  3 kind: IpAddrKind,
  4 address: String,
}

5 let home = IpAddr {
    kind: IpAddrKind::V4,
    address: String::from("127.0.0.1"),
};

6 let loopback = IpAddr {
    kind: IpAddrKind::V6,
    address: String::from("::1"),
};
```

Listing 6-1: Speichern der Daten und der `IpAddrKind`-Variante einer IP-Adresse mit einem `struct`

Hier haben wir einen Struct `IpAddr` \[2\] definiert, der zwei Felder hat: ein `kind`-Feld \[3\], das vom Typ `IpAddrKind` ist (die Enum, die wir zuvor definiert haben \[1\]), und ein `address`-Feld \[4\] vom Typ `String`. Wir haben zwei Instanzen dieses Structs. Die erste ist `home` \[5\], und sie hat den Wert `IpAddrKind::V4` als `kind` mit zugehörigen Adressdaten von `127.0.0.1`. Die zweite Instanz ist `loopback` \[6\]. Sie hat die andere Variante von `IpAddrKind` als `kind`-Wert, `V6`, und hat die Adresse `::1` damit assoziiert. Wir haben einen Struct verwendet, um die `kind`- und `address`-Werte zusammenzupacken, sodass jetzt die Variante mit dem Wert assoziiert ist.

Allerdings ist die Darstellung desselben Konzepts mit nur einer Enum kürzer: anstatt eine Enum innerhalb eines Structs zu verwenden, können wir die Daten direkt in jede Enum-Variante einfügen. Diese neue Definition der `IpAddr`-Enum sagt, dass sowohl die `V4`- als auch die `V6`-Varianten `String`-Werte haben werden:

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

Wir befestigen die Daten direkt an jeder Variante der Enum, sodass kein zusätzlicher Struct erforderlich ist. Hier ist es auch einfacher, einen weiteren Detail zu sehen, wie Enums funktionieren: Der Name jeder Enum-Variante, die wir definieren, wird auch zu einer Funktion, die eine Instanz der Enum erstellt. Das heißt, `IpAddr::V4()` ist ein Funktionsaufruf, der einen `String`-Argument nimmt und eine Instanz des `IpAddr`-Typs zurückgibt. Wir erhalten diese Konstruktorfunktion automatisch als Ergebnis der Enum-Definition.

Es gibt einen weiteren Vorteil bei der Verwendung einer Enum statt eines Structs: jede Variante kann verschiedene Typen und Mengen an zugehörigen Daten haben. Version-vier-IP-Adressen werden immer vier numerische Komponenten haben, die Werte zwischen 0 und 255 haben werden. Wenn wir `V4`-Adressen als vier `u8`-Werte speichern möchten, aber immer noch `V6`-Adressen als einen `String`-Wert ausdrücken möchten, könnten wir das mit einem Struct nicht tun. Enums können diesen Fall leicht beherrschen:

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

Wir haben verschiedene Wege gezeigt, um Datentypen zu definieren, um Version-vier- und Version-sechs-IP-Adressen zu speichern. Allerdings ist es so, dass das Speichern von IP-Adressen und die Kodierung ihrer Art so üblich ist, dass die Standardbibliothek eine Definition hat, die wir verwenden können! Schauen wir uns an, wie die Standardbibliothek `IpAddr` definiert: Sie hat die genaue Enum und Varianten, die wir definiert und verwendet haben, aber sie integriert die Adressdaten in die Varianten in Form von zwei verschiedenen Structs, die für jede Variante unterschiedlich definiert sind:

```rust
struct Ipv4Addr {
    --snip--
}

struct Ipv6Addr {
    --snip--
}

enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

Dieser Code zeigt, dass Sie beliebige Arten von Daten in eine Enum-Variante einfügen können: Strings, numerische Typen oder Structs beispielsweise. Sie können sogar eine andere Enum einschließen! Auch sind die Standardbibliothekstypen oft nicht viel komplizierter als die, die Sie selbst ausdenken könnten.

Beachte, dass auch wenn die Standardbibliothek eine Definition für `IpAddr` enthält, wir immer noch unsere eigene Definition erstellen und verwenden können, ohne Konflikt zu haben, weil wir die Definition der Standardbibliothek nicht in unseren Geltungsbereich gebracht haben. Wir werden in Kapitel 7 mehr über das Einführen von Typen in den Geltungsbereich sprechen.

Schauen wir uns ein weiteres Beispiel einer Enum in Listing 6-2 an: Diese hat eine Vielzahl von Typen in ihren Varianten eingebettet.

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Listing 6-2: Eine `Message`-Enum, deren Varianten jeweils unterschiedliche Mengen und Typen von Werten speichern

Diese Enum hat vier Varianten mit unterschiedlichen Typen:

- `Quit` hat überhaupt keine zugehörigen Daten.
- `Move` hat benannte Felder, wie ein Struct.
- `Write` enthält einen einzelnen `String`.
- `ChangeColor` enthält drei `i32`-Werte.

Das Definieren einer Enum mit Varianten wie den in Listing 6-2 ist ähnlich wie das Definieren verschiedener Arten von Struct-Definitionen, nur dass die Enum das `struct`-Schlüsselwort nicht verwendet und alle Varianten unter dem `Message`-Typ zusammengefasst sind. Die folgenden Structs könnten die gleichen Daten speichern, die die vorherigen Enum-Varianten speichern:

```rust
struct QuitMessage; // unit struct
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // tuple struct
struct ChangeColorMessage(i32, i32, i32); // tuple struct
```

Aber wenn wir die verschiedenen Structs verwenden würden, von denen jeder seinen eigenen Typ hat, könnten wir nicht so leicht eine Funktion definieren, um eine beliebige dieser Arten von Nachrichten zu nehmen, wie wir es mit der in Listing 6-2 definierten `Message`-Enum, einem einzelnen Typ, könnten.

Es gibt noch eine weitere Ähnlichkeit zwischen Enums und Structs: Genauso wie wir in der Lage sind, Methoden auf Structs mit `impl` zu definieren, sind wir auch in der Lage, Methoden auf Enums zu definieren. Hier ist eine Methode namens `call`, die wir auf unserer `Message`-Enum definieren könnten:

```rust
impl Message {
    fn call(&self) {
      1 // method body would be defined here
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

Der Methodenkörper würde `self` verwenden, um den Wert zu erhalten, auf dem wir die Methode aufgerufen haben. In diesem Beispiel haben wir eine Variable `m` \[2\] erstellt, die den Wert `Message::Write(String::from("hello"))` hat, und das ist das, was `self` im Körper der `call`-Methode \[1\] sein wird, wenn `m.call()` ausgeführt wird.

Schauen wir uns eine weitere Enum in der Standardbibliothek an, die sehr üblich und nützlich ist: `Option`.
