# Das Einfangen der Umgebung mit Closures

Wir werden zunächst untersuchen, wie wir Closures verwenden können, um Werte aus der Umgebung, in der sie definiert sind, zu erfassen und später zu verwenden. Hier ist der Szenario: von Zeit zu Zeit gibt unsere T-Shirt-Firma einen exklusiven, begrenzt editierten Shirt an jemand aus unserer Mailingliste als Werbung aus. Personen auf der Mailingliste können optional ihre Lieblingsfarbe zu ihrem Profil hinzufügen. Wenn die Person, die für ein kostenloses Shirt ausgewählt wird, ihre Lieblingsfarbe angegeben hat, erhält sie das Shirt in dieser Farbe. Wenn die Person keine Lieblingsfarbe angegeben hat, erhält sie die Farbe, von der die Firma derzeit am meisten hat.

Es gibt viele Möglichkeiten, dies zu implementieren. Für dieses Beispiel werden wir eine Enumeration namens `ShirtColor` verwenden, die die Varianten `Red` und `Blue` hat (um die Anzahl der verfügbaren Farben zur Vereinfachung zu begrenzen). Wir repräsentieren den Vorrat der Firma mit einer Struktur `Inventory`, die ein Feld namens `shirts` hat, das ein `Vec<ShirtColor>` enthält, das die derzeit im Lager befindlichen Shirt-Farben darstellt. Die Methode `giveaway`, die auf `Inventory` definiert ist, erhält die optionale Shirt-Farben-Präferenz des Gewinners des kostenlosen Shirts und gibt die Shirt-Farbe zurück, die die Person erhält. Diese Einrichtung ist in Listing 13-1 gezeigt.

Dateiname: `src/main.rs`

```rust
#[derive(Debug, PartialEq, Copy, Clone)]
enum ShirtColor {
    Red,
    Blue,
}

struct Inventory {
    shirts: Vec<ShirtColor>,
}

impl Inventory {
    fn giveaway(
        &self,
        user_preference: Option<ShirtColor>,
    ) -> ShirtColor {
      1 user_preference.unwrap_or_else(|| self.most_stocked())
    }

    fn most_stocked(&self) -> ShirtColor {
        let mut num_red = 0;
        let mut num_blue = 0;

        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}

fn main() {
    let store = Inventory {
      2 shirts: vec![
            ShirtColor::Blue,
            ShirtColor::Red,
            ShirtColor::Blue,
        ],
    };

    let user_pref1 = Some(ShirtColor::Red);
  3 let giveaway1 = store.giveaway(user_pref1);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref1, giveaway1
    );

    let user_pref2 = None;
  4 let giveaway2 = store.giveaway(user_pref2);
    println!(
        "The user with preference {:?} gets {:?}",
        user_pref2, giveaway2
    );
}
```

Listing 13-1: Shirt-Firma-Gewinnspiel-Situation

Die `store`, die in `main` definiert ist, hat noch zwei blaue Shirts und ein rotes Shirt für diese begrenzt editierten Werbung übrig, die verteilt werden sollen \[2\]. Wir rufen die Methode `giveaway` für einen Benutzer auf, der eine Vorliebe für ein rotes Shirt hat \[3\] und für einen Benutzer ohne jede Vorliebe \[4\].

Wiederum könnte dieser Code auf viele Weise implementiert werden, und hier, um sich auf Closures zu konzentrieren, haben wir uns an Konzepte gehalten, die Sie bereits gelernt haben, außer für den Körper der `giveaway`-Methode, der einen Closure verwendet. In der `giveaway`-Methode erhalten wir die Benutzerpräferenz als Parameter vom Typ `Option<ShirtColor>` und rufen die Methode `unwrap_or_else` auf `user_preference` auf \[1\]. Die Methode `unwrap_or_else` auf `Option<T>` wird von der Standardbibliothek definiert. Sie nimmt ein Argument: einen Closure ohne Argumente, der einen Wert `T` zurückgibt (der gleiche Typ wie der in der `Some`-Variante von `Option<T>` gespeicherte Typ, in diesem Fall `ShirtColor`). Wenn die `Option<T>` die `Some`-Variante ist, gibt `unwrap_or_else` den Wert aus der `Some` zurück. Wenn die `Option<T>` die `None`-Variante ist, ruft `unwrap_or_else` den Closure auf und gibt den von dem Closure zurückgegebenen Wert zurück.

Wir geben den Closure-Ausdruck `|| self.most_stocked()` als Argument an `unwrap_or_else` an. Dies ist ein Closure, das keine Parameter selbst hat (wenn das Closure Parameter hätte, würden sie zwischen den beiden vertikalen Rohren erscheinen). Der Körper des Closures ruft `self.most_stocked()` auf. Wir definieren hier das Closure, und die Implementierung von `unwrap_or_else` wird das Closure später auswerten, wenn das Ergebnis benötigt wird.

Wenn Sie diesen Code ausführen, wird Folgendes ausgegeben:

```rust
The user with preference Some(Red) gets Red
The user with preference None gets Blue
```

Ein interessanter Aspekt hier ist, dass wir einen Closure übergeben haben, der `self.most_stocked()` auf der aktuellen `Inventory`-Instanz aufruft. Die Standardbibliothek musste nichts über die von uns definierten Typen `Inventory` oder `ShirtColor` oder die Logik wissen, die wir in diesem Szenario verwenden möchten. Das Closure fängt eine unveränderliche Referenz auf die `self` `Inventory`-Instanz ein und übergibt sie zusammen mit dem von uns angegebenen Code an die Methode `unwrap_or_else`. Funktionen hingegen können ihre Umgebung nicht auf diese Weise erfassen.
