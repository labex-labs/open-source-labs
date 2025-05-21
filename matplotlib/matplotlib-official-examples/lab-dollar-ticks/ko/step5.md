# 플롯 저장 및 재사용 가능한 함수 생성

이 마지막 단계에서는 통화 서식이 지정된 플롯을 생성하고 시각화를 파일에 저장하는 재사용 가능한 함수를 만들 것입니다. 이 접근 방식을 사용하면 향후 다른 금융 데이터 세트에 동일한 서식을 쉽게 적용할 수 있습니다.

노트북의 새 셀에 다음 코드를 추가하고 실행합니다.

```python
def create_currency_plot(x_data, y_data, title='Financial Data',
                         xlabel='X-Axis', ylabel='Amount ($)',
                         filename=None, show_stats=True):
    """
    Create a plot with currency formatting on the y-axis.

    Parameters:
    -----------
    x_data : array-like
        Data for the x-axis
    y_data : array-like
        Data for the y-axis (currency values)
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    filename : str, optional
        If provided, save the plot to this filename
    show_stats : bool
        Whether to show statistics (average, min, max)

    Returns:
    --------
    fig, ax : tuple
        The figure and axes objects
    """
    # Import the necessary module for formatting
    import matplotlib.ticker as ticker

    # Create a figure and axes
    fig, ax = plt.subplots(figsize=(12, 7))

    # Plot the data
    ax.plot(x_data, y_data, marker='o', linestyle='-', color='blue',
            linewidth=2, markersize=6, label='Data')

    if show_stats:
        # Calculate statistics
        avg_value = np.mean(y_data)
        max_value = np.max(y_data)
        min_value = np.min(y_data)
        max_x = x_data[np.argmax(y_data)]
        min_x = x_data[np.argmin(y_data)]

        # Add a horizontal line for average value
        ax.axhline(y=avg_value, color='r', linestyle='--', alpha=0.7,
                   label=f'Average: ${avg_value:.2f}')

        # Add annotations for max and min values
        ax.annotate(f'Max: ${max_value:.2f}', xy=(max_x, max_value),
                    xytext=(max_x+1, max_value+200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

        ax.annotate(f'Min: ${min_value:.2f}', xy=(min_x, min_value),
                    xytext=(min_x+1, min_value-200),
                    arrowprops=dict(facecolor='black', shrink=0.05, width=1.5))

    # Format y-axis with dollar signs
    formatter = ticker.StrMethodFormatter('${x:,.2f}')
    ax.yaxis.set_major_formatter(formatter)

    # Customize tick parameters
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Add labels and title
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    # Add grid for better readability
    ax.grid(True, linestyle='--', alpha=0.7)

    # Add legend
    if show_stats:
        ax.legend(loc='best', fontsize=10)

    # Adjust layout
    plt.tight_layout()

    # Save the plot if filename is provided
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight')
        print(f"Plot saved as '{filename}'")

    return fig, ax

# Use our function to create and save a plot
fig, ax = create_currency_plot(
    days,
    daily_revenue,
    title='Monthly Revenue Report',
    xlabel='Day of Month',
    ylabel='Daily Revenue ($)',
    filename='revenue_plot.png'
)

# Display the plot
plt.show()

print("Function created and plot saved successfully!")
```

이 코드를 실행하면 다음이 표시됩니다.

1. 이전 단계에서 생성한 것과 유사하지만 사용자 지정 함수를 사용하여 생성된 플롯
2. 플롯이 `revenue_plot.png`라는 파일에 저장되었음을 확인하는 메시지

우리가 만든 함수는 다음과 같습니다.

- x 및 y 축에 대한 데이터를 사용합니다.
- 레이블 및 제목 사용자 지정을 허용합니다.
- 플롯을 파일에 저장하는 옵션이 있습니다.
- 평균, 최소값 및 최대값과 같은 통계를 표시하거나 숨길 수 있습니다.
- 필요한 경우 추가 사용자 지정을 위해 figure 및 axes 객체를 반환합니다.

이 재사용 가능한 함수를 사용하면 향후 일관된 형식의 금융 플롯을 쉽게 만들 수 있습니다. 다른 데이터 세트로 이 함수를 호출하기만 하면 모든 통화 서식 및 통계 주석을 자동으로 처리합니다.

플롯이 올바르게 저장되었는지 확인하기 위해 파일이 있는지 확인해 보겠습니다.

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

파일이 존재하고 크기가 표시되는 메시지가 표시됩니다.

축하합니다! Matplotlib 를 사용하여 달러 기호로 플롯의 서식을 지정하고 전문적인 금융 시각화를 만드는 방법을 성공적으로 배웠습니다.
