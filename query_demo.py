from rdflib import Graph


def run_query():
    g = Graph()
    g.parse("data.ttl", format="ttl")  # 之前导出的 TTL 文件

    q = """
    SELECT ?person ?company
    WHERE {
        ?person <http://example.org/works_at> ?company .
    }
    """

    results = g.query(q)
    for row in results:
        print(f"{row.person.split('/')[-1]} works at {row.company.split('/')[-1]}")


if __name__ == "__main__":
    run_query()
