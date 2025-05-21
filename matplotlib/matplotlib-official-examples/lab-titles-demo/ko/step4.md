# 서브플롯을 사용한 고급 제목 위치 지정

이 단계에서는 서브플롯 레이아웃 및 축 객체를 사용할 때 제목 위치 지정을 위한 고급 기술을 배우게 됩니다. 또한 `suptitle()` 함수를 사용하여 여러 서브플롯이 있는 figure 에 전체 제목을 추가하는 방법도 배우게 됩니다.

## 서브플롯 및 개별 제목이 있는 figure 생성

각각 자체적으로 다르게 배치된 제목이 있는 2x2 그리드의 서브플롯을 생성해 보겠습니다.

```python
# 2x2 그리드의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 더 쉬운 반복을 위해 축의 2D 배열을 평탄화합니다.
axes = axes.flatten()

# 데이터를 플롯하고 각 서브플롯에 대해 다른 위치로 제목 설정
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)

# 왼쪽 상단 서브플롯: 기본 가운데 정렬 제목
axes[0].set_title('Default (Centered)')

# 오른쪽 상단 서브플롯: 왼쪽 정렬 제목
axes[1].set_title('Left-Aligned', loc='left')

# 왼쪽 하단 서브플롯: 오른쪽 정렬 제목
axes[2].set_title('Right-Aligned', loc='right')

# 오른쪽 하단 서브플롯: 사용자 정의 위치 제목
axes[3].set_title('Custom Position', y=0.85, loc='center')

# 서브플롯 간 간격 추가
plt.tight_layout()
plt.show()
```

셀을 실행합니다. 각기 다르게 배치된 제목이 있는 네 개의 서브플롯이 표시되어야 합니다.

## suptitle() 을 사용하여 figure 수준 제목 추가

여러 서브플롯으로 작업할 때 전체 figure 에 대한 전체 제목을 추가하고 싶을 수 있습니다. 이는 `suptitle()` 함수를 사용하여 수행할 수 있습니다.

```python
# 2x2 그리드의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 더 쉬운 반복을 위해 축의 2D 배열을 평탄화합니다.
axes = axes.flatten()

# 각 서브플롯에 데이터 플롯
for i, ax in enumerate(axes):
    ax.plot(range(10))
    ax.grid(True)
    ax.set_title(f'Subplot {i+1}')

# figure 에 전체 제목 추가
fig.suptitle('Multiple Subplots with an Overall Title', fontsize=16)

# 서브플롯 간 간격 추가
plt.tight_layout()
# suptitle 에 대한 상단 간격 추가
plt.subplots_adjust(top=0.9)
plt.show()
```

셀을 실행합니다. 각자 자체 제목이 있고 맨 위에 figure 에 대한 전체 제목이 있는 네 개의 서브플롯이 표시되어야 합니다.

## 축 제목과 figure 제목 결합

개별 서브플롯 제목을 전체 figure 제목과 결합할 수 있습니다.

```python
# 2x2 그리드의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# 각 서브플롯에 다른 제목 위치로 데이터 플롯
axes[0, 0].plot(range(10))
axes[0, 0].grid(True)
axes[0, 0].set_title('Centered Title', loc='center')

axes[0, 1].plot(range(10))
axes[0, 1].grid(True)
axes[0, 1].set_title('Left-Aligned Title', loc='left')

axes[1, 0].plot(range(10))
axes[1, 0].grid(True)
axes[1, 0].set_title('Right-Aligned Title', loc='right')

axes[1, 1].plot(range(10))
axes[1, 1].grid(True)
axes[1, 1].set_title('Lower Title', y=0.85)

# figure 에 전체 제목 추가
fig.suptitle('Advanced Title Positioning Demo', fontsize=16)

# 서브플롯 간 간격 추가
plt.tight_layout()
# suptitle 에 대한 상단 간격 추가
plt.subplots_adjust(top=0.9)
plt.show()
```

셀을 실행합니다. 각기 다르게 배치된 제목이 있고 figure 상단에 전체 제목이 있는 네 개의 서브플롯이 있는 figure 가 표시되어야 합니다.

`suptitle()` 함수는 전체 figure 를 설명하는 기본 제목을 추가하는 데 유용하며, 축 객체에 대한 개별 `set_title()` 호출은 각 서브플롯에 더 구체적인 제목을 추가합니다.
