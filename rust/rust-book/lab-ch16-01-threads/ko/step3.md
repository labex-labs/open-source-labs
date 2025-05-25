# join 핸들을 사용하여 모든 스레드가 완료될 때까지 대기

Listing 16-1 의 코드는 메인 스레드가 종료되어 생성된 스레드가 대부분의 경우 조기에 중단될 뿐만 아니라, 스레드가 실행되는 순서에 대한 보장이 없기 때문에 생성된 스레드가 전혀 실행되지 않을 수도 있습니다!

`thread::spawn`의 반환 값을 변수에 저장하여 생성된 스레드가 실행되지 않거나 조기에 종료되는 문제를 해결할 수 있습니다. `thread::spawn`의 반환 유형은 `JoinHandle<T>`입니다. `JoinHandle<T>`는 소유된 값으로, `join` 메서드를 호출하면 해당 스레드가 완료될 때까지 대기합니다. Listing 16-2 는 Listing 16-1 에서 생성한 스레드의 `JoinHandle<T>`를 사용하는 방법과 `join`을 호출하여 `main`이 종료되기 전에 생성된 스레드가 완료되도록 하는 방법을 보여줍니다.

파일 이름: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }

    handle.join().unwrap();
}
```

Listing 16-2: 스레드가 완료될 때까지 실행되도록 보장하기 위해 `thread::spawn`에서 `JoinHandle<T>` 저장

핸들에서 `join`을 호출하면 핸들로 표현되는 스레드가 종료될 때까지 현재 실행 중인 스레드가 블록됩니다. 스레드를 *블로킹 (blocking)*한다는 것은 해당 스레드가 작업을 수행하거나 종료되는 것을 방지한다는 의미입니다. 메인 스레드의 `for` 루프 뒤에 `join` 호출을 배치했으므로, Listing 16-2 를 실행하면 다음과 유사한 출력이 생성됩니다.

    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 1 from the spawned thread!
    hi number 3 from the main thread!
    hi number 2 from the spawned thread!
    hi number 4 from the main thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!

두 스레드는 계속 번갈아 가며 실행되지만, 메인 스레드는 `handle.join()` 호출로 인해 대기하며, 생성된 스레드가 완료될 때까지 종료되지 않습니다.

하지만 `main`의 `for` 루프 앞에 `handle.join()`을 이동하면 어떻게 되는지 살펴보겠습니다. 다음과 같습니다.

파일 이름: `src/main.rs`

```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(1));
        }
    });

    handle.join().unwrap();

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1));
    }
}
```

메인 스레드는 생성된 스레드가 완료될 때까지 대기한 다음 `for` 루프를 실행하므로, 출력은 더 이상 인터리브되지 않습니다. 다음과 같이 표시됩니다.

    hi number 1 from the spawned thread!
    hi number 2 from the spawned thread!
    hi number 3 from the spawned thread!
    hi number 4 from the spawned thread!
    hi number 5 from the spawned thread!
    hi number 6 from the spawned thread!
    hi number 7 from the spawned thread!
    hi number 8 from the spawned thread!
    hi number 9 from the spawned thread!
    hi number 1 from the main thread!
    hi number 2 from the main thread!
    hi number 3 from the main thread!
    hi number 4 from the main thread!

`join`이 호출되는 위치와 같은 작은 세부 사항이 스레드가 동시에 실행되는지 여부에 영향을 미칠 수 있습니다.
