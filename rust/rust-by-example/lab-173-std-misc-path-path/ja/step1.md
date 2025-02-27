# パス

`Path` 構造体は、基礎となるファイルシステム内のファイルパスを表します。`Path` には 2 種類のバージョンがあります。UNIX 系のシステム向けの `posix::Path` と、Windows 向けの `windows::Path` です。プレリュードは、適切な特定プラットフォーム用の `Path` バリアントをエクスポートします。

`Path` は `OsStr` から作成でき、パスが指すファイル/ディレクトリから情報を取得するためのいくつかのメソッドを提供します。

`Path` は不変です。`Path` の所有バージョンは `PathBuf` です。`Path` と `PathBuf` の関係は、`str` と `String` の関係に似ています。`PathBuf` はインプレースで変更可能で、`Path` に解引用できます。

`Path` は内部的に UTF-8 文字列として表されていなく、代わりに `OsString` として格納されていることに注意してください。したがって、`Path` を `&str` に変換することは無料ではなく、失敗する可能性があります（`Option` が返されます）。ただし、`Path` はそれぞれ `into_os_string` と `as_os_str` を使用して、自由に `OsString` または `&OsStr` に変換できます。

```rust
use std::path::Path;

fn main() {
    // `&'static str` から `Path` を作成する
    let path = Path::new(".");

    // `display` メソッドは `Display` 可能な構造体を返す
    let _display = path.display();

    // `join` は、OS 固有の区切り文字を使用してパスとバイトコンテナを結合し、`PathBuf` を返す
    let mut new_path = path.join("a").join("b");

    // `push` は `PathBuf` に `&Path` を追加する
    new_path.push("c");
    new_path.push("myfile.tar.gz");

    // `set_file_name` は `PathBuf` のファイル名を更新する
    new_path.set_file_name("package.tgz");

    // `PathBuf` を文字列スライスに変換する
    match new_path.to_str() {
        None => panic!("new path is not a valid UTF-8 sequence"),
        Some(s) => println!("new path is {}", s),
    }
}
```

他の `Path` メソッド（`posix::Path` または `windows::Path`）と `Metadata` 構造体を必ず確認してください。
