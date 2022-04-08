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

Monitor Execution State
+++++++++++++++++++++++++++

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

Analyzing Stage
++++++++++++++++++

- Analysts try to determine the location and root cause of captured violations

  - help with
  
    - debuggers
  
      - GDB
      - windbg
    
    - other binary analysis tools
  
      - IDA Pro
      - OllyDbg
    
    - binary instrumentation tools

      - Pin

|

Types of fuzzers
---------------------

Testcases Generation Method

- mutation based
- generation based

|

Generation Based Fuzzers
++++++++++++++++++++++++++++


- knowledge of program input is required

- File Format Fuzzing

  - usually a configuration file that predefines the file format is provided

  - testcases are generated according to the configuration file

  - testcases are able to pass the validation of programs more easily and could be more likely to test the deeper code of target programs

|

Mutation Based Fuzzers 
++++++++++++++++++++++++++

- easy to start
- more applicable
- widely used by state-of-the-art fuzzers

|

- A set of valid initial inputs are required
- Testcases are generated through the mutation of initial inputs and testcases generated during the fuzzing process

|

Comparison
############

.. raw:: html

    <img src="https://i.imgur.com/9Sv2Ivx.png" width="450px">


|

|

White, Gray, Black Box
+++++++++++++++++++++++++++++


With respect to the dependence on program source code and the degree of program analysis, fuzzers could be classified as white box, gray box and black box.

- white box

  - assumed to have access to the source code of programs
  - more information could be collected through analysis on source code and how testcases affect the program running state

- gray box

  - works without source code
  - gain the internal information of target programs through program analysis

- black box

  - without any knowledge on target program internals


Common Fuzzers
################

.. raw:: html

    <img src="https://i.imgur.com/n6qxcjC.png" width="450px">

|

Strategies of exploring the programs
+++++++++++++++++++++++++++++++++++++++

- Directed Fuzzing
  
  - aims at generation of testcases that cover target code and target paths of programs
  - expect a faster test on programs

- Coverage-based Fuzzing

  - aims at generation of testcases that cover as much code of programs as possible
  -  expect a more thorough test and detect as more bugs as possible


- For both directed fuzzers and coverage-based fuzzers, how to extract the information of executed paths is a key problem

|

Smart, Dumb Fuzzers
++++++++++++++++++++++

Fuzzers could be classified as dumb fuzz and smart
fuzz according to whether there is a feedback between
the monitoring of program execution state and testcase
generation

|

- Smart Fuzzers

  - adjustment the generation of testcases according to the collected information that how testcases affect the program behavior
  
    - mutation based fuzzer
  
      -  feedback information could be used to determine which part of testcases should be mutated and the way to mutate them
      
  - generate better testcases
    
    - gain a better efficiency
  


- Dumb Fuzzers

  -  acquires a better testing speed


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
 

  





