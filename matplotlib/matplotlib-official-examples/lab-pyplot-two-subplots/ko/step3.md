# 서브플롯 생성

`.pyplot.subplot`을 사용하여 두 개의 서브플롯이 있는 figure 를 생성합니다.

```python
plt.figure()

plt.subplot(211)
plt.plot(t1, f(t1), color='tab:blue', marker='o')
plt.plot(t2, f(t2), color='black')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), color='tab:orange', linestyle='--')

plt.show()
```

`subplot()` 함수는 세 개의 인수를 받습니다: 행의 수, 열의 수, 그리고 현재 플롯의 인덱스입니다. 인덱스는 왼쪽 상단 모서리에서 1 부터 시작하여 행별로 증가합니다. 이 예제에서는 상단과 하단에 각각 하나씩 두 개의 서브플롯이 있는 figure 를 생성합니다.

첫 번째 서브플롯에서는 `t1`을 `f(t1)`에 대해, `t2`를 `f(t2)`에 대해 플롯합니다. 첫 번째 플롯의 색상을 파란색으로 설정하고 각 데이터 포인트에 원형 마커를 추가합니다. 두 번째 플롯의 색상은 검정색으로 설정합니다.

두 번째 서브플롯에서는 `t2`를 `2*np.pi*t2`의 코사인 함수에 대해 플롯합니다. 플롯의 색상은 주황색으로, 선 스타일은 점선으로 설정합니다.
