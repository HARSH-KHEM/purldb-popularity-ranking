"""
PageRank-based package popularity ranking for PURLdb.
Part of GSoC proposal prototype.
"""

from packagedb.models import Package
from packageurl import PackageURL

def get_purl_key(purl):
    try:
        p = PackageURL.from_string(purl.strip())
        return (p.type, p.namespace, p.name)
    except Exception:
        return None

def build_dependency_graph():
    graph = {}
    packages = list(Package.objects.all())

    for pkg in packages:
        graph[pkg.uuid] = []

    # map download_url → package
    url_to_pkg = {
        p.download_url.strip(): p
        for p in packages
        if p.download_url
    }

    # build edges
    for pkg in packages:
        for dep in pkg.dependencies.all():

            dep_url = dep.purl.strip()

            dep_pkg = url_to_pkg.get(dep_url)

            if dep_pkg:
                graph[pkg.uuid].append(dep_pkg.uuid)

    return graph


def build_reverse_graph(graph):
    reverse = {node: [] for node in graph}

    for node in graph:
        for dep in graph[node]:
            reverse[dep].append(node)

    return reverse


def compute_pagerank(graph, iterations=10, d=0.85):
    ranks = {node: 1.0 for node in graph}
    reverse_graph = build_reverse_graph(graph)
    N = len(graph)

    for _ in range(iterations):
        new_ranks = {}

        for node in graph:
            rank_sum = 0

            for incoming in reverse_graph.get(node, []):
                out_degree = len(graph[incoming])

                if out_degree > 0:
                    rank_sum += ranks[incoming] / out_degree
                else:
                    rank_sum += ranks[incoming] / N  # 🔥 fix

            new_ranks[node] = (1 - d) + d * rank_sum

        ranks = new_ranks

    # normalization
    max_rank = max(ranks.values())

    if max_rank > 0:
        for k in ranks:
            ranks[k] /= max_rank

    return ranks


def save_ranks_to_db(ranks):
    packages = Package.objects.all()

    for pkg in packages:
        score = ranks.get(pkg.uuid, 0.0)
        pkg.rank_score = score
        pkg.save(update_fields=["rank_score"])


def run_ranking():
    print("Building graph...")
    graph = build_dependency_graph()

    print("Computing PageRank...")
    ranks = compute_pagerank(graph)

    print("Saving results...")
    save_ranks_to_db(ranks)

    print("Ranking completed!")


def update_package_ranks():
    graph = build_dependency_graph()
    ranks = compute_pagerank(graph)

    for uuid, score in ranks.items():
        try:
            pkg = Package.objects.get(uuid=uuid)   
            pkg.rank_score = score
            pkg.save(update_fields=["rank_score"])
        except Package.DoesNotExist:
            continue
        
def debug_graph(graph):
    edge_count = 0

    for node, deps in graph.items():
        if deps:
            print(f"{node} -> {deps}")
            edge_count += len(deps)

    print(f"\nTotal nodes: {len(graph)}")
    print(f"Total edges: {edge_count}")
