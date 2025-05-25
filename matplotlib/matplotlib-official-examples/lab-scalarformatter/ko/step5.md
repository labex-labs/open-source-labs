# 눈금 레이블 형식 구성

서브플롯의 눈금 레이블 형식을 구성합니다. 첫 번째 서브플롯은 기본 설정을 사용하고, 두 번째 서브플롯은 수학 표현식의 멋진 형식을 사용하며, 세 번째 서브플롯은 오프셋 표기법을 사용하지 않습니다.

```python
# Subplot 1 (default settings)
axs[0, 0].set_title("default settings")

# Subplot 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Subplot 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
