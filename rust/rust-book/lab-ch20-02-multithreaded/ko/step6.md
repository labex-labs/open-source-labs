# 컴파일러 기반 개발을 사용하여 ThreadPool 구축하기

Listing 20-12 의 변경 사항을 `src/main.rs`에 적용한 다음, `cargo check`의 컴파일러 오류를 사용하여 개발을 진행해 보겠습니다. 다음은 처음으로 얻는 오류입니다.

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

훌륭합니다! 이 오류는 `ThreadPool` 타입 또는 모듈이 필요하다는 것을 알려주므로, 이제 하나를 구축하겠습니다. `ThreadPool` 구현은 웹 서버가 수행하는 작업의 종류와는 독립적입니다. 따라서 `hello` 크레이트를 바이너리 크레이트에서 라이브러리 크레이트로 전환하여 `ThreadPool` 구현을 포함시키겠습니다. 라이브러리 크레이트로 변경한 후에는 웹 요청을 처리하는 것뿐만 아니라 스레드 풀을 사용하여 수행하려는 모든 작업에 대해 별도의 스레드 풀 라이브러리를 사용할 수도 있습니다.

다음 내용을 포함하는 `src/lib.rs` 파일을 생성합니다. 이는 현재로서는 가질 수 있는 `ThreadPool` 구조체의 가장 간단한 정의입니다.

파일 이름: `src/lib.rs`

```rust
pub struct ThreadPool;
```

그런 다음 `main.rs` 파일을 편집하여 다음 코드를 `src/main.rs`의 맨 위에 추가하여 라이브러리 크레이트에서 `ThreadPool`을 범위 내로 가져옵니다.

파일 이름: `src/main.rs`

```rust
use hello::ThreadPool;
```

이 코드는 아직 작동하지 않지만, 다음 오류를 얻기 위해 다시 확인해 보겠습니다.

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

이 오류는 다음으로 `ThreadPool`에 대해 `new`라는 연관 함수를 생성해야 함을 나타냅니다. 또한 `new`는 인수로 `4`를 허용하고 `ThreadPool` 인스턴스를 반환할 수 있는 하나의 매개변수를 가져야 한다는 것을 알고 있습니다. 이러한 특성을 갖는 가장 간단한 `new` 함수를 구현해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

`size` 매개변수의 타입으로 `usize`를 선택했습니다. 왜냐하면 음수 스레드 수는 말이 안 된다는 것을 알고 있기 때문입니다. 또한 이 `4`를 스레드 컬렉션의 요소 수로 사용할 것이며, 이는 "정수 타입"에서 논의한 것처럼 `usize` 타입의 용도임을 알고 있습니다.

코드를 다시 확인해 보겠습니다.

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

이제 `ThreadPool`에 `execute` 메서드가 없기 때문에 오류가 발생합니다. "유한한 수의 스레드 생성하기"에서 스레드 풀이 `thread::spawn`과 유사한 인터페이스를 가져야 한다고 결정했음을 기억하십시오. 또한 `execute` 함수를 구현하여 제공된 클로저를 가져와 풀의 유휴 스레드에 제공하여 실행하도록 하겠습니다.

`ThreadPool`에 `execute` 메서드를 정의하여 클로저를 매개변수로 받도록 하겠습니다. "클로저에서 캡처된 값을 이동시키고 Fn 트레이트"에서 세 가지 다른 트레이트인 `Fn`, `FnMut`, `FnOnce`를 사용하여 클로저를 매개변수로 사용할 수 있음을 기억하십시오. 여기에서 어떤 종류의 클로저를 사용할지 결정해야 합니다. 결국 표준 라이브러리 `thread::spawn` 구현과 유사한 작업을 수행할 것이므로, `thread::spawn`의 시그니처가 매개변수에 대해 갖는 바운드를 살펴볼 수 있습니다. 문서는 다음을 보여줍니다.

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

`F` 타입 매개변수가 여기서 우리가 관심을 갖는 것입니다. `T` 타입 매개변수는 반환 값과 관련이 있으며, 우리는 그것에 관심이 없습니다. `spawn`이 `F`에 대한 트레이트 바운드로 `FnOnce`를 사용한다는 것을 알 수 있습니다. 이는 우리가 원하는 것일 가능성이 높습니다. 왜냐하면 결국 `execute`에서 얻은 인수를 `spawn`에 전달할 것이기 때문입니다. 요청을 실행하기 위한 스레드가 해당 요청의 클로저를 한 번만 실행하므로, `FnOnce`가 우리가 사용하려는 트레이트라는 것을 더욱 확신할 수 있습니다. 이는 `FnOnce`의 `Once`와 일치합니다.

`F` 타입 매개변수는 또한 트레이트 바운드 `Send`와 라이프타임 바운드 `'static`을 갖습니다. 이는 우리의 상황에서 유용합니다. 클로저를 한 스레드에서 다른 스레드로 전송하려면 `Send`가 필요하고, 스레드가 실행하는 데 얼마나 걸릴지 모르기 때문에 `'static`이 필요합니다. 이러한 바운드를 가진 타입 `F`의 제네릭 매개변수를 사용하는 `ThreadPool`에 `execute` 메서드를 생성해 보겠습니다.

파일 이름: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

이 `FnOnce`는 매개변수를 받지 않고 유닛 타입 `()`을 반환하는 클로저를 나타내므로, `FnOnce` 뒤에 `()`를 계속 사용합니다 \[1]. 함수 정의와 마찬가지로 반환 타입을 시그니처에서 생략할 수 있지만, 매개변수가 없더라도 괄호가 필요합니다.

다시 말하지만, 이것은 `execute` 메서드의 가장 간단한 구현입니다. 아무것도 하지 않지만, 우리는 단지 코드를 컴파일하려고 노력하고 있습니다. 다시 확인해 보겠습니다.

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

컴파일됩니다! 하지만 `cargo run`을 시도하고 브라우저에서 요청을 하면, 장의 시작 부분에서 보았던 브라우저의 오류가 표시됩니다. 우리 라이브러리는 실제로 `execute`에 전달된 클로저를 아직 호출하지 않습니다!

> 참고: Haskell 및 Rust 와 같이 엄격한 컴파일러가 있는 언어에 대해 들을 수 있는 말은 "코드가 컴파일되면 작동한다"는 것입니다. 그러나 이 말은 보편적으로 사실이 아닙니다. 우리 프로젝트는 컴파일되지만, 아무것도 하지 않습니다! 실제 완전한 프로젝트를 구축하는 경우, 코드가 컴파일되고 원하는 동작을 하는지 확인하기 위해 단위 테스트를 작성하는 것이 좋습니다.
