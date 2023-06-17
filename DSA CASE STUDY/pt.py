import heapq
import time
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = []

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)
        self.graph[node2].append(node1)

    def remove_node(self, node):
        del self.graph[node]
        for key in self.graph:
            self.graph[key] = [x for x in self.graph[key] if x != node]

    def remove_edge(self, node1, node2):
        self.graph[node1] = [x for x in self.graph[node1] if x != node2]
        self.graph[node2] = [x for x in self.graph[node2] if x != node1]

    def get_connections(self, node):
        return self.graph[node]

    def mutual_friends(self, node1, node2):
        friends1 = set(self.graph[node1])
        friends2 = set(self.graph[node2])
        return friends1.intersection(friends2)

    def shortest_path(self, node1, node2):
        visited = set()
        queue = PriorityQueue()
        queue.insert(0, [node1])  # Insert initial path with priority 0
        if node1 == node2:
            return [node1]
        while not queue.is_empty():
            path = queue.pop()
            current_node = path[-1]
            if current_node not in visited:
                neighbors = self.graph[current_node]
                for neighbor in neighbors:
                    new_path = list(path)
                    new_path.append(neighbor)
                    priority = len(new_path)  # Use path length as priority
                    queue.insert(priority, new_path)
                    if neighbor == node2:
                        return new_path
                visited.add(current_node)
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


class HashTable:
    def __init__(self):
        self.table = {}

    def insert(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table.get(key)

    def remove(self, key):
        if key in self.table:
            del self.table[key]


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.index = 0

    def insert(self, priority, item):
        heapq.heappush(self.heap, (priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.heap)[-1]

    def is_empty(self):
        return len(self.heap) == 0


class DisjointSets:
    def __init__(self):
        self.sets = {}

    def make_set(self, item):
        self.sets[item] = item

    def find(self, item):
        if self.sets[item] != item:
            self.sets[item] = self.find(self.sets[item])
        return self.sets[item]

    def union(self, item1, item2):
        root1 = self.find(item1)
        root2 = self.find(item2)
        self.sets[root2] = root1


class SocialNetworkAnalysis:
    def __init__(self):
        self.graph = Graph()
        self.hashtable = HashTable()
        self.priorityqueue = PriorityQueue()
        self.disjointsets = DisjointSets()

    def add_user(self, node, user_info):
        self.graph.add_node(node)
        self.hashtable.insert(node, user_info)

    def add_connection(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes does not exist.")
            return
        self.graph.add_edge(node1, node2)

    def remove_user(self, node):
        if node not in self.graph.graph:
            print("The user node does not exist.")
            return
        self.graph.remove_node(node)
        self.hashtable.remove(node)

    def remove_connection(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes does not exist.")
            return
        self.graph.remove_edge(node1, node2)

    def get_user_info(self, node):
        if node not in self.graph.graph:
            print("The user node does not exist.")
            return
        return self.hashtable.get(node)

    def get_connections(self, node):
        if node not in self.graph.graph:
            print("The user node does not exist.")
            return
        return self.graph.get_connections(node)

    def find_mutual_friends(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes does not exist.")
            return -1
        return self.graph.mutual_friends(node1, node2)

    def find_shortest_path(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes does not exist.")
            return -1
        return self.graph.shortest_path(node1, node2)

    def find_popular_users(self):
        return self.graph.popular_users()

    def visualize_network(self):
        self.graph.visualize_network()

    def suggest_connection(self):
        users = list(self.graph.graph.keys())
        num_users = len(users)
        for i in range(num_users - 1):
            for j in range(i + 1, num_users):
                user1 = users[i]
                user2 = users[j]
                if not self.graph.get_connections(user1) and not self.graph.get_connections(user2):
                    mutual_friends = self.find_mutual_friends(user1, user2)
                    if mutual_friends:
                        return user1, user2, mutual_friends
        return None

    def run_social_network_analysis(self):
        social_network = SocialNetworkAnalysis()

        social_network.add_user("Alice", "2")
        social_network.add_user("Bob", "2")
        social_network.add_user("Charlie", "2")

        social_network.add_connection("Alice", "Bob")
        social_network.add_connection("Bob", "Charlie")

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            connections = social_network.get_connections("Bob")
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_connections = sum(execution_times) / len(execution_times)
        print("Average execution time for getting connections:", avg_execution_time_connections)

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            mutual_friends = social_network.find_mutual_friends("Alice", "Charlie")
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_mutual_friends = sum(execution_times) / len(execution_times)
        print("Average execution time for finding mutual friends:", avg_execution_time_mutual_friends)

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            shortest_path = social_network.find_shortest_path("Alice", "Charlie")
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_shortest_path = sum(execution_times) / len(execution_times)
        print("Average execution time for finding shortest path:", avg_execution_time_shortest_path)

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            popular_users = social_network.find_popular_users()
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_popular_users = sum(execution_times) / len(execution_times)
        print("Average execution time for finding popular users:", avg_execution_time_popular_users)

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            social_network.visualize_network()
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_visualize_network = sum(execution_times) / len(execution_times)
        print("Average execution time for visualizing network:", avg_execution_time_visualize_network)

        execution_times = []

        for _ in range(10000):
            start_time = time.time()
            social_network.suggest_connection()
            end_time = time.time()
            execution_time = end_time - start_time
            execution_times.append(execution_time)

        avg_execution_time_suggest_connection = sum(execution_times) / len(execution_times)
        print("Average execution time for suggesting connection:", avg_execution_time_suggest_connection)

        x = [
            "Get Connections",
            "Find Mutual Friends",
            "Find Shortest Path",
            "Find Popular Users",
            "Visualize Network",
            "Suggest Connection"
        ]
        y = [
            avg_execution_time_connections,
            avg_execution_time_mutual_friends,
            avg_execution_time_shortest_path,
            avg_execution_time_popular_users,
            avg_execution_time_visualize_network,
            avg_execution_time_suggest_connection
        ]

        plt.figure(figsize=(10, 6))
        plt.bar(x, y)
        plt.xlabel("Operations")
        plt.ylabel("Average Execution Time (seconds)")
        plt.title("Runtime Complexity of Social Network Analysis")
        plt.show()


s = SocialNetworkAnalysis()
s.run_social_network_analysis()
