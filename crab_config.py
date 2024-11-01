#---------------------------------------------
# CRAB SUBMISSION SETUP:
#
# Working example:
# crab submit crab_config.py General.requestName=nanoRDF_Run2_2017_UL_Rare_THQ General.workArea=submitted Data.inputDataset=/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
#
#
# The following parameters fed from outside (bulksubmission)
# 1. General.requestName : This directory is created in the output area.
# 2. General.workArea : The crab-job logs are dumped in this folder, which is later used to monitor progress.
# 3. Data.inputDataset : Full DAS string of the input sample
# Rest of the parameters are same for all jobs, and are defined below.
#---------------------------------------------

from WMCore.Configuration import Configuration
from CRABClient.UserUtilities import config

config = config()

#-----------------------------------------------------------------------------
#datetime object
import datetime,sys
timestamp = datetime.datetime.now().strftime("_%Y%m%d_%H%M%S")
datasetStr  = sys.argv[4]
datasetName = sys.argv[5]
print(f"submitting crab jobs for {datasetName}>> {datasetStr} \n")
##----------------------------------------------------------------------------

### General:
config.General.transferOutputs = True
config.General.transferLogs = True

### JobType:
config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'PSet.py'
config.JobType.scriptExe = 'crab_script.sh'
config.JobType.inputFiles = ['nanoRDF.py','FrameworkJobReport.xml','jsonfiles/Cert_Collisions2022_355100_362760_Golden.json']
config.JobType.outputFiles = ['ntuple_skim.root']

### Data (input/output):
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1  # Number of files per job
config.Data.outLFNDirBase = '/store/user/phazarik/nanoRDFjobs' #Customize here according to your needs.
config.Data.publication = False
config.Data.outputDatasetTag = f'NanoRDF_2016postVFP_{timestamp}'

### Site:
config.Site.storageSite = 'T2_IN_TIFR' #Customize here according to your needs.
