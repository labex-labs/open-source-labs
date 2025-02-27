# Exportieren einer bequemen öffentlichen API mit `pub use`

Die Struktur Ihrer öffentlichen API ist ein wichtiger Aspekt, wenn Sie eine Crate veröffentlichen. Personen, die Ihre Crate verwenden, sind weniger vertraut mit der Struktur als Sie und können Schwierigkeiten haben, die Elemente zu finden, die sie verwenden möchten, wenn Ihre Crate eine große Modulhierarchie hat.

Im siebten Kapitel haben wir behandelt, wie man Elemente öffentlich macht, indem man das Schlüsselwort `pub` verwendet, und wie man Elemente in einen Gültigkeitsbereich bringt, indem man das Schlüsselwort `use` verwendet. Die Struktur, die Ihnen während der Entwicklung einer Crate sinnvoll erscheint, kann jedoch für Ihre Benutzer nicht sehr bequem sein. Sie möchten möglicherweise Ihre Structs in einer Hierarchie mit mehreren Ebenen organisieren, aber dann können Personen, die einen Typ verwenden möchten, den Sie tief in der Hierarchie definiert haben, Schwierigkeiten haben, herauszufinden, dass dieser Typ existiert. Sie können auch ärgerlich darüber sein, dass sie `use my_crate::some_module::another_module::UsefulType;` statt `use my_crate::UsefulType;` eingeben müssen.

Die gute Nachricht ist, dass Sie nicht umorganisieren müssen, wenn die Struktur für andere unbrauchbar ist: Stattdessen können Sie Elemente erneut exportieren, um eine öffentliche Struktur zu erstellen, die von Ihrer privaten Struktur unterschiedlich ist, indem Sie `pub use` verwenden. _Neuexportieren_ nimmt ein öffentliches Element an einem Ort und macht es an einem anderen Ort öffentlich, als wäre es dort definiert.

Nehmen wir beispielsweise an, dass wir eine Bibliothek namens `art` für die Modellierung künstlerischer Konzepte erstellt haben. Innerhalb dieser Bibliothek befinden sich zwei Module: Ein `kinds`-Modul, das zwei Enums namens `PrimaryColor` und `SecondaryColor` enthält, und ein `utils`-Modul, das eine Funktion namens `mix` enthält, wie in Listing 14-3 gezeigt.

Dateiname: `src/lib.rs`

```rust
//! # Kunst
//!
//! Eine Bibliothek zur Modellierung künstlerischer Konzepte.

pub mod kinds {
    /// Die primären Farben gemäß dem RYB-Farbmodell.
    pub enum PrimaryColor {
        Rot,
        Gelb,
        Blau,
    }

    /// Die sekundären Farben gemäß dem RYB-Farbmodell.
    pub enum SecondaryColor {
        Orange,
        Grün,
        Lila,
    }
}

pub mod utils {
    use crate::kinds::*;

    /// Kombiniert zwei primäre Farben in gleichen Mengen, um
    /// eine sekundäre Farbe zu erzeugen.
    pub fn mix(
        c1: PrimaryColor,
        c2: PrimaryColor,
    ) -> SecondaryColor {
        --snip--
    }
}
```

Listing 14-3: Eine `art`-Bibliothek mit Elementen, die in die Module `kinds` und `utils` organisiert sind

Abbildung 14-3 zeigt, wie die Titelseite der Dokumentation für diese Crate, die von `cargo doc` generiert wird, aussehen würde.

Abbildung 14-3: Titelseite der Dokumentation für `art`, die die Module `kinds` und `utils` auflistet

Beachten Sie, dass die Typen `PrimaryColor` und `SecondaryColor` sowie die Funktion `mix` nicht auf der Titelseite aufgelistet sind. Wir müssen auf `kinds` und `utils` klicken, um sie zu sehen.

