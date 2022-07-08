Morest: Model-based RESTful API Testing with Execution Feedback
===================================================================

- OpenAPI
  - Swagger
  
- RAML
- API Blueprint

|

Two most recent Blackbox RESTful API testing techniques

- Restler

  - a bottom-up approach
  - connect the APIs into an Operation Dependency Graph (ODG)

- Resttestgen

  - a top-down approach

|

Morest
---------

- producer-consumer dependencies

- dynamically updating RESTful-service Property Graph (RPG)

- both the bottom-up and top-down approaches


|

Operation Dependency Graph
++++++++++++++++++++++++++++

- OpenAPI specifications

- ODG is a graph 𝐺 = (𝑉 , 𝐸) where 𝑉 is a set of nodes and 𝐸 is a set of directed edges


|

.. image:: https://i.imgur.com/ZLendCp.png


|

property graph
+++++++++++++++++

|

.. image:: https://docs.oracle.com/en/database/oracle/property-graph/21.3/spgdg/img/two_vertices.png

|

.. code::

  Definition 1 (Property Graph). 
  
  A property graph is a directed, edge-labeled, 
  attributed multigraph 𝐺 = (𝑉 , 𝐸, 𝜆, 𝜇) where 
  𝑉 is a set of nodes (or vertices), 
  𝐸 is a set of directed edges, 
  𝜆 : 𝐸 → Σ is an edge labeling function assigning a label from the alphabet Σ to each edge 
  and 𝜇 : (𝑉 ∪ 𝐸) × 𝐾 → 𝑆 is a function assigning key(from K)-value(from S) pairs of properties to the edges and nodes.

|

Related


- `neo4j - Graph Modeling <https://neo4j.com/developer/guide-data-modeling/>`_

- `neo4j - Link Prediction with GDSL and scikit-learn <https://neo4j.com/developer/graph-data-science/link-prediction/scikit-learn/>`_


|

 Experiment
 ++++++++++++
 
 
 - `EvoMaster <https://github.com/EMResearch/EvoMaster>`_
 
  - EvoMaster (www.evomaster.org) is the first (2016) open-source AI-driven tool that automatically generates system-level test cases for web/enterprise applications.
 
 
 - `EvoMaster Benchmark (EMB) <https://github.com/EMResearch/EMB>`_
 
  - EvoMaster Benchmark (EMB): a set of web/enterprise applications for scientific research in Software Engineering.
    EMB collected several different systems, in different programming languages, like Java, Kotlin, JavaScript and C#. In this documentation, EMB will refer to these projects as System Under Test (SUT). Currently, the SUTs are either REST or GraphQL APIs.


 
 
 
 
 
 

