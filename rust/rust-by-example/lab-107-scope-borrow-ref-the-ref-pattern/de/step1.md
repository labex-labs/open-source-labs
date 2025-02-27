# Das `ref`-Muster

Wenn Sie Mustermatching durchführen oder über die `let`-Bindung zerlegen, können Sie das Schlüsselwort `ref` verwenden, um Referenzen auf die Felder einer Struktur/Tupel zu erstellen. Im folgenden Beispiel werden einige Fälle gezeigt, in denen dies nützlich sein kann:

```rust
#[derive(Clone, Copy)]
struct Point { x: i32, y: i32 }

fn main() {
    let c = 'Q';

    // Ein `ref`-Borrow auf der linken Seite einer Zuweisung ist äquivalent zu
    // einem `&`-Borrow auf der rechten Seite.
    let ref ref_c1 = c;
    let ref_c2 = &c;

    println!("ref_c1 entspricht ref_c2: {}", *ref_c1 == *ref_c2);

    let point = Point { x: 0, y: 0 };

    // `ref` ist auch gültig, wenn eine Struktur zerlegt wird.
    let _copy_of_x = {
        // `ref_to_x` ist eine Referenz auf das `x`-Feld von `point`.
        let Point { x: ref ref_to_x, y: _ } = point;

        // Geben Sie eine Kopie des `x`-Felds von `point` zurück.
        *ref_to_x
    };

    // Eine mutable Kopie von `point`
    let mut mutable_point = point;

    {
        // `ref` kann mit `mut` kombiniert werden, um mutable Referenzen zu erstellen.
        let Point { x: _, y: ref mut mut_ref_to_y } = mutable_point;

        // Ändern Sie das `y`-Feld von `mutable_point` über eine mutable Referenz.
        *mut_ref_to_y = 1;
    }

    println!("point ist ({}, {})", point.x, point.y);
    println!("mutable_point ist ({}, {})", mutable_point.x, mutable_point.y);

    // Ein mutables Tupel, das einen Zeiger enthält
    let mut mutable_tuple = (Box::new(5u32), 3u32);

    {
        // Zerlegen Sie `mutable_tuple`, um den Wert von `last` zu ändern.
        let (_, ref mut last) = mutable_tuple;
        *last = 2u32;
    }

    println!("tuple ist {:?}", mutable_tuple);
}
```
