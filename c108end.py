import csv
import pandas as pd 
import plotly.express as px
diceresult=[]
import plotly.figure_factory as ff
count=[]
df=pd.read_csv("data.csv")

fig=ff.create_distplot([df["Avg Rating"].tolist()],["Avg Rating"],show_hist=False) 
fig.show()