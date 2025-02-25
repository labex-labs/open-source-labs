# Проверить директорию

В этом шаге вы проверите, существует ли указанная директория. Если директория не существует, вы выйдете из программы и выведете сообщение об ошибке.

```python
if not args.imagedir.is_dir():
    sys.exit(f"Could not find input directory {args.imagedir}")
```
