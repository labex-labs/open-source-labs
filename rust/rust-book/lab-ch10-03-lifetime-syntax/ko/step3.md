# 차용 검사기 (Borrow Checker)

Rust 컴파일러에는 모든 차용 (borrow) 이 유효한지 확인하기 위해 범위를 비교하는 *차용 검사기*가 있습니다. Listing 10-17 은 Listing 10-16 과 동일한 코드를 보여주지만 변수의 생명주기를 주석 처리했습니다.

```rust
fn main() {
    let r;                // ---------+-- 'a
                          //          |
    {                     //          |
        let x = 5;        // -+-- 'b  |
        r = &x;           //  |       |
    }                     // -+       |
                          //          |
    println!("r: {r}");   //          |
}                         // ---------+
```

Listing 10-17: 각각 `'a`와 `'b`로 명명된 `r`과 `x`의 생명주기 주석

여기서 `r`의 생명주기를 `'a`로, `x`의 생명주기를 `'b`로 주석 처리했습니다. 보시다시피 내부 `'b` 블록은 외부 `'a` 생명주기 블록보다 훨씬 작습니다. 컴파일 시간에 Rust 는 두 생명주기의 크기를 비교하고 `r`의 생명주기는 `'a`이지만 `'b`의 생명주기를 가진 메모리를 참조한다는 것을 확인합니다. 프로그램은 `'b`가 `'a`보다 짧기 때문에 거부됩니다. 즉, 참조 대상이 참조만큼 오래 살지 못합니다.

Listing 10-18 은 댕글링 참조가 없고 오류 없이 컴파일되는 코드를 수정합니다.

```rust
fn main() {
    let x = 5;            // ----------+-- 'b
                          //           |
    let r = &x;           // --+-- 'a  |
                          //   |       |
    println!("r: {r}");   //   |       |
                          // --+       |
}                         // ----------+
```

Listing 10-18: 데이터가 참조보다 더 긴 생명주기를 가지므로 유효한 참조

여기서 `x`는 `'b` 생명주기를 가지며, 이 경우 `'a`보다 큽니다. 즉, Rust 는 `r`의 참조가 `x`가 유효한 동안 항상 유효하다는 것을 알고 있으므로 `r`이 `x`를 참조할 수 있습니다.

이제 참조의 생명주기가 어디에 있는지, 그리고 Rust 가 참조가 항상 유효하도록 생명주기를 분석하는 방법을 알았으므로 함수의 컨텍스트에서 매개변수 및 반환 값의 제네릭 생명주기를 살펴보겠습니다.
