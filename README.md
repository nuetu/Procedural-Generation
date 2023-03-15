# Procedural Generation
Personal project that fills a grid with any random, but available, block to create new patterns.
Blocks have 4 sides, each either with a flush or open attribute. 
If you imagine a straight vertical line inside a square, it touches the top and bottom, but not the sides.
Therefore it is 
- top: flush, 
- right: open, 
- bottom: flush, 
- left: open

Any block connecting to it on any side would have to have the same side attribute to connect. 
- A block on top of the vertical line block could be anything, but must have it's bottom be flush.
- A block to the right of the vertical line block could be anything, but must have it's left be open.
- A block on bottom of the vertical line block could be anything, but must have it's top be flush.
- A block to the left of the vertical line block could be anything, but must have it's right be open.

All blocks exist as rectangles merged together at 0, 90, 180, and 270 degrees to form 16 different blocks. 

the program explains how to use it, but if you run it then type run() in the terminal it will populate the grid using Tkinter python graphics library.
