# Rc`<T>` 복제는 참조 카운트를 증가시킵니다

Listing 15-18 의 작동 예제를 변경하여 `a`의 `Rc<List>`에 대한 참조를 생성하고 삭제할 때 참조 카운트가 변경되는 것을 볼 수 있습니다.

Listing 15-19 에서 `main`을 변경하여 리스트 `c` 주변에 내부 범위를 갖도록 합니다. 그러면 `c`가 범위를 벗어날 때 참조 카운트가 어떻게 변경되는지 확인할 수 있습니다.

파일 이름: `src/main.rs`

```rust
--snip--

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!(
        "count after creating a = {}",
        Rc::strong_count(&a)
    );
    let b = Cons(3, Rc::clone(&a));
    println!(
        "count after creating b = {}",
        Rc::strong_count(&a)
    );
    {
        let c = Cons(4, Rc::clone(&a));
        println!(
            "count after creating c = {}",
            Rc::strong_count(&a)
        );
    }
    println!(
        "count after c goes out of scope = {}",
        Rc::strong_count(&a)
    );
}
```

Listing 15-19: 참조 카운트 출력

참조 카운트가 변경되는 프로그램의 각 지점에서 `Rc::strong_count` 함수를 호출하여 얻는 참조 카운트를 출력합니다. 이 함수는 `count` 대신 `strong_count`로 명명되었습니다. `Rc<T>` 타입에는 또한 `weak_count`가 있기 때문입니다. "Weak`<T>`를 사용하여 참조 사이클 방지"에서 `weak_count`가 무엇에 사용되는지 살펴보겠습니다.

이 코드는 다음을 출력합니다.

    count after creating a = 1
    count after creating b = 2
    count after creating c = 3
    count after c goes out of scope = 2

`a`의 `Rc<List>`는 초기 참조 카운트가 1 임을 알 수 있습니다. 그런 다음 `clone`을 호출할 때마다 카운트가 1 씩 증가합니다. `c`가 범위를 벗어나면 카운트가 1 씩 감소합니다. 참조 카운트를 증가시키기 위해 `Rc::clone`을 호출해야 하는 것처럼 참조 카운트를 감소시키기 위해 함수를 호출할 필요는 없습니다. `Drop` 트레이트의 구현은 `Rc<T>` 값이 범위를 벗어날 때 자동으로 참조 카운트를 감소시킵니다.

이 예제에서 볼 수 없는 것은 `b`와 `a`가 `main`의 끝에서 범위를 벗어날 때 카운트가 0 이 되고 `Rc<List>`가 완전히 정리된다는 것입니다. `Rc<T>`를 사용하면 단일 값이 여러 소유자를 가질 수 있으며, 카운트는 소유자가 여전히 존재하는 한 값이 유효하게 유지되도록 보장합니다.

불변 참조를 통해 `Rc<T>`는 프로그램의 여러 부분 간에 읽기 전용으로 데이터를 공유할 수 있습니다. `Rc<T>`가 여러 가변 참조도 허용했다면, 4 장에서 논의한 차용 규칙 중 하나를 위반할 수 있습니다. 동일한 위치에 대한 여러 가변 차용은 데이터 경합 및 불일치를 유발할 수 있습니다. 하지만 데이터를 변경할 수 있는 것은 매우 유용합니다! 다음 섹션에서는 내부 가변성 패턴과 이 불변성 제한 사항을 처리하기 위해 `Rc<T>`와 함께 사용할 수 있는 `RefCell<T>` 타입을 논의합니다.
