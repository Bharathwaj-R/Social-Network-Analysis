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
            for i in self.graph:
                self.graph[i] = [x for x in self.graph[i] if x != node]
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
        while True:
            print("-----------")
            print("1. Add User")
            print("2. Add Connection")
            print("3. Remove User")
            print("4. Remove Connection")
            print("5. Get Connections")
            print("6. Find Mutual Friends")
            print("7. Find Shortest Path")
            print("8. Find Popular Users")
            print("9. Visualize Network")
            print("10. Suggest Connection")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                node = input("Enter user node: ")
                self.add_user(node)
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
                connections = self.get_connections(node)
                print("Connections:", connections)
            elif choice == 6:
                node1 = input("Enter first user node: ")
                node2 = input("Enter second user node: ")
                mutual_friends = self.mutual_friends(node1, node2)
                print("Mutual Friends:", mutual_friends)
            elif choice == 7:
                node1 = input("Enter first user node: ")
                node2 = input("Enter second user node: ")
                shortest_path = self.shortest_path(node1, node2)
                print("Shortest Path:", shortest_path)
            elif choice == 8:
                popular_users = self.find_popular_users()
                if popular_users:
                    print("Popular Users:", popular_users)
                else:
                    print("There are no popular users!!!")
            elif choice == 9:
                if self.visualize_network():
                    self.visualize_network()
                else:
                    print("No network is present!!!")
            elif choice == 10:
                self.suggest_connection()
            elif choice == 0:
                break
            else:
                print("Invalid choice. Try again.")


social_network = SocialNetworkAnalysis()
social_network.run_social_network_analysis()
