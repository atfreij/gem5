from __future__ import print_function
from __future__ import absolute_import

import m5
from m5.objects import *

binary_dir = '/path/to/spec2006/benchspec/CPU2006/'
out_dir = '/path/to/spec2006_output/'

#400.perlbench
def createPerl():
    perlbench = Process()
    perlbench.processName="perlbench"
    perlbench.executable = binary_dir + '400.perlbench/exe/perlbench_base.x86'
    #test input
    #data = binary_dir + '400.perlbench/data/test/input/attrs.pl'
    #ref input
    data = binary_dir + '400.perlbench/data/ref/input/checkspam.pl'
    perlbench.cmd = [perlbench.executable] + ['-I./lib', data, '2500', '5', '25', '11', '150', '1', '1', '1', '1' ]
    perlbench.output = out_dir + 'perlbench.out'
    perlbench.errout = out_dir + 'perlbench.err'
    return perlbench

#401.bzip2
def createBzip2():
    bzip2 = Process()
    bzip2.processName= "bzip2"
    bzip2.executable =  binary_dir +'401.bzip2/exe/bzip2_base.x86'
    # ref input
    data_dir = binary_dir + '401.bzip2/data/ref/input/'
    bzip2.cmd = [bzip2.executable] + [data_dir+'input.source', '280']
    #bzip2.cmd = [bzip2.executable] + [data_dir+'chicken.jpg', '30']
    #bzip2.cmd = [bzip2.executable] + [data_dir+'liberty.jpg', '30']
    #bzip2.cmd = [bzip2.executable] + [data_dir+'input.program', '280']
    #bzip2.cmd = [bzip2.executable] + [data_dir+'text.html', '280']
    #bzip2.cmd = [bzip2.executable] + [data_dir+'input.combined', '200']
    bzip2.output = out_dir + 'bzip2.out'
    return bzip2


#403.gcc
def createGcc():
    gcc = Process()
    gcc.processName= "gcc"
    gcc.executable = binary_dir + '403.gcc/exe/gcc_base.x86'
    #ref input
    data_dir = binary_dir + '403.gcc/data/ref/input/'
    gcc.cmd = [gcc.executable] + [data_dir + '166.in', '-o', '166.s']
    #gcc.cmd = [gcc.executable] + [data_dir + '200.in', '-o', '200.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'c-typeck.in', '-o', 'c-typeck.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'cp-decl.in', '-o', 'cp-decl.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'expr.in', '-o', 'expr.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'expr2.in', '-o', 'expr2.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'g23.in', '-o', 'g23.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 's04.in', '-o', 's04.s']
    #gcc.cmd = [gcc.executable] + [data_dir + 'scilab.in', '-o', 'scilab.s']
    gcc.output = out_dir + 'gcc.out'
    return gcc


#410.bwaves
def createBwaves():
    bwaves = Process()
    bwaves.processName="bwaves"
    bwaves.executable = binary_dir + '410.bwaves/exe/bwaves_base.x86'
    # ref input
    bwaves.cmd = [bwaves.executable]
    bwaves.input = binary_dir + '410.bwaves/data/ref/input/bwaves.in'
    bwaves.output = out_dir + 'bwaves.out'
    return bwaves

#416.gamess
def createGamess():
    gamess = Process()
    gamess.processName="gamess"
    gamess.executable = binary_dir +'416.gamess/exe/gamess_base.x86'
    #ref input
    data_dir = binary_dir + '416.gamess/data/ref/input/'
    gamess.cmd = [gamess.executable]
    #gamess.input = data_dir + 'cytosine.2.config'
    #gamess.output = out_dir + 'cytosine.2.out'
    #gamess.errout = out_dir + 'cytosine.2.err'

    gamess.input = data_dir + 'h2ocu2+.gradient.config'
    gamess.output = data_dir + 'h2ocu2+.gradient.out'
    gamess.errout = data_dir + 'h2ocu2+.gradient.err'

    #gamess.input = data_dir + 'triazolium.config'
    #gamess.output = out_dir + 'triazolium.out'
    #gamess.errout = out_dir + 'triazolium.err'
    return gamess

