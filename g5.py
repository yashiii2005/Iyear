import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import pandas as pd

# Load iris dataset from Seaborn
iris = sns.load_dataset('iris')

# A. Scatter plot of petal length vs petal width
scatter_fig = px.scatter(iris, x='petal_length', y='petal_width', color='species', title='Petal Length vs Petal Width', labels={'petal_length': 'Petal Length (cm)', 'petal_width': 'Petal Width (cm)', 'species': 'Species'})
scatter_fig.show()

# C. Pie chart of flower type frequency
pie_data = iris['species'].value_counts().reset_index()
pie_fig = go.Figure(data=[go.Pie(labels=pie_data['index'], values=pie_data['species'])])
pie_fig.update_layout(title='Flower Type Frequency')
pie_fig.show()