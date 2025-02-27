# `read_lines`

## 単純なアプローチ

これは、初心者がファイルから行を読み取るための最初の実装として合理的な最初の試みかもしれません。

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}
```

`lines()` メソッドはファイル内の行のイテレータを返すので、インラインでマップを実行して結果を収集することもでき、より簡潔で流暢な式になります。

```rust
use std::fs::read_to_string;

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename)
     .unwrap()  // ファイル読み取りエラー時にパニック
     .lines()  // 文字列を文字列スライスのイテレータに分割
     .map(String::from)  // 各スライスを文字列に変換
     .collect()  // それらをベクタにまとめる
}
```

上記の両方の例では、`lines()` から返される `&str` 参照をそれぞれ `.to_string()` と `String::from` を使って所有型 `String` に変換する必要があることに注意してください。

## より効率的なアプローチ

ここでは、開いた `File` の所有権を `BufReader` 構造体に渡します。`BufReader` は内部バッファを使って中間割り当てを削減します。

また、`read_lines` を更新してイテレータを返すようにし、各行に対して新しい `String` オブジェクトをメモリに割り当てなくなります。

```rust
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    // File hosts.txt は現在のパスに存在している必要があります
    if let Ok(lines) = read_lines("./hosts.txt") {
        // イテレータを消費し、(オプショナルな) String を返します
        for line in lines {
            if let Ok(ip) = line {
                println!("{}", ip);
            }
        }
    }
}

// 出力は Result にラップされていて、エラーのマッチングを可能にします
// ファイルの行の Reader へのイテレータを返します。
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
```

このプログラムを実行すると、各行が個別に表示されます。

```shell
$ echo -e "127.0.0.1\n192.168.0.1\n" > hosts.txt
$ rustc read_lines.rs && ./read_lines
127.0.0.1
192.168.0.1
```

(`File::open` は引数として汎用的な `AsRef<Path>` を期待するので、`where` キーワードを使って同じ汎用的な制約付きで汎用的な `read_lines()` メソッドを定義しています。)

このプロセスは、ファイルのすべての内容を使ってメモリ内に `String` を作成するよりも効率的です。特に大きなファイルを扱う場合、これは性能問題を引き起こす可能性があります。
