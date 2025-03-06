# プロットの保存と再利用可能な関数の作成

この最後のステップでは、通貨フォーマットのプロットを生成する再利用可能な関数を作成し、可視化結果をファイルに保存します。このアプローチにより、将来的に異なる金融データセットに同じフォーマットを簡単に適用できます。

ノートブックの新しいセルに以下のコードを追加して実行します。

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

このコードを実行すると、以下のような結果が表示されるはずです。

1. 前のステップで作成したものと同様のプロットですが、今回は自作の関数を使って生成されます。
2. プロットが `revenue_plot.png` という名前のファイルに保存されたことを確認するメッセージ

作成した関数は以下の機能を持っています。

- X 軸と Y 軸のデータを受け取ります。
- ラベルとタイトルをカスタマイズできます。
- プロットをファイルに保存するオプションがあります。
- 平均、最小、最大などの統計情報を表示または非表示にできます。
- 必要に応じてさらにカスタマイズできるように、図と軸のオブジェクトを返します。

この再利用可能な関数により、将来的に一貫したフォーマットの金融プロットを簡単に作成できます。異なるデータセットでこの関数を呼び出すだけで、通貨フォーマットと統計注釈を自動的に処理します。

プロットが正しく保存されたことを確認するために、ファイルが存在するかどうかを確認しましょう。

```python
import os
if os.path.exists('revenue_plot.png'):
    print("Plot file exists! Size:", os.path.getsize('revenue_plot.png'), "bytes")
else:
    print("Plot file was not saved correctly.")
```

ファイルが存在することとそのサイズを確認するメッセージが表示されるはずです。

おめでとうございます！Matplotlib を使って、ドル記号でプロットをフォーマットし、プロフェッショナルな見た目の金融可視化を作成する方法を成功裏に学びました。
