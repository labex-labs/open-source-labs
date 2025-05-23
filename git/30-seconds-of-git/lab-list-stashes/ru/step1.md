# Перечислить все сохраненные изменения

Вы работаете над проектом в репозитории Git и внесли некоторые изменения, которые еще не готовы быть закоммичены. Вы решаете сохранить эти изменения, чтобы можно было работать над другой задачей. Позже вы хотите увидеть список всех сохраненных изменений, которые вы создали, чтобы определить, какое из них применить. Как вы перечислите все сохраненные изменения в репозитории Git?

1. Перейдите в директорию `git-playground`:

```
cd git-playground
```

2. Создайте новый файл с именем `test.txt` и добавьте в него некоторый контент:

```
echo "hello,world" > test.txt
git add.
```

3. Используйте следующую команду, чтобы сохранить ваши изменения:

```
git stash save "Added test.txt"
```

4. Создайте еще один новый файл с именем `test2.txt` и добавьте в него некоторый контент:

```
echo "hello,labex" > test2.txt
git add.
```

5. Используйте следующую команду, чтобы сохранить ваши изменения:

```
git stash save "Added test2.txt"
```

6. Используйте следующую команду, чтобы перечислить все сохраненные изменения:

```
git stash list
```

Вы должны увидеть вывод, похожий на следующий:

```
stash@{0}: On master: Added test2.txt
stash@{1}: On master: Added test.txt
```
