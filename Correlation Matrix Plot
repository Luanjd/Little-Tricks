# Define the heatmap parameters
pd.options.display.float_format = "{:,.2f}".format

# Define correlation matrix
data_train_num = data_train.iloc[:, 1:]
corr_matrix = data_train_num.corr()

# Replace any correlation < |0.3| by 0 for a better visibility
corr_matrix[(corr_matrix < 0.3) & (corr_matrix > -0.3)] = 0

# Mask the upper part of the heatmap
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

# Choose the color map
cmap = "Blues"

# plot the heatmap
sns.set(rc = {'figure.figsize':(20,15)})
sns.heatmap(corr_matrix, mask=mask, vmax=1.0, vmin=-1.0, linewidths=0.1,
            annot_kws={"size": 9, "color": "black"}, square=True, cmap=cmap, annot=True,
            )
plt.title('Correlation Plot For Numerical Variables', fontsize='xx-large',fontweight='heavy')
