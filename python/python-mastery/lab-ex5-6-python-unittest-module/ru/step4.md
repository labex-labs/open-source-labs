# Запуск выбранных тестов и использование обнаружения тестов

Модуль `unittest` в Python представляет собой мощный инструмент, позволяющий эффективно тестировать ваш код. Он предоставляет несколько способов запуска конкретных тестов или автоматического обнаружения и запуска всех тестов в вашем проекте. Это очень полезно, так как помогает сосредоточиться на определенных частях кода при тестировании или быстро проверить весь набор тестов проекта.

## Запуск конкретных тестов

Иногда вы можете захотеть запустить только определенные тестовые методы или тестовые классы, а не весь набор тестов. Вы можете достичь этого, используя опцию шаблона с модулем `unittest`. Это дает вам больше контроля над тем, какие тесты будут выполнены, что может быть полезно при отладке определенной части кода.

1. Чтобы запустить только тесты, связанные с созданием объекта `Stock`:

```bash
python3 -m unittest teststock.TestStock.test_create
```

В этой команде `python3 -m unittest` сообщает Python запустить модуль `unittest`. `teststock` - это имя тестового файла, `TestStock` - имя тестового класса, а `test_create` - конкретный тестовый метод, который мы хотим запустить. Запустив эту команду, вы можете быстро проверить, работает ли код, связанный с созданием объекта `Stock`, как ожидается.

2. Чтобы запустить все тесты в классе `TestStock`:

```bash
python3 -m unittest teststock.TestStock
```

Здесь мы опускаем имя конкретного тестового метода. Таким образом, эта команда выполнит все тестовые методы внутри класса `TestStock` в файле `teststock`. Это полезно, когда вы хотите проверить общую функциональность тестовых случаев объекта `Stock`.

## Использование обнаружения тестов

Модуль `unittest` может автоматически обнаруживать и запускать все тестовые файлы в вашем проекте. Это избавляет вас от необходимости вручную указывать каждый тестовый файл для запуска, особенно в больших проектах с большим количеством тестовых файлов.

1. Переименуйте текущий файл, чтобы он соответствовал шаблону именования для обнаружения тестов:

```bash
mv teststock.py test_stock.py
```

Механизм обнаружения тестов в `unittest` ищет файлы, соответствующие шаблону именования `test_*.py`. Переименовав файл в `test_stock.py`, мы облегчаем модулю `unittest` поиск и запуск тестов в этом файле.

2. Запустите обнаружение тестов:

```bash
python3 -m unittest discover
```

Эта команда сообщает модулю `unittest` автоматически обнаружить и запустить все тестовые файлы, соответствующие шаблону `test_*.py` в текущем каталоге. Он просмотрит каталог и выполнит все найденные в соответствующих файлах тестовые случаи.

3. Вы также можете указать каталог для поиска тестов:

```bash
python3 -m unittest discover -s . -p "test_*.py"
```

Где:

- `-s .` указывает каталог, с которого начнется поиск (в данном случае текущий каталог). Точка (`.`) представляет текущий каталог. Вы можете изменить это на другой путь к каталогу, если хотите искать тесты в другом месте.
- `-p "test_*.py"` - это шаблон для сопоставления тестовых файлов. Это гарантирует, что в качестве тестовых файлов будут рассматриваться только файлы с именами, начинающимися с `test_` и имеющими расширение `.py`.

Вы должны увидеть, что все 12 тестов запускаются и проходят успешно, как и раньше.

4. Переименуйте файл обратно в исходное имя для согласованности с лабораторной работой:

```bash
mv test_stock.py teststock.py
```

После запуска обнаружения тестов мы переименовываем файл обратно в исходное имя, чтобы сохранить согласованность лабораторной среды.

Используя обнаружение тестов, вы можете легко запустить все тесты в проекте, не указывая каждый тестовый файл отдельно. Это делает процесс тестирования более эффективным и менее подверженным ошибкам.
