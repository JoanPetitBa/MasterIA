from heapq import heapify, heappop, heappush
import os
import networkx as nx
import matplotlib.pyplot as plt

graph = {
   "Lleida": {
       "Barcelona": 1.5,
       "Tarragona": 1,
       "Girona": 2.5,
       #"Valencia": 3.5,
       #"Castellon de la Plana": 2.75,
       "Zaragoza": 1.5,
       "Huesca": 1.25,
       #"Alicante": 4.5,
       "Teruel": 2.75
   },
   "Barcelona": {
       "Lleida": 1.5,
       #"Tarragona": 1,
       #"Girona": 1.25,
       #"Valencia": 3.5,
       #"Castellon de la Plana": 2.75,
       #"Zaragoza": 3,
       "Huesca": 3.5,
       #"Alicante": 5,
       "Teruel": 4
   },
   "Tarragona": {
       "Lleida": 1,
       #"Barcelona": 1,
       #"Girona": 2.25,
       "Valencia": 2.75,
       "Castellon de la Plana": 2,
       "Zaragoza": 2.5,
       "Huesca": 3,
       "Alicante": 4,
       #"Teruel": 3
   },
   "Girona": {
       "Lleida": 2.5,
       #"Barcelona": 1.25,
       #"Tarragona": 2.25,
       "Valencia": 4.5,
       #"Castellon de la Plana": 4,
       "Zaragoza": 4.5,
       #"Huesca": 5,
       "Alicante": 6,
       "Teruel": 5
   },
   "Valencia": {
       #"Lleida": 3.5,
       #"Barcelona": 3.5,
       "Tarragona": 2.75,
       "Girona": 4.5,
       #"Castellon de la Plana": 1,
       "Zaragoza": 3,
       "Huesca": 3.5,
       "Alicante": 1.75,
       "Teruel": 2
   },
   "Castellon de la Plana": {
       #"Lleida": 2.75,
       #"Barcelona": 2.75,
       "Tarragona": 2,
       #"Girona": 4,
       #"Valencia": 1,
       #"Zaragoza": 2.75,
       "Huesca": 3.25,
       #"Alicante": 2.75,
       "Teruel": 1.5
   },
   "Zaragoza": {
       "Lleida": 1.5,
       #"Barcelona": 3,
       "Tarragona": 2.5,
       "Girona": 4.5,
       "Valencia": 3,
       #"Castellon de la Plana": 2.75,
       #"Huesca": 0.75,
       "Alicante": 4.25,
       "Teruel": 2
   },
   "Huesca": {
       "Lleida": 1.25,
       "Barcelona": 3.5,
       "Tarragona": 3,
       #"Girona": 5,
       "Valencia": 3.5,
       "Castellon de la Plana": 3.25,
       #"Zaragoza": 0.75,
       "Alicante": 5,
       "Teruel": 3
   },
   "Alicante": {
       #"Lleida": 4.5,
       #"Barcelona": 5,
       "Tarragona": 4,
       "Girona": 6,
       "Valencia": 1.75,
       #"Castellon de la Plana": 2.75,
       "Zaragoza": 4.25,
       "Huesca": 5,
       "Teruel": 3
   },
   "Teruel": {
       "Lleida": 2.75,
       "Barcelona": 4,
       #"Tarragona": 3,
       "Girona": 5,
       "Valencia": 2,
       "Castellon de la Plana": 1.5,
       "Zaragoza": 2,
       "Huesca": 3,
       "Alicante": 3
   }
}

class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph  # A dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight  # Add a connection to its neighbor

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0  # Set the source value to 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        # Predecessors dictionary to reconstruct paths
        predecessors = {node: None for node in self.graph}

        while pq:  # While the priority queue isn't empty
            current_distance, current_node = heappop(pq)

            if current_node in visited:
                continue 
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                # Calculate the distance from current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    predecessors[neighbor] = current_node
                    heappush(pq, (tentative_distance, neighbor))

        return distances, predecessors
       
    def shortest_path(self, source: str, target: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        path = []
        current_node = target

        # Backtrack from the target node using predecessors
        while current_node:
            path.append(current_node)
            current_node = predecessors[current_node]

        # Reverse the path and return it
        path.reverse()
        return path if path[0] == source else []

os.system("cls")
# Create the Graph object
G = Graph(graph)

origen = "Zaragoza"
desti = "Castellon de la Plana"

# Get shortest distances and predecessors
distances, predecessors = G.shortest_distances(origen)

# Print the total shortest distance to the destination
total_time = distances[desti]
print(f"The shortest time from {origen} to {desti} is {total_time}h")

# Get the shortest path
path = G.shortest_path(origen, desti)
print(f"The shortest path from {origen} to {desti} is {', '.join(path)}")