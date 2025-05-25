# 제한 및 레이블 설정

이 단계에서는 메인 플롯 축에 대한 제한과 레이블을 설정합니다.

```python
main_ax.set_xlim(0, 1)
main_ax.set_ylim(1.1 * np.min(s), 2 * np.max(s))
main_ax.set_xlabel('time (s)')
main_ax.set_ylabel('current (nA)')
main_ax.set_title('Gaussian colored noise')
```
