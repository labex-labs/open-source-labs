# Введение

В этом руководстве вы узнаете, как использовать методы аппроксимации ядра в scikit-learn.

Ядерные методы, такие как методы опорных векторов (SVM), являются мощными инструментами для нелинейной классификации. Эти методы основаны на понятии ядровой функции, которая отображает входные данные в пространство признаков высокой размерности. Однако работа с явными отображениями признаков может быть вычислительно дорогой, особенно для больших наборов данных. Методы аппроксимации ядра предоставляют решение путём генерации низкоразмерных приближений пространства признаков ядра.

В этом руководстве мы рассмотрим несколько методов аппроксимации ядра, доступных в scikit-learn, включая метод Ньюстроема, аппроксимацию ядра с радиальной базисной функцией (RBF), аппроксимацию ядра с добавленным квадратом хи-квадрат (ACS), аппроксимацию ядра с отклонённым квадратом хи-квадрат (SCS) и аппроксимацию полиномиального ядра с использованием тензорного эскиза. Мы покажем, как использовать эти методы, и обсудим их преимущества и ограничения.

## Советы по работе с ВМ

После запуска ВМ нажмите в левом верхнем углу, чтобы переключиться на вкладку **Notebook** и приступить к практике с использованием Jupyter Notebook.

Иногда вам может потребоваться подождать несколько секунд, пока Jupyter Notebook загрузится полностью. Валидация операций не может быть автоматизирована из-за ограничений Jupyter Notebook.

Если вы сталкиваетесь с проблемами во время обучения, не стесняйтесь обращаться к Labby. Оставьте отзыв после занятия, и мы оперативно решим проблему для вас.