#429.mcf
def createMcf():
    mcf = Process()
    mcf.processName="mcf"
    mcf.executable =  binary_dir +'429.mcf/exe/mcf_base.x86'
    #ref input
    data_dir = binary_dir + '429.mcf/data/ref/input/'
    mcf.cmd = [mcf.executable] + [data_dir+'inp.in']
    mcf.output = out_dir + 'inp.out'
    mcf.errout = out_dir + 'inp.err'
    return mcf

#433.milc
def createMilc():
    milc = Process()
    milc.processName="milc"
    milc.executable = binary_dir +'433.milc/exe/milc_base.x86'
    # ref input
    data_dir = binary_dir + '433.milc/data/ref/input/'
    milc.cmd = [milc.executable]
    milc.input = data_dir + 'su3imp.in'
    #milc.output = out_dir + 'milc.out'
    return milc


#434.zeusmp
def createZeusmp():
    zeusmp = Process()
    zeusmp.processName="zeusmp"
    zeusmp.executable = binary_dir +'434.zeusmp/exe/zeusmp_base.x86'
    # ref input
    zeusmp.cmd = [zeusmp.executable]
    zeusmp.output = out_dir + 'zeusmp.stdout'
    zeusmp.errout = out_dir + 'zeusmp.err'
    return zeusmp



#435.gromacs
def createGromacs():
    gromacs = Process()
    gromacs.processName= "gromacs"
    gromacs.executable = binary_dir +'435.gromacs/exe/gromacs_base.x86'
    # ref input
    gromacs.cmd = [gromacs.executable] + ['-silent','-deffnm', 'gromacs', '-nice','0']
    gromacs.input = binary_dir + '435.gromacs/data/ref/input/gromacs.tpr'
    gromacs.output = out_dir + 'gromacs.ref.out'
    gromacs.errout = out_dir + 'gromacs.err'
    return gromacs

#436.cactusADM
def createCactus():
    cactusADM = Process()
    cactusADM.processName="cactusADM"
    cactusADM.executable = binary_dir +'436.cactusADM/exe/cactusADM_base.x86'
    # ref input
    cactusADM.cmd = [cactusADM.executable] + [binary_dir +'436.cactusADM/data/ref/input/benchADM.par']
    cactusADM.output = out_dir + 'benchADM.out'
    cactusADM.errout = out_dir + 'benchADM.err'
    return cactusADM


#437.leslie3d
def createLeslie3d():
    leslie3d = Process()
    leslie3d.processName="leslie3d"
    leslie3d.executable = binary_dir +'437.leslie3d/exe/leslie3d_base.x86'
    # ref input
    leslie3d.input = binary_dir + '437.leslie3d/data/ref/input/leslie3d.in'
    leslie3d.cmd = [leslie3d.executable]
    leslie3d.output = out_dir + 'leslie3d.stdout'
    leslie3d.errout = out_dir + 'leslie3d.err'
    return leslie3d

#444.namd
def createNamd():
    namd = Process()
    namd.processName="namd"
    namd.executable = binary_dir +'444.namd/exe/namd_base.x86'
    # ref input
    data = binary_dir + '444.namd/data/all/input/namd.input'
    namd.cmd = [namd.executable] + ['--input', data, '--iterations', '38',  '--output', 'namd.out']
    namd.output = out_dir + 'namd.stdout'
    namd.output = out_dir + 'namd.err'
    return namd

#445.gobmk
def createGobmk():
    gobmk = Process()
    gobmk.processName="gobmk"
    gobmk.executable = binary_dir +'445.gobmk/exe/gobmk_base.x86'
    # ref input
    data_dir = binary_dir + '445.gobmk/data/ref/input/'
    gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
    gobmk.input = data_dir + '13x13.tst'
    gobmk.output = out_dir + '13x13.err'
    #gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
    #gobmk.input = data_dir + 'nngs.tst'
    #gobmk.output = out_dir + 'nngs.err'
    #gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
    #gobmk.input = data_dir + 'score2.tst'
    #gobmk.output = out_dir + 'score2.err'
    #gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
    #gobmk.input = data_dir + 'trevorc.tst'
    #gobmk.output = out_dir + 'trevorc.err'
    #gobmk.cmd = [gobmk.executable] + ['--quiet','--mode', 'gtp']
    #gobmk.input = data_dir + 'trevord.tst'
    #gobmk.output = out_dir + 'trevord.err'
    return gobmk

