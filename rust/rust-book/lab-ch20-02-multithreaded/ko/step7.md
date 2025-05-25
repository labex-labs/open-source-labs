# new 에서 스레드 수 유효성 검사하기

`new` 및 `execute`의 매개변수로 아무것도 하지 않고 있습니다. 원하는 동작으로 이러한 함수의 본문을 구현해 보겠습니다. 먼저, `new`에 대해 생각해 보겠습니다. 앞서 음수 스레드 수를 가진 풀은 의미가 없기 때문에 `size` 매개변수에 부호 없는 타입을 선택했습니다. 그러나 0 개의 스레드를 가진 풀도 의미가 없지만, 0 은 완벽하게 유효한 `usize`입니다. Listing 20-13 에 표시된 것처럼 `assert!` 매크로를 사용하여 `size`가 0 보다 큰지 확인하는 코드를 추가하고 0 을 받으면 프로그램이 패닉하도록 하겠습니다.

파일 이름: `src/lib.rs`

```rust
impl ThreadPool {
    /// 새로운 ThreadPool 을 생성합니다.
    ///
    /// size 는 풀의 스레드 수입니다.
    ///
  1 /// # Panics
    ///
    /// `new` 함수는 size 가 0 이면 패닉합니다.
    pub fn new(size: usize) -> ThreadPool {
      2 assert!(size > 0);

        ThreadPool
    }

    --snip--
}
```

Listing 20-13: `size`가 0 이면 패닉하도록 `ThreadPool::new` 구현하기

또한 doc 주석을 사용하여 `ThreadPool`에 대한 몇 가지 문서를 추가했습니다. 14 장에서 논의한 것처럼, 함수가 패닉할 수 있는 상황을 명시하는 섹션을 추가하여 훌륭한 문서화 관행을 따랐습니다 \[1]. `cargo doc --open`을 실행하고 `ThreadPool` 구조체를 클릭하여 `new`에 대해 생성된 문서가 어떻게 보이는지 확인해 보세요!

여기에서 수행한 것처럼 `assert!` 매크로를 추가하는 대신 \[2], Listing 12-9 의 I/O 프로젝트에서 `Config::build`를 수행한 것처럼 `new`를 `build`로 변경하고 `Result`를 반환할 수 있습니다. 그러나 이 경우 스레드 없이 스레드 풀을 생성하려고 하는 것은 복구할 수 없는 오류여야 한다고 결정했습니다. 야심이 있다면, `new` 함수와 비교하기 위해 다음 시그니처를 가진 `build`라는 함수를 작성해 보세요.

```rust
pub fn build(
    size: usize
) -> Result<ThreadPool, PoolCreationError> {
```
