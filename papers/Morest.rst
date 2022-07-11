Morest: Model-based RESTful API Testing with Execution Feedback
===================================================================

- `paper <https://arxiv.org/pdf/2204.12148.pdf>`_
- `website <https://sites.google.com/view/restful-morest/home>`_


|

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

OpenAPI
++++++++++

OpenAPI Specification (formerly Swagger Specification) is an API description format for REST APIs. 
An OpenAPI file allows you to describe your entire API.

endpoints

- endpoints (``/users``)
- operations on each endpoint (``GET /users``, ``POST /users``)

|

schema object

- `Swagger - Data Models (Schemas) <https://swagger.io/docs/specification/data-models/>`_
- OpenAPI 3.0 data types are based on an extended subset `JSON Schema Specification Wright Draft 00 <https://json-schema.org/>`_. The data types are described using a `Schema object <https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.3.md#schemaObject>`_

|

property graph
+++++++++++++++++

|

.. image:: https://docs.oracle.com/en/database/oracle/property-graph/21.3/spgdg/img/two_vertices.png

|

|

.. image:: https://i.imgur.com/si1QAaY.png

|

Related


- `neo4j - Graph Modeling <https://neo4j.com/developer/guide-data-modeling/>`_

- `neo4j - Link Prediction with GDSL and scikit-learn <https://neo4j.com/developer/graph-data-science/link-prediction/scikit-learn/>`_

|

- Property Graph Schema

|

Experiment
++++++++++++
 
- `EvoMaster <https://github.com/EMResearch/EvoMaster>`_

  - EvoMaster is the first (2016) open-source AI-driven tool that automatically generates system-level test cases for web/enterprise applications.


- `EvoMaster Benchmark (EMB) <https://github.com/EMResearch/EMB>`_

  - EvoMaster Benchmark (EMB): a set of web/enterprise applications for scientific research in Software Engineering.



 
 

