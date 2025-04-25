# 通过提取函数消除重复

泛型允许我们用一个代表多种类型的占位符来替换特定类型，从而消除代码重复。在深入探讨泛型语法之前，让我们先看看如何通过提取一个函数来消除重复，该函数用一个代表多个值的占位符来替换特定值，而不涉及泛型类型。然后我们将应用相同的技术来提取一个泛型函数！通过了解如何识别可以提取到函数中的重复代码，你将开始识别可以使用泛型的重复代码。

我们将从清单 10-1 中的简短程序开始，该程序用于在列表中找到最大的数字。

文件名：`src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

清单 10-1：在数字列表中找到最大的数字

我们将整数列表存储在变量`number_list`中\[1\]，并将列表中第一个数字的引用存储在名为`largest`的变量中\[2\]。然后我们遍历列表中的所有数字\[3\]，如果当前数字大于存储在`largest`中的数字\[4\]，我们就替换该变量中的引用\[5\]。但是，如果当前数字小于或等于到目前为止看到的最大数字，变量不会改变，代码会继续处理列表中的下一个数字。在考虑了列表中的所有数字之后，`largest`应该指向最大的数字，在这种情况下是 100。

现在我们的任务是在两个不同的数字列表中找到最大的数字。为此，我们可以选择复制清单 10-1 中的代码，并在程序的两个不同位置使用相同的逻辑，如清单 10-2 所示。

文件名：`src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("The largest number is {largest}");
}
```

清单 10-2：在两个数字列表中找到最大数字的代码

虽然这段代码可以工作，但复制代码既繁琐又容易出错。当我们想要更改代码时，还必须记住在多个地方进行更新。

为了消除这种重复，我们将通过定义一个对作为参数传入的任何整数列表进行操作的函数来创建一个抽象。这个解决方案使我们的代码更清晰，并让我们能够抽象地表达在列表中找到最大数字的概念。

在清单 10-3 中，我们将找到最大数字的代码提取到一个名为`largest`的函数中。然后我们调用该函数来找到清单 10-2 中两个列表中的最大数字。我们也可以在未来可能拥有的任何其他`i32`值列表上使用该函数。

文件名：`src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("The largest number is {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("The largest number is {result}");
}
```

清单 10-3：在两个列表中找到最大数字的抽象代码

`largest`函数有一个名为`list`的参数，它代表我们可能传入函数的任何具体的`i32`值切片。因此，当我们调用该函数时，代码会在我们传入的特定值上运行。

总结一下，我们将代码从清单 10-2 更改为清单 10-3 所采取的步骤如下：

1. 识别重复代码。
2. 将重复代码提取到函数体中，并在函数签名中指定该代码的输入和返回值。
3. 将两个重复代码实例更新为调用该函数。

接下来，我们将使用相同的步骤和泛型来减少代码重复。就像函数体可以对抽象的`list`而不是特定值进行操作一样，泛型允许代码对抽象类型进行操作。

例如，假设我们有两个函数：一个用于在`i32`值的切片中找到最大的项，另一个用于在`char`值的切片中找到最大的项。我们如何消除这种重复呢？让我们来看看！
