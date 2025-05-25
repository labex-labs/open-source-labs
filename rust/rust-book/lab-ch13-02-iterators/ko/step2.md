# Iterator 트레이트와 next 메서드

모든 반복자는 표준 라이브러리에 정의된 `Iterator`라는 트레이트를 구현합니다. 트레이트의 정의는 다음과 같습니다.

```rust
pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // methods with default implementations elided
}
```

이 정의는 `type Item` 및 `Self::Item`과 같은 새로운 구문을 사용합니다. 이는 이 트레이트와 함께 *연관 타입 (associated type)*을 정의하는 것입니다. 연관 타입에 대해서는 19 장에서 자세히 다루겠습니다. 지금은 이 코드가 `Iterator` 트레이트를 구현하려면 `Item` 타입도 정의해야 하며, 이 `Item` 타입은 `next` 메서드의 반환 타입에 사용된다는 것만 알면 됩니다. 즉, `Item` 타입은 반복자에서 반환되는 타입이 됩니다.

`Iterator` 트레이트는 구현자가 `next` 메서드 하나만 정의하도록 요구합니다. `next` 메서드는 한 번에 반복자의 항목 하나를 `Some`으로 래핑하여 반환하고, 반복이 끝나면 `None`을 반환합니다.

반복자에서 `next` 메서드를 직접 호출할 수 있습니다. Listing 13-12 는 벡터에서 생성된 반복자에 대해 `next`를 반복적으로 호출하여 어떤 값이 반환되는지 보여줍니다.

파일 이름: `src/lib.rs`

```rust
#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
```

Listing 13-12: 반복자에서 `next` 메서드 호출하기

`v1_iter`을 가변 (mutable) 으로 만들어야 했습니다. 반복자에서 `next` 메서드를 호출하면 반복자가 시퀀스 내에서 어디에 있는지 추적하는 데 사용하는 내부 상태가 변경됩니다. 즉, 이 코드는 반복자를 *소모 (consumes)*하거나 사용합니다. `next`를 호출할 때마다 반복자에서 항목 하나가 소모됩니다. `for` 루프를 사용할 때는 `v1_iter`을 가변으로 만들 필요가 없었습니다. 루프가 `v1_iter`의 소유권을 가져 내부적으로 가변으로 만들었기 때문입니다.

또한 `next`를 호출하여 얻는 값은 벡터의 값에 대한 불변 참조 (immutable references) 라는 점에 유의하십시오. `iter` 메서드는 불변 참조에 대한 반복자를 생성합니다. `v1`의 소유권을 가져 소유된 값을 반환하는 반복자를 생성하려면 `iter` 대신 `into_iter`를 호출할 수 있습니다. 마찬가지로, 가변 참조를 반복하려면 `iter` 대신 `iter_mut`를 호출할 수 있습니다.
