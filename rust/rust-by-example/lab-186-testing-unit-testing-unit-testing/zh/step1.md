# 单元测试

测试是 Rust 函数，用于验证非测试代码是否按预期方式运行。测试函数的主体通常会执行一些设置，运行我们想要测试的代码，然后断言结果是否符合预期。

大多数单元测试会放在带有 `#[cfg(test)]` 属性的 `tests` 模块中。测试函数用 `#[test]` 属性进行标记。

当测试函数中的某些内容导致程序恐慌（panic）时，测试就会失败。有一些辅助宏：

- `assert!(expression)` - 如果表达式求值为 `false`，则会导致程序恐慌。
- `assert_eq!(left, right)` 和 `assert_ne!(left, right)` - 分别用于测试左右表达式是否相等和不相等。

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

// 这是一个非常糟糕的加法函数，其目的是在这个例子中失败。
#[allow(dead_code)]
fn bad_add(a: i32, b: i32) -> i32 {
    a - b
}

#[cfg(test)]
mod tests {
    // 注意这个有用的习惯用法：从外部（对于模块测试）作用域导入名称。
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

    #[test]
    fn test_bad_add() {
        // 这个断言会触发，测试将失败。
        // 请注意，私有函数也可以被测试！
        assert_eq!(bad_add(1, 2), 3);
    }
}
```

可以使用 `cargo test` 来运行测试。

```shell
$ cargo test

running 2 tests
test tests::test_bad_add... FAILED
test tests::test_add... ok

failures:

---- tests::test_bad_add stdout ----
thread 'tests::test_bad_add' panicked at 'assertion failed: `(left == right)`
  left: `-1`,
 right: `3`', src/lib.rs:21:8
note: Run with $(RUST_BACKTRACE=1) for a backtrace.

failures:
tests::test_bad_add

test result: FAILED. 1 passed
1 failed
0 ignored
0 measured
0 filtered out
```

## 测试与 `?`

之前的单元测试示例都没有返回类型。但在 Rust 2018 中，你的单元测试可以返回 `Result<()>`，这使得你可以在测试中使用 `?` 运算符！这可以使测试更加简洁。

```rust
fn sqrt(number: f64) -> Result<f64, String> {
    if number >= 0.0 {
        Ok(number.powf(0.5))
    } else {
        Err("negative floats don't have square roots".to_owned())
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_sqrt() -> Result<(), String> {
        let x = 4.0;
        assert_eq!(sqrt(x)?.powf(2.0), x);
        Ok(())
    }
}
```

更多细节请参考《版本指南》。

## 测试恐慌情况

要检查在某些情况下应该恐慌的函数，可以使用 `#[should_panic]` 属性。这个属性接受一个可选参数 `expected =`，后面跟着恐慌消息的文本。如果你的函数可能以多种方式恐慌，这有助于确保你的测试正在测试正确的恐慌情况。

```rust
pub fn divide_non_zero_result(a: u32, b: u32) -> u32 {
    if b == 0 {
        panic!("Divide-by-zero error");
    } else if a < b {
        panic!("Divide result is zero");
    }
    a / b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_divide() {
        assert_eq!(divide_non_zero_result(10, 2), 5);
    }

    #[test]
    #[should_panic]
    fn test_any_panic() {
        divide_non_zero_result(1, 0);
    }

    #[test]
    #[should_panic(expected = "Divide result is zero")]
    fn test_specific_panic() {
        divide_non_zero_result(1, 10);
    }
}
```

运行这些测试会得到：

```shell
$ cargo test

running 3 tests
test tests::test_any_panic... ok
test tests::test_divide... ok
test tests::test_specific_panic... ok

test result: ok. 3 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## 运行特定测试

要运行特定的测试，可以在 `cargo test` 命令中指定测试名称。

```shell
$ cargo test test_any_panic
running 1 test
test tests::test_any_panic... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
2 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

要运行多个测试，可以指定测试名称的一部分，使其与所有要运行的测试匹配。

```shell
$ cargo test panic
running 2 tests
test tests::test_any_panic... ok
test tests::test_specific_panic... ok

test result: ok. 2 passed
0 failed
0 ignored
0 measured
1 filtered out

Doc-tests tmp-test-should-panic

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```

## 忽略测试

可以使用 `#[ignore]` 属性标记测试，以排除某些测试。或者使用命令 `cargo test -- --ignored` 来运行它们。

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(2, 2), 4);
    }

    #[test]
    fn test_add_hundred() {
        assert_eq!(add(100, 2), 102);
        assert_eq!(add(2, 100), 102);
    }

    #[test]
    #[ignore]
    fn ignored_test() {
        assert_eq!(add(0, 0), 0);
    }
}
```

```shell
$ cargo test
running 3 tests
test tests::ignored_test... ignored
test tests::test_add... ok
test tests::test_add_hundred... ok

test result: ok. 2 passed
0 failed
1 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out

$ cargo test -- --ignored
running 1 test
test tests::ignored_test... ok

test result: ok. 1 passed
0 failed
0 ignored
0 measured
0 filtered out

Doc-tests tmp-ignore

running 0 tests

test result: ok. 0 passed
0 failed
0 ignored
0 measured
0 filtered out
```
