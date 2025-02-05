# 创建引用循环

让我们看看引用循环是如何发生的以及如何防止它，首先从清单15-25中`List`枚举的定义和`tail`方法开始。

文件名：`src/main.rs`

```rust
use crate::List::{Cons, Nil};
use std::cell::RefCell;
use std::rc::Rc;

#[derive(Debug)]
enum List {
    Cons(i32, RefCell<Rc<List>>),
    Nil,
}

impl List {
    fn tail(&self) -> Option<&RefCell<Rc<List>>> {
        match self {
            Cons(_, item) => Some(item),
            Nil => None,
        }
    }
}
```

清单15-25：一个cons列表定义，它持有一个`RefCell<T>`，这样我们就可以修改`Cons`变体所指向的内容

我们正在使用清单15-5中`List`定义的另一种变体。`Cons`变体中的第二个元素现在是`RefCell<Rc<List>>`\[1\]，这意味着我们不再像清单15-24中那样能够修改`i32`值，而是想要修改`Cons`变体所指向的`List`值。我们还添加了一个`tail`方法\[2\]，以便在我们有`Cons`变体时方便地访问第二个元素。

在清单15-26中，我们添加了一个`main`函数，它使用了清单15-25中的定义。这段代码在`a`中创建了一个列表，在`b`中创建了一个指向`a`中列表的列表。然后它将`a`中的列表修改为指向`b`，从而创建了一个引用循环。在这个过程中，有一些`println!`语句来显示在各个点上的引用计数是多少。

文件名：`src/main.rs`

```rust
fn main() {
    let a = Rc::new(Cons(5, RefCell::new(Rc::new(Nil))));

    println!("a initial rc count = {}", Rc::strong_count(&a));
    println!("a next item = {:?}", a.tail());

    let b = Rc::new(Cons(10, RefCell::new(Rc::clone(&a))));

    println!(
        "a rc count after b creation = {}",
        Rc::strong_count(&a)
    );
    println!("b initial rc count = {}", Rc::strong_count(&b));
    println!("b next item = {:?}", b.tail());

    if let Some(link) = a.tail() {
        *link.borrow_mut() = Rc::clone(&b);
    }

    println!(
        "b rc count after changing a = {}",
        Rc::strong_count(&b)
    );
    println!(
        "a rc count after changing a = {}",
        Rc::strong_count(&a)
    );

    // 取消注释下一行以查看我们有一个循环；
    // 它将使堆栈溢出
    // println!("a next item = {:?}", a.tail());
}
```

清单15-26：创建两个相互指向的`List`值的引用循环

我们在变量`a`中创建了一个持有`List`值的`Rc<List>`实例，其初始列表为`5, Nil`\[1\]。然后我们在变量`b`中创建了一个持有另一个`List`值的`Rc<List>`实例，该值包含`10`并指向`a`中的列表\[2\]。

我们修改`a`使其指向`b`而不是`Nil`，从而创建一个循环。我们通过使用`tail`方法获取对`a`中`RefCell<Rc<List>>`的引用，并将其放入变量`link`中来实现这一点\[3\]。然后我们对`RefCell<Rc<List>>`使用`borrow_mut`方法，将其中的值从持有`Nil`值的`Rc<List>`更改为`b`中的`Rc<List>`\[4\]。

当我们运行这段代码时，暂时保留最后一个`println!`注释，我们将得到以下输出：

    a initial rc count = 1
    a next item = Some(RefCell { value: Nil })
    a rc count after b creation = 2
    b initial rc count = 1
    b next item = Some(RefCell { value: Cons(5, RefCell { value: Nil }) })
    b rc count after changing a = 2
    a rc count after changing a = 2

在我们将`a`中的列表修改为指向`b`之后，`a`和`b`中`Rc<List>`实例的引用计数都为2。在`main`函数结束时，Rust会丢弃变量`b`，这会将`b`的`Rc<List>`实例的引用计数从2减为1。此时，`Rc<List>`在堆上的内存不会被释放，因为其引用计数是1而不是0。然后Rust会丢弃`a`，这也会将`a`的`Rc<List>`实例的引用计数从2减为1。这个实例的内存也无法被释放，因为另一个`Rc<List>`实例仍然引用它。分配给列表的内存将永远不会被回收。为了直观地展示这个引用循环，我们在图15-4中创建了一个示意图。

图15-4：列表`a`和`b`相互指向的引用循环

如果你取消注释最后一个`println!`并运行程序，Rust将尝试打印这个循环，其中`a`指向`b`，`b`又指向`a`，依此类推，直到堆栈溢出。

与实际程序相比，在这个示例中创建引用循环的后果并不是非常严重：在我们创建引用循环之后，程序就结束了。然而，如果一个更复杂的程序在循环中分配了大量内存并长时间持有它，那么程序将使用比所需更多的内存，可能会使系统不堪重负，导致可用内存耗尽。

创建引用循环并不容易，但也不是不可能。如果你有包含`Rc<T>`值的`RefCell<T>`值或类似的具有内部可变性和引用计数的嵌套类型组合，你必须确保不创建循环；你不能依赖Rust来捕获它们。创建引用循环将是你程序中的一个逻辑错误，你应该使用自动化测试、代码审查和其他软件开发实践来尽量减少这种情况。

另一种避免引用循环的解决方案是重新组织你的数据结构，使一些引用表示所有权，而一些引用不表示所有权。结果，你可以有由一些所有权关系和一些非所有权关系组成的循环，并且只有所有权关系会影响一个值是否可以被释放。在清单15-25中，我们总是希望`Cons`变体拥有它们的列表，所以重新组织数据结构是不可能的。让我们看一个使用由父节点和子节点组成的图的示例，看看非所有权关系何时是防止引用循环的合适方法。
