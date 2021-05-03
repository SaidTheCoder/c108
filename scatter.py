import pandas as pd 
import plotly.express as px
df=pd.read_csv("data.csv")
fig=px.scatter(df,x="Height(Inches)",y="Weight(Pounds)",size_max=40)
fig.show()
