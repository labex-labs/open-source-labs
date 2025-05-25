# `abort`와 `unwind`

이전 섹션에서는 오류 처리 메커니즘인 `panic`을 설명했습니다. 패닉 설정에 따라 다른 코드 경로를 조건부로 컴파일할 수 있습니다. 현재 사용 가능한 값은 `unwind`와 `abort`입니다.

이전 레모네이드 예제를 기반으로, 패닉 전략을 명시적으로 사용하여 다른 코드 라인을 실행합니다.

```rust

fn drink(beverage: &str) {
   // You shouldn't drink too much sugary beverages.
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

다음은 `drink()`를 다시 작성하고 `unwind` 키워드를 명시적으로 사용하는 또 다른 예입니다.

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

패닉 전략은 `abort` 또는 `unwind`를 사용하여 명령줄에서 설정할 수 있습니다.

```console
rustc lemonade.rs -C panic=abort
```
