# Kapselung, die Implementierungsdetails versteckt

Ein weiteres Aspekt, das häufig mit der OOP assoziiert wird, ist das Konzept der _Kapselung_, was bedeutet, dass die Implementierungsdetails eines Objekts nicht für den Code zugänglich sind, der dieses Objekt verwendet. Daher ist die einzige Möglichkeit, mit einem Objekt zu interagieren, über seine öffentliche Schnittstelle; der Code, der das Objekt verwendet, sollte nicht in das Innere des Objekts eindringen und Daten oder Verhalten direkt ändern können. Dies ermöglicht es dem Programmierer, die internen Details eines Objekts zu ändern und umzuschreiben, ohne dass der Code, der das Objekt verwendet, geändert werden muss.

Wir haben in Kapitel 7 diskutiert, wie die Kapselung kontrolliert werden kann: Wir können das Schlüsselwort `pub` verwenden, um zu bestimmen, welche Module, Typen, Funktionen und Methoden in unserem Code öffentlich sein sollten, und standardmäßig ist alles andere privat. Beispielsweise können wir eine Struktur `AveragedCollection` definieren, die ein Feld enthält, das einen Vektor von `i32` -Werten enthält. Die Struktur kann auch ein Feld haben, das den Durchschnitt der Werte im Vektor enthält, was bedeutet, dass der Durchschnitt nicht jedes Mal berechnet werden muss, wenn jemand ihn benötigt. Mit anderen Worten, `AveragedCollection` wird den berechneten Durchschnitt für uns zwischenspeichern. Listing 17-1 zeigt die Definition der `AveragedCollection` -Struktur.

Dateiname: `src/lib.rs`

```rust
pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}
```

Listing 17-1: Eine `AveragedCollection` -Struktur, die eine Liste von ganzen Zahlen und den Durchschnitt der Elemente in der Sammlung aufbewahrt

Die Struktur ist als `pub` markiert, sodass anderer Code sie verwenden kann, aber die Felder innerhalb der Struktur bleiben privat. Dies ist in diesem Fall wichtig, weil wir sicherstellen möchten, dass jederzeit, wenn ein Wert zur Liste hinzugefügt oder entfernt wird, auch der Durchschnitt aktualisiert wird. Wir tun dies, indem wir `add`, `remove` und `average` -Methoden auf der Struktur implementieren, wie in Listing 17-2 gezeigt.

Dateiname: `src/lib.rs`

```rust
impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}
```

Listing 17-2: Implementierungen der öffentlichen Methoden `add`, `remove` und `average` auf `AveragedCollection`

Die öffentlichen Methoden `add`, `remove` und `average` sind die einzigen Wege, um auf Daten in einer Instanz von `AveragedCollection` zuzugreifen oder zu modifizieren. Wenn ein Element der `list` mit der `add` -Methode hinzugefügt oder mit der `remove` -Methode entfernt wird, rufen die Implementierungen jeder die private `update_average` -Methode auf, die auch die Aktualisierung des `average` -Felds übernimmt.

Wir lassen die Felder `list` und `average` privat, sodass es keinem externen Code möglich ist, direkt Elemente zur `list` -Liste hinzuzufügen oder zu entfernen; andernfalls könnte das `average` -Feld möglicherweise unzugleich bleiben, wenn sich die `list` ändert. Die `average` -Methode gibt den Wert im `average` -Feld zurück, was es externen Code ermöglicht, den `average` zu lesen, aber nicht zu modifizieren.

Da wir die Implementierungsdetails der Struktur `AveragedCollection` kapselt haben, können wir in Zukunft leicht Aspekte wie die Datenstruktur ändern. Beispielsweise könnten wir für das `list` -Feld ein `HashSet<i32>` anstelle eines `Vec<i32>` verwenden. Solange die Signaturen der öffentlichen Methoden `add`, `remove` und `average` gleich blieben, müsste der Code, der `AveragedCollection` verwendet, nicht geändert werden. Wenn wir `list` stattdessen als öffentlich gemacht hätten, wäre dies nicht unbedingt der Fall: `HashSet<i32>` und `Vec<i32>` haben unterschiedliche Methoden zum Hinzufügen und Entfernen von Elementen, sodass der externe Code wahrscheinlich geändert werden müsste, wenn er direkt `list` modifizierte.

Wenn die Kapselung ein erforderlicher Aspekt für eine Sprache ist, um als objektorientiert angesehen zu werden, dann erfüllt Rust diese Anforderung. Die Möglichkeit, `pub` für verschiedene Teile des Codes zu verwenden oder nicht, ermöglicht die Kapselung von Implementierungsdetails.
