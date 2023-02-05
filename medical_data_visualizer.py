import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = df["weight"] / (df["height"]/100)**2
df.loc[df["overweight"] > 25, "overweight"] = 1
df.loc[df["overweight"] !=1, "overweight"] = 0

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. 
# If the value is more than 1, make the value 1.

df["cholesterol"].replace({1:0, 2:1, 3:1}, inplace=True)
df["gluc"].replace({1:0, 2:1, 3:1}, inplace=True)

# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = df.copy(deep=True)

    df_cat = pd.melt(df_cat, id_vars="cardio", value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(["cardio", "variable", "value"]).agg(total = ("value", "count"))
    df_cat = pd.DataFrame(df_cat)
    df_cat.reset_index(inplace=True)
    

    # Draw the catplot with 'sns.catplot()'

    # Get the figure for the output
    fig = sns.catplot(data = df_cat, 
            x ="variable", 
            y = "total", 
            hue = "value", 
            col = "cardio", 
            kind = "bar").fig


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data

    df_heat = df.copy(deep=True)
    df_heat = df_heat[
    (df_heat['ap_lo'] <= df_heat['ap_hi']) &
    (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
    (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
    (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
    (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
    ]

    # Calculate the correlation matrix
    corr = df_heat.corr(method="pearson")

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(12,12))


    # Draw the heatmap with 'sns.heatmap()'
    ax = sns.heatmap(data=corr, 
            mask=mask, 
            annot=True,
           cmap="cubehelix",
            fmt=".1f",
           annot_kws={"fontsize":8},
                linewidths=1)


    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