#447.dealII
def createDealII():
    dealII = Process()
    dealII.processName="dealII"
    dealII.executable = binary_dir +'447.dealII/exe/dealII_base.x86'
    # ref input
    dealII.cmd = [dealII.executable]+['23']
    dealII.output = out_dir + 'log'
    dealII.errout = out_dir + 'dealII'
    return dealII

#450.soplex
def createSoplex():
    ##input file miss
    soplex = Process()
    soplex.processName="soplex"
    soplex.executable = binary_dir +'450.soplex/exe/soplex_base.x86'
    # ref input
    data_dir = binary_dir + '450.soplex/data/ref/input/'
    soplex.cmd = [soplex.executable] + ['-m45000', data_dir+'pds-50.mps']
    #soplex.cmd = [soplex.executable] + ['-m3500', data_dir+'ref.mps']
    #soplex.output = out_dir + 'soplex.out'
    return soplex

#453.povray
def createPovray():
    povray = Process()
    povray.processName="povray"
    povray.executable = binary_dir +'453.povray/exe/povray_base.x86'
    # ref input
    data = binary_dir + '453.povray/data/ref/input/SPEC-benchmark-ref.ini'
    povray.cmd = [povray.executable] + [data]
    povray.output = out_dir + 'SPEC-benchmark-ref.stdout'
    povray.errout = out_dir + 'SPEC-benchmark-ref.err'
    return povray


#454.calculix
def createCalculix():
    calculix = Process()
    calculix.processName="calculix"
    calculix.executable = binary_dir +'454.calculix/exe/calculix_base.x86'
    # ref input
    calculix.cmd = [calculix.executable] + ['-i', 'hyperviscoplastic']
    #calculix.input = binary_dir + '454.calculix/data/ref/input/hyperviscoplastic.inp'
    calculix.output = out_dir + 'hyperviscoplastic.log'
    calculix.errout = out_dir + 'hyperviscoplastic.err'
    return calculix

#456.hmmer
def createHmmer():
    hmmer = Process()
    hmmer.processName="hmmer"
    hmmer.executable = binary_dir +'456.hmmer/exe/hmmer_base.x86'
    # ref input
    data_dir = binary_dir + '456.hmmer/data/ref/input/'
    hmmer.cmd = [hmmer.executable] + [data_dir + 'nph3.hmm', data_dir+'swiss41']
    hmmer.output = out_dir + 'nhps.hmm'
    hmmer.errout = out_dir + 'nhps.err'
    #hmmer.cmd = [hmmer.executable] + ['--fixed', '0', '--mean', '500', '--num', '500000', '--sd', '350', '--seed', '0', data_dir +'retro.hmm']
    #hmmer.output = out_dir + 'retro.out'
    #hmmer.errout = out_dir + 'retro.out'
    return hmmer

#458.sjeng
def createSjeng():
    sjeng = Process()
    sjeng.processName="sjeng"
    sjeng.executable = binary_dir +'458.sjeng/exe/sjeng_base.x86'
    # ref input
    data = binary_dir + '458.sjeng/data/ref/input/ref.txt'
    sjeng.cmd = [sjeng.executable] + [data]
    sjeng.output = out_dir + 'ref.out'
    sjeng.errout = out_dir + 'ref.err'
    return sjeng

#459.GemsFDTD
def createGemsFDTD():
    GemsFDTD = Process()
    GemsFDTD.processName="GemsFDTD"
    GemsFDTD.executable = binary_dir +'459.GemsFDTD/exe/GemsFDTD_base.x86'
    # ref input
    GemsFDTD.cmd = [GemsFDTD.executable]
    GemsFDTD.output = out_dir + 'GemsFDTD.log'
    GemsFDTD.errout = out_dir + 'GemsFDTD.err'
    return GemsFDTD

