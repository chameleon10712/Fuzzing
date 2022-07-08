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




