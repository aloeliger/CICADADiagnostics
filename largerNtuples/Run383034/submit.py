from CRABClient.UserUtilities import config
import os
import datetime

config = config()
config.General.requestName = 'CICADA_Commissioning_Run383034_16July2024'
config.General.workArea = 'crab'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'L1Ntuples_RAW2DIGI_L1.py'
config.JobType.maxMemoryMB = 4000
#config.JobType.inputFiles=['/afs/hep.wisc.edu/cms/aloeliger/anomalyTriggerWork/CMSSW_14_0_0_pre2/src/anomalyDetection/CICADA']

config.Data.inputDataset='/ZeroBias/Run2024F-v1/RAW'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.runRange = '383034'
config.Data.publication = False
config.Data.outputDatasetTag = 'CICADA_Commissioning_Run383034_16July2024'

config.Site.storageSite = 'T2_US_Wisconsin'
