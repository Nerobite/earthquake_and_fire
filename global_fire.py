from plotly.graph_objs import Layout
from plotly import offline
import pandas as pd

df = pd.read_csv('MODIS_Global_24h.csv')
df.head()

frps = df['frp']
lats = df['latitude']
lons = df['longitude']

maxy = df[df['frp']==df['frp'].max()]
maxy

data = [{
        'type' : 'scattergeo',
        'lon' : lons,
        'lat' : lats,
        'marker' : {
            'size': [0.0033*frp for frp in frps],
            'color': frps,
            'colorscale': 'Jet',
            'reversescale': False,
            'colorbar': {'title' : 'Fire Radiative Power'}
        }
}]
my_layout = Layout(title = 'MODIS_Global_fire_24h')
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename = 'Global_fire_24h.html')