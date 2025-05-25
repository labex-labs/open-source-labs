# 버튼 콜백 함수 생성

이제 `Next` 및 `Previous` 버튼에 대한 두 개의 콜백 함수를 생성합니다. 이 함수들은 다른 주파수를 가진 새로운 사인파로 플롯을 업데이트합니다.

```python
class Index:
    ind = 0

    def next(self, event):
        self.ind += 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

    def prev(self, event):
        self.ind -= 1
        i = self.ind % len(freqs)
        ydata = np.sin(2*np.pi*freqs[i]*t)
        l.set_ydata(ydata)
        plt.draw()

callback = Index()
```
