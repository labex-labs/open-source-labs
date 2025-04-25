# 異なるエラーのマッチング

リスト 9-4 のコードは、`File::open` が失敗した理由に関係なく `panic!` します。ただし、異なる失敗理由に対して異なるアクションを取りたい場合があります。`File::open` がファイルが存在しないために失敗した場合、ファイルを作成して新しいファイルのハンドルを返したいです。`File::open` がその他の理由（たとえば、ファイルを開く権限がないため）で失敗した場合でも、コードはリスト 9-4 と同じように `panic!` する必要があります。このため、リスト 9-5 に示すように、内部の `match` 式を追加します。

ファイル名：`src/main.rs`

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let greeting_file_result = File::open("hello.txt");

    let greeting_file = match greeting_file_result {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => {
                match File::create("hello.txt") {
                    Ok(fc) => fc,
                    Err(e) => panic!(
                        "Problem creating the file: {:?}",
                        e
                    ),
                }
            }
            other_error => {
                panic!(
                    "Problem opening the file: {:?}",
                    other_error
                );
            }
        },
    };
}
```

リスト 9-5: 異なる種類のエラーを異なる方法で処理する

`Err` バリアント内で `File::open` が返す値の型は `io::Error` で、これは標準ライブラリが提供する構造体です。この構造体には、`io::ErrorKind` 値を取得するために呼び出せる `kind` メソッドがあります。列挙型 `io::ErrorKind` は標準ライブラリが提供し、`io` 操作から生じる可能性のある異なる種類のエラーを表すバリアントがあります。使用したいバリアントは `ErrorKind::NotFound` で、これは開こうとしているファイルがまだ存在しないことを示します。したがって、`greeting_file_result` に対してマッチングを行いますが、`error.kind()` に対しても内部のマッチングを行います。

内部のマッチングでチェックしたい条件は、`error.kind()` が返す値が `ErrorKind` 列挙型の `NotFound` バリアントであるかどうかです。そうであれば、`File::create` でファイルを作成しようとします。ただし、`File::create` も失敗する可能性があるため、内部の `match` 式には 2 番目のアームが必要です。ファイルを作成できない場合、異なるエラーメッセージが表示されます。外部の `match` の 2 番目のアームは同じままであるため、欠落したファイルエラー以外のエラーではプログラムがパニックになります。
