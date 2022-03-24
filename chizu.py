import folium

m = folium.Map(location=[33.868259, 130.884596], zoom_control=15)

tooltip = "クリック"
folium.Marker(
    [33.868259, 130.884596],
    popup='<span style="white-space: nowrap;">現住所</span>',
    tooltip=tooltip,
).add_to(m)

m.save("map.html")
