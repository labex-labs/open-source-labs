# Введение

В этом лабораторном занятии мы будем использовать алгоритм спектрального бикластеризации для кластеризации данных, одновременно учитывая строки (образцы) и столбцы (признаки) матрицы. Его цель - выявить паттерны не только между образцами, но и внутри подмножеств образцов, что позволяет обнаруживать локализованную структуру в данных. Это делает спектральное бикластеризацию особенно подходящей для наборов данных, где порядок или расположение признаков фиксировано, например, в изображениях, временных рядах или геномах. Мы будем использовать библиотеку scikit-learn для генерации датасета в виде шахматной доски и бикластеризации его с использованием алгоритма спектрального бикластеризации.

## Советы по использованию ВМ

После запуска ВМ кликните в левом верхнем углу, чтобы переключиться на вкладку **Ноутбук** и получить доступ к Jupyter Notebook для практики.

Иногда вам может потребоваться подождать несколько секунд, пока Jupyter Notebook загрузится. Валидация операций не может быть автоматизирована из-за ограничений Jupyter Notebook.

Если вы сталкиваетесь с проблемами при обучении, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.
