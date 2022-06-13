attribute_number = len(raw_regression_data.columns)
print("Attribute Number: {}".format(attribute_number))

# subplots 
fig = plt.figure(figsize=(24, 32))
ax = fig.subplots(attribute_number//3,3)
# iterations
for num, title in enumerate(raw_regression_data.columns):
    idx = num//3 # divided with no remainder
    idy = num%3  # remainder 
    if raw_regression_data[title].dtype in ['object']:
        value_count_dict = raw_regression_data[title].value_counts().to_dict()
        keys = list(value_count_dict.keys())
        values = list(value_count_dict.values())
        if len(raw_regression_data[title].unique().tolist()) < 8:
            ax[idx, idy].bar(keys, values, color='r')
        else:
            ax[idx, idy].barh(keys, values, color='r')
    else:
        ax[idx, idy].hist(raw_regression_data[title].values, bins=50);
    
    # set title with attribute
    ax[idx, idy].set_xlabel(title, fontsize=17)
    # set grid width
    ax[idx, idy].grid(linestyle='--', alpha=0.5)
    # font size of ticks
    ax[idx, idy].tick_params(labelsize=14)
plt.tight_layout()
