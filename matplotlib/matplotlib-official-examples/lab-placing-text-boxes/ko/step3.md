# 통계 정보가 있는 텍스트 상자 추가

이제 기본 히스토그램이 있으므로 데이터에 대한 통계 정보를 표시하는 텍스트 상자를 추가하여 이를 향상시켜 보겠습니다. 이렇게 하면 시각화가 보는 사람에게 더 유익해집니다.

## 텍스트 내용 생성

먼저 텍스트 상자 안에 들어갈 텍스트 내용을 준비해야 합니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
# Create a string with the statistics
textstr = '\n'.join((
    r'$\mu=%.2f$' % (mu,),           # Mean
    r'$\mathrm{median}=%.2f$' % (median,),  # Median
    r'$\sigma=%.2f$' % (sigma,)       # Standard deviation
))

print("Text content for our box:")
print(textstr)
```

다음과 유사한 출력이 표시됩니다.

```
Text content for our box:
$\mu=-0.31$
$\mathrm{median}=-0.28$
$\sigma=29.86$
```

이 코드는 데이터의 평균, 중앙값 및 표준 편차를 포함하는 여러 줄의 문자열을 생성합니다. 이 코드의 몇 가지 흥미로운 측면을 살펴보겠습니다.

1. `\n'.join(...)` 메서드는 여러 문자열을 줄 바꿈 문자로 연결합니다.
2. 각 문자열 앞의 `r`은 특수 문자를 포함할 때 유용한 "raw" 문자열로 만듭니다.
3. `$...$` 표기법은 matplotlib 에서 LaTeX 스타일의 수학적 서식을 사용하는 데 사용됩니다.
4. `\mu` 및 `\sigma`는 그리스 문자 μ(mu) 및 σ(sigma) 에 대한 LaTeX 기호입니다.
5. `%.2f`는 소수점 두 자리로 부동 소수점 숫자를 표시하는 서식 지정자입니다.

## 텍스트 상자 생성 및 추가

이제 히스토그램을 다시 만들고 텍스트 상자를 추가해 보겠습니다. 새 셀에 다음 코드를 입력하고 실행합니다.

```python
# Create a new figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a histogram with 50 bins
histogram = ax.hist(x, bins=50, color='skyblue', edgecolor='black')

# Add title and labels
ax.set_title('Distribution of Random Data with Statistics', fontsize=16)
ax.set_xlabel('Value', fontsize=12)
ax.set_ylabel('Frequency', fontsize=12)

# Define the properties of the text box
properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)

# Add the text box to the plot
# Position the box in the top left corner (0.05, 0.95) in axes coordinates
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=properties)

# Display the plot
plt.tight_layout()
plt.show()
```

이 셀을 실행하면 통계 정보가 표시된 텍스트 상자가 왼쪽 상단 모서리에 있는 히스토그램이 표시됩니다.

## 텍스트 상자 코드 이해

텍스트 상자를 생성하는 코드의 중요한 부분을 자세히 살펴보겠습니다.

1. `properties = dict(boxstyle='round', facecolor='wheat', alpha=0.5)`:
   - 텍스트 상자 속성이 있는 사전을 생성합니다.
   - `boxstyle='round'`: 상자에 둥근 모서리가 있도록 합니다.
   - `facecolor='wheat'`: 상자의 배경색을 밀색으로 설정합니다.
   - `alpha=0.5`: 상자를 반투명하게 만듭니다 (50% 불투명도).

2. `ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=properties)`:
   - (0.05, 0.95) 위치에 축에 텍스트를 추가합니다.
   - `transform=ax.transAxes`: 이것은 중요합니다. 즉, 좌표가 데이터 단위가 아닌 축 단위 (0-1) 로 표시된다는 의미입니다. 따라서 (0.05, 0.95) 는 "플롯의 왼쪽 가장자리에서 5% 및 하단 가장자리에서 95%"를 의미합니다.
   - `fontsize=14`: 글꼴 크기를 설정합니다.
   - `verticalalignment='top'`: 텍스트의 맨 위가 지정된 y 좌표에 오도록 텍스트를 정렬합니다.
   - `bbox=properties`: 텍스트 상자 속성을 적용합니다.

텍스트 상자는 플롯을 확대하거나 데이터 범위를 변경하더라도 플롯 축을 기준으로 동일한 위치에 유지됩니다. 이는 `transform=ax.transAxes`를 사용하여 데이터 좌표 대신 축 좌표를 사용했기 때문입니다.
