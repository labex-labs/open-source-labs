# 정답 추측 후 종료

`break` 문을 추가하여 사용자가 이기면 게임이 종료되도록 프로그래밍해 보겠습니다.

파일 이름: `src/main.rs`

```rust
--snip--

match guess.cmp(&secret_number) {
    Ordering::Less => println!("Too small!"),
    Ordering::Greater => println!("Too big!"),
    Ordering::Equal => {
        println!("You win!");
        break;
    }
}
```

`You win!` 뒤에 `break` 줄을 추가하면 사용자가 비밀 번호를 올바르게 추측했을 때 프로그램이 루프를 종료합니다. 루프를 종료하는 것은 또한 프로그램을 종료하는 것을 의미합니다. 루프가 `main`의 마지막 부분이기 때문입니다.
