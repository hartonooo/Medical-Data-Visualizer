# Medical-Data-Visualizer
certification python project from <a href="https://www.freecodecamp.org/learn/data-analysis-with-python/data-analysis-with-python-projects/medical-data-visualizer" target="_blank" rel="noopener noreferrer">freecodecamp</a>


1. using Python to explore the relationship between cardiac disease, body measurements, blood markers, and lifestyle choices.

2. visualize and make calculations from medical examination data using matplotlib, seaborn, and pandas. The dataset values were collected during medical examinations.

3. import libraries

    <details>
      <summary>libraries</summary>
      <pre>
      import pandas as pd
      import seaborn as sns
      import matplotlib.pyplot as plt
      import numpy as np
      </pre>
    </details>  

4. import data
    <details>
      <summary>read data</summary>
      <pre>
      df = pd.read_csv("medical_examination.csv")
      </pre>
    </details>

5. add 'overweight' column
    <details>
      <summary>overweight</summary>
      <pre>
      df['overweight'] = df["weight"] / (df["height"]/100)**2
      df.loc[df["overweight"] > 25, "overweight"] = 1
      df.loc[df["overweight"] !=1, "overweight"] = 0
      </pre>
    </details>

6. normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

    <details>
      <summary>normalize</summary>
      <pre>
      df["cholesterol"].replace({1:0, 2:1, 3:1}, inplace=True)
      df["gluc"].replace({1:0, 2:1, 3:1}, inplace=True)
      </pre>
    </details>

7. create categorical plot

    <details>
      <summary>draw_cat_plot</summary>
      <pre>
      def draw_cat_plot():
          - create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
          df_cat = df.copy(deep=True)
          df_cat = pd.melt(df_cat, id_vars="cardio", value_vars=["active", "alco", "cholesterol", "gluc", "overweight", "smoke"]) </br>          
          - group and reformat the data to split it by 'cardio'. Show the counts of each feature. 
          df_cat = df_cat.groupby(["cardio", "variable", "value"]).agg(total = ("value", "count"))
          df_cat = pd.DataFrame(df_cat)
          df_cat.reset_index(inplace=True)
      </pre>
    </details>
    
    <details>
      <summary>draw plot</summary>
      <pre>
      fig = sns.catplot(data = df_cat, 
            x ="variable", 
            y = "total", 
            hue = "value", 
            col = "cardio", 
            kind = "bar").fig
            </br>
      fig.savefig('catplot.png')
      return fig
      </pre>
    </details>
    
    <details>
    <summary><b>Cat Plot</b></summary>
      <img src="https://github.com/mas-tono/Medical-Data-Visualizer/blob/main/image/catplot.png">      
    </details>
    
    
 8. clean the data by filtering out the following patient segments that represent incorrect data:
 
    <details><summary>criteria</summary>
  
      - diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
      - height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
      - height is more than the 97.5th percentile
      - weight is less than the 2.5th percentile
      - weight is more than the 97.5th percentile  
    </details>
 
    <details>
      <summary>draw_heat_map</summary>
      <pre>
      def draw_heat_map():
        df_heat = df.copy(deep=True)
        df_heat = df_heat[
        (df_heat['ap_lo'] <= df_heat['ap_hi']) &
        (df_heat['height'] >= df_heat['height'].quantile(0.025)) &
        (df_heat['height'] <= df_heat['height'].quantile(0.975)) &
        (df_heat['weight'] >= df_heat['weight'].quantile(0.025)) &
        (df_heat['weight'] <= df_heat['weight'].quantile(0.975))
        ]
      </pre>
    </details>
    
    <details>
      <summary>correlation matrix</summary>
      <pre>
      corr = df_heat.corr(method="pearson")
      </br>      
      - masking for upper triangle of heat map      
      mask = np.triu(corr)
      </pre>
    </details>
    
    <details>
      <summary>draw heat map</summary>
      <pre>      
      fig, ax = plt.subplots(figsize=(12,12))
      ax = sns.heatmap(data=corr, 
            mask=mask, 
            annot=True,
           cmap="cubehelix",
            fmt=".1f",
           annot_kws={"fontsize":8},
                linewidths=1)    
      fig.savefig('heatmap.png')
      return fig
      </pre>
    </details>
    
    <details>
      <summary><b>Heat Map</b></summary>
      <img src="https://github.com/mas-tono/Medical-Data-Visualizer/blob/main/image/heatmap.png">      
    </details>


9. put them together in medical_data_visualizer.py file

10. call via main.py
