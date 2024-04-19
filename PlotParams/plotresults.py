import plotly.express as px
import pandas as pd

df = pd.read_csv('C:/Users/ronan/TDAMapperRF/RF_Metrics_Normalized.csv')

fig = px.scatter_3d(df, x='n_clusters', y = 'n_cubes', z = 'perc_overlap', color='AUROC',)
fig.show()
fig.write_html("grid_search_results_normalized.html")