# `abort` と `unwind`

前のセクションでは、エラーハンドリングメカニズム `panic` を説明しました。異なるコードパスは、panic設定に基づいて条件付きでコンパイルできます。利用可能な現在の値は、`unwind` と `abort` です。

以前のレモネードの例を基に、明示的にパニック戦略を使用して異なるコード行を実行します。

```rust
fn drink(beverage: &str) {
   // 糖分多い飲み物はあまり飲んではいけません。
    if beverage == "lemonade" {
        if cfg!(panic="abort"){ println!("This is not your party. Run!!!!");}
        else{ println!("Spit it out!!!!");}
    }
    else{ println!("Some refreshing {} is all I need.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

ここに、`drink()` を書き直して明示的に `unwind` キーワードを使用する別の例があります。

```rust
#[cfg(panic = "unwind")]
fn ah(){ println!("Spit it out!!!!");}

#[cfg(not(panic="unwind"))]
fn ah(){ println!("This is not your party. Run!!!!");}

fn drink(beverage: &str){
    if beverage == "lemonade"{ ah();}
    else{println!("Some refreshing {} is all I need.", beverage);}
}

fn main() {
    drink("water");
    drink("lemonade");
}
```

パニック戦略は、コマンドラインから `abort` または `unwind` を使用して設定できます。

```console
rustc lemonade.rs -C panic=abort
```
