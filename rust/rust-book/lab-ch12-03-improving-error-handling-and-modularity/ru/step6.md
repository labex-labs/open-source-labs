# Fixing the Error Handling

Теперь мы поработаем над исправлением нашей обработки ошибок. Напомним, что попытка получить доступ к значениям в векторе `args` по индексу 1 или индексу 2 вызовет панику программы, если в векторе меньше трех элементов. Попробуйте запустить программу без аргументов; она будет выглядеть так:

```bash
$ cargo run
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
     Running `target/debug/minigrep`
thread 'main' panicked at 'index out of bounds: the len is 1 but
the index is 1', src/main.rs:27:21
note: run with `RUST_BACKTRACE=1` environment variable to display
a backtrace
```

Строка `index out of bounds: the len is 1 but the index is 1` — это сообщение об ошибке для программистов. Это не поможет нашим конечным пользователям понять, что они должны сделать вместо этого. Исправим это сейчас.
