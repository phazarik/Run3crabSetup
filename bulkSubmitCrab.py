#----------------------------------------------
# Submitting crab jobs in bulk.
#
# Note: Manage the parameters that are fed
# into crab_config.py according to your need.
#---------------------------------------------

import os,sys

samples=[
    #('Run3Summer22EE_EraF_Muon'    ,"/Muon/Run2022F-22Sep2023-v2/NANOAOD"),
    #('Run3Summer22EE_EraG_Muon'    ,"/Muon/Run2022G-22Sep2023-v1/NANOAOD"),
    ("Run2_2017_UL_Rare", "/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/THW_ctcvcp_5f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    ("Run2_2017_UL_Rare", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    #("Run2_2017_UL_Rare", "/TZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM")
]


jobname ="nanoRDF"
    

for name, dataset in samples:
    requestname = jobname + '_' + name + '_' + dataset.split('/')[1].split('_')[0]
    workarea = 'submitted' #Dumping all the crab_XXX directories here.

    # Setting the arguments:
    argument3 = 'General.requestName=' + requestname # Name of the sub-directory in the output area.
    argument4 = 'General.workArea='    + workarea    # Name of the crab_XXX folder, generated locally to monitoring.
    argument5 = 'Data.inputDataset='   + dataset     # Input DAS string

    # Main process line:
    processline = f'crab submit crab_config.py {argument3} {argument4} {argument5}'
    print('\n' + processline)
    #os.system(processline)
    #print('Done!\n')
    #break

    # Working Example:
    # crab submit crab_config.py General.requestName=nanoRDF_Run2_2017_UL_Rare_THQ General.workArea=submitted Data.inputDataset=/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
