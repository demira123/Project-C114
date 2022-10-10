import pandas as pd
import plotly.express as pe
import numpy as num

data=pd.read_csv("heightWeight.csv")

height = data["Height"].tolist()

weight = data["Weight"].tolist()

# graph = pe.scatter(x=height, y=weight)
# graph.show()


# ------------------------------------ using Hit & Trial method ---------------------------------------------

# y = mx + b

m = 0.95
b = -93

y = []

for x in height:
    y2= m*x + b
    y.append(y2)



graph = pe.scatter(x=height, y=weight)
graph.update_layout(shapes=[
    dict(
        type="line",
        y0 = min(y) , 
        y1 = max(y) , 
        x0 = min(height) , 
        x1 = max(height)
    )
])


graph.show()


# ----------------------------------- using Algorithm -----------------------------------

heightArray = num.array(height)
weightArray = num.array(weight)

# using numpy's polyfit() 
m,b=num.polyfit(heightArray,weightArray , 1)


sgraph=pe.scatter(x= heightArray , y=weightArray)
sgraph.update_layout(shapes=[
    dict(
        type="line",
        y0=min(y),
        y1=max(y),
        x0=min(heightArray),
        x1=max(heightArray)
    )
]

)

sgraph.show()

x = 166
y = m*x + b
print("Weight of a human body with height of 166 cm : "  , y )




















