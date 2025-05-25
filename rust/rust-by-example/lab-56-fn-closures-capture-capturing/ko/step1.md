# 캡처

클로저는 본질적으로 유연하며, 주석 없이도 클로저가 작동하도록 기능이 필요한 작업을 수행합니다. 이를 통해 캡처는 사용 사례에 따라 유연하게 적응할 수 있으며, 때로는 이동하고 때로는 빌림을 합니다. 클로저는 변수를 다음과 같이 캡처할 수 있습니다.

- 참조: `&T`
- 가변 참조: `&mut T`
- 값: `T`

클로저는 변수를 참조로 캡처하는 것을 우선하며, 필요한 경우에만 값으로 캡처합니다.

```rust
fn main() {
    use std::mem;

    let color = String::from("green");

    // `color` 를 출력하는 클로저로, `color` 를 즉시 참조 (`&`) 하고
    // 참조와 클로저를 `print` 변수에 저장합니다. `print` 가 마지막으로 사용될 때까지
    // 참조가 유지됩니다.
    //
    // `println!` 는 불변 참조로만 인수를 요구하므로 더 제한적인 것을 강제하지 않습니다.
    let print = || println!("`color`: {}", color);

    // 참조를 사용하여 클로저를 호출합니다.
    print();

    // 클로저가 `color` 에 대한 불변 참조만 보유하고 있으므로 `color` 를 다시 불변으로 참조할 수 있습니다.
    let _reborrow = &color;
    print();

    // 마지막으로 `print` 를 사용한 후 이동 또는 재빌림이 허용됩니다.
    let _color_moved = color;


    let mut count = 0;
    // `count` 를 증가시키는 클로저는 `&mut count` 또는 `count` 를 사용할 수 있지만,
    // `&mut count`가 덜 제한적이므로 이것을 사용합니다. 즉시 `count` 를 참조합니다.
    //
    // `inc` 에 `mut` 가 필요한 이유는 `&mut` 가 내부에 저장되기 때문입니다. 따라서
    // 클로저를 호출하면 클로저가 변경되므로 `mut` 가 필요합니다.
    let mut inc = || {
        count += 1;
        println!("`count`: {}", count);
    };

    // 가변 참조를 사용하여 클로저를 호출합니다.
    inc();

    // 클로저는 나중에 호출되기 때문에 여전히 `count` 를 가변으로 참조합니다.
    // 재빌림 시도는 오류로 이어집니다.
    // let _reborrow = &count;
    // ^ TODO: 이 줄을 주석 해제해 보세요.
    inc();

    // 클로저가 더 이상 `&mut count`를 참조할 필요가 없으므로 오류 없이 재빌림이 가능합니다.
    let _count_reborrowed = &mut count;


    // 복사할 수 없는 형식.
    let movable = Box::new(3);

    // `mem::drop` 은 `T` 를 요구하므로 값으로 가져와야 합니다. 복사 가능한 형식은 클로저로 복사하여 원본을 변경하지 않습니다.
    // 복사할 수 없는 형식은 이동해야 하므로 `movable` 는 즉시 클로저로 이동합니다.
    let consume = || {
        println!("`movable`: {:?}", movable);
        mem::drop(movable);
    };

    // `consume` 은 변수를 소비하므로 한 번만 호출할 수 있습니다.
    consume();
    // consume();
    // ^ TODO: 이 줄을 주석 해제해 보세요.
}
```

수직 파이프 앞에 `move`를 사용하면 클로저가 캡처된 변수의 소유권을 가져옵니다.

```rust
fn main() {
    // `Vec` 은 복사할 수 없는 의미론을 가집니다.
    let haystack = vec![1, 2, 3];

    let contains = move |needle| haystack.contains(needle);

    println!("{}", contains(&1));
    println!("{}", contains(&4));

    // println!("There're {} elements in vec", haystack.len());
    // ^ 위의 줄을 주석 해제하면 컴파일 타임 오류가 발생합니다.
    // 빌림 검사기는 변수가 이동된 후 재사용하는 것을 허용하지 않기 때문입니다.

    // 클로저의 서명에서 `move` 를 제거하면 클로저가 _haystack_ 변수를 불변으로 참조하므로 _haystack_은 여전히
    // 사용 가능하며 위의 줄을 주석 해제해도 오류가 발생하지 않습니다.
}
```
