# 객체는 데이터와 동작을 포함합니다

Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides 의 저서인 _Design Patterns: Elements of Reusable Object-Oriented Software_ (Addison-Wesley, 1994) 는 통칭하여 _The Gang of Four_ 책이라고 불리며, 객체 지향 디자인 패턴의 카탈로그입니다. 이 책은 OOP 를 다음과 같이 정의합니다.

객체 지향 프로그램은 객체로 구성됩니다. *객체*는 데이터와 해당 데이터를 조작하는 절차를 모두 묶습니다. 절차는 일반적으로 _메소드_ 또는 *연산*이라고 불립니다.

이 정의를 사용하면 Rust 는 객체 지향적입니다. 구조체 (struct) 와 열거형 (enum) 은 데이터를 가지고 있으며, `impl` 블록은 구조체와 열거형에 대한 메소드를 제공합니다. 메소드를 가진 구조체와 열거형이 객체라고 _불리지는_ 않지만, Gang of Four 의 객체 정의에 따르면 동일한 기능을 제공합니다.
