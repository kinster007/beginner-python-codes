"""
Given a list of filenames, we want to rename all the files with extension hpp to the extension h. To do this, we would like to generate a new list called newfilenames, consisting of the new filenames.
"""
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
x = "hpp"
i = len(x)

for name in filenames:
    if name[-i:] == x:
        newname = name[:-i] + "h"
        newfilenames.append(newname)
    else:
        newfilenames.append(name)

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

"""
Using list Comprehension
"""

names = [names for names in filenames if "hpp" in names]

#continue in the same manner ahead