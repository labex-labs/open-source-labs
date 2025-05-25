# 데이터 업데이트

데이터를 업데이트하는 `update` 메서드를 정의합니다. 이 메서드는 ax (축) 를 입력 매개변수로 사용합니다. 뷰 제한을 가져와서 선을 업데이트하고, 뷰 제한의 너비가 delta 와 다른지 확인합니다. 뷰 제한의 너비가 delta 와 다르면 delta 를 업데이트하고 xstart 와 xend 를 가져옵니다. 그런 다음 데이터를 다운샘플링된 데이터로 설정하고 유휴 상태로 그립니다.

```python
def update(self, ax):
    # Update the line
    lims = ax.viewLim
    if abs(lims.width - self.delta) > 1e-8:
        self.delta = lims.width
        xstart, xend = lims.intervalx
        self.line.set_data(*self.downsample(xstart, xend))
        ax.figure.canvas.draw_idle()
```
