# Отметка версий на crates.io как устаревших с помощью cargo yank

Хотя вы не можете удалить предыдущие версии коробки, вы можете предотвратить добавление их в качестве новых зависимостей в будущих проектах. Это полезно, когда версия коробки по какой-то причине не работает. В таких случаях Cargo поддерживает помечаение версии коробки как устаревшей.

_Помечание_ версии как устаревшей предотвращает добавление этой версии в зависимости для новых проектов, при этом позволяет всем существующим проектам, которые зависят от нее, продолжать работу. По сути, помечаение означает, что все проекты с _Cargo.lock_ не будут сломаны, и любые будущие сгенерированные файлы _Cargo.lock_ не будут использовать помеченную версию.

Чтобы пометить версию коробки как устаревшую, в директории коробки, которую вы ранее опубликовали, запустите `cargo yank` и укажите, какую версию вы хотите пометить. Например, если мы опубликовали коробку под названием `guessing_game` версии 1.0.1 и хотим пометить ее, в директории проекта `guessing_game` мы выполним:

```bash
$ cargo yank --vers 1.0.1
Updating crates.io index
Yank guessing_game@1.0.1
```

Добавив `--undo` к команде, вы также можете отменить пометку и снова разрешить проектам зависеть от версии:

```bash
$ cargo yank --vers 1.0.1 --undo
Updating crates.io index
Unyank guessing_game@1.0.1
```

Пометка версии как устаревшей _не_ удаляет никакого кода. Например, она не может удалить случайно загруженные секреты. Если это случилось, вы должны немедленно сбросить эти секреты.
