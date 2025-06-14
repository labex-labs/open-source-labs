# Box 를 사용하여 재귀적 타입 활성화

*재귀적 타입 (recursive type)*의 값은 자체의 일부로 동일한 타입의 다른 값을 가질 수 있습니다. 재귀적 타입은 컴파일 시간에 Rust 가 타입이 차지하는 공간의 크기를 알아야 하기 때문에 문제를 야기합니다. 그러나 재귀적 타입 값의 중첩은 이론적으로 무한히 계속될 수 있으므로 Rust 는 값에 필요한 공간의 크기를 알 수 없습니다. Box 는 알려진 크기를 가지므로, 재귀적 타입 정의에 box 를 삽입하여 재귀적 타입을 활성화할 수 있습니다.

재귀적 타입의 예로, *cons list*를 살펴보겠습니다. 이는 함수형 프로그래밍 언어에서 일반적으로 발견되는 데이터 타입입니다. 우리가 정의할 cons list 타입은 재귀를 제외하고는 간단합니다. 따라서 우리가 사용할 예제의 개념은 재귀적 타입을 포함하는 더 복잡한 상황에 직면할 때마다 유용할 것입니다.
