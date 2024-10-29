# CRAB setup for skimming nanoAOD

I inherited this setup from [Arnab Laha](https://github.com/alaha999).

This repository contains a minimal setup for CRAB job submission. The python script which is processed is designed to read a nanoAOD file in RDataFrame, do some basic filtering of events (`nElectron+nMuon > 0` and each `lepton pT>10`) and keep the filtered events in a cloned tree. It also keeps track of the original number of generated events in a new branch for later use.

### How to run

1. Login to `lxplus8`.
2. Be in a CMSSW environment. In my case, its `CMSSW_13_0_13`, but the exact version is not crucial. This is just needed for using RDataFrame and submitting crab jobs.
3. Generate voms-proxy for CMS to access the files from DAS.
4. Run `crab_script.sh` locally to see if it can process the input file mentioned in `PSet.py`. This is running `nanoRDF.py` which is designed to skim the input file using `RDataFrame`. This may take a while to run in a local lxplus area.
5. Submit the crab job by running `crab_config.py`. This submits a crab-job for one dataset and manages how `crab_script.sh` should run remotely. In my case, I submit jobs in bulk and feed some config parameters externally. The following is an example of how to submit one job.
```
crab submit crab_config.py General.requestName=nanoRDF_Run2_2017_UL_Rare_THQ General.workArea=submitted Data.inputDataset=/THQ_ctcvcp_4f_Hincl_TuneCP5_13TeV_madgraph_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM
```

> **Note:** Parameters fed into `crab_config.py` from outside are `General.requestName`, `General.workArea` and `Data.inputDataset`. Rest of the parameters are same for all jobs and are defined inside `crab_config.py`.
