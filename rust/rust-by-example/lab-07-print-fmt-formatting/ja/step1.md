# フォーマット

フォーマットは、_フォーマット文字列_ を通じて指定されることがわかりました。

- `format!("{}", foo)` -> `"3735928559"`
- `format!("0x{:X}", foo)` -> `"0xDEADBEEF"`
- `format!("0o{:o}", foo)` -> `"0o33653337357"`

同じ変数 (`foo`) は、使用する _引数型_ に応じて異なる形式でフォーマットできます。`X` と `o` と _指定なし_ の場合です。

このフォーマット機能はトレイトを通じて実装されており、各引数型に対して 1 つのトレイトがあります。最も一般的なフォーマットトレイトは `Display` で、引数型が指定されていない場合 (たとえば `{}`) を処理します。

```rust
use std::fmt::{self, Formatter, Display};

struct City {
    name: &'static str,
    // 緯度
    lat: f32,
    // 経度
    lon: f32,
}

impl Display for City {
    // `f` はバッファで、このメソッドはフォーマット済みの文字列をそこに書き込む必要があります。
    fn fmt(&self, f: &mut Formatter) -> fmt::Result {
        let lat_c = if self.lat >= 0.0 { 'N' } else { 'S' };
        let lon_c = if self.lon >= 0.0 { 'E' } else { 'W' };

        // `write!` は `format!` と同じですが、フォーマット済みの文字列を
        // バッファ (最初の引数) に書き込みます。
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
        City { name: "Dublin", lat: 53.347778, lon: -6.259722 },
        City { name: "Oslo", lat: 59.95, lon: 10.75 },
        City { name: "Vancouver", lat: 49.25, lon: -123.1 },
    ] {
        println!("{}", city);
    }
    for color in [
        Color { red: 128, green: 255, blue: 90 },
        Color { red: 0, green: 3, blue: 254 },
        Color { red: 0, green: 0, blue: 0 },
    ] {
        // fmt::Display の実装を追加したら、これを {} に変更してください。
        println!("{:?}", color);
    }
}
```

`std::fmt` のドキュメントには、フォーマットトレイトとその引数型の完全な一覧を見ることができます。

## アクティビティ

上記の `Color` 構造体に対して `fmt::Display` トレイトの実装を追加して、出力が次のように表示されるようにしましょう。

```plaintext
RGB (128, 255, 90) 0x80FF5A
RGB (0, 3, 254) 0x0003FE
RGB (0, 0, 0) 0x000000
```

困ったときのヒント 3 つ:

- RGB カラー空間で色を計算する公式は: `RGB = (R*65536)+(G*256)+B, (R が赤、G が緑、B が青の場合)`。詳細は RGB カラー形式と計算を参照してください。
- 各色を複数回リストする必要がある場合があります。
- `:0>2` を使ってゼロで埋めて幅 2 にすることができます。
