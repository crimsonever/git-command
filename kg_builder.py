import pandas as pd
from rdflib import Graph, URIRef, Literal, Namespace
import networkx as nx
import matplotlib.pyplot as plt


def load_triples(csv_path):
    return pd.read_csv(csv_path)


def build_rdf_graph(triples):
    g = Graph()
    EX = Namespace("http://example.org/")

    for _, row in triples.iterrows():
        subj = URIRef(EX[row['subject']])
        pred = URIRef(EX[row['predicate']])
        obj = URIRef(EX[row['object']])
        g.add((subj, pred, obj))

    return g


def rdf_to_nx_graph(rdf_graph):
    G = nx.DiGraph()
    for s, p, o in rdf_graph:
        G.add_edge(str(s).split("/")[-1], str(o).split("/")[-1], label=str(p).split("/")[-1])
    return G


def visualize_graph(G):
    pos = nx.spring_layout(G)
    edge_labels = nx.get_edge_attributes(G, 'label')

    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
    plt.title("Knowledge Graph")
    plt.show()


if __name__ == "__main__":
    triples = load_triples("data/triples.csv")
    rdf_graph = build_rdf_graph(triples)
    rdf_graph.serialize(destination="data.ttl", format="ttl")
    nx_graph = rdf_to_nx_graph(rdf_graph)
    visualize_graph(nx_graph)
