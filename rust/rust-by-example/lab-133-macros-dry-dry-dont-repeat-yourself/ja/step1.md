# DRY（Don't Repeat Yourself）

マクロを使うことで、関数やテスト スートの共通部分を抽出して、DRY なコードを書くことができます。ここでは、`Vec<T>` 上の `+=`、`*=`、`-=` 演算子を実装してテストする例を示します。

```rust
use std::ops::{Add, Mul, Sub};

macro_rules! assert_equal_len {
    // `tt`（トークン ツリー）指定子は、演算子やトークンに使用されます。
    ($a:expr, $b:expr, $func:ident, $op:tt) => {
        assert!($a.len() == $b.len(),
                "{:?}: 次元の不一致: {:?} {:?} {:?}",
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

// `add_assign`、`mul_assign`、および `sub_assign` 関数を実装します。
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

    // `add_assign`、`mul_assign`、および `sub_assign` をテストします。
    test!(add_assign, 1u32, 2u32, 3u32);
    test!(mul_assign, 2u32, 3u32, 6u32);
    test!(sub_assign, 3u32, 2u32, 1u32);
}
```

```shell
$ rustc --test dry.rs && ./dry
running 3 tests
test test::mul_assign... ok
test test::add_assign... ok
test test::sub_assign... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
```
