# 奇妙なコードの再利用（多重継承を含む）

2 つのまったく関係のないオブジェクトを考えてみましょう。

```python
class Dog:
    def noise(self):
        return 'Bark'

    def chase(self):
        return 'Chasing!'

class LoudDog(Dog):
    def noise(self):
        # LoudBike（以下）とのコードの共通性
        return super().noise().upper()
```

そして

```python
class Bike:
    def noise(self):
        return 'On Your Left'

    def pedal(self):
        return 'Pedaling!'

class LoudBike(Bike):
    def noise(self):
        # LoudDog（上記）とのコードの共通性
        return super().noise().upper()
```

`LoudDog.noise()` と `LoudBike.noise()` の実装にはコードの共通性があります。実際、コードはまったく同じです。自然なことながら、そのようなコードはソフトウェアエンジニアを引き付けるはずです。
