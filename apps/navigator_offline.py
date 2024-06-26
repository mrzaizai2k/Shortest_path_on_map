import sys
sys.path.append("") # nopep8
import geopandas as gpd
import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np

ox.__version__
from typing import Tuple, List, Literal
from networkx.classes.multidigraph import MultiDiGraph




# printing the closest node id to origin and destination points origin_node, destination_node

def get_location_from_address(address: str) -> (float, float):
    """ 
    Get (lat, long) coordintates from address
    Args:
        address: string with address
    Returns:
        location: (lat, long) coordinates
    Example:
        location_orig = get_location_from_address("Gare du Midi, Bruxelles")
    """
    from geopy.geocoders import Nominatim

    locator = Nominatim(user_agent = "myapp")
    location = locator.geocode(address)

    return location.latitude, location.longitude

def get_graph(address_orig: str, address_dest: str) -> (MultiDiGraph, Tuple[float], Tuple[float]):
    """ 
    Convert the origin and destination addresses into (lat, long) coordinates and find the 
    graph of streets from the bounding box.
    Args:
        address_orig: departure address
        address_dest: arrival address
    Returns:
        graph: street graph from OpenStreetMap
        location_orig: departure coordinates
        location_dest: arrival coordinates
    Example:
        graph, location_orig, location_dest = get_graph("Gare du Midi, Bruxelles", "Gare du Nord, Bruxelles")
    """

    # find location by address
    location_orig = get_location_from_address(address_orig)
    location_dest = get_location_from_address(address_dest)

    G = ox.graph_from_xml("./data/mapHCM.osm")

    return G,  location_orig, location_dest


# def get_graph_from_mode(address_orig: str, address_dest: str, mode: str, city: str="Brussels", dist: float=1000.) -> (MultiDiGraph, Tuple[float], Tuple[float]):
#     """
#     Convert the origin and destination addresses into (lat, long) coordinates and find the
#     graph of streets from the bounding box.
#     Args:
#         address_orig: departure address
#         address_dest: arrival address
#         mode: get graph from place or from address
#         city: name of the city/town
#         dist: distance from the original address in meters
#     Returns:
#         graph: street graph from OpenStreetMap
#         location_orig: departure coordinates
#         location_dest: arrival coordinates
#     Examples:
#         graph, location_orig, location_dest = get_graph_from_mode("Gare du Midi, Bruxelles", "Gare du Nord, Bruxelles", mode="place", city="Bruxelles")
#         graph, location_orig, location_dest = get_graph_from_mode("Gare du Midi, Bruxelles", "Gare du Nord, Bruxelles", mode="address", dist=2000)
#     """

#     assert mode in ['place', 'address']

#     # find location by address
#     location_orig = get_location_from_address(address_orig)
#     location_dest = get_location_from_address(address_dest)

#     if mode == 'place':
#         graph = osmnx.graph_from_place(city, network_type = 'drive')
#     else:
#         graph = osmnx.graph.graph_from_address(address_orig, dist=dist, dist_type='bbox', network_type = 'drive')

#     return graph, location_orig, location_dest


def find_shortest_path(graph: MultiDiGraph, 
                       location_orig: Tuple[float], location_dest: Tuple[float], 
                       optimizer: Literal["bellman-ford", "dijkstra"]) -> List[int]:

    """
    Find the shortest path between two points from the street graph
    Args:
        graph: street graph from OpenStreetMap
        location_orig: departure coordinates
        location_dest: arrival coordinates
        optimizer: type of optimizer (Length or Time)
    Returns:
        route:
    """

    # find the nearest node to the departure and arrival location
    # define origin and desination locations

    node_orig = ox.nearest_nodes(graph, location_orig[1],location_orig[0])
    node_dest = ox.nearest_nodes(graph, location_dest[1],location_dest[0])
    if optimizer in ['Dijkstra', 'Bellman-Ford']:
        route = nx.shortest_path(graph, node_orig, node_dest, weight='length', method=optimizer.lower())
    elif optimizer == "Floyd Warshall":
        predecessors, _ = nx.floyd_warshall_predecessor_and_distance(graph)
        route = nx.reconstruct_path(node_orig, node_dest, predecessors)
    return route
