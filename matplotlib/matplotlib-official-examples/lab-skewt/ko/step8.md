# SkewT-logP 다이어그램 생성

이제 앞서 등록한 SkewXAxes 투영을 사용하여 SkewT-logP 다이어그램을 생성합니다. 먼저 figure 객체를 생성하고 SkewXAxes 투영을 사용하여 서브플롯 (subplot) 을 추가합니다. 그런 다음 semilogy 함수를 사용하여 온도 및 이슬점 데이터를 다이어그램에 플롯합니다. 마지막으로 X 축과 Y 축의 제한 및 눈금을 설정하고 플롯을 표시합니다.

```python
fig = plt.figure(figsize=(6.5875, 6.2125))
ax = fig.add_subplot(projection='skewx')

ax.semilogy(T, p, color='C3')
ax.semilogy(Td, p, color='C2')

ax.axvline(0, color='C0')

ax.yaxis.set_major_formatter(ScalarFormatter())
ax.yaxis.set_minor_formatter(NullFormatter())
ax.set_yticks(np.linspace(100, 1000, 10))
ax.set_ylim(1050, 100)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.set_xlim(-50, 50)

plt.grid(True)
plt.show()
```
