Angr
======



CFG
-----

- Control Flow Graph

  - A basic analysis that one might carry out on a binary is a Control Flow Graph. A CFG is a graph with (conceptually) basic blocks as nodes and jumps/calls/rets/etc as edges.

  
- angr includes analyses to recover the control-flow graph of a binary program. This also includes recovery of function boundaries, as well as reasoning about indirect jumps and other useful metadata.

|

- Angr

  - static CFG (CFGFast)
  - dynamic CFG (CFGEmulated)


    .. code:: py

      >>> import angr
      # load your project
      >>> p = angr.Project('/bin/true', load_options={'auto_load_libs': False})

      # Generate a static CFG
      >>> cfg = p.analyses.CFGFast()

      # generate a dynamic CFG
      >>> cfg = p.analyses.CFGEmulated(keep_state=True)

|

Shared Libraries
--------------------

The CFG analysis does not distinguish between code from different binary objects. This means that by default, it will try to analyze control flow through loaded shared libraries. This is almost never intended behavior, since this will extend the analysis time to several days, probably. To load a binary without shared libraries, add the following keyword argument to the ``Project`` constructor: ``load_options={'auto_load_libs': False}``


