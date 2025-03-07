# Запуск кода при очистке с помощью трейта Drop

Второй важный для шаблона умных указателей трейт — это `Drop`, который позволяет настроить то, что происходит, когда значение выходит за пределы области видимости. Вы можете предоставить реализацию для трейта `Drop` для любого типа, и этот код может быть использован для освобождения ресурсов, таких как файлы или соединения с сетью.

Мы представляем трейт `Drop` в контексте умных указателей, потому что функциональность трейта `Drop`几乎总是在实现智能指针时使用。例如，当`Box<T>`被释放时，它将释放盒子所指向的堆上的空间。

В некоторых языках для некоторых типов программисту приходится вызывать код для освобождения памяти или ресурсов каждый раз, когда он заканчивает использовать экземпляр этих типов. Например, это включает в себя файловые дескрипторы, сокеты и блокировки. Если они забывают, система может перегрузиться и упасть. В Rust вы можете указать, чтобы определённый кусок кода выполнялся каждый раз, когда значение выходит за пределы области видимости, и компилятор автоматически вставит этот код. Таким образом, вам не нужно беспокоиться о том, где размещать код по очистке в программе, когда экземпляр определённого типа заканчивается — вы по-прежнему не будете утешать ресурсы!

Вы указываете код для выполнения, когда значение выходит за пределы области видимости, реализуя трейт `Drop`. Трейт `Drop` требует от вас реализации одного метода с именем `drop`, который принимает изменяемую ссылку на `self`. Чтобы понять, когда Rust вызывает `drop`, давайте реализуем `drop` с помощью инструкций `println!` на данный момент.

Listing 15-14 показывает структуру `CustomSmartPointer`, чья единственная настраиваемая функциональность заключается в том, что она будет выводить `Dropping CustomSmartPointer!` когда экземпляр выходит за пределы области видимости, чтобы показать, когда Rust запускает метод `drop`.

Filename: `src/main.rs`

```rust
struct CustomSmartPointer {
    data: String,
}

1 impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
      2 println!(
            "Dropping CustomSmartPointer with data `{}`!",
            self.data
        );
    }
}

fn main() {
  3 let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
  4 let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };
  5 println!("CustomSmartPointers created.");
6 }
```

Listing 15-14: Структура `CustomSmartPointer`, которая реализует трейт `Drop`, где мы будем размещать код по очистке

Трейт `Drop` включен в прелюд, поэтому мы не нужно подключать его в область видимости. Мы реализуем трейт `Drop` для `CustomSmartPointer` \[1\] и предоставляем реализацию для метода `drop`, который вызывает `println!` \[2\]. Тело метода `drop` — это то место, где вы можете разместить любую логику, которую хотите выполнить, когда экземпляр вашего типа выходит за пределы области видимости. Здесь мы выводим некоторый текст, чтобы показать визуально, когда Rust вызовет `drop`.

В `main` мы создаём два экземпляра `CustomSmartPointer` в \[3\] и \[4\], а затем выводим `CustomSmartPointers created` \[5\]. В конце `main` \[6\] наши экземпляры `CustomSmartPointer` выйдут за пределы области видимости, и Rust вызовет код, который мы поместили в метод `drop` \[2\], выводя наше финальное сообщение. Обратите внимание, что нам не нужно явно вызывать метод `drop`.

Когда мы запускаем эту программу, мы увидим следующий вывод:

    CustomSmartPointers created.
    Dropping CustomSmartPointer with data `other stuff`!
    Dropping CustomSmartPointer with data `my stuff`!

Rust автоматически вызвал `drop` для нас, когда наши экземпляры вышли за пределы области видимости, вызывая код, который мы указали. Переменные удаляются в обратном порядке их создания, поэтому `d` был удален перед `c`. Цель этого примера — дать вам визуальное руководство по тому, как работает метод `drop`; обычно вы бы указали код по очистке, который ваш тип должен выполнять, а не сообщение для печати.

К сожалению, не так просто отключить автоматическую функциональность `drop`. Отключение `drop` обычно не нужно; вся суть трейта `Drop` в том, что это делается автоматически. Иногда, однако, вы можете захотеть очистить значение заранее. Например, когда используете умные указатели, которые управляют блокировками: вы можете захотеть заставить метод `drop`, который освобождает блокировку, чтобы другой код в той же области видимости мог получить блокировку. Rust не позволяет вам явно вызывать метод `drop` из трейта `Drop`; вместо этого вы должны вызвать функцию `std::mem::drop` из стандартной библиотеки, если вы хотите заставить значение быть удалённым до конца его области видимости.

Если мы попытаемся явно вызвать метод `drop` из трейта `Drop`, изменив функцию `main` из Listing 15-14, как показано в Listing 15-15, мы получим ошибку компиляции.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-15: Попытка явно вызвать метод `drop` из трейта `Drop` для ранней очистки

Когда мы пытаемся скомпилировать этот код, мы получим эту ошибку:

```bash
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`
```

Это сообщение об ошибке говорит, что нам не разрешается явно вызывать `drop`. Сообщение об ошибке использует термин _деструктор_, который является общим термином программирования для функции, которая очищает экземпляр. _Деструктор_ аналогичен _конструктору_, который создает экземпляр. Функция `drop` в Rust — это один конкретный деструктор.

Rust не позволяет нам явно вызывать `drop`, потому что Rust по-прежнему автоматически вызовет `drop` для значения в конце `main`. Это вызовет ошибку _двойного освобождения_, потому что Rust будет пытаться очистить одно и то же значение дважды.

Мы не можем отключить автоматическую вставку `drop`, когда значение выходит за пределы области видимости, и мы не можем явно вызывать метод `drop`. Поэтому, если нам нужно заставить значение быть очищенным заранее, мы используем функцию `std::mem::drop`.

Функция `std::mem::drop` отличается от метода `drop` в трейте `Drop`. Мы вызываем её, передав в качестве аргумента значение, которое мы хотим принудительно удалить. Функция находится в прелюде, поэтому мы можем изменить `main` в Listing 15-15 для вызова функции `drop`, как показано в Listing 15-16.

Filename: `src/main.rs`

```rust
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!(
        "CustomSmartPointer dropped before the end of main."
    );
}
```

Listing 15-16: Вызов `std::mem::drop` для явного удаления значения, пока оно не выходит за пределы области видимости

Запуск этого кода выведет следующее:

    CustomSmartPointer created.
    Dropping CustomSmartPointer with data `some data`!
    CustomSmartPointer dropped before the end of main.

Текст `Dropping CustomSmartPointer with data`some data`!` выводится между текстами `CustomSmartPointer created.` и `CustomSmartPointer dropped before the end of main.`, показывая, что код метода `drop` вызывается для удаления `c` в этот момент.

Вы можете использовать код, указанный в реализации трейта `Drop`, многими способами, чтобы сделать очистку удобной и безопасной: например, вы можете использовать его для создания собственного аллокатора памяти! С помощью трейта `Drop` и системы владения в Rust вам не нужно запоминать, чтобы выполнять очистку, потому что Rust делает это автоматически.

Вы также не нужно беспокоиться о проблемах, возникающих из-за случайной очистки значений, которые по-прежнему используются: система владения, которая гарантирует, что ссылки всегда действительны, также гарантирует, что `drop` вызывается только один раз, когда значение больше не используется.

Теперь, когда мы изучили `Box<T>` и некоторые характеристики умных указателей, давайте рассмотрим несколько других умных указателей, определённых в стандартной библиотеке.
