# 왼쪽 및 오른쪽 제목 위치 지정

Matplotlib 을 사용하면 `loc` 매개변수를 사용하여 제목을 플롯의 왼쪽 또는 오른쪽에 배치할 수 있습니다. 이 단계에서는 제목을 플롯의 왼쪽 및 오른쪽에 정렬하는 방법을 배우게 됩니다.

## 왼쪽 정렬 제목이 있는 플롯 생성

제목을 왼쪽에 배치한 플롯을 생성해 보겠습니다. 새 셀에 다음 코드를 입력합니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Left-Aligned Title', loc='left')  # 제목을 왼쪽에 배치
plt.show()
```

![left-aligned-title](../assets/screenshot-20250306-9pLPZz36@2x.png)

셀을 실행합니다. 이제 제목이 가운데 정렬 대신 플롯의 왼쪽 가장자리에 정렬되어 표시되는 것을 확인하세요.

`title()` 함수의 `loc` 매개변수는 제목의 수평 위치를 결정합니다. `loc='left'`로 설정하면 Matplotlib 에 제목을 플롯의 왼쪽에 배치하도록 지시하는 것입니다.

## 오른쪽 정렬 제목이 있는 플롯 생성

이제 제목을 오른쪽에 배치한 다른 플롯을 생성해 보겠습니다. 새 셀에 다음 코드를 입력합니다.

```python
plt.figure(figsize=(8, 5))
plt.plot(range(10))
plt.grid(True)
plt.title('Right-Aligned Title', loc='right')  # 제목을 오른쪽에 배치
plt.show()
```

![right-aligned-title](../assets/screenshot-20250306-PpNxbjp2@2x.png)

셀을 실행합니다. 이제 제목이 플롯의 오른쪽 가장자리에 정렬되어 표시되어야 합니다.

## 다른 제목 위치 비교

다양한 제목 위치 (가운데, 왼쪽 및 오른쪽) 를 비교하기 위해 세 개의 플롯 시퀀스를 생성해 보겠습니다. 새 셀에 다음 코드를 입력합니다.

```python
# 가로로 정렬된 3 개의 서브플롯이 있는 figure 생성
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 플롯 1: 가운데 정렬 제목 (기본값)
axes[0].plot(range(10))
axes[0].grid(True)
axes[0].set_title('Center Title')

# 플롯 2: 왼쪽 정렬 제목
axes[1].plot(range(10))
axes[1].grid(True)
axes[1].set_title('Left Title', loc='left')

# 플롯 3: 오른쪽 정렬 제목
axes[2].plot(range(10))
axes[2].grid(True)
axes[2].set_title('Right Title', loc='right')

plt.tight_layout()  # 서브플롯 간 간격 조정
plt.show()
```

![three-title-positions](../assets/screenshot-20250306-EzNR2plC@2x.png)

세 가지 제목 위치를 나란히 보려면 셀을 실행합니다. 이 시각적 비교는 `loc` 매개변수가 제목 위치 지정에 미치는 영향을 이해하는 데 도움이 됩니다.

서브플롯으로 작업할 때는 전역 `plt.title()` 함수 대신 개별 축 객체에서 `set_title()` 메서드를 사용합니다.
