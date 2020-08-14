To install the packages I expect to use during this workshop with mini/Anaconda:

    conda install -c conda-forge biopython emcee numpy jupyter scipy matplotlib scikit-image scikit-learn mdtraj pyemma numba nglview

**Workshop 1:** Python list review, NumPy intro, basic plotting with matplotlib, nonlinear curve fitting with scipy, and Bayesian inference for nonlinear least squares, using pulse proteolysis data as an example. *several sessions*

**Workshop 2:** Retrieving and parsing data from the Protein Data Bank using biopython's PDB module. Preparing structures and generating input scripts for Rosetta's loopmodel application. *multiple sessions*

**Workshop 3:** Identifying colonies in petri dish images and quantifying changes in fluorescence with scikit-image using colonies expressing fluorescent, light-sensitive domains as an example, with parallel computing using multiprocessing. Another example of similar methods on single-molecule TIRF timeseries data?

**Workshop 4:** Working with sequence data and alignments using biopython. Phylogenies as well?

**Workshop 5:** Solving a system of coupled differential equations using scipy, as applied to the kinetic model from <https://doi.org/10.7554/eLife.53670>. An example of applying the Gillespie algorithm to the stochastic dynamics of the same model at low volumes/molecule numbers.

**Workshop 6:** Working with molecular dynamics trajectories using mdtraj.

**Bonus:** Short examples using numba, mdtraj, and Bio.SeqIO?

**Bonus Colab notebooks:** Notebooks created for Google Colab, including in-notebook package installation, to demonstrate quantum chemistry with Psi4, modeling with PyRosetta, Bayesian inference with CmdStanPy, ???
