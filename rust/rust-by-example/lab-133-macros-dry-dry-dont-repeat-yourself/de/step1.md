# DRY (Don't Repeat Yourself)

Makros ermöglichen es, DRY-Code zu schreiben, indem man die gemeinsamen Teile von Funktionen und/oder Testsuite extrahiert. Hier ist ein Beispiel, das die Operatoren `+=`, `*=` und `-=` auf `Vec<T>` implementiert und testet:

```rust
use std::ops::{Add, Mul, Sub};

macro_rules! assert_equal_len {
    // Der Designator `tt` (Tokenbaum) wird für
    // Operatoren und Tokens verwendet.
    ($a:expr, $b:expr, $func:ident, $op:tt) => {
        assert!($a.len() == $b.len(),
                "{:?}: Dimensionenunterschied: {:?} {:?} {:?}",
                stringify!($func),
                ($a.len(),),
                stringify!($op),
                ($b.len(),));
    };
}

macro_rules! op {
    ($func:ident, $bound:ident, $op:tt, $method:ident) => {
        fn $func<T: $bound<T, Output=T> + Copy>(xs: &mut Vec<T>, ys: &Vec<T>) {
            assert_equal_len!(xs, ys, $func, $op);

            for (x, y) in xs.iter_mut().zip(ys.iter()) {
                *x = $bound::$method(*x, *y);
                // *x = x.$method(*y);
            }
        }
    };
}

// Implementiere die Funktionen `add_assign`, `mul_assign` und `sub_assign`.
op!(add_assign, Add, +=, add);
op!(mul_assign, Mul, *=, mul);
op!(sub_assign, Sub, -=, sub);

mod test {
    use std::iter;
    macro_rules! test {
        ($func:ident, $x:expr, $y:expr, $z:expr) => {
            #[test]
            fn $func() {
                for size in 0usize..10 {
                    let mut x: Vec<_> = iter::repeat($x).take(size).collect();
                    let y: Vec<_> = iter::repeat($y).take(size).collect();
                    let z: Vec<_> = iter::repeat($z).take(size).collect();

                    super::$func(&mut x, &y);

                    assert_eq!(x, z);
                }
            }
        };
    }

    // Teste `add_assign`, `mul_assign` und `sub_assign`.
    test!(add_assign, 1u32, 2u32, 3u32);
    test!(mul_assign, 2u32, 3u32, 6u32);
    test!(sub_assign, 3u32, 2u32, 1u32);
}
```

```shell
$ rustc --test dry.rs && ./dry
läuft 3 Tests
test test::mul_assign... ok
test test::add_assign... ok
test test::sub_assign... ok

Testresultat: ok. 3 erfolgreich
0 fehlgeschlagen
0 ignoriert
0 gemessen
```
