#----------------------------------------------
# Submitting crab jobs in bulk.
#
# Note: Manage the parameters that are fed
# into crab_config.py according to your need.
#---------------------------------------------

import os,sys

samples=[
    ("Run2_2016postVFP_THQ",  "/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_THW",  "/THW_ctcvcp_5f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    ("Run2_2016postVFP_TTHH", "/TTHH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTTJ", "/TTTJ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTTT", "/TTTT_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTTW", "/TTTW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTWH", "/TTWH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTWW", "/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    ("Run2_2016postVFP_TTWZ", "/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    ("Run2_2016postVFP_TTZH", "/TTZH_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    ("Run2_2016postVFP_TTZZ", "/TTZZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    ("Run2_2016postVFP_tZq",  "/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
]

jobname ="nanoRDF"
    

for name, dataset in samples:
    requestname = jobname + '_' + name# + '_' + dataset.split('/')[1].split('_')[0]
    workarea = 'submitted' #Dumping all the crab_XXX directories here.

    # Setting the arguments:
    argument3 = 'General.requestName=' + requestname # Name of the sub-directory in the output area.
    argument4 = 'General.workArea='    + workarea    # Name of the crab_XXX folder, generated locally to monitoring.
    argument5 = 'Data.inputDataset='   + dataset     # Input DAS string

    # Main process line:
    processline = f'crab submit crab_config.py {argument3} {argument4} {argument5}'
    print('\nProcessing ...')
    print('\033[33m'+processline+'\033[0m')
    os.system(processline)
    #print('Done!\n')
    #break

    # Working Example:
    # crab submit crab_config.py General.requestName=nanoRDF_Run2_2017_UL_Rare_THQ General.workArea=submitted Data.inputDataset=/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM

print("\nDone!")
