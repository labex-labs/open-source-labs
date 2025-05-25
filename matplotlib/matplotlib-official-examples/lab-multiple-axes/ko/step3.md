# 원과 초기 점 그리기

세 번째 단계는 왼쪽 subplot 에 원과 초기 점을 그리는 것입니다. 원을 생성하기 위해 각도 배열을 생성한 다음 각 각도의 사인과 코사인을 플롯합니다. 또한 원점에 단일 점을 플롯합니다.

```python
x = np.linspace(0, 2 * np.pi, 50)
axl.plot(np.cos(x), np.sin(x), "k", lw=0.3)
point, = axl.plot(0, 0, "o")
```
