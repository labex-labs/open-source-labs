# 두 번째 y 축의 눈금 레이블 설정

`set_xticks` 함수를 사용하여 두 번째 y 축의 눈금 레이블을 설정할 수 있으며, 눈금 위치와 레이블을 인수로 전달합니다.

```python
ax2.set_xticks([0., .5*np.pi, np.pi, 1.5*np.pi, 2*np.pi],
               labels=["$0$", r"$\frac{1}{2}\pi$",
                       r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
```
