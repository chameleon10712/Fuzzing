Fuzzing: a survey
======================

This paper

- coverage-based fuzzing

|

- feedback-driven fuzzing mode

- genetic algorithm

|

AFL

- coveraged-based
- feedback-driven

|

Background
-------------

- ``static analysis``

  - the analysis of programs that is performed without actually executing the programs
  - usually performed on the source code
  - by analysis on 
  
    - the lexical, grammar, semantics features, and data flow analysis, model checking

  - pros
  
    - detect hiding bugs
    
  - cons
  
    - high false rate
|

- ``dynamic analysis``

  - need to execute the target program in real systems or emulators
  - pros
  
    -  high accuracy
    
  - cons
  
    - heavy human involvement => low efficiency

|


- ``taint analysis``

|

- ``symbolic execution``

  - theoretical
  
    - could cover any execution path in a program

  - limitation
  
    - path explosion problem
    
      - large scale program
    
    |
    
    - environments interaction
    
      - interacts with components out of the symbolic execution environments, consistency problems may arise
      
        - sys call
        - signal handling
        
      
    

|

- ``fuzzing``

  - a fuzzing test starts with generating massive normal and abnormal inputs to target applications

|

Fuzzing
----------

.. image:: https://i.imgur.com/eV6slIp.png


|

Working process of fuzzing
+++++++++++++++++++++++++++++

.. image:: https://i.imgur.com/e5nWNAl.png




Terms
--------

- ``TCG``

  - Tiny Code Generator
  - `[GitHub] tcg/README  <https://github.com/qemu/qemu/tree/master/tcg#readme>`_
  - `[Blog] 2021 QEMU - AFL++ and TCG <http://blog.terrynini.tw/en/2021-QEMU-AFL-and-TCG/>`_







