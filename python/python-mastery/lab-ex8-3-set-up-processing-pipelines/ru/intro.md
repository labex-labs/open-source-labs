# Введение

В этом практическом занятии (лабораторной работе) вы научитесь использовать корутины (сопрограммы) для создания конвейеров обработки данных. Корутины, мощная особенность языка Python, поддерживают кооперативную многозадачность, позволяя функциям приостанавливать и возобновлять выполнение в более поздний момент.

Цели этого практического занятия (лабораторной работы) — понять, как работают корутины в Python, реализовать конвейеры обработки данных на основе корутин и преобразовать данные на нескольких этапах с использованием корутин. Вы создадите два файла: `cofollow.py` — программа для отслеживания файлов на основе корутин, и `coticker.py` — приложение для отслеживания котировок акций с использованием корутин. Предполагается, что программа `stocksim.py` из предыдущего упражнения по-прежнему работает в фоновом режиме, генерируя данные о котировках акций в журнальном файле.
