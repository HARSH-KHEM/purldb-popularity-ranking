# GSoC Proposal: Package Popularity Ranking in PURLdb

## 1. Introduction

This proposal aims to implement a dependency-based popularity ranking system for software packages in PURLdb.

Modern software ecosystems contain millions of packages, but their importance varies significantly. Common metrics such as download counts or GitHub stars do not fully reflect real-world usage or ecosystem impact.

This project proposes a graph-based approach in which package importance is derived from dependency relationships using a PageRank-style algorithm. Packages that are widely depended upon by others are assigned higher importance scores, capturing their role within the ecosystem.

---

## 2. Current Work

A working prototype of the proposed system has already been implemented.

The current implementation includes:

* Construction of a dependency graph using package relationships
* A PageRank-style algorithm to compute importance scores
* Normalization of scores for consistent comparison
* Storage of computed scores in the database (`rank_score`)
* A REST API endpoint (`/top-packages/`) to expose ranked results
* Support for query-based result limiting

The prototype demonstrates that:

* Packages with high dependency centrality receive higher scores
* Less connected or isolated packages receive lower scores

This validates the feasibility of dependency-based ranking within PURLdb.

---

## 3. Proposed Work

Building on the existing prototype, the project will focus on improving ranking quality, robustness, and integration within PURLdb.

### 3.1 Improved Graph Construction

* Ensure accurate dependency resolution across ecosystems
* Handle missing, incomplete, or inconsistent dependency data
* Optimize graph building for large-scale datasets

### 3.2 Ranking Enhancements

* Introduce weighted edges (e.g., direct vs transitive dependencies)
* Improve handling of dangling nodes and sparse graphs
* Explore convergence optimizations for scalability

### 3.3 Freshness and Activity Signals

* Incorporate package activity (e.g., recent releases or updates)
* Apply decay functions to reduce scores of inactive packages
* Combine structural importance with temporal relevance

### 3.4 API Enhancements

* Extend API to support filtering, pagination, and sorting
* Provide richer metadata in responses
* Ensure efficient query performance

### 3.5 Evaluation and Validation

* Evaluate ranking quality on selected ecosystems
* Compare results with existing popularity indicators
* Analyze ranking stability and interpretability

---

## 4. Timeline

### Community Bonding Period

* Study PURLdb architecture, data models, and APIs
* Review existing prototype with mentors and incorporate feedback
* Finalize design decisions for graph construction and ranking

### Phase 1 (Weeks 1–4)

* Improve dependency graph construction
* Optimize PageRank computation for scalability
* Validate correctness on sample datasets

### Phase 2 (Weeks 5–8)

* Implement ranking enhancements (weights, improvements)
* Integrate freshness and activity-based scoring
* Begin performance optimization

### Phase 3 (Weeks 9–12)

* Extend API functionality and improve usability
* Conduct evaluation and benchmarking
* Finalize documentation and testing

---

## 5. Deliverables

* Dependency-based ranking system integrated into PURLdb
* Enhanced PageRank algorithm with weighting and freshness signals
* API endpoints for accessing ranked packages
* Documentation and usage examples
* Evaluation results and performance analysis

---

## 6. Why Me

I have already developed a working prototype of this system, including graph construction, ranking computation, and API exposure.

This demonstrates my ability to understand the problem, design a solution, and implement it within the PURLdb ecosystem.

I am comfortable working with Python, Django, and graph-based algorithms, and I am motivated to refine this system into a robust and scalable solution.

---

## 7. Expected Impact

* Enables identification of critical packages within ecosystems
* Helps prioritize indexing and analysis in PURLdb
* Provides a more accurate measure of real-world package importance
* Establishes a foundation for advanced multi-signal ranking systems

---

## 8. Conclusion

This project introduces a scalable and meaningful approach to ranking software packages based on their actual role within dependency networks.

By leveraging dependency relationships, it provides a more accurate representation of ecosystem importance and enhances the analytical capabilities of PURLdb.
