import FWCore.ParameterSet.Config as cms

process = cms.Process("NANO")
process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(10))
process.source = cms.Source("PoolSource",fileNames=cms.untracked.vstring())

#The files mentioned here are run locally for debugging purposes.
process.source.fileNames = [
    #"/store/mc/RunIISummer20UL18NanoAODv9/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/2540000/10995124-9BEC-5A48-8D83-30542D27979D.root",
    #"/store/data/Run2022C/Muon/NANOAOD/16Dec2023-v1/2550000/019b0054-1684-410d-9fb2-837f92da4956.root"
    #'/store/mc/RunIISummer20UL17NanoAODv9/ZGToLLG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v1/130000/249DA2C1-115B-9546-B8C9-78D620B7ACA4.root'
    "/store/mc/RunIISummer20UL17NanoAODv9/WGToLNuG_01J_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/NANOAODSIM/106X_mc2017_realistic_v9-v1/270000/0AA28444-751E-824A-99FB-09E076775A92.root"
]
