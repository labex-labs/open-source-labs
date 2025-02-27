# Перебираем мини - пакеты примеров и обновляем классификаторы

```python
# Мы будем подавать классификатору мини - пакеты по 1000 документам; это означает,
# что в памяти будет в любом случае не более 1000 документов. Чем меньше размер
# пакета документов, тем больше относительный накладной расход методов partial fit.
minibatch_size = 1000

# Создаем data_stream, который разбирает файлы Reuters в формате SGML и
# итерируется по документам как по потоку.
minibatch_iterators = iter_minibatches(data_stream, minibatch_size)
total_vect_time = 0.0

# Основной цикл: итерируемся по мини - пакетам примеров
for i, (X_train_text, y_train) in enumerate(minibatch_iterators):
    tick = time.time()
    X_train = vectorizer.transform(X_train_text)
    total_vect_time += time.time() - tick

    for cls_name, cls in partial_fit_classifiers.items():
        tick = time.time()
        # обновляем оценщик примерами из текущего мини - пакета
        cls.partial_fit(X_train, y_train, classes=all_classes)

        # накапливаем статистику по точности теста
        cls_stats[cls_name]["total_fit_time"] += time.time() - tick
        cls_stats[cls_name]["n_train"] += X_train.shape[0]
        cls_stats[cls_name]["n_train_pos"] += sum(y_train)
        tick = time.time()
        cls_stats[cls_name]["accuracy"] = cls.score(X_test, y_test)
        cls_stats[cls_name]["prediction_time"] = time.time() - tick
        acc_history = (cls_stats[cls_name]["accuracy"], cls_stats[cls_name]["n_train"])
        cls_stats[cls_name]["accuracy_history"].append(acc_history)
        run_history = (
            cls_stats[cls_name]["accuracy"],
            total_vect_time + cls_stats[cls_name]["total_fit_time"],
        )
        cls_stats[cls_name]["runtime_history"].append(run_history)

        if i % 3 == 0:
            print(progress(cls_name, cls_stats[cls_name]))
    if i % 3 == 0:
        print("\n")
```
