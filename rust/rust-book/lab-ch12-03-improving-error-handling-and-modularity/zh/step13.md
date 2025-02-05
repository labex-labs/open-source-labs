# 将代码拆分为库包

到目前为止，我们的 `minigrep` 项目看起来很不错！现在我们将拆分 `src/main.rs` 文件，并将一些代码放入 `src/lib.rs` 文件中。这样，我们就可以测试代码，并且让 `src/main.rs` 文件承担的职责更少。

让我们将 `src/main.rs` 中不在 `main` 函数内的所有代码移动到 `src/lib.rs` 中：

- `run` 函数定义
- 相关的 `use` 语句
- `Config` 的定义
- `Config::build` 函数定义

`src/lib.rs` 的内容应该具有清单 12-13 中所示的签名（为简洁起见，我们省略了函数体）。请注意，在我们按照清单 12-14 修改 `src/main.rs` 之前，这段代码不会编译。

文件名：`src/lib.rs`

```rust
use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub file_path: String,
}

impl Config {
    pub fn build(
        args: &[String],
    ) -> Result<Config, &'static str> {
        --snip--
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    --snip--
}
```

清单 12-13：将 `Config` 和 `run` 移动到 `src/lib.rs` 中

我们大量使用了 `pub` 关键字：应用于 `Config`、其字段和 `build` 方法，以及 `run` 函数。现在我们有了一个具有可测试公共 API 的库包！

现在，我们需要将移动到 `src/lib.rs` 中的代码引入到 `src/main.rs` 中二进制包的作用域内，如清单 12-14 所示。

文件名：`src/main.rs`

```rust
use std::env;
use std::process;

use minigrep::Config;

fn main() {
    --snip--
    if let Err(e) = minigrep::run(config) {
        --snip--
    }
}
```

清单 12-14：在 `src/main.rs` 中使用 `minigrep` 库包

我们添加了一行 `use minigrep::Config`，将库包中的 `Config` 类型引入到二进制包的作用域内，并且在调用 `run` 函数时加上了我们的包名作为前缀。现在所有功能应该都连接起来并且能正常工作了。使用 `cargo run` 运行程序，确保一切正常。

呼！这工作量可不小，但我们为未来的成功奠定了基础。现在处理错误变得容易多了，并且我们使代码更具模块化。从现在开始，几乎所有工作都将在 `src/lib.rs` 中完成。

让我们利用这种新获得的模块化来做一些用旧代码很难做到但用新代码却很容易做到的事情：编写一些测试！
