# streamlit run app.py
# 
import streamlit as st
import folium
import osmnx
import networkx as nx
import leafmap.foliumap as leafmap
from streamlit_folium import st_folium
from folium.plugins import Draw
from apps.navigator_offline import (get_location_from_address,
                            get_graph,
                            find_shortest_path) 
import osmnx as ox
import ast


BASEMAPS = ['Satellite', 'Roadmap', 'Terrain', 'Hybrid', 'OpenStreetMap']
TRAVEL_MODE = ['Drive', 'Walk', 'Bike']
TRAVEL_OPTIMIZER = ['Dijkstra', 'Bellman-Ford', 'Floyd Warshall', 'auto']

MAP_PATH = "./data/HCMmap.osm"



def clear_text():
    st.session_state["go_from"] = ""
    st.session_state["go_to"] = ""


st.set_page_config(page_title="🚋 Route finder", layout="wide")

# ====== SIDEBAR ======
with st.sidebar:

    st.title("Choose you travel settings")

    st.markdown("A simple app that finds and displays the shortest path between two points on a map.")

    basemap = st.selectbox("Choose basemap", BASEMAPS)
    if basemap in BASEMAPS[:-1]:
        basemap=basemap.upper()

    transport = st.selectbox("Choose transport", TRAVEL_MODE)
    optimizer = st.selectbox("Choose algorithm", TRAVEL_OPTIMIZER)

    address_from = st.text_input("Go from [lat, lon]", key="go_from")
    address_to = st.text_input("Go to [lat, lon]", key="go_to")
    
    st.button("Clear all address boxes", on_click=clear_text)
    st.write(address_to)


# ====== MAIN PAGE ======

m = leafmap.Map(center = (10.78082, 106.6911188), zoom=16)

m.add_basemap(basemap)

def get_pos(lat, lng):
    return lat, lng

# m.add_child(folium.LatLngPopup())
Draw(export=True).add_to(m)
m.add_child(
        folium.ClickForMarker("<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}"),
)

m.add_child(
        folium.ClickForLatLng(format_str='"[" + lat + "," + lng + "]"', alert=True)
)



data = None

if address_from and address_to:

    # Search information 
    graph = ox.graph_from_xml(MAP_PATH)

    st.markdown(f'**From**: {address_from}')
    st.markdown(f'**To**: {address_to}')
    st.write(graph)

    # find the shortest path

    location_orig = ast.literal_eval(address_from)
    location_dest = ast.literal_eval(address_to)
    
    route = find_shortest_path(graph, location_orig, location_dest, optimizer)

    osmnx.plot_route_folium(graph, route, m)
    # map = st_folium(m, height=800, width=1400)
    print(route)


map = st_folium(m, height=800, width=1400)
# m.to_streamlit()
