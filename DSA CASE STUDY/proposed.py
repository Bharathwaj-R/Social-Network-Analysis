import heapq

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
            path = queue.rem()
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

    def rem(self):
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

    def add_user(self, node, user_info):
        self.graph.add_node(node)
        self.hashtable.insert(node, user_info)

    def add_connection(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes do not exist.")
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
            print("One or both of the user nodes do not exist.")
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
            print("One or both of the user nodes do not exist.")
            return None
        return self.graph.mutual_friends(node1, node2)

    def find_shortest_path(self, node1, node2):
        if node1 not in self.graph.graph or node2 not in self.graph.graph:
            print("One or both of the user nodes do not exist.")
            return None
        return self.graph.shortest_path(node1, node2)

    def find_popular_users(self):
        return self.graph.popular_users()

    def visualize_network(self):
        self.graph.visualize_network()

    def suggest_connection(self):
        all_users = list(self.graph.graph.keys())
        suggested_connections = []
        
        for i in range(len(all_users)):
            for j in range(i + 1, len(all_users)):
                user1 = all_users[i]
                user2 = all_users[j]
                mutual_friends = self.find_mutual_friends(user1, user2)
                if mutual_friends:
                    suggested_connections.append((user1, user2, mutual_friends))
        
        if suggested_connections:
            suggested_connections.sort(key=lambda x: len(x[2]), reverse=True)
            return suggested_connections[0]
        else:
            return None

    def run_social_network_analysis(self):
        while True:
            print("-----------")
            print("1. Add User")
            print("2. Add Connection")
            print("3. Remove User")
            print("4. Remove Connection")
            print("5. Get User Info")
            print("6. Get Connections")
            print("7. Find Mutual Friends")
            print("8. Find Shortest Path")
            print("9. Find Popular Users")
            print("10. Visualize Network")
            print("11. Suggest Connection")
            print("0. Exit")

            choice = int(input("Enter your choice: "))
            if choice == 0:
                break
            else:
                if choice == 1:
                    node = input("Enter user node: ")
                    user_info = input("Enter user info: ")
                    self.add_user(node, user_info)
                elif choice == 2:
                    node1 = input("Enter first user node: ")
                    node2 = input("Enter second user node: ")
                    self.add_connection(node1, node2)
                elif choice == 3:
                    node = input("Enter user node to remove: ")
                    self.remove_user(node)
                elif choice == 4:
                    node1 = input("Enter first user node: ")
                    node2 = input("Enter second user node: ")
                    self.remove_connection(node1, node2)
                elif choice == 5:
                    node = input("Enter user node: ")
                    user_info = self.get_user_info(node)
                    print("User Info:", user_info)
                elif choice == 6:
                    node = input("Enter user node: ")
                    connections = self.get_connections(node)
                    print("Connections:", connections)
                elif choice == 7:
                    node1 = input("Enter first user node: ")
                    node2 = input("Enter second user node: ")
                    mutual_friends = self.find_mutual_friends(node1, node2)
                    if mutual_friends is not None:
                        print("Mutual Friends:", mutual_friends)
                elif choice == 8:
                    node1 = input("Enter first user node: ")
                    node2 = input("Enter second user node: ")
                    shortest_path = self.find_shortest_path(node1, node2)
                    if shortest_path is not None:
                        print("Shortest Path:", shortest_path)
                elif choice == 9:
                    popular_users = self.find_popular_users()
                    if popular_users:
                        print("Popular Users:", popular_users)
                    else:
                        print("There are no popular users!!!")
                elif choice == 10:
                    self.visualize_network()
                elif choice == 11:
                    suggested_connection = self.suggest_connection()
                    if suggested_connection is not None:
                        print("Suggested Connection:", suggested_connection)
                    else:
                        print("No suggested connection available.")
                else:
                    print("Invalid choice. Try again.")

social_network = SocialNetworkAnalysis()
social_network.run_social_network_analysis()
