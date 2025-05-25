# UpdateDist 클래스 정의

다음으로, 새로운 데이터가 관찰될 때 베타 분포를 업데이트하는 데 사용될 `UpdateDist`라는 클래스를 정의합니다. `UpdateDist` 클래스는 두 개의 인수를 받습니다: Matplotlib 축 객체와 초기 성공 확률입니다.

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

`__init__` 메서드는 초기 성공 횟수를 0 (`self.success = 0`) 으로 설정하고 초기 성공 확률을 인수로 전달된 값 (`self.prob = prob`) 으로 설정하여 클래스 인스턴스를 초기화합니다. 또한 베타 분포를 나타내는 선 객체를 생성하고 플롯 매개변수를 설정합니다.

`__call__` 메서드는 애니메이션이 업데이트될 때마다 호출됩니다. 이 메서드는 동전 던지기 실험을 시뮬레이션하고 그에 따라 베타 분포를 업데이트합니다.

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

애니메이션의 첫 번째 프레임인 경우 (`if i == 0`), 성공 횟수를 0 으로 재설정하고 선 객체를 지웁니다. 그렇지 않으면 0 과 1 사이의 난수를 생성 (`np.random.rand()`) 하고 이를 성공 확률 (`self.prob`) 과 비교하여 동전 던지기 실험을 시뮬레이션합니다. 난수가 성공 확률보다 작으면 성공으로 간주하고 `beta_pdf` 함수를 사용하여 베타 분포를 업데이트합니다. 마지막으로, 새로운 데이터로 선 객체를 업데이트하고 반환합니다.
