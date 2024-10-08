"""
File: Minimum_Vortex_Cover_gui.py
Author: Biltu Maji
Date: 28/09/2024
Description: This file use to demonstrate One of NP problem 'Minmum Vortex cover' with aprroximation method with Gui
Input : Ex . 
            Node: 5
            Edge: 1-3,3-5,5-2,5-4
"""

import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
graph_frame=None
min_vortex={} ##set

def create_graph():
    """
    This Function Create Undireted graph
    """
    G = nx.Graph()
    nodes = [int(x) for x in nodes_entry.get().split(",")]
    print(type(edges_entry))
    print(edges_entry.get().split(","))
    edges = [tuple(int(x) for x in edge.split("-")) for edge in edges_entry.get().split(",")]
    print(edges)
    G.add_nodes_from(nodes)
    G.add_edges_from(edges)
    return G

def draw_graph(G):
    global graph_frame
    global min_vortex
    node_color=[]
    for node in G:
        if node in min_vortex:
            node_color.append('orange')
        else:
            node_color.append('skyblue')
    if graph_frame:
        graph_frame.destroy()
    graph_frame = tk.Frame(window)
    graph_frame.pack()
    fig, ax = plt.subplots(figsize=(5, 4))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_color, node_size=700, font_size=10)
    canvas = FigureCanvasTkAgg(fig, master=graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()
    min_vortex={}

def find_minimum_vertex_cover(G):
    """
    To find Min Vortex cover used 'min_weighted_vertex_cover' algo
    """
    global min_vortex
    approx_mvc = nx.algorithms.approximation.vertex_cover.min_weighted_vertex_cover(G)
    result_label.config(text=f"Minimum Vertex Cover: {approx_mvc}")
    min_vortex=approx_mvc
    draw_graph(G)

window = tk.Tk()
window.title("Minimum Vertex Cover")

nodes_label = tk.Label(window, text="Nodes (comma-separated):")
nodes_label.pack()
nodes_entry = tk.Entry(window)
nodes_entry.pack()

edges_label = tk.Label(window, text="Edges (comma-separated, semicolon-delimited):")
edges_label.pack()
edges_entry = tk.Entry(window)
edges_entry.pack()

create_button = tk.Button(window, text="Create Graph", command=lambda: draw_graph(create_graph()))
create_button.pack()

mvc_button = tk.Button(window, text="Find Minimum Vertex Cover", command=lambda: find_minimum_vertex_cover(create_graph()))
mvc_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()