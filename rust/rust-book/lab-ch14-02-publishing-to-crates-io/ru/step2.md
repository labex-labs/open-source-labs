# Создание полезных комментариев документации

Точная документация ваших пакетов поможет другим пользователям понять, как и когда их использовать, поэтому стоит потратить время на написание документации. В главе 3 мы обсуждали, как комментировать Rust-код с использованием двух слэшей, `//`. Rust также имеет особый вид комментария для документации, который удобно называется _комментарием документации_, и который генерирует HTML-документацию. HTML отображает содержимое комментариев документации для публичных API-элементов, предназначенных для программистов, которые интересуются тем, как _использовать_ ваш коробок, а не как он _реализован_.

Комментарии документации используют три слэша, `///`, вместо двух и поддерживают разметку Markdown для форматирования текста. Размещайте комментарии документации сразу перед элементом, который они документируют. Список 14-1 показывает комментарии документации для функции `add_one` в коробке с именем `my_crate`.

Имя файла: `src/lib.rs`

````rust
/// Добавляет единицу к заданному числу.
///
/// # Примеры
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
///
/// assert_eq!(6, answer);
/// ```rust
pub fn add_one(x: i32) -> i32 {
    x + 1
}
````

Список 14-1: Комментарий документации для функции

Здесь мы даем описание того, что делает функция `add_one`, начинаем раздел с заголовком `Примеры` и затем предоставляем код, демонстрирующий, как использовать функцию `add_one`. Мы можем сгенерировать HTML-документацию из этого комментария документации, запустив `cargo doc`. Эта команда запускает инструмент `rustdoc`, поставляемый вместе с Rust, и помещает сгенерированную HTML-документацию в каталог `target/doc`.

Для удобства запуск `cargo doc --open` создаст HTML-документацию для текущего коробка (а также документацию для всех зависимостей вашего коробка) и откроет результат в веб-браузере. Перейдите к функции `add_one`, и вы увидите, как отображается текст в комментариях документации, как показано на рис. 14-1.

Рисунок 14-1: HTML-документация для функции `add_one`
