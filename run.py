#!/usr/bin/env python

"""
Author: Alex Freij (atfreij@ncsu.edu)

This script is to simplify gem5 with SPEC2006 benchmarks execution in the command line.
It compiles all information from a configuration JSON file and command line arguments to build the command.
"""

import os
import sys
import subprocess
import datetime
import argparse
import json
  
# command line argument parser
parser = argparse.ArgumentParser(description="Script to execute gem5 simulator with selected SPEC2006 benchmark.\n" \
					   "Benchmarks: perlbench, bzip2, gcc, bwaves, gamess, mcf, milc, zeusmp, "\
					   "gromacs, cactusADM, leslie3d, namd, gobmk, dealII, soplex, povray, "\
					   "calculix, hmmer, sjeng, GemsFDTD, libquantum, h264ref, tonto, lbm, "\
					   "omnetpp, astar, wrf, sphinx3, xalancbmk, specran_i, spendrand_f")
parser.add_argument('-b,', '--benchmark', dest="benchmark", default=None, help='Benchmark name')
parser.add_argument('-o,', '--output-dir', dest="output_dir", default=None, help='Name of output directory for results')
parser.add_argument('-c,', '--config', dest="config", default=None, help='Configuration JSON for simulator parameters')
args = parser.parse_args()

if args.benchmark is None or args.output_dir is None or args.config is None:
  parser.print_help()
  sys.exit(1)

# Load JSON config file
try:
  with open(args.config) as config:
    configs = json.load(config)
except IOError as e:
  print("IOError({0}): {1}".format(e.errno,e.strerror))
  print("Config file not found or not selected.")
  sys.exit()

# Retrieve working directories from config
gem5_dir = configs["directories"]["gem5_dir"]
spec_dir = configs["directories"]["benchmark_dir"]
sim_output = configs["directories"]["output_dir"]

# check directory paths
if os.path.exists(gem5_dir) == False:
  print('Cannot find specified gem5 directory. Fix path and try again.\n')
  print('Path used: ' + gem5_dir)
  sys.exit()
if os.path.exists(spec_dir) == False:
  print('Cannot find specified SPEC2006 directory. Fix path and try again.\n')
  print('Path used: ' + spec_dir)
  sys.exit()
if os.path.exists(sim_output) == False:
  print('Cannot find specified sim_output directory.')
  print('Creating new directory at ' + sim_output)
  os.mkdir(sim_output)

# checking parsed cmd args
if args.benchmark == 'none':
  print("No valid benchmark was entered. Exiting now.\n")
  parser.print_help()
  sys.exit()
else:
  try:
    cwd = os.getcwd()
  #  testcwd = os.chdir(args.benchmark)
  except OSError as e:
    print("Cannot find benchmark directory.")
    print("OSError({0}): {1}".format(e.errno, e.strerror))
    sys.exit(1)
  finally:
    os.chdir(cwd)

if args.output_dir == 'none':
  print("No valid output directory was set. Exiting now.\n")
  parser.print_help()
  sys.exit()

if args.config == 'none':
  print("No configuration JSON chosen. Exiting now.\n")
  parser.print_help()
  sys.exit()
else:
  if not os.path.isfile(args.config):
    print("Configuration JSON does not exist. Exiting now.\n")
    parser.print_help()
    sys.exit()

# check if valid benchmark passed in, output directory is just to specify which benchmark ran (with similar configs)
# check if >1 benchmark passed in, only allow 1 now
benchmark = ''
output = ''

# TODO: multicore system allows for different workloads per core, if multiple 
if len(args.benchmark.split(',')) > 1:
  print("Cannot execute more than 1 benchmark. Exiting.\n")
  sys.exit()

if args.benchmark == 'perlbench':
  benchmark = '400.perlbench'
  output = '400.perlbench'
elif args.benchmark == 'bzip2':
  benchmark = '401.bzip2'
  output = '401.bzip2'
elif args.benchmark == 'gcc':
  benchmark = '403.gcc'
  output = '403.gcc'
elif args.benchmark == 'bwaves':
  benchmark = '410.bwaves'
  output = '410.bwaves'
elif args.benchmark == 'gamess':
  benchmark = '416.gamess'
  output = '416.gamess'
elif args.benchmark == 'mcf':
  benchmark = '429.mcf'
  output = '429.mcf'
elif args.benchmark == 'milc':
  benchmark = '433.milc'
  output = '433.milc'
elif args.benchmark == 'zeusmp':
  benchmark = '434.zeusmp'
  output = '434.zeusmp'
elif args.benchmark == 'gromacs':
  benchmark = '435.gromacs'
  output = '435.gromacs'
elif args.benchmark == 'cactusADM':
  benchmark = '436.cactusADM'
  output = '436.cactusADM'
elif args.benchmark == 'leslie3d':
  benchmark = '437.leslie3d'
  output = '437.leslie3d'
