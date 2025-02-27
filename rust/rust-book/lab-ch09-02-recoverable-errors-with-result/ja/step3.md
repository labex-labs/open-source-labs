# Result<T, E> とのマッチングの代替方法

`match` がたくさんありますね！`match` 式は非常に便利ですが、また非常に基本的なものでもあります。13 章では、クロージャについて学びます。クロージャは、`Result<T, E>` に定義された多くのメソッドとともに使用されます。これらのメソッドは、コードで `Result<T, E>` 値を処理する際に `match` を使用するよりも簡潔になる場合があります。

たとえば、リスト 9-5 と同じロジックを書く別の方法を示します。今回はクロージャと `unwrap_or_else` メソッドを使用します。

    // src/main.rs
    use std::fs::File;
    use std::io::ErrorKind;

    fn main() {
        let greeting_file = File::open("hello.txt").unwrap_or_else(|error| {
            if error.kind() == ErrorKind::NotFound {
                File::create("hello.txt").unwrap_or_else(|error| {
                    panic!("Problem creating the file: {:?}", error);
                })
            } else {
                panic!("Problem opening the file: {:?}", error);
            }
        });
    }

このコードは、リスト 9-5 と同じ動作をしますが、`match` 式を含まず、読みやすくなっています。13 章を読んだ後にこの例に戻り、標準ライブラリのドキュメントで `unwrap_or_else` メソッドを調べてみてください。エラーを処理する際に、これらのメソッドの多くは巨大なネストされた `match` 式を整理することができます。
