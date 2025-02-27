# DRY (Don't Repeat Yourself)

Las macros permiten escribir código DRY extrayendo las partes comunes de funciones y/o suites de pruebas. Aquí hay un ejemplo que implementa y prueba los operadores `+=`, `*=` y `-=` en `Vec<T>`:

```rust
use std::ops::{Add, Mul, Sub};

macro_rules! assert_equal_len {
    // El designador `tt` (árbol de tokens) se utiliza para
    // operadores y tokens.
    ($a:expr, $b:expr, $func:ident, $op:tt) => {
        assert!($a.len() == $b.len(),
                "{:?}: error de dimensión: {:?} {:?} {:?}",
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

// Implementa las funciones `add_assign`, `mul_assign` y `sub_assign`.
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

    // Prueba `add_assign`, `mul_assign` y `sub_assign`.
    test!(add_assign, 1u32, 2u32, 3u32);
    test!(mul_assign, 2u32, 3u32, 6u32);
    test!(sub_assign, 3u32, 2u32, 1u32);
}
```

```shell
$ rustc --test dry.rs && ./dry
ejecutando 3 pruebas
test test::mul_assign... ok
test test::add_assign... ok
test test::sub_assign... ok

resultado de las pruebas: ok. 3 pasadas
0 fallidas
0 ignoradas
0 medidas
```
