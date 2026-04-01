# GSoC Proposal: Package Popularity Ranking in PURLdb

## 1. Introduction

This proposal aims to implement a dependency-based popularity ranking system for packages in PURLdb.

Modern software ecosystems contain millions of packages, but not all packages are equally important. Existing metrics such as download counts or GitHub stars do not fully capture real-world usage.

This project proposes a graph-based approach, where package importance is derived from dependency relationships using a PageRank-style algorithm.

---

## 2. Current Work

I have already implemented a working prototype of this system.

The implementation includes:

* Construction of a dependency graph using package relationships
* A PageRank-style algorithm to compute importance scores
* Normalization of scores for consistent comparison
* Storage of results in the database (`rank_score`)
* A REST API endpoint (`/top-packages/`) to expose ranked results
* Support for query-based limiting

Example result:

* Highly depended-upon packages receive higher scores
* Less connected packages receive lower scores

This prototype demonstrates the feasibility of dependency-based ranking within PURLdb.

---

## 3. Proposed Work

Building upon the current prototype, the project will focus on improving ranking quality and integrating additional signals.

### 3.1 Improved Graph Construction

* Ensure accurate dependency resolution across ecosystems
* Handle missing or incomplete dependency data

### 3.2 Ranking Enhancements

* Introduce weighting for dependencies (e.g., direct vs transitive)
* Improve handling of dangling nodes

### 3.3 Freshness Signal

* Incorporate package activity (e.g., recent releases)
* Apply decay to outdated or inactive packages

### 3.4 API Improvements

* Extend API to support filtering and pagination
* Provide richer metadata in responses

### 3.5 Evaluation

* Validate ranking quality on selected ecosystems
* Compare results with existing popularity indicators

---

## 4. Timeline

### Community Bonding Period

* Study PURLdb architecture and data models
* Refine current prototype based on mentor feedback

### Phase 1 (Weeks 1–4)

* Improve dependency graph construction
* Optimize PageRank computation
* Ensure scalability for large datasets

### Phase 2 (Weeks 5–8)

* Implement ranking enhancements (weights, improvements)
* Add freshness-based scoring

### Phase 3 (Weeks 9–12)

* Extend API functionality
* Perform evaluation and testing
* Prepare documentation

---

## 5. Deliverables

* Dependency-based ranking system integrated into PURLdb
* Improved PageRank algorithm with enhancements
* API endpoint for accessing ranked packages
* Documentation and usage examples

---

## 6. Why Me

I have already implemented a working prototype of the ranking system, including graph construction, ranking computation, and API exposure.

This demonstrates my ability to understand the problem and contribute effectively to PURLdb.

I am comfortable working with Python, Django, and graph-based algorithms, and I am motivated to further improve this system.

---

## 7. Conclusion

This project introduces a scalable and meaningful approach to ranking software packages based on actual usage within ecosystems.

By leveraging dependency relationships, it provides a more accurate measure of package importance and lays the foundation for further enhancements in PURLdb.
