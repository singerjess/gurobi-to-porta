 
PORTA is a collection of routines for analyzing polytopes and
polyhedra. The polyhedra are either given as the convex hull of a set
of points plus (possibly) the convex cone of a set of vectors, or as a
system of linear equations and inequalities.

The name PORTA is an abbreviation for POlyhedron Representation
Transformation Algorithm and points to the basic function 'traf'.  This
function performs a transformation from one  of  the two
representations to the other representation.  For this, 'traf' uses a
Fourier - Motzkin elimination  algorithm which projects  a linear
system on subspaces xi = 0. This projection of a given  system  of
linear  inequalities  can  be  done separately by using the function
'fmel'.

Sometimes it is of interest to know all integral points contained  in
a  polyhedron  which  is given by a system of linear equations and
inequalities. For this one has the  function 'vint' which enumerates
all the valid integral points within given bounds.  As a special
function in this context 'fctp' checks the facet inducing property of a
set of linear inequalities for a polyhedron given as a convex hull plus
a convex cone.  The function 'fctp' uses a  function 'dim', which
computes the dimension of a polyhedron given as a convex hull plus a
convex cone.  Finally 'portsort' is helpful  to  make datafiles
readable.  portsort sorts and formats given systems.

All functions read and write the data from  and  to  files.  Such files
can be manipulated by the user with a default texteditor.  PORTA
guarantees correct numerical results, because only  integer operations
are  performed. If an arithmetic overflow occurs with the systems
integer arithmetic  then  the  computations can be restarted with a double
precision integer arithmetic.
 
    Copyright (C) 1997-2009 Thomas Christof, Andreas Loebel
 
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.
 
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
 
    You should have received a copy of the GNU General Public License
    along with this program; if not, write to the Free Software
    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA



1. First run `make`
For valid points:
 ```./bin/valid -V ../examples/file.ieq ```

To get the facets:
 ```./bin/xporta -T ../examples/file.poi```

To calculate dimension:
 ```./bin/valid -D ../examples/file.ieq ../examples/file.poi```
 