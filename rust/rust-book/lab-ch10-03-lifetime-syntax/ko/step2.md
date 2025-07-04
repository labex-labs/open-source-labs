# 생명주기를 사용하여 댕글링 참조 방지

생명주기의 주요 목표는 프로그램이 참조하려는 데이터가 아닌 다른 데이터를 참조하게 만드는 *댕글링 참조 (dangling references)*를 방지하는 것입니다. Listing 10-16 의 프로그램을 생각해 봅시다. 이 프로그램은 외부 범위와 내부 범위를 가지고 있습니다.

```rust
fn main() {
  1 let r;

    {
      2 let x = 5;
      3 r = &x;
  4 }

  5 println!("r: {r}");
}
```

Listing 10-16: 값이 범위를 벗어난 참조를 사용하려는 시도

> 참고: Listing 10-16, 10-17, 및 10-23 의 예제는 초기값을 지정하지 않고 변수를 선언하므로 변수 이름이 외부 범위에 존재합니다. 언뜻 보면 이것은 Rust 가 null 값을 갖지 않는다는 것과 충돌하는 것처럼 보일 수 있습니다. 그러나 값을 지정하기 전에 변수를 사용하려고 하면 컴파일 시간 오류가 발생하며, 이는 Rust 가 실제로 null 값을 허용하지 않음을 보여줍니다.

외부 범위는 초기값이 없는 `r`이라는 변수를 선언하고 \[1], 내부 범위는 초기값이 `5`인 `x`라는 변수를 선언합니다 \[2]. 내부 범위 내에서 `r`의 값을 `x`에 대한 참조로 설정하려고 시도합니다 \[3]. 그런 다음 내부 범위가 종료되고 \[4], `r`의 값을 출력하려고 시도합니다 \[5]. 이 코드는 `r`이 참조하는 값이 사용하려는 시점 전에 범위를 벗어나기 때문에 컴파일되지 않습니다. 다음은 오류 메시지입니다.

```bash
error[E0597]: `x` does not live long enough
 --> src/main.rs:6:13
  |
6 |         r = &x;
  |             ^^ borrowed value does not live long enough
7 |     }
  |     - `x` dropped here while still borrowed
8 |
9 |     println!("r: {r}");
  |                   - borrow later used here
```

오류 메시지는 변수 `x`가 "충분히 오래 살지 못한다"고 말합니다. 그 이유는 7 행에서 내부 범위가 종료될 때 `x`가 범위를 벗어나기 때문입니다. 그러나 `r`은 외부 범위에 대해 여전히 유효합니다. 해당 범위가 더 크기 때문에 "더 오래 산다"고 말합니다. Rust 가 이 코드가 작동하도록 허용했다면, `r`은 `x`가 범위를 벗어났을 때 할당 해제된 메모리를 참조하게 될 것이고, `r`으로 하려는 모든 작업은 제대로 작동하지 않을 것입니다. 그렇다면 Rust 는 이 코드가 유효하지 않다는 것을 어떻게 결정할까요? 차용 검사기 (borrow checker) 를 사용합니다.
