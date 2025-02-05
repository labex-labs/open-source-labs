# 指针/引用

对于指针，需要区分解构（destructuring）和解引用（dereferencing），因为它们是不同的概念，其使用方式与C/C++等语言不同。

- 解引用使用`*`
- 解构使用`&`、`ref`和`ref mut`

```rust
fn main() {
    // 分配一个`i32`类型的引用。`&`表示正在分配一个引用。
    let reference = &4;

    match reference {
        // 如果`reference`与`&val`进行模式匹配，结果类似于：
        // `&i32`
        // `&val`
        // ^ 我们可以看到，如果去掉匹配的`&`，那么`i32`应该被赋给`val`。
        &val => println!("通过解构获取到一个值: {:?}", val),
    }

    // 为了避免使用`&`，你可以在匹配之前进行解引用。
    match *reference {
        val => println!("通过解引用获取到一个值: {:?}", val),
    }

    // 如果你一开始没有使用引用会怎样呢？`reference`是一个`&`
    // 因为右边已经是一个引用了。这里不是引用，因为右边不是。
    let _not_a_reference = 3;

    // Rust提供`ref`正是为了这个目的。它修改了赋值，以便为元素创建一个引用；这个引用被赋值。
    let ref _is_a_reference = 3;

    // 相应地，通过定义两个没有引用的值，可以通过`ref`和`ref mut`获取引用。
    let value = 5;
    let mut mut_value = 6;

    // 使用`ref`关键字创建一个引用。
    match value {
        ref r => println!("获取到一个指向值的引用: {:?}", r),
    }

    // 类似地使用`ref mut`。
    match mut_value {
        ref mut m => {
            // 获取到一个引用。在对其进行任何操作之前，我们必须先解引用。
            *m += 10;
            println!("我们加了10。`mut_value`: {:?}", m);
        },
    }
}
```
