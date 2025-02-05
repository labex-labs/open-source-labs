# `abort` 和 `unwind`

上一节阐述了错误处理机制 `panic`。不同的代码路径可以根据 `panic` 设置进行条件编译。当前可用的值是 `unwind` 和 `abort`。

基于之前的柠檬水示例，我们显式地使用 `panic` 策略来执行不同的代码行。

```rust
fn drink(beverage: &str) {
   // 你不应喝太多含糖饮料。
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

这里是另一个专注于重写 `drink()` 并显式使用 `unwind` 关键字的示例。

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

可以通过在命令行使用 `abort` 或 `unwind` 来设置 `panic` 策略。

```console
rustc lemonade.rs -C panic=abort
```
