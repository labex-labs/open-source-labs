# 플롯 저장 및 공유

마지막 단계는 사용자 정의 플롯을 저장하여 보고서, 프레젠테이션에 포함하거나 다른 사람과 공유할 수 있도록 하는 것입니다.

## 다양한 형식으로 플롯 저장

Matplotlib 를 사용하면 PNG, JPG, PDF, SVG 등을 포함한 다양한 형식으로 플롯을 저장할 수 있습니다. 다양한 형식으로 플롯을 저장하는 방법을 알아보겠습니다.

```python
# Create a plot similar to our previous customized one
fig, ax = plt.subplots(figsize=(10, 6))

# Generate data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot the data
ax.plot(x, y1, linewidth=2, color='blue', label='sin(x)')
ax.plot(x, y2, linewidth=2, color='red', label='cos(x)')

# Move the x-axis tick labels to the top
ax.tick_params(
    axis='x',
    top=True,
    labeltop=True,
    bottom=False,
    labelbottom=False
)

# Customize tick labels
ax.set_xticks(np.arange(0, 2*np.pi + 0.1, np.pi/2))
ax.set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])

# Add title and labels
ax.set_title('Plot with X-Axis Labels at the Top', fontsize=14)
ax.set_xlabel('X-axis at the top')
ax.set_ylabel('Y-axis')

# Add grid and legend
ax.grid(True)
ax.legend()

# Save the figure in different formats
plt.savefig('plot_with_top_xlabels.png', dpi=300, bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.pdf', bbox_inches='tight')
plt.savefig('plot_with_top_xlabels.svg', bbox_inches='tight')

# Show the plot
plt.show()

print("The plot has been saved in PNG, PDF, and SVG formats in the current directory.")
```

이 코드를 실행하면 플롯이 세 가지 다른 형식으로 저장됩니다.

- PNG: 웹 및 일반 사용에 적합한 래스터 이미지 형식
- PDF: 출판물 및 보고서에 이상적인 벡터 형식
- SVG: 웹 및 편집 가능한 그래픽에 탁월한 벡터 형식

파일은 Jupyter 노트북의 현재 작업 디렉토리에 저장됩니다.

## 저장 매개변수 이해

`savefig()`와 함께 사용된 매개변수를 살펴보겠습니다.

- `dpi=300`: PNG 와 같은 래스터 형식의 해상도 (dots per inch) 를 설정합니다.
- `bbox_inches='tight'`: 불필요한 공백 없이 모든 요소를 포함하도록 그림 경계를 자동으로 조정합니다.

## 저장된 파일 보기

Jupyter 에서 파일 브라우저로 이동하여 저장된 파일을 볼 수 있습니다.

1. 왼쪽 상단의 "Jupyter" 로고를 클릭합니다.
2. 파일 브라우저에서 저장된 이미지 파일을 볼 수 있습니다.
3. 파일을 클릭하여 보거나 다운로드합니다.

## 추가 플롯 내보내기 옵션

저장된 플롯을 더 세밀하게 제어하려면 필요에 따라 그림 크기를 사용자 정의하거나 배경을 조정하거나 DPI 를 변경할 수 있습니다.

```python
# Control the background color and transparency
fig.patch.set_facecolor('white')  # Set figure background color
fig.patch.set_alpha(0.8)          # Set background transparency

# Save with custom settings
plt.savefig('custom_background_plot.png',
            dpi=400,              # Higher resolution
            facecolor=fig.get_facecolor(),  # Use the figure's background color
            edgecolor='none',     # No edge color
            bbox_inches='tight',  # Tight layout
            pad_inches=0.1)       # Add a small padding

print("A customized plot has been saved with specialized export settings.")
```

이것은 출력 형식과 모양을 정밀하게 제어하여 플롯을 저장하는 방법을 보여줍니다.
