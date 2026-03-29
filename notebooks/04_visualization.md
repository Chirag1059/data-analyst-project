# Steps for Creating Visualizations

## 1. Distribution Plots
- Use libraries like `matplotlib` or `seaborn`.
- Example code: `sns.histplot(data['column_name'])` to visualize the distribution of a specific variable.

## 2. Correlation Heatmaps
- Use `seaborn`'s `heatmap` to visualize correlations between variables.
- Example code: `sns.heatmap(data.corr(), annot=True)` to display the correlation matrix.

## 3. Categorical Analysis
- Use bar plots for categorical data using `seaborn` or `matplotlib`.
- Example code: `sns.countplot(x='categorical_column', data=data)`.

## 4. Scatter Plots
- Use scatter plots to analyze relationships between two continuous variables.
- Example code: `plt.scatter(data['column_x'], data['column_y'])`.

## 5. Box Plots
- Use `seaborn`'s `boxplot` to visualize the distribution of data based on categories.
- Example code: `sns.boxplot(x='categorical_column', y='numerical_column', data=data)`.

## 6. Bar Plots
- Use bar plots to compare quantities between different groups.
- Example code: `sns.barplot(x='categorical_column', y='numerical_column', data=data)`.

## 7. Line Plots
- Use `matplotlib` or `seaborn` for line plots to show trends over time.
- Example code: `plt.plot(data['date'], data['value'])`.

## 8. Saving Figures
- Save figures using `plt.savefig('figure_name.png')`.
- Ensure to set the `dpi` for better quality: `plt.savefig('figure_name.png', dpi=300)`.

## 9. Conclusion
- Always provide labels, titles, and legends to make the plots informative.
- Consider using `plt.show()` to display the plot interactively.