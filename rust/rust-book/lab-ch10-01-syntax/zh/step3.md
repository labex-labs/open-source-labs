# 在函数定义中

在定义使用泛型的函数时，我们将泛型放在函数签名中，通常在那里我们会指定参数和返回值的数据类型。这样做会使我们的代码更灵活，并为函数调用者提供更多功能，同时防止代码重复。

继续以我们的`largest`函数为例，清单10-4展示了两个函数，它们都在切片中找到最大值。然后我们将把它们合并成一个使用泛型的单一函数。

文件名：`src/main.rs`

```rust
fn largest_i32(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn largest_char(list: &[char]) -> &char {
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

    let result = largest_i32(&number_list);
    println!("The largest number is {result}");

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest_char(&char_list);
    println!("The largest char is {result}");
}
```

清单10-4：两个仅在名称和签名中的类型上有所不同的函数

`largest_i32`函数是我们在清单10-3中提取的，用于在切片中找到最大`i32`的函数。`largest_char`函数用于在切片中找到最大的`char`。函数体有相同的代码，所以让我们通过在一个单一函数中引入泛型类型参数来消除重复。

要在一个新的单一函数中对类型进行参数化，我们需要给类型参数命名，就像我们给函数的值参数命名一样。你可以使用任何标识符作为类型参数名。但我们将使用`T`，因为按照惯例，Rust中的类型参数名很短，通常只有一个字母，并且Rust的类型命名惯例是驼峰式大小写。`T`是大多数Rust程序员的默认选择，它是*type*的缩写。

当我们在函数体中使用一个参数时，我们必须在签名中声明参数名，以便编译器知道该名称的含义。类似地，当我们在函数签名中使用类型参数名时，我们必须在使用它之前声明类型参数名。要定义泛型`largest`函数，我们将类型名称声明放在函数名和参数列表之间的尖括号`<>`内，如下所示：

```rust
fn largest<T>(list: &[T]) -> &T {
```

我们将这个定义理解为：函数`largest`对于某个类型`T`是泛型的。这个函数有一个名为`list`的参数，它是类型`T`的值的切片。`largest`函数将返回一个对相同类型`T`的值的引用。

清单10-5展示了在签名中使用通用数据类型的组合`largest`函数定义。该清单还展示了我们如何使用`i32`值的切片或`char`值来调用该函数。请注意，这段代码目前还无法编译，但我们将在本章后面修复它。

文件名：`src/main.rs`

```rust
fn largest<T>(list: &[T]) -> &T {
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

    let char_list = vec!['y','m', 'a', 'q'];

    let result = largest(&char_list);
    println!("The largest char is {result}");
}
```

清单10-5：使用通用类型参数的`largest`函数；目前还无法编译

如果我们现在编译这段代码，会得到如下错误：

```bash
error[E0369]: binary operation `>` cannot be applied to type `&T`
 --> src/main.rs:5:17
  |
5 |         if item > largest {
  |            ---- ^ ------- &T
  |            |
  |            &T
  |
help: consider restricting type parameter `T`
  |
1 | fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
  |             ++++++++++++++++++++++
```

帮助文本提到了`std::cmp::PartialOrd`，它是一个*特性*，我们将在下一节讨论特性。目前，只需知道这个错误表明`largest`函数体不适用于`T`可能的所有类型。因为我们想在函数体中比较`T`类型的值，所以我们只能使用其值可以排序的类型。为了启用比较，标准库有`std::cmp::PartialOrd`特性，你可以在类型上实现它（有关此特性的更多信息，请参阅附录C）。按照帮助文本的建议，我们将对`T`有效的类型限制为仅那些实现`PartialOrd`的类型，这样这个示例就会编译，因为标准库在`i32`和`char`上都实现了`PartialOrd`。
