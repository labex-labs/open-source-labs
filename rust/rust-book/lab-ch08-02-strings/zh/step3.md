# 创建新字符串

`Vec<T>` 可用的许多操作 `String` 也同样可用，因为 `String` 实际上是围绕字节向量实现的一个包装器，并带有一些额外的保证、限制和功能。与 `Vec<T>` 和 `String` 以相同方式工作的一个函数示例是用于创建实例的 `new` 函数，如清单 8-11 所示。

```rust
let mut s = String::new();
```

清单 8-11：创建一个新的空 `String`

这行代码创建了一个名为 `s` 的新的空字符串，之后我们可以向其中加载数据。通常，我们会有一些初始数据来开始构建字符串。为此，我们使用 `to_string` 方法，任何实现了 `Display` 特性的类型都有这个方法，就像字符串字面值一样。清单 8-12 展示了两个示例。

```rust
let data = "initial contents";

let s = data.to_string();

// 该方法也可以直接用于字面值：
let s = "initial contents".to_string();
```

清单 8-12：使用 `to_string` 方法从字符串字面值创建 `String`

这段代码创建了一个包含“initial contents”的字符串。

我们还可以使用函数 `String::from` 从字符串字面值创建 `String`。清单 8-13 中的代码与清单 8-12 中使用 `to_string` 的代码等效。

```rust
let s = String::from("initial contents");
```

清单 8-13：使用 `String::from` 函数从字符串字面值创建 `String`

因为字符串用途广泛，所以我们可以对字符串使用许多不同的通用 API，这为我们提供了很多选择。其中一些可能看起来有些冗余，但它们都有各自的用途！在这种情况下，`String::from` 和 `to_string` 做的是相同的事情，所以选择哪一个只是风格和可读性的问题。

记住字符串是 UTF-8 编码的，所以我们可以在其中包含任何正确编码的数据，如清单 8-14 所示。

```rust
let hello = String::from("السلام عليكم");
let hello = String::from("Dobrý den");
let hello = String::from("Hello");
let hello = String::from("שָׁלוֹם");
let hello = String::from("नमस्ते");
let hello = String::from("こんにちは");
let hello = String::from("안녕하세요");
let hello = String::from("你好");
let hello = String::from("Olá");
let hello = String::from("Здравствуйте");
let hello = String::from("Hola");
```

清单 8-14：在字符串中存储不同语言的问候语

所有这些都是有效的 `String` 值。
