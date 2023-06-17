import time
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)
        else:
            print("One or both of the user nodes does not exist.")

    def remove_node(self, node):
        if node in self.graph:
            del self.graph[node]
            for key in self.graph:
                self.graph[key] = [x for x in self.graph[key] if x != node]
        else:
            print("User node does not exist.")

    def remove_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1] = [x for x in self.graph[node1] if x != node2]
            self.graph[node2] = [x for x in self.graph[node2] if x != node1]
        else:
            print("One or both of the user nodes does not exist.")

    def get_connections(self, node):
        if node in self.graph:
            return self.graph[node]
        else:
            print("User node does not exist.")
            return []

    def mutual_friends(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            friends1 = set(self.graph[node1])
            friends2 = set(self.graph[node2])
            return friends1.intersection(friends2)
        else:
            print("One or both of the user nodes does not exist.")
            return []

    def shortest_path(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            visited = set()
            queue = [[node1]]
            if node1 == node2:
                return [node1]
            while queue:
                path = queue.pop(0)
                current_node = path[-1]
                if current_node not in visited:
                    neighbors = self.graph[current_node]
                    for neighbor in neighbors:
                        new_path = list(path)
                        new_path.append(neighbor)
                        queue.append(new_path)
                        if neighbor == node2:
                            return new_path
                    visited.add(current_node)
            return []
        else:
            print("One or both of the user nodes does not exist.")
            return []

    def popular_users(self):
        users = {}
        for node in self.graph:
            users[node] = len(self.graph[node])
        popular = [k for k, v in sorted(users.items(), key=lambda item: item[1], reverse=True)]
        return popular

    def visualize_network(self):
        for node, connections in self.graph.items():
            print(f"{node} is connected to: {', '.join(connections)}")


class SocialNetworkAnalysis:
    def __init__(self):
        self.graph = Graph()

    def add_user(self, node):
        if node not in self.graph.graph:
            self.graph.add_node(node)
        else:
            print("Username already taken. Please choose a different username.")

    def add_connection(self, node1, node2):
        self.graph.add_edge(node1, node2)

    def remove_user(self, node):
        self.graph.remove_node(node)

    def remove_connection(self, node1, node2):
        self.graph.remove_edge(node1, node2)

    def get_connections(self, node):
        return self.graph.get_connections(node)

    def mutual_friends(self, node1, node2):
        return self.graph.mutual_friends(node1, node2)

    def shortest_path(self, node1, node2):
        return self.graph.shortest_path(node1, node2)

    def popular_users(self):
        return self.graph.popular_users()

    def visualize_network(self):
        self.graph.visualize_network()

    def suggest_connection(self):
        for node1 in self.graph.graph:
            for node2 in self.graph.graph:
                if node1 != node2 and node2 not in self.graph.graph[node1]:
                    print(f"Suggest connecting {node1} and {node2}")

    def run_social_network_analysis(self):
        social_network = SocialNetworkAnalysis()

        social_network.add_user("Alice")
        social_network.add_user("Bob")
        social_network.add_user("Charlie")

        social_network.add_connection("Alice", "Bob")
        social_network.add_connection("Bob", "Charlie")

        operations = [
            ("Add User", social_network.add_user, ["User"]),
            ("Add Connection", social_network.add_connection, ["User1", "User2"]),
            ("Remove User", social_network.remove_user, ["User"]),
            ("Remove Connection", social_network.remove_connection, ["User1", "User2"]),
            ("Get Connections", social_network.get_connections, ["User"]),
            ("Mutual Friends", social_network.mutual_friends, ["User1", "User2"]),
            ("Shortest Path", social_network.shortest_path, ["User1", "User2"]),
            ("Popular Users", social_network.popular_users, []),
            ("Visualize Network", social_network.visualize_network, []),
            ("Suggest Connection", social_network.suggest_connection, [])
        ]

        execution_times = []

        for operation, func, args in operations:
            start_time = time.time()
            for _ in range(10000):
                func(*args)
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

            print(f"{operation} execution time: {execution_time} seconds")

        x = [operation[0] for operation in operations]
        y = execution_times

        plt.figure(figsize=(10, 6))
        plt.bar(x, y)
        plt.xlabel("Operations")
        plt.ylabel("Execution Time (seconds)")
        plt.title("Runtime Complexity of Social Network Analysis")
        plt.xticks(rotation=45)
        plt.show()

social_network = SocialNetworkAnalysis()
social_network.run_social_network_analysis()
