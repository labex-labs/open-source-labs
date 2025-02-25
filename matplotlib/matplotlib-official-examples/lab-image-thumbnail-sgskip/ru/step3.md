# Анализ аргументов

В этом шаге вы будете анализировать аргументы, переданные в вашу программу. Вам необходимо создать объект `ArgumentParser` и добавить аргумент с именем `imagedir`. Этот аргумент задает путь к директории, содержащей изображения. Вы можете использовать параметр `type`, чтобы указать тип данных аргумента. В этом случае аргумент должен быть типа `Path`.

```python
parser = ArgumentParser(description="Build thumbnails of all images in a directory.")
parser.add_argument("imagedir", type=Path)
args = parser.parse_args()
```
