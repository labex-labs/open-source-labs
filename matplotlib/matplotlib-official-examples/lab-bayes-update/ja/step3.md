# UpdateDistクラスを定義する

次に、新しいデータが観察されるたびにベータ分布を更新するために使用される `UpdateDist` という名前のクラスを定義します。`UpdateDist` クラスは2つの引数を取ります：Matplotlibの軸オブジェクトと成功の初期確率。

```python
class UpdateDist:
    def __init__(self, ax, prob=0.5):
        self.success = 0
        self.prob = prob
        self.line, = ax.plot([], [], 'k-')
        self.x = np.linspace(0, 1, 200)
        self.ax = ax

        # Set up plot parameters
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 10)
        self.ax.grid(True)

        # This vertical line represents the theoretical value, to
        # which the plotted distribution should converge.
        self.ax.axvline(prob, linestyle='--', color='black')
```

`__init__` メソッドは、成功の初期数をゼロに設定 (`self.success = 0`)、成功の初期確率を引数として渡された値に設定 (`self.prob = prob`) することで、クラスインスタンスを初期化します。また、ベータ分布を表す線オブジェクトを作成し、グラフのパラメータを設定します。

`__call__` メソッドは、アニメーションが更新されるたびに呼び出されます。これはコイントス実験をシミュレートし、それに応じてベータ分布を更新します。

```python
def __call__(self, i):
        # This way the plot can continuously run and we just keep
        # watching new realizations of the process
        if i == 0:
            self.success = 0
            self.line.set_data([], [])
            return self.line,

        # Choose success based on exceed a threshold with a uniform pick
        if np.random.rand() < self.prob:
            self.success += 1
        y = beta_pdf(self.x, self.success + 1, (i - self.success) + 1)
        self.line.set_data(self.x, y)
        return self.line,
```

アニメーションの最初のフレームの場合 (`if i == 0`)、成功の数をゼロにリセットし、線オブジェクトをクリアします。それ以外の場合、0から1の間の乱数 (`np.random.rand()`) を生成し、それを成功の確率 (`self.prob`) と比較することでコイントス実験をシミュレートします。乱数が成功の確率より小さい場合、それを成功として数え、`beta_pdf` 関数を使ってベータ分布を更新します。最後に、新しいデータで線オブジェクトを更新して返します。
