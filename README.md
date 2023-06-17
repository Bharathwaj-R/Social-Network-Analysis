
Table of Contents :

1	Topic Introduction	
2	Applications	
3	Existing Data Structures used	
4	List of problems identified in using existing data structures	
5	Proposed hybrid data structure	
6	Added operations	
7	Comparison between proposed data structure and existing data structure	
8	References	
9	Appendix	

Topic: 
Social Network Analysis
Social Network Analysis (SNA) is a field of study that analyzes the relationships and interactions between individuals or entities within a network. By examining the structure and dynamics of social networks, SNA provides insights into social systems and their impact on various phenomena. SNA uses mathematical and statistical techniques to map and measure social connections, identify influential actors, detect communities, and understand information flow and diffusion processes. It has applications in sociology, psychology, organizational studies, marketing, and other disciplines where understanding social relationships is crucial.
At the heart of SNA is the concept of nodes and edges. Nodes represent individuals, organizations, or any entities in the network, while edges depict the relationships or interactions between them. Through visualizing and analyzing these networks, SNA uncovers patterns and properties that help us understand social structures and dynamics. Measures such as centrality, connectivity, clustering, and path analysis provide quantitative insights into network characteristics, identifying key individuals, hubs, and pathways of information dissemination.
SNA has numerous practical applications. In social media analysis, it helps understand user behaviors, detect influential users or communities, and analyze sentiment and opinion dynamics. In organizational studies, SNA uncovers informal communication networks, identifies influential employees or leaders, and assesses collaboration patterns. In epidemiology, SNA aids in tracking disease spread, identifying high-risk individuals, and evaluating intervention strategies. By leveraging SNA, researchers and practitioners gain a deeper understanding of social systems, enabling them to make informed decisions, design effective interventions, and improve social outcomes.

Applications of Social Network Analysis in real-life:
Social Media Analysis: SNA is used to analyze social media networks, understand user behavior, and identify influential users for targeted advertising and brand management.
Organizational Analysis: SNA helps study communication and collaboration patterns in organizations, identify key influencers, improve information flow, and enhance teamwork and decision-making processes.
Epidemiology and Public Health: SNA aids in understanding the spread of diseases, identifying high-risk individuals, and designing effective intervention strategies and public health policies.
Influence and Opinion Dynamics: SNA helps study how information spreads within networks, identify influential individuals or opinion leaders, and design persuasive communication strategies and behavior change initiatives.
Collaborative Networks and Innovation: SNA is used to map collaborations among researchers, institutions, and industries, identify potential partners, evaluate knowledge flow, and foster innovation ecosystems. 
Existing data structures used

The existing data structures which are used for this purpose are:
Graph with Adjacency List:
1.	In the adjacency list representation, a graph is stored as an array of linked lists or arrays.
2.	Each node in the graph corresponds to an index in the array, and the linked list or array at that index stores the neighbors of that node.
3.	Each element in the linked list or array represents an edge and contains information such as the connected node and possibly additional attributes (weight, edge type, etc.).
4.	This representation is suitable for sparse graphs, where the number of edges is relatively small compared to the number of nodes.
5.	It offers efficient storage and traversal of the graph's edges and is particularly useful when the focus is on exploring node connections or performing operations like breadth-first search or depth-first search.
6.	The space complexity of the adjacency list representation is O(N + E), where N is the number of nodes and E is the number of edges.
Graph with Adjacency Matrix:
1.	In the adjacency matrix representation, a graph is stored as a 2D matrix.
2.	The rows and columns of the matrix correspond to the nodes in the graph.
3.	The value stored in the cell (i, j) represents the presence or absence of an edge between nodes i and j.
4.	This representation is suitable for dense graphs, where the number of edges is close to the maximum possible (E ≈ N^2).
5.	It allows for efficient lookup of edge existence and provides constant time complexity (O(1)) for checking whether an edge exists between two nodes.
6.	However, the adjacency matrix consumes more memory compared to the adjacency list, even for sparse graphs, as it requires a matrix of size N x N.
7.	The space complexity of the adjacency matrix representation is O(N^2), where N is the number of nodes.

List of problems identified in using existing data structures
The problems faced when using the above-mentioned existing data structures are:
1.	Memory consumption - Some data structures, such as tries and graphs, can consume significant memory resources, especially when dealing with large-scale malware signature databases. This can lead to increased storage costs and slower processing.
2.	False positives and false negatives - Data structures like Bloom filters may introduce false positives, where a non-malicious signature is mistakenly identified as malware, or false negatives, where a malware signature is not detected. Balancing accuracy and efficiency is a challenge in malware signature detection [1].
3.	Scalability - As the volume of malware signatures grows exponentially, scalability becomes a concern. Efficient storage, retrieval, and search of signatures become challenging for data structures that don't scale well with the increasing size of the database.
4.	Performance trade-offs - Different data structures offer varying trade-offs between time complexity, memory consumption, and accuracy. Choosing the most appropriate data structure for a specific use case requires careful consideration of these factors.
5.	Dynamic signature updates - Malware signatures are continuously updated as new threats emerge. Efficiently handling dynamic updates in data structures without causing disruptions or performance degradation can be a complex task.
 
Proposed hybrid data structure
List of data structure used in proposed hybrid data structure :
- Graph: Represents a graph using adjacency lists and provides various graph-related operations.
- HashTable: Implements a basic hash table for storing key-value pairs.
- PriorityQueue: Implements a priority queue using a heap for efficient priority-based operations.
- DisjointSets: Implements the disjoint-set data structure for efficient set operations.

Graph:
add_node(node): O(1)
add_edge(node1, node2): O(1)
remove_node(node): O(|V| + |E|), where |V| is the number of nodes and |E| is the number of edges.
remove_edge(node1, node2): O(|V|), where |V| is the number of nodes.
get_connections(node): O(1)
mutual_friends(node1, node2): O(|V1| + |V2|), where |V1| and |V2| are the number of connections for node1 and node2 respectively.
shortest_path(node1, node2): O(|V| + |E|), where |V| is the number of nodes and |E| is the number of edges.
popular_users(): O(|V|log|V|), where |V| is the number of nodes.
visualize_network(): O(|V| + |E|), where |V| is the number of nodes and |E| is the number of edges.

HashTable:
insert(key, value): O(1)
get(key): O(1)
remove(key): O(1)
PriorityQueue (implemented using a heap):
insert(priority, item): O(log n), where n is the number of items in the priority queue.
pop(): O(log n), where n is the number of items in the priority queue.
is_empty(): O(1)
DisjointSets:
make_set(item): O(1)
find(item): O(log n), where n is the number of items in the disjoint sets.
union(item1, item2): O(log n), where n is the number of items in the disjoint sets.



