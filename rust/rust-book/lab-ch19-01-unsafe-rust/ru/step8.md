# Реализация небезопасного трейта

Мы можем использовать `unsafe`, чтобы реализовать небезопасный трейт. Трейт считается небезопасным, когда по крайней мере один из его методов имеет некоторое инвариантное свойство, которое компилятор не может проверить. Мы объявляем, что трейт небезопасный, добавляя ключевое слово `unsafe` перед `trait` и помечая реализацию трейта как `unsafe` также, как показано в Листинге 19-11.

    unsafe trait Foo {
        // методы здесь
    }

    unsafe impl Foo for i32 {
        // реализации методов здесь
    }

Листинг 19-11: Определение и реализация небезопасного трейта

С помощью `unsafe impl` мы обязуемся соблюдать инварианты, которые компилятор не может проверить.

В качестве примера вспомните маркерные трейты `Send` и `Sync`, о которых мы говорили в разделе "Расширяемая параллельность с трейтами Send и Sync": компилятор автоматически реализует эти трейты, если наши типы полностью состоят из типов `Send` и `Sync`. Если мы реализуем тип, содержащий тип, который не является `Send` или `Sync`, например, сырой указатель, и хотим пометить этот тип как `Send` или `Sync`, мы должны использовать `unsafe`. Rust не может проверить, что наш тип соблюдает гарантии, что его можно безопасно передавать между потоками или доступать из нескольких потоков; поэтому мы должны проводить эти проверки вручную и указать это с помощью `unsafe`.
