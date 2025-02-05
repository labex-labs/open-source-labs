# 冻结

当数据通过相同名称被不可变地绑定时，它也会被“冻结”。在不可变绑定超出作用域之前，“冻结”的数据无法被修改：

```rust
fn main() {
    let mut _mutable_integer = 7i32;

    {
        // 由不可变的 `_mutable_integer` 进行遮蔽
        let _mutable_integer = _mutable_integer;

        // 错误！`_mutable_integer` 在这个作用域中被冻结
        _mutable_integer = 50;
        // FIXME ^ 注释掉这一行

        // `_mutable_integer` 超出作用域
    }

    // 可以！`_mutable_integer` 在这个作用域中没有被冻结
    _mutable_integer = 3;
}
```
