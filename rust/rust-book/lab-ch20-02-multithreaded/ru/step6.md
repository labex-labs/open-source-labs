# Построение ThreadPool с использованием разработки, управляемой компилятором

Внесите изменения из Listing 20-12 в `src/main.rs`, а затем используйте ошибки компилятора из `cargo check` для продвижения нашей разработки. Вот первая ошибка, которую мы получаем:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0433]: failed to resolve: use of undeclared type `ThreadPool`
  --> src/main.rs:11:16
   |
11 |     let pool = ThreadPool::new(4);
   |                ^^^^^^^^^^ use of undeclared type `ThreadPool`
```

Отлично! Эта ошибка говорит нам, что нам нужен тип или модуль `ThreadPool`, поэтому мы сейчас построим его. Реализация нашего `ThreadPool` будет независима от вида работы, выполняемой нашим веб-сервером. Поэтому давайте переключим крейт `hello` из бинарного крейта в библиотечный крейт, чтобы поместить в него нашу реализацию `ThreadPool`. После перехода к библиотечному крейту мы также сможем использовать отдельную библиотеку для пула потоков для любой работы, которую мы хотим выполнять с использованием пула потоков, а не только для обслуживания веб-запросов.

Создайте файл `src/lib.rs`, содержащий следующее, что представляет собой самую простую определение структуры `ThreadPool`, которое мы можем иметь на данный момент:

Filename: `src/lib.rs`

```rust
pub struct ThreadPool;
```

Затем отредактируйте файл `main.rs`, чтобы импортировать `ThreadPool` из библиотечного крейта, добавив следующий код в начало `src/main.rs`:

Filename: `src/main.rs`

```rust
use hello::ThreadPool;
```

Этот код по-прежнему не будет работать, но давайте проверим его снова, чтобы получить следующую ошибку, которую нам нужно исправить:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no function or associated item named `new` found for struct
`ThreadPool` in the current scope
  --> src/main.rs:12:28
   |
12 |     let pool = ThreadPool::new(4);
   |                            ^^^ function or associated item not found in
`ThreadPool`
```

Эта ошибка показывает, что дальше нам нужно создать ассоциированную функцию под названием `new` для `ThreadPool`. Мы также знаем, что `new` должен иметь один параметр, который может принимать `4` в качестве аргумента и должен возвращать экземпляр `ThreadPool`. Реализуем самую простую функцию `new`, которая будет обладать этими свойствами:

Filename: `src/lib.rs`

```rust
pub struct ThreadPool;

impl ThreadPool {
    pub fn new(size: usize) -> ThreadPool {
        ThreadPool
    }
}
```

Мы выбрали `usize` в качестве типа параметра `size`, потому что знаем, что отрицательное количество потоков не имеет смысла. Мы также знаем, что будем использовать это `4` в качестве количества элементов в коллекции потоков, для чего предназначен тип `usize`, как обсуждалось в разделе "Целочисленные типы".

Давайте проверим код снова:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `execute` found for struct `ThreadPool` in the
current scope
  --> src/main.rs:17:14
   |
17 |         pool.execute(|| {
   |              ^^^^^^^ method not found in `ThreadPool`
```

Теперь ошибка возникает потому, что у `ThreadPool` нет метода `execute`. Напомним из раздела "Создание конечного количества потоков", что мы решили, что наш пул потоков должен иметь интерфейс, похожий на `thread::spawn`. Кроме того, мы реализуем функцию `execute` так, чтобы она принимала замыкание, которое ей передают, и передавала его неактивному потоку в пуле для выполнения.

Мы определим метод `execute` для `ThreadPool`, чтобы он принимал замыкание в качестве параметра. Напомним из раздела "Перемещение захваченных значений из замыканий и трейтов Fn", что мы можем принимать замыкания в качестве параметров с тремя различными трейтами: `Fn`, `FnMut` и `FnOnce`. Мы должны решить, какой тип замыкания использовать здесь. Мы знаем, что в конечном итоге будем делать что-то похожее на реализацию `thread::spawn` из стандартной библиотеки, поэтому мы можем посмотреть, какие ограничения имеет сигнатура `thread::spawn` на своем параметре. Документация показывает нам следующее:

```rust
pub fn spawn<F, T>(f: F) -> JoinHandle<T>
    where
        F: FnOnce() -> T,
        F: Send + 'static,
        T: Send + 'static,
```

Тип параметр `F` - это то, с чем мы сейчас concerned; тип параметр `T` связан с возвращаемым значением, и мы не заботимся об этом. Мы можем видеть, что `spawn` использует `FnOnce` в качестве ограничения трейта для `F`. Вероятно, это то, что нам и нужно, потому что в конечном итоге мы передадим аргумент, который получаем в `execute` в `spawn`. Мы можем быть более уверены в том, что `FnOnce` - это трейт, который мы хотим использовать, потому что поток для выполнения запроса будет выполнять только один раз замыкание этого запроса, что соответствует `Once` в `FnOnce`.

Тип параметр `F` также имеет ограничение трейта `Send` и ограничение времени жизни `'static`, которые полезны в нашей ситуации: нам нужно `Send`, чтобы передать замыкание из одного потока в другой, и `'static`, потому что мы не знаем, сколько времени поток будет выполняться. Создадим метод `execute` для `ThreadPool`, который будет принимать обобщенный параметр типа `F` с этими ограничениями:

Filename: `src/lib.rs`

```rust
impl ThreadPool {
    --snip--
    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() 1 + Send + 'static,
    {
    }
}
```

Мы по-прежнему используем `()` после `FnOnce` \[1\], потому что этот `FnOnce` представляет собой замыкание, которое не имеет параметров и возвращает единичный тип `()`. Похоже на определения функций, возвращаемый тип может быть опущен из сигнатуры, но даже если у нас нет параметров, мы по-прежнему нуждаемся в скобках.

Опять же, это самая простая реализация метода `execute`: она ничего не делает, но мы просто пытаемся заставить наш код скомпилироваться. Давайте проверим его снова:

```bash
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 0.24s
```

Он скомпилировался! Но обратите внимание, что если вы попытаетесь выполнить `cargo run` и сделать запрос в браузере, вы увидите ошибки в браузере, которые мы видели в начале главы. Наша библиотека еще не вызывает замыкание, переданное в `execute`!

> Примечание: Вы, возможно, слышите выражение о языках с строгими компиляторами, таких как Haskell и Rust: "если код скомпилируется, он работает". Но это утверждение не всегда верно. Наш проект скомпилируется, но он абсолютно ничего не делает! Если бы мы строили настоящий, полноценный проект, это было бы хорошее время для начала написания юнит-тестов, чтобы проверить, что код скомпилируется _и_ имеет нужное поведение.
