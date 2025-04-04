# Введение

В этом практическом занятии показано, как использовать класс `BayesianGaussianMixture` из scikit-learn для подгонки набора данных с тремя смешанными Гауссовыми распределениями. Класс может автоматически подбирать количество компонентов смеси с использованием априорного распределения концентрации, которое задается с помощью параметра `weight_concentration_prior_type`. В этом практическом занятии показывается разница между использованием априорного распределения Дирихле и Дирихлева процесса для выбора количества компонентов с ненулевыми весами.

## Советы по использованию ВМ

После запуска ВМ нажмите в левом верхнем углу, чтобы переключиться на вкладку **Notebook** и приступить к работе с Jupyter Notebook.

Иногда может потребоваться подождать несколько секунд, пока Jupyter Notebook не загрузится полностью. Проверка операций не может быть автоматизирована из-за ограничений Jupyter Notebook.

Если вы столкнетесь с проблемами во время обучения, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.