#462.libquantum
def createLib():
    libquantum = Process()
    libquantum.processName="libquantum"
    libquantum.executable = binary_dir +'462.libquantum/exe/libquantum_base.x86'
    # ref input
    libquantum.cmd = [libquantum.executable] + ['1397','8']
    libquantum.output = out_dir + 'libquantum.out'
    libquantum.output = out_dir + 'libquantum.err'
    return libquantum

#464.h264ref
def createH264ref():
    h264ref = Process()
    h264ref.processName="h264ref"
    h264ref.executable = binary_dir +'464.h264ref/exe/h264ref_base.x86'
    # ref input
    data_dir = binary_dir + '464.h264ref/data/ref/input/'
    h264ref.cmd = [h264ref.executable] + ['-d', data_dir+'foreman_ref_encoder_baseline.cfg']
    h264ref.output = out_dir + 'foreman_ref_encoder_baseline_encodelog.out'
    h264ref.errout = out_dir + 'foreman_ref_baseline_encodelog.err'

    #h264ref.cmd = [h264ref.executable] + ['-d', data_dir+'foreman_ref_encoder_main.cfg']
    #h264ref.output = out_dir + 'foreman_ref_encoder_main_encodelog.out'
    #h264ref.errout = out_dir + 'foreman_ref_main_encodelog.err'

    #h264ref.cmd = [h264ref.executable] + ['-d', data_dir+'sss_encoder_main.cfg']
    #h264ref.output = out_dir + 'sss_encoder_main_encodelog.out'
    #h264ref.errout = out_dir + 'sss_encoder_main_encodelog.err'
    return h264ref


#465.tonto
def createTonto():
    tonto = Process()
    tonto.processName="tonto"
    tonto.executable = binary_dir +'465.tonto/exe/tonto_base.x86'
    # ref input
    tonto.cmd = [tonto.executable]
    tonto.output = out_dir + 'tonto.out'
    tonto.errout = out_dir + 'tonto.err'
    return tonto

#470.lbm
def createLbm():
    lbm = Process()
    lbm.processName="lbm"
    lbm.executable = binary_dir +'470.lbm/exe/lbm_base.x86'
    # ref input
    lbm.cmd = [lbm.executable] + ['300', 'reference.dat', '0', '0', binary_dir+'470.lbm/data/ref/input/100_100_130_ldc.of']
    lbm.output = out_dir + 'lbm.out'
    lbm.errout = out_dir + 'lbm.err'
    return lbm

#471.omnetpp
def createOmnetpp():
    omnetpp = Process()
    omnetpp.processName="omnetpp"
    omnetpp.executable = binary_dir +'471.omnetpp/exe/omnetpp_base.x86'
    # ref input
    data = binary_dir + '471.omnetpp/data/ref/input/omnetpp.ini'
    omnetpp.cmd = [omnetpp.executable] + [data]
    omnetpp.output = out_dir + 'omnetpp.log'
    omnetpp.errout = out_dir + 'omnetpp.err'
    return omnetpp

#473.astar
def createAstar():
    astar = Process()
    astar.processName="astar"
    astar.executable = binary_dir +'473.astar/exe/astar_base.x86'
    # ref input
    data_dir = binary_dir + '473.astar/data/ref/input/'
    astar.cmd = [astar.executable] + [data_dir + 'BigLakes2048.cfg']
    astar.output = out_dir + 'BigLakes2048.out'
    astar.errout = out_dir + 'BigLakes2048.err'
    #astar.cmd = [astar.executable] + [data_dir + 'rivers.cfg']
    #astar.output = out_dir + 'rivers.out'
    #astar.errout = out_dir + 'rivers.err'
    return astar

#481.wrf
def createWrf():
    wrf = Process()
    wrf.processName="wrf"
    wrf.executable = binary_dir +'481.wrf/exe/wrf_base.x86'
    # ref input
    wrf.cmd = [wrf.executable]
    wrf.output = out_dir + 'rsl.out.0000'
    wrf.errout = out_dir + 'wrf.err'
    return wrf

