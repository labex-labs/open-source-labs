# DRY（不要重复自己）

宏允许通过提取函数和/或测试套件的公共部分来编写DRY代码。以下是一个在 `Vec<T>` 上实现并测试 `+=`、`*=` 和 `-=` 运算符的示例：

```rust
use std::ops::{Add, Mul, Sub};

macro_rules! assert_equal_len {
    // `tt`（标记树）指示符用于
    // 运算符和标记。
    ($a:expr, $b:expr, $func:ident, $op:tt) => {
        assert!($a.len() == $b.len(),
                "{:?}: 维度不匹配: {:?} {:?} {:?}",
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

// 实现 `add_assign`、`mul_assign` 和 `sub_assign` 函数。
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

    // 测试 `add_assign`、`mul_assign` 和 `sub_assign`。
    test!(add_assign, 1u32, 2u32, 3u32);
    test!(mul_assign, 2u32, 3u32, 6u32);
    test!(sub_assign, 3u32, 2u32, 1u32);
}
```

```shell
$ rustc --test dry.rs && ./dry
运行 3 个测试
测试 test::mul_assign... 通过
测试 test::add_assign... 通过
测试 test::sub_assign... 通过

测试结果：通过。3 个通过
0 个失败
0 个忽略
0 个测量
```
