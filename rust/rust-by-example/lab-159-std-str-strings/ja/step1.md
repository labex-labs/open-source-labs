# 文字列

Rustには2種類の文字列があります。`String` と `&str` です。

`String` はバイトのベクタ (`Vec<u8>`) として格納されますが、常に有効なUTF-8シーケンスであることが保証されています。`String` はヒープ上に割り当てられ、拡張可能で、null終端ではありません。

`&str` は、常に有効なUTF-8シーケンスを指すスライス (`&[u8]`) であり、`&[T]` が `Vec<T>` のビューと同じように、`String` の中身を参照するために使用できます。

```rust
fn main() {
    // (すべての型注釈は余分です)
    // 読み取り専用メモリに割り当てられた文字列を参照する
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("Pangram: {}", pangram);

    // 単語を逆順に反復処理します。新しい文字列を割り当てることはありません
    println!("Words in reverse");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // 文字をベクタにコピーし、ソートして重複を削除します
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // 空の拡張可能な `String` を作成します
    let mut string = String::new();
    for c in chars {
        // 文字列を末尾に挿入します
        string.push(c);
        // 文字列を末尾に挿入します
        string.push_str(", ");
    }

    // トリミングされた文字列は元の文字列へのスライスであるため、新しい割り当ては行われません
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("Used characters: {}", trimmed_str);

    // ヒープ上に文字列を割り当てます
    let alice = String::from("I like dogs");
    // 新しいメモリを割り当てて、修正された文字列をそこに格納します
    let bob: String = alice.replace("dog", "cat");

    println!("Alice says: {}", alice);
    println!("Bob says: {}", bob);
}
```

さらに多くの `str`/`String` メソッドは、`std::str` と `std::string` モジュールの下で見つけることができます。

## リテラルとエスケープ

特殊文字を含む文字列リテラルを書く方法は複数あります。すべてが同様の `&str` を生成するため、書きやすい形式を使うのが最善です。同様に、バイト文字列リテラルを書く方法も複数あり、すべて `&[u8; N]` を生成します。

一般的に、特殊文字はバックスラッシュ文字 (`\`) でエスケープされます。これにより、文字列に任意の文字を追加できます。表示できない文字や入力方法がわからない文字でもです。リテラルのバックスラッシュを取得するには、もう1つのバックスラッシュでエスケープします。`\\`

リテラル内に出現する文字列または文字リテラルの区切り文字はエスケープする必要があります。`"\""`、`'\''`

```rust
fn main() {
    // バイトを16進数値でエスケープして書くことができます...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("What are you doing\x3F (\\x3F means?) {}", byte_escape);

    //...またはUnicodeコードポイントです。
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Unicode character {} (U+211D) is called {}",
                unicode_codepoint, character_name );


    let long_string = "String literals
                        can span multiple lines.
                        The linebreak and indentation here ->\
                        <- can be escaped too!";
    println!("{}", long_string);
}
```

時には、エスケープする文字が多すぎたり、そのままの文字列を書く方がはるかに便利な場合があります。ここで生文字列リテラルが役に立ちます。

```rust
fn main() {
    let raw_str = r"Escapes don't work here: \x3F \u{211D}";
    println!("{}", raw_str);

    // 生文字列に引用符が必要な場合は、ペアの # を追加します
    let quotes = r#"And then I said: "There is no escape!""#;
    println!("{}", quotes);

    // 文字列に "#" が必要な場合は、区切り文字にさらに多くの "#" を使います。
    // 最大65535個の "#" を使うことができます。
    let longer_delimiter = r###"A string with "# in it. And even "##!"###;
    println!("{}", longer_delimiter);
}
```

UTF-8でない文字列が必要ですか？（覚えておいてください。`str` と `String` は有効なUTF-8でなければなりません）。または、ほとんどがテキストであるバイトの配列が必要ですか？バイト文字列が助けになります！

```rust
use std::str;

fn main() {
    // これは実際には `&str` ではないことに注意してください
    let bytestring: &[u8; 21] = b"this is a byte string";

    // バイト配列には `Display` トレイトがないため、表示するのは少し制限されます
    println!("A byte string: {:?}", bytestring);

    // バイト文字列にはバイトエスケープがあります...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //...ですが、Unicodeエスケープはありません
    // let escaped = b"\u{211D} is not allowed";
    println!("Some escaped bytes: {:?}", escaped);


    // 生バイト文字列は生文字列と同じように機能します
    let raw_bytestring = br"\u{211D} is not escaped here";
    println!("{:?}", raw_bytestring);

    // バイト配列を `str` に変換すると失敗する場合があります
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("And the same as text: '{}'", my_str);
    }

    let _quotes = br#"You can also use "fancier" formatting, \
                    like with normal raw strings"#;

    // バイト文字列は必ずしもUTF-8でなくてもよいです
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" in SHIFT-JIS

    // しかし、その場合、必ずしも `str` に変換できるわけではありません
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("Conversion successful: '{}'", my_str),
        Err(e) => println!("Conversion failed: {:?}", e),
    };
}
```

文字エンコーディング間の変換については、encodingクレートを参照してください。

文字列リテラルとエスケープ文字の書き方のより詳細な一覧は、Rustリファレンスの「トークン」の章に記載されています。