elif args.benchmark == 'namd':
  benchmark = '444.namd'
  output = '444.namd'
elif args.benchmark == 'gobmk':
  benchmark = '445.gobmk'
  output = '445.gobmk'
elif args.benchmark == 'dealII':
  benchmark = '447.dealII'
  output = '447.dealII'
elif args.benchmark == 'soplex':
  benchmark = '450.soplex'
  output = '450.soplex'
elif args.benchmark == 'povray':
  benchmark = '453.povray'
  output = '453.povray'
elif args.benchmark == 'calculix':
  benchmark = '454.calculix'
  output = '454.calculix'
elif args.benchmark == 'hmmer':
  benchmark = '456.hmmer'
  output = '456.hmmer'
elif args.benchmark == 'sjeng':
  benchmark = '458.sjeng'
  output = '458.sjeng'
elif args.benchmark == 'GemsFDTD':
  benchmark = '459.GemsFDTD'
  output = '459.GemsFDTD'
elif args.benchmark == 'libquantum':
  benchmark = '462.libquantum'
  output = '462.libquantum'
elif args.benchmark == 'h264ref':
  benchmark = '464.h264ref'
  output = '464.h264ref'
elif args.benchmark == 'tonto':
  benchmark = '465.tonto'
  output = '465.tonto'
elif args.benchmark == 'lbm':
  benchmark = '470.lbm'
  output = '470.lbm'
elif args.benchmark == 'omnetpp':
  benchmark = '471.omnetpp'
  output = '471.omnetpp'
elif args.benchmark == 'astar':
  benchmark = '473.astar'
  output = '473.astar'
elif args.benchmark == 'wrf':
  benchmark = '481.wrf'
  output = '481.wrf'
elif args.benchmark == 'sphinx3':
  benchmark = '482.sphinx3'
  output = '482.sphinx3'
elif args.benchmark == 'xalanbmk':
  benchmark = '483.xalanbmk'
  output = '483.xalanbmk'
elif args.benchmark == 'specrand_i':
  benchmark = '998.specrand'
  output = '998.specrand'
elif args.benchmark == 'specrand_f':
  benchmark = '999.specrand'
  output = '999.specrand'


if not benchmark:
  print("Invalid benchmark. Exiting now.\n")
  sys.exit()
  
# load JSON config file and build out command 
# base command setup
config_str  = (gem5_dir + 'build/X86/gem5.' + configs["sim"]["version"])
if configs["sim"]["debug-flags"]:
  config_str += (' --debug-flags=' + configs["sim"]["debug-flags"])

config_str += (' --outdir=' + sim_output + args.output_dir + '/' + output)
config_str += (' ' + gem5_dir + configs["sim"]["config"])
config_str += (' --benchmark=' + args.benchmark)

# CPU args
config_str += (' -n ' + configs["cpu"]["count"])
config_str += (' --cpu-type=' + configs["cpu"]["type"])
config_str += (' --cpu-clock=' + configs["cpu"]["clock"])

#System args
config_str += (' --sys-clock=' + configs["sys"]["clock"])

# Memory args
config_str += (' --mem-type=' + configs["mem"]["mem_type"])
config_str += (' --mem-size=' + configs["mem"]["mem_size"])

# Cache args
config_str += (' --caches')
config_str += (' --l1i_size=' + configs["cache"]["l1i_size"])
config_str += (' --l1i_assoc=' + configs["cache"]["l1i_assoc"])
config_str += (' --l1d_size=' + configs["cache"]["l1d_size"])
config_str += (' --l1d_assoc=' + configs["cache"]["l1d_assoc"])
config_str += (' --l2cache')
config_str += (' --l2_size=' + configs["cache"]["l2_size"])
config_str += (' --l2_assoc=' + configs["cache"]["l2_assoc"])
config_str += (' --l3cache')
config_str += (' --l3_size=' + configs["cache"]["l3_size"])
config_str += (' --l3_assoc=' + configs["cache"]["l3_assoc"])

# Advanced args
config_str += (' --fast-forward=' + configs["sim"]["fast_forward"])
config_str += (' --maxinsts=' + configs["sim"]["max_insts"])

# changing to SPEC runtime dir, need to do this?
if os.path.exists(spec_dir + benchmark + '/run'):
  os.chdir(spec_dir + benchmark + '/run/run_base_ref_x86.0000')
else:
  print('run/ not found. This indicates that the benchmark was not built.\n'\
          'Build benchmark or create run/ and try again.')
  sys.exit()

print('Current working directory: ' + os.getcwd())
print('Gem5 cmd:')
print(config_str)
print('run.py complete. Passing control to gem5.')

try:
  subprocess.call(config_str, shell=True)
except OSError as e:
  print('Something went wrong: ')
  print("OSError ({0}): {1}".format(e.errno, e.strerror))
  sys.exit()
