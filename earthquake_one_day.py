import json
from plotly.graph_objs import Layout
from plotly import offline

#Изучение структуры данных.
filename = 'earthquake_1d.json'
with open(filename, 'r', encoding="utf-8") as f:
    all_eq_data = json.load(f)
all_eq_dicts = all_eq_data['features']
title_eq = all_eq_data['metadata']
# print(len(all_eq_dicts))
title_json = title_eq['title']

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict['properties']['mag'])
    lons.append(eq_dict['geometry']['coordinates'][0])
    lats.append(eq_dict['geometry']['coordinates'][1])
    hover_texts.append(eq_dict['properties']['title'])

#Нанесение даннных на карту
data = [{
        'type' : 'scattergeo',
        'lon' : lons,
        'lat' : lats,
        'text':hover_texts,
        'marker' : {
            'size': [3*mag for mag in mags],
            'color': mags,
            'colorscale': 'Hot',
            'reversescale': True,
            'colorbar': {'title' : 'Magnitude'}
        }
}]
title_json = title_eq['title']
my_layout = Layout(title = title_json)
fig = {'data' : data, 'layout' : my_layout}
offline.plot(fig, filename = 'global_earthquakes_1d.html')