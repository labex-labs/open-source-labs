# Typumwandlung

Rust bietet keine implizite Typumwandlung (Kohäsion) zwischen primitiven Typen. Es ist jedoch möglich, explizite Typumwandlungen mit dem Schlüsselwort `as` durchzuführen.

Die Regeln für die Umwandlung zwischen ganzzahligen Typen folgen im Allgemeinen den C-Konventionen, Ausnahmen sind Fälle, in denen C undefiniertes Verhalten aufweist. Das Verhalten aller Umwandlungen zwischen ganzzahligen Typen ist in Rust gut definiert.

```rust
// Unterdrücke alle Warnungen von Umwandlungen, die einen Überlauf verursachen.
#![allow(overflowing_literals)]

fn main() {
    let dezimal = 65.4321_f32;

    // Fehler! Keine implizite Umwandlung
    let ganzzahl: u8 = dezimal;
    // FIXME ^ Kommentiere diese Zeile aus

    // Explizite Umwandlung
    let ganzzahl = dezimal as u8;
    let zeichen = ganzzahl as char;

    // Fehler! Es gibt Einschränkungen in den Umwandlungsregeln.
    // Ein Float kann nicht direkt in ein Zeichen umgewandelt werden.
    let zeichen = dezimal as char;
    // FIXME ^ Kommentiere diese Zeile aus

    println!("Typumwandlung: {} -> {} -> {}", dezimal, ganzzahl, zeichen);

    // Wenn eine beliebige Zahl in einen unsigned-Typ, T, umgewandelt wird,
    // wird T::MAX + 1 addiert oder subtrahiert, bis der Wert
    // in den neuen Typ passt

    // 1000 passt bereits in ein u16
    println!("1000 als u16 ist: {}", 1000 as u16);

    // 1000 - 256 - 256 - 256 = 232
    // Im Hintergrund werden die ersten 8 am wenigsten signifikanten Bits (LSB) beibehalten,
    // während der Rest bis zum am meisten signifikanten Bit (MSB) abgeschnitten wird.
    println!("1000 als u8 ist : {}", 1000 as u8);
    // -1 + 256 = 255
    println!("  -1 als u8 ist : {}", (-1i8) as u8);

    // Für positive Zahlen ist dies das Gleiche wie der Modulo
    println!("1000 mod 256 ist : {}", 1000 % 256);

    // Wenn in einen vorzeichenbehafteten Typ umgewandelt wird, ist das (bitweise) Ergebnis dasselbe wie
    // zunächst in den entsprechenden unsigned-Typ umzuwandeln. Wenn das am meisten signifikante
    // Bit dieses Werts 1 ist, ist der Wert negativ.

    // Es sei denn, es passt bereits, natürlich.
    println!(" 128 als i16 ist: {}", 128 as i16);

    // Im Grenzfall ist der Wert 128 in der 8-Bit-Zweierkomplement-Darstellung -128
    println!(" 128 als i8 ist : {}", 128 as i8);

    // Wiederholen des obigen Beispiels
    // 1000 als u8 -> 232
    println!("1000 als u8 ist : {}", 1000 as u8);
    // und der Wert von 232 in der 8-Bit-Zweierkomplement-Darstellung ist -24
    println!(" 232 als i8 ist : {}", 232 as i8);

    // Seit Rust 1.45 führt das Schlüsselwort `as` eine *sättigende Umwandlung* durch
    // beim Casten von Float zu Int. Wenn der Gleitkomma-Wert den oberen Grenzwert überschreitet oder
    // kleiner als der untere Grenzwert ist, ist der zurückgegebene Wert
    // gleich dem überschrittenen Grenzwert.

    // 300.0 als u8 ist 255
    println!(" 300.0 als u8 ist : {}", 300.0_f32 as u8);
    // -100.0 als u8 ist 0
    println!("-100.0 als u8 ist : {}", -100.0_f32 as u8);
    // nan als u8 ist 0
    println!("   nan als u8 ist : {}", f32::NAN as u8);

    // Dieses Verhalten verursacht geringe Laufzeitkosten und kann vermieden werden
    // mit unsicheren Methoden, jedoch können die Ergebnisse überlaufen und
    // **unsichere Werte** zurückgeben. Verwenden Sie diese Methoden mit Vorsicht:
    unsafe {
        // 300.0 als u8 ist 44
        println!(" 300.0 als u8 ist : {}", 300.0_f32.to_int_unchecked::<u8>());
        // -100.0 als u8 ist 156
        println!("-100.0 als u8 ist : {}", (-100.0_f32).to_int_unchecked::<u8>());
        // nan als u8 ist 0
        println!("   nan als u8 ist : {}", f32::NAN.to_int_unchecked::<u8>());
    }
}
```
