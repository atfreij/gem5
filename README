~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This repository to set a baseline version of gem5 that is used across our research group. This is a slightly modified version to enable the following features:

1. Per-core L2 cache and unified L3 cache (one core enabled, not a multi-core environment)
2. SPEC2006 benchmark simulation (some unused benchmarks intentionally left out)
3. Configuration file (config.json) to easily change simulation parameters
4. src/mem/DRAMCtrl.py:l328: added in metadata cache parameters, but not enabled in dram_ctrl.cc/.hh
5. src/mem/DRAMCtrl.py:l699: NVM-based timing parameters. To use default DRAM-based timing parameters, comment out l:699-708 

There is some initial setup required to run the simulator, specifically with benchmarks and directories within the configuration scripts.

1. To install SPEC CPU2006 and build benchmarks, read the instructions [here](https://www.spec.org/cpu2006/Docs/install-guide-unix.html). 
	1. **NOTE**: to run with gem5, the benchmarks need to be statically compiled. In your chosen `.cfg` file, search for `COPTIMIZE, CXXOPTIMIZE,` and `FOPTIMIZE` flags, and set each to `-O2 -static`.
2. configs/custom/spec2006.py:
	1. set `binary_dir` to the spec2006/benchspec/CPU2006/ subdirectory in your SPEC path
	2. set `out_dir` to desired SPEC2006 output directory. This is where output files from SPEC will be dumped. This directory **must** be created before running `run.py`.
3. config.json: 
	1. set `gem5_dir` to the working directory of your gem5 project
	2. set `benchmark_dir` to the `benchspec/CPU2006/` subdirectory of your `spec2006` folder
	3. set `output_dir` to your desired simulation results folder. If one doesn't exist, the `run.py` script will create it when run. This is where the results from the gem5 simulator will be dumped.

Once setup is complete, to build gem5:

`scons build/X86/gem5.opt -j9`
**NOTE**: gem5.debug can also be built this way by replacing `.opt` with `.debug`. `-jX` is dependent on the number of cores in the local system, it is recommended to use `num_cores + 1`.

Once built, to run gem5 with a specified benchmark:

`./run.py -b benchmark_name -o sim_results_dir -c config.json`
	
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the gem5 simulator.

The main website can be found at http://www.gem5.org

A good starting point is http://www.gem5.org/Introduction, and for
more information about building the simulator and getting started
please see http://www.gem5.org/Documentation and
http://www.gem5.org/Tutorials.

To build gem5, you will need the following software: g++ or clang,
Python (gem5 links in the Python interpreter), SCons, SWIG, zlib, m4,
and lastly protobuf if you want trace capture and playback
support. Please see http://www.gem5.org/Dependencies for more details
concerning the minimum versions of the aforementioned tools.

Once you have all dependencies resolved, type 'scons
build/<ARCH>/gem5.opt' where ARCH is one of ALPHA, ARM, NULL, MIPS,
POWER, SPARC, or X86. This will build an optimized version of the gem5
binary (gem5.opt) for the the specified architecture. See
http://www.gem5.org/Build_System for more details and options.

With the simulator built, have a look at
http://www.gem5.org/Running_gem5 for more information on how to use
gem5.

The basic source release includes these subdirectories:
   - configs: example simulation configuration scripts
   - ext: less-common external packages needed to build gem5
   - src: source code of the gem5 simulator
   - system: source for some optional system software for simulated systems
   - tests: regression tests
   - util: useful utility programs and files

To run full-system simulations, you will need compiled system firmware
(console and PALcode for Alpha), kernel binaries and one or more disk
images. Please see the gem5 download page for these items at
http://www.gem5.org/Download

If you have questions, please send mail to gem5-users@gem5.org

Enjoy using gem5 and please share your modifications and extensions.