#482.sphinx3
def createSphinx3():
    sphinx3 = Process()
    sphinx3.processName="sphinx3"
    sphinx3.executable = binary_dir +'482.sphinx3/exe/sphinx_livepretend_base.x86'
    # ref input
    data = binary_dir + '482.sphinx3/data/ref/input/args.an4'
    sphinx3.cmd = [sphinx3.executable] + ['ctlfile', '.', data]
    sphinx3.output = out_dir + 'sphinx3.out'
    sphinx3.errout = out_dir + 'sphinx3.err'
    return sphinx3

#483.xalancbmk
def createXalancbmk():
    xalancbmk = Process()
    xalancbmk.processName="xalancbmk"
    xalancbmk.executable = binary_dir +'483.xalancbmk/exe/Xalan_base.x86'
    # ref input
    data_dir = binary_dir + '483.xalancbmk/data/ref/input/'
    xalancbmk.cmd = [xalancbmk.executable] + ['-v',data_dir+'t5.xml', data_dir+'xalanc.xsl']
    xalancbmk.output = out_dir + 'xalancbmk.out'
    xalancbmk.errout = out_dir + 'xalancbmk.err'
    return xalancbmk

#998.specrand
def createSpecrandI():
    specrand_i = Process()
    specrand_i.processName="specrand_i"
    specrand_i.executable = binary_dir +'998.specrand/exe/specrand_base.x86'
    # ref input
    specrand_i.cmd = [specrand_i.executable] + ['1255432124', '234923']
    specrand_i.output = out_dir + '998.specrand_234923.out'
    specrand_i.errout = out_dir + '998.specrand_234923.err'
    return specrand_i

#999.specrand
def createSpecrandF():
    specrand_f = Process()
    specrand_f.processName="specrand_f"
    specrand_f.executable = binary_dir +'999.specrand/exe/specrand_base.x86'
    # ref input
    specrand_f.cmd = [specrand_f.executable] + ['1255432124', '234923']
    specrand_f.output = out_dir + '998.specrand_234923.out'
    specrand_f.errout = out_dir + '998.specrand_234923.err'
    return specrand_f


def getProcess(pro_name):
    if pro_name == "perlbench":
        return createPerl()
    elif pro_name == "bzip2":
        return createBzip2()
    elif pro_name == "gcc":
        return createGcc()
    elif pro_name == "bwaves":
        return createBwaves()
    elif pro_name == "gamess":
        return createGamess()
    elif pro_name == "mcf":
        return createMcf()
    elif pro_name == "milc":
        return createMilc()
    elif pro_name == "zeusmp":
        return createZeusmp()
    elif pro_name == "gromacs":
        return createGromacs()
    elif pro_name == "cactusADM":
        return createCactus()
    elif pro_name == "leslie3d":
        return createLeslie3d()
    elif pro_name == "namd":
        return createNamd()
    elif pro_name == "gobmk":
        return createGobmk()
    elif pro_name == "dealII":
        return createDealII()
    elif pro_name == "soplex":
        return createSoplex()
    elif pro_name == "povray":
        return createPovray()
    elif pro_name == "calculix":
        return createCalculix()
    elif pro_name == "hmmer":
        return createHmmer()
    elif pro_name == "sjeng":
        return createSjeng()
    elif pro_name == "GemsFDTD":
        return createGemsFDTD()
    elif pro_name == "libquantum":
        return createLib()
    elif pro_name == "h264ref":
        return createH264ref()
    elif pro_name == "tonto":
        return createTonto()
    elif pro_name == "lbm":
        return createLbm()
    elif pro_name == "omnetpp":
        return createOmnetpp()
    elif pro_name == "astar":
        return createAstar()
    elif pro_name == "wrf":
        return createWrf()
    elif pro_name == "sphinx3":
        return createSphinx3()
    elif pro_name == "xalancbmk":
        return createXalancbmk()
    elif pro_name == "specrand_i":
        return createSpecrandI()
    elif pro_name == "specrand_f":
        return createSpecrandF()
    else:
        print(pro_name, end="")
        print("is not a valid process name")
        sys.exit(1)
