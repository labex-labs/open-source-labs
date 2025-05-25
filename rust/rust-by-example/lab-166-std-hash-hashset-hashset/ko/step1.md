# HashSet

`HashSet`은 키 (key) 만 중요하게 생각하는 `HashMap`과 같다고 생각해 볼 수 있습니다. (`HashSet<T>`는 실제로 `HashMap<T, ()>`의 래퍼일 뿐입니다).

"그게 무슨 의미인가요?"라고 물을 수 있습니다. "`Vec`에 키를 저장하면 되지 않나요?"

`HashSet`의 독특한 특징은 중복된 요소가 없다는 점입니다. 이는 모든 집합 컬렉션이 충족해야 하는 조건입니다. `HashSet`은 그러한 구현 중 하나일 뿐입니다. (참고: `BTreeSet`)

`HashSet`에 이미 존재하는 값을 삽입하면 (즉, 새 값이 기존 값과 같고 해시 값도 같으면), 새 값이 이전 값을 대체합니다.

이것은 어떤 항목을 하나 이상 원하지 않을 때 또는 이미 어떤 항목을 가지고 있는지 알고 싶을 때 유용합니다.

하지만 집합은 그 이상의 기능을 제공합니다.

집합에는 4 가지 주요 연산이 있습니다 (다음 모든 호출은 반복자를 반환합니다):

- `union`: 두 집합 모두에 있는 모든 고유한 요소를 가져옵니다.

- `difference`: 첫 번째 집합에 있지만 두 번째 집합에는 없는 모든 요소를 가져옵니다.

- `intersection`: 두 집합 모두에만 있는 모든 요소를 가져옵니다.

- `symmetric_difference`: 한 집합 또는 다른 집합에 있지만 _두 집합 모두에 없는_ 모든 요소를 가져옵니다.

다음 예제에서 이러한 모든 연산을 시도해 보세요:

```rust
use std::collections::HashSet;

fn main() {
    let mut a: HashSet<i32> = vec![1i32, 2, 3].into_iter().collect();
    let mut b: HashSet<i32> = vec![2i32, 3, 4].into_iter().collect();

    assert!(a.insert(4));
    assert!(a.contains(&4));

    // `HashSet::insert()` 는 이미 값이 있으면 false 를 반환합니다.
    assert!(b.insert(4), "값 4 는 이미 집합 B 에 있습니다!");
    // FIXME ^ 이 줄을 주석 처리하세요

    b.insert(5);

    // 컬렉션의 요소 유형이 `Debug` 를 구현하면
    // 해당 컬렉션도 `Debug` 를 구현합니다.
    // 일반적으로 요소를 `[elem1, elem2, ...]` 형식으로 출력합니다.
    println!("A: {:?}", a);
    println!("B: {:?}", b);

    // 임의의 순서로 [1, 2, 3, 4, 5] 를 출력합니다.
    println!("Union: {:?}", a.union(&b).collect::<Vec<&i32>>());

    // 이것은 [1] 을 출력해야 합니다.
    println!("Difference: {:?}", a.difference(&b).collect::<Vec<&i32>>());

    // 임의의 순서로 [2, 3, 4] 를 출력합니다.
    println!("Intersection: {:?}", a.intersection(&b).collect::<Vec<&i32>>());

    // [1, 5] 를 출력합니다.
    println!("Symmetric Difference: {:?}",
             a.symmetric_difference(&b).collect::<Vec<&i32>>());
}
```

(예제는 설명서에서 수정되었습니다.)
