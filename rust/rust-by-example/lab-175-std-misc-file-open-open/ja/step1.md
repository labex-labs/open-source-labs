# `open`

`open` 関数を使用すると、読み取り専用モードでファイルを開くことができます。

`File` は、リソース（ファイル記述子）を所有し、`drop` されたときにファイルを閉じる処理を行います。

```rust
use std::fs::File;
use std::io::prelude::*;
use std::path::Path;

fn main() {
    // 開きたいファイルへのパスを作成する
    let path = Path::new("hello.txt");
    let display = path.display();

    // 読み取り専用モードでパスを開き、`io::Result<File>` を返す
    let mut file = match File::open(&path) {
        Err(why) => panic!("couldn't open {}: {}", display, why),
        Ok(file) => file,
    };

    // ファイルの内容を文字列に読み込み、`io::Result<usize>` を返す
    let mut s = String::new();
    match file.read_to_string(&mut s) {
        Err(why) => panic!("couldn't read {}: {}", display, why),
        Ok(_) => print!("{} contains:\n{}", display, s),
    }

    // `file` がスコープ外になり、"hello.txt" ファイルが閉じられる
}
```

期待される正常な出力は以下の通りです。

```shell
$ echo "Hello World!" > hello.txt
$ rustc open.rs && ./open
hello.txt contains:
Hello World!
```

（前の例を、異なるエラー条件下でテストすることをお勧めします。たとえば、`hello.txt` が存在しない場合や、`hello.txt` が読み取り可能でない場合など）
