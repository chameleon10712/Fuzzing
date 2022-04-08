Fuzzing: a survey
======================

`link <https://cybersecurity.springeropen.com/track/pdf/10.1186/s42400-018-0002-y.pdf>`_

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
  
    - high detection speed
    - detect hiding bugs
    
  - cons
  
    - high false rate
|

- ``dynamic analysis``

  - need to execute the target program in real systems or emulators
  - pros
  
    -  high accuracy
    
  - cons

    - debugging, analyzing and running of the target programs in dynamic analysis cause a heavy human involvement
    
      - low efficiency
      
    - slow speed, low efficiency, high requirements on the technical level of testers, poor scalability, and is difficult to carry out large-scale testing.

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

4 main stages

- the testcase generation stage
- testcase running stage
- program execution state monitoring
- analysis of exceptions.



.. image:: https://i.imgur.com/e5nWNAl.png

|

Testcase
+++++++++++

- A fuzzing test starts from the generation of a bunch of program inputs, i.e., testcases.
- The quality of generated testcases directly effects the test effects.

|

Testcase Generators
+++++++++++++++++++++

- 2 kind of generators are used in state-of-the-art fuzzers

  - generation based generators
  - mutation based generators

|

Start & Finish
+++++++++++++++++

- Fuzzers automatically start and finish the target program process and drive the testcase handling process of target programs. 

  - predefine the parameters and environment variables

- Fuzzers stops at

  - predefined timeout
  - program execution hangs or crashes

|

Monitor Execution
+++++++++++++++++++

- monitor on

  - system signals
  - crashes
  - other violations

|

Capture Violations
+++++++++++++++++++++

For violations without intuitive program abnormal behaviors:

- Tools

  - AddressSanitizer
  - DataFlowsanitizer
  - ThreadSanitizer
  - LeakSanitizer

- When violations are captured, fuzzers store the corresponding testcase for latter replay and analysis


|

Terms
--------

- ``TCG``

  - Tiny Code Generator
  - `tcg/README  <https://github.com/qemu/qemu/tree/master/tcg#readme>`_
  - `ref <http://blog.terrynini.tw/en/2021-QEMU-AFL-and-TCG/>`_

|

- ``Sanitizer``

  - `ref <https://hpc-wiki.info/hpc/Compiler_Sanitizers>`_
  - The C/C++ compilers ``Clang/LLVM`` and ``GCC`` support so-called sanitizers
  - These sanitizers are built into the application code and track the execution at runtime to report execution errors
  - Current
  
    - ``AddressSanitizer`` and ``LeakSanitizer``
  
      - ``AddressSanitizer``

        - memory error detector for C/C++

      - ``LeakSanitizer``

        - detects memory leaks
        - is part of the ``AddressSanitizer`` for many operating systems
        
      - They detect following errors
      
        - Use after free (dangling pointer dereference)
        - Heap buffer overflow
        - Stack buffer overflow
        - Global buffer overflow
        - Use after return
        - Use after scope
        - Initialization order bugs
        - Memory leaks
    
    - ``ThreadSanitizer``
 

  





