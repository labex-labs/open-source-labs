# 複数のループ間を区別するためのループラベル

ループの中にループがある場合、`break`と`continue`はその時点で最内側のループに適用されます。任意で、ループに「ループラベル」を指定することができます。その後、`break`または`continue`とともに使用して、それらのキーワードが最内側のループではなく、ラベル付きのループに適用されることを指定できます。ループラベルは、シングルクォートで始める必要があります。2つのネストされたループの例を以下に示します：

```rust
fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}
```

外側のループには`'counting_up`というラベルがあり、0から2までカウントアップします。ラベルのない内側のループは、10から9までカウントダウンします。ラベルを指定しない最初の`break`は、内側のループのみを終了します。`break 'counting_up;`文は、外側のループを終了します。このコードは以下のように出力されます：

       Compiling loops v0.1.0 (file:///projects/loops)
        Finished dev [unoptimized + debuginfo] target(s) in 0.58s
         Running `target/debug/loops`
    count = 0
    remaining = 10
    remaining = 9
    count = 1
    remaining = 10
    remaining = 9
    count = 2
    remaining = 10
    End count = 2
