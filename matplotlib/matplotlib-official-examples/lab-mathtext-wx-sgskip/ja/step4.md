# 関数を定義する

アプリケーションが表示する関数のリストを定義します。各関数は、数式と、入力値を受け取り出力値を返すラムダ関数によって定義されます。

```python
functions = [
    (r'$\sin(2 \pi x)$', lambda x: np.sin(2*np.pi*x)),
    (r'$\frac{4}{3}\pi x^3$', lambda x: (4/3)*np.pi*x**3),
    (r'$\cos(2 \pi x)$', lambda x: np.cos(2*np.pi*x)),
    (r'$\log(x)$', lambda x: np.log(x))
]
```
