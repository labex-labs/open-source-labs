# 소개

**Reference Cycles Can Leak Memory**에 오신 것을 환영합니다. 이 랩은 [Rust Book](https://doc.rust-lang.org/book/)의 일부입니다. LabEx 에서 Rust 기술을 연습할 수 있습니다.

이 랩에서는 Rust 의 메모리 안전성 보장이 실수로 메모리 누수를 발생시키기 어렵게 만들지만, 불가능하게 만드는 것은 아니라는 점을 살펴봅니다. 특히 `Rc<T>`와 `RefCell<T>`를 사용할 때, 이는 값들이 drop 되지 못하게 하고 메모리 누수를 유발하는 참조 사이클 (reference cycles) 을 초래할 수 있습니다.
