#-----------------------------------------------------------------
#            Author: Arnab Laha (github/alaha999)
#-----------------------------------------------------------------
# This script takes nanoAOD files as inputs, and clones the
# 'Event' tree in th eoutput, while filtering out some events.
# It creates a new branch 'nevtgen' to keep the original number
# of generated events, which is needed for lumi calculation.
#-----------------------------------------------------------------

# READ THE FOLLOWING BEFORE RUNNING LOCALLY.
# The inputs and outputs are managed by PSet.py
# crab_submit.sh can be run locally to see if everything is working.
# Make sure to uncomment/comment the appropriate functions at the end for running on Data/MC.
# In case of data, it requires a json file to filter out the bad events.
# The golden-jsons for different data-taking periods are available here -
# https://twiki.cern.ch/twiki/bin/view/CMS/LumiRecommendationsRun2

import ROOT
import sys
import PSet

ROOT.gROOT.SetBatch(True)


def process_input_files(psetfiles,redirector='root://cms-xrd-global.cern.ch//'):
    
    inputfiles = ROOT.std.vector("string")()

    for files in psetfiles:
        file_lfn = redirector+files
        inputfiles.push_back(str(file_lfn))
        print(f"processing >>>{file_lfn}")
        
    return inputfiles


def open_df(files):
    
    df = ROOT.RDataFrame("Events",files)
    
    return df

def processSkimTree(event_selection):
    
    ### inputfiles
    inputfiles = process_input_files(PSet.process.source.fileNames)

    ### create a dataframe
    df = open_df(inputfiles)
    nevt=df.Count().GetValue()
    df = df.Define("nevtgen",f"{nevt}")
    ### define any custom column
        
    
    ### apply event selection filter
    df = df.Filter(event_selection)

    
    ### output Skim Tree
    outputfilename= 'ntuple_skim.root'
    print ("OUTPUT FILENAME >>>",outputfilename)
    
    ### branches
    branchesToSave = df.GetColumnNames()
    
    df.Snapshot("Events",outputfilename,branchesToSave)


def lumi_filter(run, lumi):
    """Check if a given run and lumisection pass the golden JSON lumi mask."""
    str_run = str(run)
    if str_run in golden_json:
        for lumi_range in golden_json[str_run]:
            if lumi_range[0] <= lumi <= lumi_range[1]:
                return True
    return False


def processDataSkimTree(event_selection,jsonfile):
    
    ### inputfiles
    inputfiles = process_input_files(PSet.process.source.fileNames)

    ### create a dataframe
    df = open_df(inputfiles)
    nevt=df.Count().GetValue()
    df = df.Define("nevtgen",f"{nevt}")


    ### define any custom column
    import json
    with open(jsonfile) as json_file:
        golden_json = json.load(json_file)    

    #print(golden_json)
    ### Prepare a dictionary to pass to C++ (converting Python data to C++)
    golden_json_cpp = {}
    for run, lumi_ranges in golden_json.items():
        golden_json_cpp[int(run)] = lumi_ranges

    ### Pass the dictionary to ROOT (C++) via gInterpreter
    ROOT.gInterpreter.Declare(f"""
    #include <map>
    #include <vector>

    std::map<unsigned int, std::vector<std::pair<unsigned int, unsigned int>>> golden_json = {{
        {', '.join([f'{{{run}, {{{",".join([f"{{{lumi[0]}, {lumi[1]}}}" for lumi in lumi_ranges])}}}}}' for run, lumi_ranges in golden_json_cpp.items()])}
    }};

    bool lumi_filter_func(unsigned int run, unsigned int lumi) {{
        auto it = golden_json.find(run);
        if (it != golden_json.end()) {{
            for (const auto& lumi_range : it->second) {{
                if (lumi_range.first <= lumi && lumi_range.second >= lumi) {{
                    return true;
                }}
            }}
        }}
        return false;
    }}
    """)

        
    ### Filter events using the lumi mask
    df = df.Filter("lumi_filter_func(run, luminosityBlock)", "Golden JSON Lumi Mask")
    
    ### apply event selection filter
    df = df.Filter(event_selection)
    
    ### output Skim Tree
    outputfilename= 'ntuple_skim.root'
    print ("OUTPUT FILENAME >>> ",outputfilename)
    
    ### branches
    branchesToSave = df.GetColumnNames()
    
    df.Snapshot("Events",outputfilename,branchesToSave)
    
    
##----------------    

if __name__=="__main__":

    ### BE VERY CAREFUL HERE
    event_selection="(nMuon+nElectron)>0 && All(Muon_pt>10) && All(Electron_pt>10)"

    #---------------------------------------------------------------------------------------------------------------
    ### FOR MC
    processSkimTree(event_selection)

    #---------------------------------------------------------------------------------------------------------------
    ### FOR DATA

    #goldenjson={
    #    '2022':'Cert_Collisions2022_355100_362760_Golden.json',
    #    '2023':'Cert_Collisions2023_366442_370790_Golden.json'}
    
    #processDataSkimTree(event_selection,jsonfile=goldenjson['2022'])

    ### Note: This json file needs to be given as one of the input files to the crab setup.
    ### OR, you can keep all data events, and filter out the bad events later.
