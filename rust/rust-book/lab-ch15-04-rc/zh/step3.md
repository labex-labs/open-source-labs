# 克隆 Rc`<T>` 会增加引用计数

让我们修改清单 15-18 中的示例代码，以便我们可以看到在创建和丢弃对 `a` 中 `Rc<List>` 的引用时引用计数的变化情况。

在清单 15-19 中，我们将修改 `main` 函数，使其在链表 `c` 周围有一个内部作用域；这样我们就可以看到当 `c` 超出作用域时引用计数是如何变化的。

文件名：`src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

清单 15-19：打印引用计数

在程序中引用计数发生变化的每个点，我们都会打印引用计数，这是通过调用 `Rc::strong_count` 函数获得的。这个函数被命名为 `strong_count` 而不是 `count`，是因为 `Rc<T>` 类型还有一个 `weak_count`；我们将在“使用 Weak`<T>` 防止引用循环”中看到 `weak_count` 的用途。

这段代码会输出以下内容：

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

我们可以看到 `a` 中的 `Rc<List>` 初始引用计数为 1；然后每次我们调用 `clone`，计数就会增加 1。当 `c` 超出作用域时，计数就会减少 1。我们不需要像调用 `Rc::clone` 来增加引用计数那样调用一个函数来减少引用计数：当一个 `Rc<T>` 值超出作用域时，`Drop` 特性的实现会自动减少引用计数。

在这个示例中我们看不到的是，当 `b` 然后是 `a` 在 `main` 函数结束时超出作用域时，计数变为 0，并且 `Rc<List>` 会被完全清理。使用 `Rc<T>` 允许一个值有多个所有者，并且计数确保只要有任何一个所有者仍然存在，该值就仍然有效。

通过不可变引用，`Rc<T>` 允许你在程序的多个部分之间只读共享数据。如果 `Rc<T>` 也允许你有多个可变引用，那么你可能会违反第 4 章中讨论的一条借用规则：对同一位置的多个可变借用可能会导致数据竞争和不一致。但是能够修改数据是非常有用的！在下一节中，我们将讨论内部可变性模式以及可以与 `Rc<T>` 一起使用以处理这种不可变性限制的 `RefCell<T>` 类型。
