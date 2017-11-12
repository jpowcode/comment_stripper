Comment Stripper
################

When writing code I like to make sure it is commented properly for future me.
I also like to include features such as doc strings. The problem I find is
that when working on this code the comments take up a lot of space and make it
difficult to see large portions of actual code that is not a comment on the
screen. I've written a program that will extract the comments from a file and
write a new file without the comments. This program as act as a watcher that
continually waits for a change to made to the file with comments and writes to
the commentless file. Now this may be a feature that is available in some
IDE's, but I use `ATOM <https://atom.io/>`__ and I couldn't find anything that
would do this for me.
The way I set up ATOM is with two windows, one on the left with the file
including comments (which I make edits in) and one on the right which contains
the comment less code and is upodated as I work. Comment stripper currently
supports python, c, haskell, javascript, html, clojure and perl. It can be used
to convert a file to one without comments using this example command on a test c
programme.

.. code-block:: bash

  python commentStripper.py -i test.c -o test_out.c

it can also be used in watch mode where the programme output is continually
updated by running the following example command on a test python programme.

.. code-block:: bash

  python commentStripper.py -w -i test.py -o test_out.py
