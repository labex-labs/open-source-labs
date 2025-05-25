# 결과 시각화

이 단계에서는 특징 이산화 과정의 결과를 시각화합니다. 각 분류기와 데이터 세트에 대한 테스트 세트의 분류 정확도를 플롯합니다.

```python
plt.tight_layout()

# 그림 위에 제목 추가
plt.subplots_adjust(top=0.90)
suptitles = [
    "선형 분류기",
    "특징 이산화 및 선형 분류기",
    "비선형 분류기",
]
for i, suptitle in zip([1, 3, 5], suptitles):
    ax = axes[0, i]
    ax.text(
        1.05,
        1.25,
        suptitle,
        transform=ax.transAxes,
        horizontalalignment="center",
        size="x-large",
    )
plt.show()
```
