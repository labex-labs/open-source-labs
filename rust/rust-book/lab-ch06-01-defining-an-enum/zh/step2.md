# 枚举值

我们可以像这样创建 `IpAddrKind` 的两个变体的实例：

```rust
let four = IpAddrKind::V4;
let six = IpAddrKind::V6;
```

注意，枚举的变体在其标识符下进行了命名空间划分，我们使用双冒号将两者分隔开。这很有用，因为现在 `IpAddrKind::V4` 和 `IpAddrKind::V6` 这两个值都是同一类型：`IpAddrKind`。例如，我们可以定义一个接受任何 `IpAddrKind` 的函数：

```rust
fn route(ip_kind: IpAddrKind) {}
```

然后我们可以使用任何一个变体来调用这个函数：

```rust
route(IpAddrKind::V4);
route(IpAddrKind::V6);
```

使用枚举还有更多优点。再考虑一下我们的 IP 地址类型，目前我们没有办法存储实际的 IP 地址 _数据_；我们只知道它是哪种 _类型_。鉴于你刚刚在第 5 章中学到了结构体，你可能会想用结构体来解决这个问题，如清单 6-1 所示。

```rust
1 enum IpAddrKind {
    V4,
    V6,
}

2 struct IpAddr {
  3 kind: IpAddrKind,
  4 address: String,
}

5 let home = IpAddr {
    kind: IpAddrKind::V4,
    address: String::from("127.0.0.1"),
};

6 let loopback = IpAddr {
    kind: IpAddrKind::V6,
    address: String::from("::1"),
};
```

清单 6-1：使用 `struct` 存储 IP 地址的数据和 `IpAddrKind` 变体

在这里，我们定义了一个结构体 `IpAddr` \[2\]，它有两个字段：一个 `kind` 字段 \[3\]，其类型为 `IpAddrKind`（我们之前定义的枚举 \[1\]），以及一个 `address` 字段 \[4\]，其类型为 `String`。我们有这个结构体的两个实例。第一个是 `home` \[5\]，它的 `kind` 值为 `IpAddrKind::V4`，关联的地址数据为 `127.0.0.1`。第二个实例是 `loopback` \[6\]。它的 `kind` 值是 `IpAddrKind` 的另一个变体 `V6`，并关联地址 `::1`。我们使用结构体将 `kind` 和 `address` 值捆绑在一起，所以现在变体与值相关联。

然而，仅使用枚举来表示相同的概念更简洁：我们不是在结构体中使用枚举，而是可以直接将数据放入每个枚举变体中。`IpAddr` 枚举的这个新定义表示 `V4` 和 `V6` 变体都将有相关联的 `String` 值：

```rust
enum IpAddr {
    V4(String),
    V6(String),
}

let home = IpAddr::V4(String::from("127.0.0.1"));

let loopback = IpAddr::V6(String::from("::1"));
```

我们直接将数据附加到枚举的每个变体上，所以不需要额外的结构体。在这里，也更容易看出枚举工作方式的另一个细节：我们定义的每个枚举变体的名称也成为了一个构造枚举实例的函数。也就是说，`IpAddr::V4()` 是一个函数调用，它接受一个 `String` 参数并返回一个 `IpAddr` 类型的实例。定义枚举时会自动为我们定义这个构造函数。

使用枚举而不是结构体还有另一个优点：每个变体可以有不同类型和数量的关联数据。IPv4 地址总是有四个数字组件，其值在 0 到 255 之间。如果我们想将 `V4` 地址存储为四个 `u8` 值，但仍然将 `V6` 地址表示为一个 `String` 值，使用结构体就无法做到。枚举轻松地处理这种情况：

```rust
enum IpAddr {
    V4(u8, u8, u8, u8),
    V6(String),
}

let home = IpAddr::V4(127, 0, 0, 1);

let loopback = IpAddr::V6(String::from("::1"));
```

我们展示了几种不同的方法来定义数据结构以存储 IPv4 和 IPv6 地址。然而，事实证明，想要存储 IP 地址并编码它们的类型是非常常见的，以至于标准库有一个我们可以使用的定义！让我们看看标准库是如何定义 `IpAddr` 的：它有我们定义和使用的完全相同的枚举和变体，但它以两个不同结构体的形式将地址数据嵌入到变体中，每个变体的定义都不同：

```rust
struct Ipv4Addr {
    --snip--
}

struct Ipv6Addr {
    --snip--
}

enum IpAddr {
    V4(Ipv4Addr),
    V6(Ipv6Addr),
}
```

这段代码说明你可以在枚举变体中放入任何类型的数据：例如字符串、数字类型或结构体。你甚至可以包含另一个枚举！此外，标准库类型通常并不比你自己想出的复杂多少。

请注意，即使标准库包含了 `IpAddr` 的定义，我们仍然可以创建并使用我们自己的定义而不会产生冲突，因为我们没有将标准库的定义引入到我们的作用域中。我们将在第 7 章中更多地讨论将类型引入作用域的问题。

让我们看一下清单 6-2 中枚举的另一个示例：这个枚举的变体中嵌入了各种各样的类型。

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

清单 6-2：一个 `Message` 枚举，其变体各自存储不同数量和类型的值

这个枚举有四个具有不同类型的变体：

- `Quit` 根本没有关联的数据。
- `Move` 有命名字段，就像结构体一样。
- `Write` 包含一个 `String`。
- `ChangeColor` 包含三个 `i32` 值。

定义一个具有如清单 6-2 中变体的枚举类似于定义不同种类的结构体定义，只是枚举不使用 `struct` 关键字，并且所有变体都在 `Message` 类型下组合在一起。以下结构体可以保存与前面枚举变体相同的数据：

```rust
struct QuitMessage; // 单元结构体
struct MoveMessage {
    x: i32,
    y: i32,
}
struct WriteMessage(String); // 元组结构体
struct ChangeColorMessage(i32, i32, i32); // 元组结构体
```

但是如果我们使用不同的结构体，每个结构体都有自己的类型，我们就不能像使用清单 6-2 中定义的 `Message` 枚举那样轻松地定义一个函数来接受任何这些类型的消息，因为 `Message` 枚举是一个单一类型。

枚举和结构体之间还有一个相似之处：就像我们能够使用 `impl` 为结构体定义方法一样，我们也能够为枚举定义方法。这是我们可以在 `Message` 枚举上定义的一个名为 `call` 的方法：

```rust
impl Message {
    fn call(&self) {
      1 // 方法体将在此处定义
    }
}

2 let m = Message::Write(String::from("hello"));
m.call();
```

方法体将使用 `self` 来获取调用该方法的值。在这个例子中，我们创建了一个变量 `m` \[2\]，其值为 `Message::Write(String::from("hello"))`，当 `m.call()` 运行时，`self` 在 `call` 方法体 \[1\] 中将是这个值。

让我们看一下标准库中另一个非常常见且有用的枚举：`Option`。
