# Введение

В этом практическом занятии показано, как использовать квантильную регрессию для создания интервалов прогноза с использованием scikit-learn. Мы сгенерируем синтетические данные для задачи регрессии, применим функцию к ним и создадим наблюдения целевой переменной с использованием логнормального распределения. Затем мы разделим данные на обучающую и тестовую выборки, подберем нелинейные квантильные и наименьших квадратов регрессоры и создадим равномерно распределенный набор значений входных переменных, охватывающий диапазон [0, 10]. Мы сравним предсказанный медиану с предсказанным средним, проанализируем метрики ошибки и калибруем доверительный интервал. Наконец, мы настроим гиперпараметры квантильных регрессоров.

## Советы по использованию ВМ

После запуска ВМ нажмите в левом верхнем углу, чтобы переключиться на вкладку **Notebook** и приступить к практике в Jupyter Notebook.

Иногда вам может потребоваться подождать несколько секунд, пока Jupyter Notebook полностью загрузится. Валидация операций не может быть автоматизирована из-за ограничений Jupyter Notebook.

Если вы столкнетесь с проблемами при обучении, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.
