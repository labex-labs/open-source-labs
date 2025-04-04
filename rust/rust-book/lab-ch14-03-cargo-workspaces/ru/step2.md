# Создание рабочего пространства

_Рабочее пространство_ — это набор пакетов, которые используют один и тот же _Cargo.lock_ и директорию вывода. Создадим проект с использованием рабочего пространства — мы будем использовать простой код, чтобы сосредоточиться на структуре рабочего пространства. Существует несколько способов структурировать рабочее пространство, поэтому мы покажем только один распространенный способ. У нас будет рабочее пространство, содержащее бинарный файл и две библиотеки. Бинарный файл, который обеспечит основную функциональность, будет зависеть от двух библиотек. Одна библиотека будет предоставлять функцию `add_one`, а другая библиотека — функцию `add_two`. Эти три ящика будут частью одного рабочего пространства. Мы начнем с создания новой директории для рабочего пространства:

```bash
mkdir add
cd add
```

Далее, в директории `add` создаем файл `Cargo.toml`, который будет настраивать целое рабочее пространство. Этот файл не будет иметь секции `[package]`. Вместо этого он будет начинаться с секции `[workspace]`, которая позволит нам добавить члены в рабочее пространство, указав путь к пакету с нашим бинарным ящиком; в этом случае путь — это _adder_:

Имя файла: `Cargo.toml`

```toml
[workspace]

members = [
    "adder",
]
```

Далее, мы создадим бинарный ящик `adder`, выполнив `cargo new` внутри директории `add`:

```bash
$ cargo new adder
     Created binary (application) `adder` package
```

На этом этапе мы можем собрать рабочее пространство, выполнив `cargo build`. Файлы в директории `add` должны выглядеть так:

    ├── Cargo.lock
    ├── Cargo.toml
    ├── adder
    │   ├── Cargo.toml
    │   └── src
    │       └── main.rs
    └── target

Рабочее пространство имеет одну директорию `target` на верхнем уровне, в которую будут помещены скомпилированные артефакты; пакет `adder` не имеет собственной директории `target`. Даже если мы выполним `cargo build` из директории `adder`, скомпилированные артефакты по-прежнему окажутся в _add/target_, а не в `add/adder/target`. Cargo структурирует директорию `target` в рабочем пространстве именно так, потому что ящики в рабочем пространстве должны зависеть друг от друга. Если каждый ящик имел свою собственную директорию `target`, каждый ящик должен был бы пересобрать каждый из других ящиков в рабочем пространстве, чтобы поместить артефакты в свою собственную директорию `target`. С помощью разделения одной директории `target` ящики могут избежать ненужной перекомпиляции.
