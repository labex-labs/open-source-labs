# 格式化

我们已经了解到格式化是通过一个**格式字符串**来指定的：

- `format!("{}", foo)` -> `"3735928559"`
- `format!("0x{:X}", foo)` -> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -> `"0o33653337357"`

同一个变量（`foo`）根据所使用的**参数类型**不同，可以有不同的格式化方式：`X` 与 `o` 以及未指定类型。

这种格式化功能是通过特性来实现的，每种参数类型都有一个对应的特性。最常见的格式化特性是 `Display`，它处理参数类型未指定的情况，例如 `{}`。

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // 纬度
    lat: f32,
    // 经度
    lon: f32,
}

impl Display for City {
    // `f` 是一个缓冲区，此方法必须将格式化后的字符串写入其中。
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` 类似于 `format!`，但它会将格式化后的字符串
        // 写入一个缓冲区（第一个参数）。
        write!(f, "{}: {:.3}°{} {:.3}°{}",
               self.name, self.lat.abs(), lat_c, self.lon.abs(), lon_c)
    }
}

#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

fn main() {
    for city in [
        City { name: "都柏林", lat: 53.347778, lon: -6.259722 },
        City { name: "奥斯陆", lat: 59.95, lon: 10.75 },
        City { name: "温哥华", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // 一旦为 fmt::Display 添加了实现，将此行改为使用 {}。
        println!("{:?}", color);
    }
}
```

你可以在 `std::fmt` 文档中查看格式化特性及其参数类型的完整列表。

## 活动

为上面的 `Color` 结构体添加 `fmt::Display` 特性的实现，使输出显示为：

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

如果你遇到困难，这里有三个提示：

- 在 RGB 颜色空间中计算颜色的公式是：`RGB = (R*65536)+(G*256)+B, （其中 R 是红色，G 是绿色，B 是蓝色）`。更多信息请参阅 RGB 颜色格式与计算。
- 你可能需要多次列出每种颜色。
- 你可以使用 `:0>2` 填充零，使其宽度为 2。
