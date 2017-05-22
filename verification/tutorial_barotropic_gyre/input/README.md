python counterpart to ```MITgcm/verification/tutorial_barotropic_gyre/input/gendata.m```

This is a tool for the ```tutorial_barotropic_gyre``` example and a good style example
for how Python looks. Some style things to noe are

* use context managers to open the output files. This ensures that the file handles are always closed once we're finished with them

* use four space indentation to be consistent with accepted python styles

* import the numpy module before the function definition, again to be consistent with accepted python style

* pass the np.ones command a tuple for the array size, rather than a list.