Eine andere Crate, die von dieser Bibliothek abhängt, würde `use`-Anweisungen benötigen, die die Elemente aus `art` in den Gültigkeitsbereich bringen und die derzeit definierte Modulstruktur angeben. Listing 14-4 zeigt ein Beispiel einer Crate, die die Elemente `PrimaryColor` und `mix` aus der `art`-Crate verwendet.

Dateiname: `src/main.rs`

```rust
use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let rot = PrimaryColor::Rot;
    let gelb = PrimaryColor::Gelb;
    mix(rot, gelb);
}
```

Listing 14-4: Eine Crate, die die Elemente der `art`-Crate mit ihrer exportierten internen Struktur verwendet

Der Autor des Codes in Listing 14-4, der die `art`-Crate verwendet, musste herausfinden, dass `PrimaryColor` im `kinds`-Modul und `mix` im `utils`-Modul ist. Die Modulstruktur der `art`-Crate ist für Entwickler, die an der `art`-Crate arbeiten, relevanter als für diejenigen, die sie verwenden. Die interne Struktur enthält keine nützlichen Informationen für jemanden, der verstehen möchte, wie man die `art`-Crate verwendet, sondern verursacht eher Verwirrung, da Entwickler, die sie verwenden, herausfinden müssen, wo sie nachzusehen ist und die Modulnamen in den `use`-Anweisungen angeben müssen.

Um die interne Organisation aus der öffentlichen API zu entfernen, können wir den Code der `art`-Crate in Listing 14-3 ändern, um `pub use`-Anweisungen hinzuzufügen, um die Elemente auf der obersten Ebene erneut zu exportieren, wie in Listing 14-5 gezeigt.

Dateiname: `src/lib.rs`

```rust
//! # Kunst
//!
//! Eine Bibliothek zur Modellierung künstlerischer Konzepte.

pub use self::kinds::PrimaryColor;
pub use self::kinds::SecondaryColor;
pub use self::utils::mix;

pub mod kinds {
    --snip--
}

pub mod utils {
    --snip--
}
```

Listing 14-5: Hinzufügen von `pub use`-Anweisungen, um Elemente erneut zu exportieren

Die API-Dokumentation, die `cargo doc` für diese Crate generiert, wird jetzt die Neuerweiterungen auf der Titelseite auflisten und verlinken, wie in Abbildung 14-4 gezeigt, was es einfacher macht, die Typen `PrimaryColor` und `SecondaryColor` sowie die Funktion `mix` zu finden.

Abbildung 14-4: Die Titelseite der Dokumentation für `art`, die die Neuerweiterungen auflistet

Die Benutzer der `art`-Crate können immer noch die interne Struktur aus Listing 14-3 sehen und verwenden, wie in Listing 14-4 gezeigt, oder sie können die bequemere Struktur in Listing 14-5 verwenden, wie in Listing 14-6 gezeigt.

Dateiname: `src/main.rs`

```rust
use art::mix;
use art::PrimaryColor;

fn main() {
    --snip--
}
```

Listing 14-6: Ein Programm, das die erneut exportierten Elemente der `art`-Crate verwendet

In Fällen mit vielen geschachtelten Modulen kann das Neuerweitern der Typen auf der obersten Ebene mit `pub use` einen großen Unterschied im Benutzererlebnis machen. Ein weiterer häufiger Gebrauch von `pub use` ist es, die Definitionen einer Abhängigkeit in der aktuellen Crate erneut zu exportieren, um die Definitionen dieser Crate zum öffentlichen API Ihrer Crate zu machen.

Das Erstellen einer nützlichen öffentlichen API-Struktur ist eher eine Kunst als eine Wissenschaft, und Sie können iterieren, um die API zu finden, die am besten für Ihre Benutzer funktioniert. Die Verwendung von `pub use` gibt Ihnen Flexibilität bei der internen Strukturierung Ihrer Crate und trennt diese interne Struktur von der, die Sie Ihren Benutzern präsentieren. Schauen Sie sich den Code einiger von den Crates an, die Sie installiert haben, um zu sehen, ob ihre interne Struktur von ihrer öffentlichen API unterschiedlich ist.
