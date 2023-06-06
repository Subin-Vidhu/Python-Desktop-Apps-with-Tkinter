Tkinter has 3 geometry managers

Pack   : add relative to other widgets

Place  : add on (x,y) coordinate

Grid    : add on AxB grid

###
Pack is one of the geometry managers.

Any widget has a .pack() function

Pack places widgets relative to others

Use only one geometry manager (don't mix pack, place, grid).

###
The place() function has x and y parameters

It puts a widget at a position relative to the top left window (0,0)

x can be as large as the window width, y can be as large as the window height.

###
A grid is an NxM field, like a chess board

All widgets have the .grid(row, column) function

You can set the positions,  btn.grid(row=0, column=0) would put it at (0,0) in the grid.