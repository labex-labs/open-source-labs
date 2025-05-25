# Union (공용체) 의 필드 접근

`unsafe`에서만 작동하는 마지막 작업은 union (공용체) 의 필드에 접근하는 것입니다. `union`은 `struct`와 유사하지만 특정 인스턴스에서는 선언된 필드 중 하나만 한 번에 사용됩니다. Union 은 주로 C 코드의 union 과 인터페이스하기 위해 사용됩니다. Union 필드에 접근하는 것은 unsafe 합니다. Rust 는 현재 union 인스턴스에 저장된 데이터의 타입을 보장할 수 없기 때문입니다. Rust Reference 에서 union 에 대해 자세히 알아볼 수 있습니다: \*https://doc.rust-lang.org/reference/items/unions.html\*\*.\*
