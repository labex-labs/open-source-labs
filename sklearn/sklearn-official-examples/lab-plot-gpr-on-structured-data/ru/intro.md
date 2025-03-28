# Введение

Гауссовы процессы - популярный инструмент в машинном обучении для задач регрессии и классификации. Однако, они обычно требуют, чтобы данные были в виде фиксированной длины вектора признаков, что может ограничивать их использование в некоторых приложениях. В этом лабе мы исследуем, как Гауссовы процессы могут быть использованы для переменной длины последовательностей, таких как генные последовательности, путём определения функции ядра, которая действует непосредственно на этих структурах. Мы будем использовать scikit-learn для реализации наших моделей Гауссовых процессов.

## Советы по ВМ

После запуска ВМ нажмите в левом верхнем углу, чтобы переключиться на вкладку **Notebook** и получить доступ к Jupyter Notebook для практики.

Иногда может потребоваться подождать несколько секунд, пока Jupyter Notebook загрузится. Валидация операций не может быть автоматизирована из-за ограничений в Jupyter Notebook.

Если вы сталкиваетесь с проблемами во время обучения, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.
