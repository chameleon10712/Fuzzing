Atheris
==========

- `Atheris Github <https://github.com/google/atheris>`_


Installation
---------------

With pip

.. code:: sh

  pip3 install atheris

|

Building from Source

.. code:: sh

  # Build latest release from source
  pip3 install --no-binary atheris atheris
  # Build development code from source
  git clone https://github.com/google/atheris.git
  cd atheris
  pip3 install .


|

Command
------------

With example file

- sample/atheris_1.py
- sample/ahteris_str.py
- sample/ahteris_api.py

|

.. code:: sh

  python3 atheris_1.py
  #basic testcase

  python3 atheris_str.py
  #str testcase

  python3 atheris_api.py
  #FastAPI testcase, require atheris_str.py


reference

- `FastAPI <https://fastapi.tiangolo.com/>`_



|

Example
------------

- `[GitHub] Geekfest-2021-Hackathon/chaos-engineering <https://github.com/Geekfest-2021-Hackathon/chaos-engineering>`_


``atheris_str.py``

.. code:: python

  def not_kirby(s: str):
      if len(s) < 5:
          return True

      if s[0] == "k":
          if s[1] == "i":
              if s[2] == "R":
                  if s[3] == "b":
                      if s[4] == "Y":
                          raise ValueError(f"{s} is not accepted by this function.")

      return True


|

output (truncated)

.. code::

  #2      INITED cov: 3 ft: 3 corp: 1/1b exec/s: 0 rss: 31Mb
  #272    NEW    cov: 5 ft: 5 corp: 2/7b lim: 6 exec/s: 0 rss: 31Mb L: 6/6 MS: 5 ShuffleBytes-CopyPart-ChangeBinInt-InsertRepeatedBytes-CrossOver-
  #2790   NEW    cov: 6 ft: 6 corp: 3/27b lim: 29 exec/s: 0 rss: 31Mb L: 20/20 MS: 3 ChangeBinInt-InsertByte-InsertRepeatedBytes-
  #2814   REDUCE cov: 6 ft: 6 corp: 3/22b lim: 29 exec/s: 0 rss: 31Mb L: 15/15 MS: 4 ChangeBinInt-ShuffleBytes-ChangeBinInt-EraseBytes-
  #2860   REDUCE cov: 6 ft: 6 corp: 3/20b lim: 29 exec/s: 0 rss: 31Mb L: 13/13 MS: 1 EraseBytes-
  #2891   REDUCE cov: 6 ft: 6 corp: 3/17b lim: 29 exec/s: 0 rss: 31Mb L: 10/10 MS: 1 EraseBytes-
  #3062   REDUCE cov: 6 ft: 6 corp: 3/15b lim: 29 exec/s: 0 rss: 31Mb L: 8/8 MS: 1 EraseBytes-
  #3219   REDUCE cov: 6 ft: 6 corp: 3/14b lim: 29 exec/s: 0 rss: 31Mb L: 7/7 MS: 2 ChangeBit-EraseBytes-
  #3542   REDUCE cov: 6 ft: 6 corp: 3/13b lim: 29 exec/s: 0 rss: 31Mb L: 6/6 MS: 3 ChangeByte-ChangeASCIIInt-EraseBytes-
  #4272   REDUCE cov: 7 ft: 7 corp: 4/20b lim: 33 exec/s: 0 rss: 31Mb L: 7/7 MS: 5 ChangeASCIIInt-ChangeByte-ChangeASCIIInt-InsertByte-ChangeBit-
  #4881   REDUCE cov: 7 ft: 7 corp: 4/19b lim: 38 exec/s: 0 rss: 31Mb L: 6/6 MS: 4 ShuffleBytes-InsertByte-ChangeBit-EraseBytes-
  #29442  REDUCE cov: 8 ft: 8 corp: 5/25b lim: 277 exec/s: 0 rss: 31Mb L: 6/6 MS: 1 ChangeByte-
  #33395  NEW    cov: 9 ft: 9 corp: 6/55b lim: 309 exec/s: 0 rss: 31Mb L: 30/30 MS: 3 CrossOver-ChangeBit-InsertRepeatedBytes-
  #33521  REDUCE cov: 9 ft: 9 corp: 6/49b lim: 309 exec/s: 0 rss: 31Mb L: 24/24 MS: 1 EraseBytes-
  #33577  REDUCE cov: 9 ft: 9 corp: 6/48b lim: 309 exec/s: 0 rss: 31Mb L: 23/23 MS: 1 EraseBytes-
  #33714  REDUCE cov: 9 ft: 9 corp: 6/40b lim: 309 exec/s: 0 rss: 31Mb L: 15/15 MS: 2 ChangeBit-EraseBytes-
  #33775  REDUCE cov: 9 ft: 9 corp: 6/37b lim: 309 exec/s: 0 rss: 31Mb L: 12/12 MS: 1 EraseBytes-
  #34551  REDUCE cov: 9 ft: 9 corp: 6/32b lim: 309 exec/s: 0 rss: 31Mb L: 7/7 MS: 1 EraseBytes-
  #35509  REDUCE cov: 9 ft: 9 corp: 6/31b lim: 317 exec/s: 0 rss: 31Mb L: 6/6 MS: 3 ShuffleBytes-ChangeBit-EraseBytes-

   === Uncaught Python exception: ===
  ValueError: kiRbY
   is not accepted by this function.
  Traceback (most recent call last):
    File "/app/samples/atheris_only/atheris_str.py", line 27, in test_one_input
      not_kirby(random_str)
    File "/app/samples/atheris_only/atheris_str.py", line 18, in not_kirby
      raise ValueError(f"{s} is not accepted by this function.")


