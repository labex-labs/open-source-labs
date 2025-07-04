# Элиминация жизненных циклов

Вы узнали, что каждая ссылка имеет жизненный цикл и что вам нужно указывать параметры жизненных циклов для функций или структур, которые используют ссылки. Однако, в Listing 4-9 была функция, показанная снова в Listing 10-25, которая скомпилировалась без аннотаций жизненных циклов.

Имя файла: `src/lib.rs`

```rust
fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}
```

Listing 10-25: Функция, которую мы определили в Listing 4-9, которая скомпилировалась без аннотаций жизненных циклов, хотя параметр и возвращаемый тип - ссылки

Причина, по которой эта функция компилируется без аннотаций жизненных циклов, историческая: в ранних версиях (до 1.0) Rust этот код не скомпилировался, потому что каждая ссылка требовала явного жизненного цикла. В то время сигнатура функции была записана так:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

После написания большого количества кода на Rust команда разработчиков Rust обнаружила, что программисты на Rust часто повторялись с теми же аннотациями жизненных циклов в определенных ситуациях. Эти ситуации были предсказуемыми и следовали нескольким определенным паттернам. Разработчики встроили эти паттерны в код компилятора, чтобы проверщик заимствований мог выводить жизненные циклы в этих ситуациях и не требовал явных аннотаций.

Это историческое обстоятельство в Rust важно, потому что возможно, что будут выявлены и добавлены в компилятор еще более определенные паттерны. В будущем может потребоваться еще меньше аннотаций жизненных циклов.

Паттерны, встроенные в анализ ссылок Rust, называются _правилами элиминации жизненных циклов_. Это не правила, которые должны следовать программисты; это набор особых случаев, которые компилятор будет рассматривать, и если ваш код соответствует этим случаям, вы не нужно явно писать жизненные циклы.

Правила элиминации не обеспечивают полного вывода. Если Rust определенно применяет правила, но по-прежнему остается неясно, какие жизненные циклы имеют ссылки, компилятор не будет гадать, какой должен быть жизненный цикл оставшихся ссылок. Вместо гадания компилятор выдаст ошибку, которую вы сможете исправить, добавив аннотации жизненных циклов.

Жизненные циклы на параметрах функций или методов называются _входными жизненными циклами_, а жизненные циклы на возвращаемых значениях - _выходными жизненными циклами_.

Компилятор использует три правила, чтобы определить жизненные циклы ссылок, когда явных аннотаций нет. Первое правило относится к входным жизненным циклам, а второе и третье правила - к выходным жизненным циклам. Если компилятор доходит до конца трех правил и по-прежнему есть ссылки, для которых он не может определить жизненные циклы, компилятор остановится с ошибкой. Эти правила применяются к определениям `fn` и `impl` блокам.

Первое правило заключается в том, что компилятор назначает параметр жизненного цикла каждому параметру, который является ссылкой. Другими словами, функция с одним параметром получает один параметр жизненного цикла: `fn foo<'a>(x: &'a i32)`; функция с двумя параметрами получает два отдельных параметра жизненного цикла: `fn foo<'a, 'b>(x: &'a i32, y: &'b i32)`; и так далее.

Второе правило гласит, что, если есть ровно один входной параметр с жизненным циклом, этот жизненный цикл назначается всем выходным параметрам с жизненным циклом: `fn foo<'a>(x: &'a i32) -> &'a i32`.

Третье правило гласит, что, если есть несколько входных параметров с жизненными циклами, но один из них - `&self` или `&mut self`, потому что это метод, то жизненный цикл `self` назначается всем выходным параметрам с жизненным циклом. Это третье правило делает методы приятнее для чтения и записи, потому что требуется меньше символов.

Давайте предположим, что мы являемся компилятором. Мы применим эти правила, чтобы определить жизненные циклы ссылок в сигнатуре функции `first_word` из Listing 10-25. Сигнатура начинается без каких-либо жизненных циклов, связанных с ссылками:

```rust
fn first_word(s: &str) -> &str {
```

Затем компилятор применяет первое правило, которое规定，что каждый параметр получает свой собственный жизненный цикл. Мы назовем его `'a`, как обычно, поэтому теперь сигнатура выглядит так:

```rust
fn first_word<'a>(s: &'a str) -> &str {
```

Второе правило применяется, потому что есть ровно один входной жизненный цикл. Второе правило规定，что жизненный цикл одного входного параметра назначается выходному параметру с жизненным циклом, поэтому сигнатура теперь выглядит так:

```rust
fn first_word<'a>(s: &'a str) -> &'a str {
```

Теперь все ссылки в этой сигнатуре функции имеют жизненные циклы, и компилятор может продолжить свой анализ, не требая от программиста аннотировать жизненные циклы в этой сигнатуре функции.

Давайте рассмотрим другой пример, на этот раз используя функцию `longest`, которая не имела параметров жизненных циклов, когда мы начали работать с ней в Listing 10-20:

```rust
fn longest(x: &str, y: &str) -> &str {
```

Применим первое правило: каждый параметр получает свой собственный жизненный цикл. На этот раз у нас два параметра вместо одного, поэтому у нас два жизненных цикла:

```rust
fn longest<'a, 'b>(x: &'a str, y: &'b str) -> &str {
```

Вы можете видеть, что второе правило не применяется, потому что есть более одного входного жизненного цикла. Третье правило также не применяется, потому что `longest` - это функция, а не метод, поэтому ни один из параметров не является `self`. После прохождения всех трех правил мы по-прежнему не определили, какой должен быть жизненный цикл возвращаемого типа. Именно поэтому мы получили ошибку при попытке скомпилировать код из Listing 10-20: компилятор прошел по правилам элиминации жизненных циклов, но по-прежнему не смог определить все жизненные циклы ссылок в сигнатуре.

Поскольку третье правило действительно применяется только в сигнатурах методов, мы рассмотрим жизненные циклы в этом контексте дальше, чтобы понять, почему третье правило означает, что мы не нужно часто аннотировать жизненные циклы в сигнатурах методов.
