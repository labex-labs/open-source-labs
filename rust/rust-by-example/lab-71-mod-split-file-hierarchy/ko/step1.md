# 파일 계층 구조

모듈은 파일/디렉토리 계층 구조에 매핑될 수 있습니다. 파일에서 가시성 예제를 살펴보겠습니다.

```shell
$ tree .
.
├── my
│   ├── inaccessible.rs
│   └── nested.rs
├── my.rs
└── split.rs
```

`split.rs`에서:

```rust
// 이 선언은 `my.rs` 라는 파일을 찾고
// 이 범위 내의 `my` 라는 모듈 안에 그 내용을 삽입합니다.
mod my;

fn function() {
    println!("called `function()`");
}

fn main() {
    my::function();

    function();

    my::indirect_access();

    my::nested::function();
}
```

`my.rs`에서:

```rust
// 마찬가지로 `mod inaccessible`와 `mod nested`는 `nested.rs`
// 와 `inaccessible.rs` 파일을 찾아 각각의 모듈 아래에 여기에 삽입합니다.
mod inaccessible;
pub mod nested;

pub fn function() {
    println!("called `my::function()`");
}

fn private_function() {
    println!("called `my::private_function()`");
}

pub fn indirect_access() {
    print!("called `my::indirect_access()`, that\n> ");

    private_function();
}
```

`my/nested.rs`에서:

```rust
pub fn function() {
    println!("called `my::nested::function()`");
}

#[allow(dead_code)]
fn private_function() {
    println!("called `my::nested::private_function()`");
}
```

`my/inaccessible.rs`에서:

```rust
#[allow(dead_code)]
pub fn public_function() {
    println!("called `my::inaccessible::public_function()`");
}
```

이전과 동일하게 작동하는지 확인해 보겠습니다.

```shell
$ rustc split.rs && ./split
called `my::function()`
called `function()`
called `my::indirect_access()`, that
> called `my::private_function()`
called `my::nested::function()`
```
