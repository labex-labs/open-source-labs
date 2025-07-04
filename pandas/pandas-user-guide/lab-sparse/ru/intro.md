# Введение

В этом практическом занятии вы научитесь использовать разреженные структуры данных в библиотеке pandas. Это полезно в ситуациях, когда у нас есть большие объемы данных, большинство из которых похожи (например, равны нулю или представляют собой NaN), и поэтому могут быть представлены более эффективно в памяти. Мы узнаем о `SparseArray`, `SparseDtype`, разреженном доступаторе, разреженных вычислениях и взаимодействии с разреженными матрицами scipy.

## Советы по использованию ВМ

После запуска ВМ нажмите в левом верхнем углу, чтобы переключиться на вкладку **Notebook** и получить доступ к Jupyter Notebook для практики.

Иногда вам может потребоваться подождать несколько секунд, пока Jupyter Notebook не загрузится полностью. Проверка операций не может быть автоматизирована из-за ограничений Jupyter Notebook.

Если вы столкнетесь с проблемами во время обучения, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Это Guided Lab, который предоставляет пошаговые инструкции, чтобы помочь вам учиться и практиковаться. Внимательно следуйте инструкциям, чтобы выполнить каждый шаг и получить практический опыт. Исторические данные показывают, что это лабораторная работа уровня <span class="text-green-600 dark:text-green-400">начальный</span> с процентом завершения <span class="text-green-600 dark:text-green-400">100%</span>. Он получил <span class="text-primary-600 dark:text-primary-400">71%</span> положительных отзывов от учащихся.
</div>
