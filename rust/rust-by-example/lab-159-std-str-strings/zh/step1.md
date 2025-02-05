# 字符串

Rust中有两种类型的字符串：`String` 和 `&str`。

`String` 作为字节向量（`Vec<u8>`）存储，但保证始终是有效的UTF-8序列。`String` 在堆上分配，可增长且不以空字符结尾。

`&str` 是一个切片（`&[u8]`），它始终指向一个有效的UTF-8序列，并且可用于查看 `String`，就像 `&[T]` 是 `Vec<T>` 的视图一样。

```rust
fn main() {
    // （所有类型注释都是多余的）
    // 指向只读内存中分配的字符串的引用
    let pangram: &'static str = "the quick brown fox jumps over the lazy dog";
    println!("全字母句: {}", pangram);

    // 反向遍历单词，不分配新字符串
    println!("反向的单词");
    for word in pangram.split_whitespace().rev() {
        println!("> {}", word);
    }

    // 将字符复制到向量中，排序并删除重复项
    let mut chars: Vec<char> = pangram.chars().collect();
    chars.sort();
    chars.dedup();

    // 创建一个空的可增长 `String`
    let mut string = String::new();
    for c in chars {
        // 在字符串末尾插入一个字符
        string.push(c);
        // 在字符串末尾插入一个字符串
        string.push_str(", ");
    }

    // 修剪后的字符串是对原始字符串的切片，因此不会进行新的
    // 分配
    let chars_to_trim: &[char] = &[' ', ','];
    let trimmed_str: &str = string.trim_matches(chars_to_trim);
    println!("使用的字符: {}", trimmed_str);

    // 在堆上分配一个字符串
    let alice = String::from("I like dogs");
    // 分配新内存并将修改后的字符串存储在那里
    let bob: String = alice.replace("dog", "cat");

    println!("爱丽丝说: {}", alice);
    println!("鲍勃说: {}", bob);
}
```

更多的 `str`/`String` 方法可以在 `std::str` 和 `std::string` 模块中找到。

## 字面量和转义

有多种方法可以编写包含特殊字符的字符串字面量。所有这些方法都会产生类似的 `&str`，因此最好使用最方便编写的形式。同样，有多种方法可以编写字节字符串字面量，它们都会产生 `&[u8; N]`。

一般来说，特殊字符用反斜杠字符 `\` 进行转义。通过这种方式，你可以在字符串中添加任何字符，甚至是不可打印的字符和你不知道如何输入的字符。如果你想要一个字面的反斜杠，用另一个反斜杠对其进行转义：`\\`

字面量中出现的字符串或字符字面量分隔符必须进行转义：`"\""`，`'\''`。

```rust
fn main() {
    // 你可以使用转义字符通过十六进制值来编写字节...
    let byte_escape = "I'm writing \x52\x75\x73\x74!";
    println!("你在做什么\x3F （\\x3F 表示?） {}", byte_escape);

    //...或者Unicode代码点。
    let unicode_codepoint = "\u{211D}";
    let character_name = "\"DOUBLE-STRUCK CAPITAL R\"";

    println!("Unicode字符 {} （U+211D） 被称为 {}",
                unicode_codepoint, character_name );


    let long_string = "字符串字面量
                        可以跨越多行。
                        这里的换行符和缩进 ->\
                        <- 也可以进行转义！";
    println!("{}", long_string);
}
```

有时需要转义的字符太多，或者直接按原样编写字符串更方便。这就是原始字符串字面量发挥作用的地方。

```rust
fn main() {
    let raw_str = r"转义在这里不起作用: \x3F \u{211D}";
    println!("{}", raw_str);

    // 如果你在原始字符串中需要引号，添加一对 #
    let quotes = r#"然后我说: "没有转义！""#;
    println!("{}", quotes);

    // 如果你在字符串中需要 "#，只需在分隔符中使用更多的 #。
    // 你最多可以使用65535个 #。
    let longer_delimiter = r###"一个包含 "# 的字符串。甚至还有 "##！"###;
    println!("{}", longer_delimiter);
}
```

想要一个不是UTF-8的字符串？（记住，`str` 和 `String` 必须是有效的UTF-8）。或者也许你想要一个大部分是文本的字节数组？字节字符串来救场！

```rust
use std::str;

fn main() {
    // 注意这实际上不是一个 `&str`
    let bytestring: &[u8; 21] = b"this is a byte string";

    // 字节数组没有 `Display` 特性，所以打印它们有点受限
    println!("一个字节字符串: {:?}", bytestring);

    // 字节字符串可以有字节转义...
    let escaped = b"\x52\x75\x73\x74 as bytes";
    //...但没有Unicode转义
    // let escaped = b"\u{211D} is not allowed";
    println!("一些转义后的字节: {:?}", escaped);


    // 原始字节字符串的工作方式与原始字符串相同
    let raw_bytestring = br"\u{211D} 在这里不会被转义";
    println!("{:?}", raw_bytestring);

    // 将字节数组转换为 `str` 可能会失败
    if let Ok(my_str) = str::from_utf8(raw_bytestring) {
        println!("作为文本也是一样: '{}'", my_str);
    }

    let _quotes = br#"你也可以使用 "更花哨" 的格式， \
                    就像普通的原始字符串一样"#;

    // 字节字符串不必是UTF-8
    let shift_jis = b"\x82\xe6\x82\xa8\x82\xb1\x82\xbb"; // "ようこそ" 的SHIFT-JIS编码

    // 但这样它们并不总是能转换为 `str`
    match str::from_utf8(shift_jis) {
        Ok(my_str) => println!("转换成功: '{}'", my_str),
        Err(e) => println!("转换失败: {:?}", e),
    };
}
```

有关字符编码之间的转换，请查看encoding crate。

Rust参考手册的“Tokens”一章中给出了编写字符串字面量和转义字符的更详细列表。
