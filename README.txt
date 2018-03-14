Required modules: sys, time, graphics, math, copy, python-chess

Graphics module is included as graphics.py.
This is a code we found at: http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf

Installing python-chess module
==============================
Step 1: go to https://pypi.python.org/pypi/python-chess
Step 2: download the tar.gz file on the front page (top-right corner).
Step 3: run "pip install absolute_location_of_tar.gz_file" from the command line.

BoardGraphics.py: handles graphical representation of the board, updates each human turn.
bGraphics2.py: handles most interactions with python-chess so ChessSimAI can
interact with the board and query about the current board state.
ChessSimAI.py: contains all code for the heuristic AI. Receives a board state and
returns the suggested play for that state.

Run the code:
python bGraphics2.py

One certain computers, some of the images where having weird data problems. If
this happens to you (and it shouldn't), comment out lines 38 to 40 and
uncomment lines 41 to 43 in BoardGraphics.py.

Also for certain computers (basically mine):
To type in moves for the board, make sure you type them in like 'h8g8', not h8g8. You might not
need to do this. We don't know why my computer can't handle it, but it can't.
