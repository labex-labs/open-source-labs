# Creating a Final Visualization with Multiple Text Elements

In this final step, we will combine everything we've learned to create a comprehensive visualization that includes multiple text elements with different styles. This will demonstrate how text boxes can be used to enhance data storytelling.

## Creating an Advanced Visualization

Let's create a more sophisticated plot that includes both our histogram and some additional visual elements. In a new cell, enter and run the following code:

```python
# Create a figure with a larger size for our final visualization
fig, ax = plt.subplots(figsize=(12, 8))

# Plot the histogram with more bins and a different color
n, bins, patches = ax.hist(x, bins=75, color='lightblue',
                           edgecolor='darkblue', alpha=0.7)

# Add title and labels with improved styling
ax.set_title('Distribution of Random Data with Statistical Annotations',
             fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Frequency', fontsize=14)

# Add grid for better readability
ax.grid(True, linestyle='--', alpha=0.7)

# Mark the mean with a vertical line
ax.axvline(x=mu, color='red', linestyle='-', linewidth=2,
           label=f'Mean: {mu:.2f}')

# Mark one standard deviation range
ax.axvline(x=mu + sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean + 1σ: {mu+sigma:.2f}')
ax.axvline(x=mu - sigma, color='green', linestyle='--', linewidth=1.5,
           label=f'Mean - 1σ: {mu-sigma:.2f}')

# Create a text box with statistics in the top left
stats_box_props = dict(boxstyle='round', facecolor='lightyellow',
                      alpha=0.8, edgecolor='gold', linewidth=2)

stats_text = '\n'.join((
    r'$\mathbf{Statistics:}$',
    r'$\mu=%.2f$ (mean)' % (mu,),
    r'$\mathrm{median}=%.2f$' % (median,),
    r'$\sigma=%.2f$ (std. dev.)' % (sigma,)
))

ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', bbox=stats_box_props)

# Add an informational text box in the top right
info_box_props = dict(boxstyle='round4', facecolor='lightcyan',
                     alpha=0.8, edgecolor='deepskyblue', linewidth=2)

info_text = '\n'.join((
    r'$\mathbf{About\ Normal\ Distributions:}$',
    r'$\bullet\ 68\%\ of\ data\ within\ 1\sigma$',
    r'$\bullet\ 95\%\ of\ data\ within\ 2\sigma$',
    r'$\bullet\ 99.7\%\ of\ data\ within\ 3\sigma$'
))

ax.text(0.95, 0.95, info_text, transform=ax.transAxes, fontsize=14,
        verticalalignment='top', horizontalalignment='right',
        bbox=info_box_props)

# Add a legend
ax.legend(fontsize=12)

# Tighten the layout and show the plot
plt.tight_layout()
plt.show()
```

When you run this cell, you'll see a comprehensive visualization with:

- A histogram of the data with improved styling
- Vertical lines marking the mean and one standard deviation range
- A statistics text box in the top-left corner
- An informational text box about normal distributions in the top-right corner
- A legend explaining the vertical lines

## Understanding the Advanced Elements

Let's examine some of the new elements we've added:

1. **Vertical Lines with `axvline()`**:
   - These lines mark important statistics directly on the plot.
   - The `label` parameter allows these lines to be included in the legend.

2. **Multiple Text Boxes with Different Styles**:
   - Each text box serves a different purpose and uses a distinct style.
   - The statistics box shows the computed values from our data.
   - The informational box provides context about normal distributions.

3. **Enhanced Formatting**:
   - LaTeX formatting is used to create bold text with `\mathbf{}`
   - Bullet points are created with `\bullet`
   - Spacing is controlled with `\ ` (backslash followed by a space)

4. **Grid and Legend**:
   - The grid helps viewers read values from the chart more accurately.
   - The legend explains the meaning of the colored lines.

## Final Notes on Text Box Placement

When placing multiple text elements in a visualization, consider:

1. **Visual hierarchy**: The most important information should stand out the most.
2. **Positioning**: Place related information near the relevant parts of the visualization.
3. **Contrast**: Ensure text is readable against its background.
4. **Consistency**: Use consistent styling for similar types of information.
5. **Clutter**: Avoid overcrowding the visualization with too many text elements.

By thoughtfully placing and styling text boxes, you can create visualizations that are both informative and visually appealing, guiding viewers to understand the key insights from your data.
