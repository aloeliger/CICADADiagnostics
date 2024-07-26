# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: L1Ntuples -s RAW2DIGI,L1 --era=Run3 --data --conditions=auto:run3_data --customise=L1Trigger/Configuration/customiseReEmul.L1TReEmulFromRAW,L1Trigger/L1TNtuples/customiseL1Ntuple.L1NtupleRAWEMU -n -1 --filein=/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/001537ef-a421-4b1c-9665-e926706dd390.root --fileout=file:./test.root --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run3_cff import Run3

process = cms.Process('L1',Run3)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.RawToDigi_Data_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1),
    output = cms.optional.untracked.allowed(cms.int32,cms.PSet)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/002052dd-4eaf-4abc-92f1-9088369dfb5c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/028b816c-93da-41c7-a74b-67007a585c1c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/035760cc-e1f1-463c-bb31-134579eb9dfc.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/03933386-7407-469d-bc9e-07a223802825.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/03ec8406-c7c9-470f-b652-4c8c993fa967.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0465511f-b91a-42a0-ba81-97a4030f30d0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/053ac6f2-4a59-4a70-af05-5e246ff9d644.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0543120b-3ee8-448e-b9a7-b77e8a65afe7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/073bd4e8-3e30-4bc6-8d4d-89ccaa5d61bd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/07dd82c3-3786-47ec-9185-bdfd6bdb802e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/07f6e6bd-a173-4ed0-be87-e97ef67a4873.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0876dd4d-242f-477f-8be3-dc862cfcde43.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/08e6cb8e-4e09-4534-a869-613274731658.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0a59c7df-7612-4505-8b78-8571ce2e6b81.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0b7bad86-ef5a-46c3-8f44-97a8abcddf52.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0bb7a4e3-07a3-42da-82a7-30bc477376ca.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0bc4281c-2f95-4b7c-9911-a2cba1885331.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0c5ad151-074e-4f1c-9771-b3fca53ee750.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0c830464-2330-450f-9199-138c3a1e19ac.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0e4214dd-3d7c-4212-84ef-6bb87157eac0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/0e61d2b4-235c-48b4-b7c1-eb38ed44bea2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/102e39a9-dbf1-4dc9-957a-afc2cc543607.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/10490750-5358-4eb6-ba4a-27259d06f218.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/10b2ec94-e03e-4ddb-9bf1-d8ffc49bc4e6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/10cd6535-3cbd-4fef-b3e1-00b29d7cb8c6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/10fdd1aa-29de-4a4b-bdcc-ed35d2f2c3b2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/116b27b5-a5e3-4aca-98ee-41b222ab9916.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/11a20bfe-e15d-4294-9d1d-fdc5b3d07317.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/13702b0f-ffec-4811-899b-6486f650f2ce.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/13dfe7e1-15da-4f63-a734-9912ca3eea80.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/14510713-51c6-46d1-8e22-8e70f99091b5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/15094f0f-e9ef-4352-b784-38de7f49ac8e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1568e344-3273-42fd-9b69-a5a44dbe5f78.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/16cbee1e-38f7-40dc-b139-e90f17185aca.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1754013a-f977-45de-8894-10bb0e7f2e50.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/18473473-429f-4690-b665-98f1484c8545.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/184e8e80-036c-46ed-a8ad-4308b61ee139.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1b1ebfe0-a56a-4ba1-aa83-ae9ebc630471.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1c931827-c85d-4726-b609-23c04a0a3079.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1dbef4dd-39e3-468f-99f8-fd53be2ed7ac.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1f6c8651-d63c-40ed-bf44-d1c4a9d94f28.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1f846e27-7d88-4ce6-87b1-4c4c33d875f7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1fa5ca80-9374-40d1-bf96-3f5419b0bc34.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/1fa6f5ee-4282-40eb-aaca-5c79450b46bc.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2003091c-cb1b-477c-8f98-aa21ede8477d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/21e1f75c-358d-402b-a998-361c1c517248.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2360a1ab-6103-4b8a-a5ff-cf51947aa0ad.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/239710f3-1886-4a37-b64a-f19c553840c1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/23f2c003-8e0b-4e9b-9dd4-baf15630b9af.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2619c9f8-f1c4-4c8b-ac7d-8c68b9bf262e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/264251de-0490-44b8-b849-e792f6ba32da.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/26b216d0-7767-451a-b570-2722b7061a46.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/26bd6729-051c-45ef-b03a-68a083cd33d4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/27373687-c8c1-4e61-9be3-c9d41058042f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/275f1939-9e43-4346-9925-98c1fe590c25.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/28043f7d-4ca8-441c-bf97-e36992a88a3a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/280caa7f-c6c9-4d46-a74a-8544bc207384.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/28c278b0-2cb1-43f3-9f93-06fadacbc570.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/290a87be-149c-4d80-9aff-2b9b5624d383.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/294a194a-be98-4eb2-9d9e-3d76cf97fc73.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/29ce416d-6878-42c0-b795-4ac2e591dd8f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2c731c32-cf6b-4da6-b210-c0d0c10faa1a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2ca91884-66ab-4e6c-b65a-a44ab8efc49e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2d7d1e1e-6d86-4503-be19-402124e08a7f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2e4cadf3-9c01-43b0-9311-64306f9110c5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2e693cac-492d-44d7-a595-5418586b8a6b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/2fec9cc9-9922-440f-bc66-984e7ee701a2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/30b2d5ab-c48b-4428-9e61-4ea24e9ab5de.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/312caa8f-6636-4848-853a-d2a46a8ceb4a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/31a4251e-4f09-4bae-a73f-4bfe810bc05d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/31cd4e68-9ed6-466d-a8a9-f4c97160e00a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/31e6c8db-cea7-49d4-b947-adbf5e025639.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3224544d-f86f-4868-8226-960f361ee174.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3265969a-3838-4d28-82fd-e35800fc7b3a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3295443c-2b64-43c1-9a35-d7c04accd349.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/331358df-923c-4e74-b2a2-7bf3fb456729.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/34e28b57-7de5-4770-a039-2154edebc4b5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/35116b08-27ac-4825-a434-884047a94172.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/35b0446e-0fcc-47b3-b4bd-7afb0f917afc.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/35b7286f-9d82-4b6c-b8e4-915ee725daa0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/35c1ff2b-61f8-415d-9624-1c088d8b7478.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3627fe8a-4ff5-48db-969c-f76a03a82ff8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/36e22fe6-9020-4b81-8f1f-b5ded25a7d62.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/377cd1e9-8c19-43f4-b245-1793e0b2d41d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3a946134-ba1b-4570-ab2e-336344822718.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3b0d835d-cbef-4975-b153-a47e8fa3c79e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3c21858d-72e4-451c-b5f5-0d51414d1534.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3ce4868b-77be-4bec-aa2b-14d275e832d9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3da63f36-1b45-4201-8b4c-02eb0c9cc67d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/3f8bef70-41b6-4d57-8eb7-69ca8f106fa6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/40d4ad29-256c-4fbc-aa63-2bdf8575f21d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/40f392b6-e05c-4ba5-add3-6d5268409acb.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/410333e1-850f-439c-847d-6fcfe83c72e1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/42de0cef-8c37-4306-b576-c44121facfcd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/42fe4caa-c65b-4278-83ba-64b5bb3c7032.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/43be66d9-37d6-4454-b6a9-015c246d07cd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4422a064-c253-4c6f-999b-9a58db367bcd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/45316304-5a21-45c2-a43a-85056f8be5d9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/45934371-2948-4f1b-ad2e-066a8fa21ffd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/45f6bbe5-ff17-4c7f-b099-31c458b097de.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/467bb8dd-c7f3-4654-81d3-9149419a7b00.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/47d1ae11-5a50-4125-a050-ece2f2d67fba.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/490ac475-81bc-4254-9ecb-4efde31cf5d6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4945363a-d1c7-4b16-bc62-05aeec1e76c9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4b80c6ae-1b66-484c-b558-6f116f21fb99.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4bfdf96e-0216-4397-b102-5d2ba6bcc3b8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4c4f51e8-9cbf-4e5c-83ac-9d8f70dd4ede.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4c6d3844-8b3f-4637-8c92-5176c9732e05.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4eb2e51e-e4aa-4ccf-a162-4a383ff38434.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4ee0cb09-061b-46e2-940b-da49083cedf8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4f4aaa3c-e6e2-40c5-a730-3dcea2bab0f6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/4f99b202-8d5f-450e-946b-4a4a0dab06ea.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5042397a-7e70-44cf-9d8d-a33761a2f22f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/50ff962d-8576-41cc-83b8-84e0de91deed.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5216d7a5-7db8-48cd-98e8-5e3ca97a95f5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/52d61032-ab99-47cc-8642-0b29f2ecb332.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5384054e-8ebb-4e48-a871-b5db335f442d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/53ef31fa-1875-4fdb-be79-f17283635d35.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/54356409-c97e-483d-840b-13f82d1ab151.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/549dce9b-57fa-4384-b64d-060065c56eff.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/555ffaf3-543c-4dbe-840c-cf030b8b7a01.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/557b5259-4df6-4157-b0c6-b6bedd9ac4be.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/557c206b-dc31-415c-868e-8b8d03de0ee0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/559e1ba0-4c28-438e-aac8-e17400647297.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/55fb01d4-9dc5-4bc9-9a4f-1db2ef9d31a1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/560e306a-6de3-4b16-8c0d-61dcc434897e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/56485d39-633f-44d4-b16a-0587f3ec4039.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/565135db-ad17-4bdd-9580-6067e84b3ba2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/566645ab-27e0-4e51-953d-952598154663.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/57b0de0c-156d-4358-903e-1a0c0b8aff15.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5849d2ad-09bb-4abe-beb0-e843c23a02e7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/58a5aeaf-e935-4265-8491-a6221c58641d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5908e56e-2c9a-43c1-9d6d-1aa5377e86d0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/59a17882-bb86-4414-8d1c-26df310a6f63.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5aa4cc43-0229-48a3-ac0d-d4fa3e634cf7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5b6bf8da-9339-4d05-aeb5-1ded4e3781d5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5c033887-a457-47f3-af49-b127fcff7f03.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5e7d3681-6aab-4b58-9966-37b2477550c9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/5f168973-60a9-41b1-ac0d-c64b555ba22f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/60810290-6df4-4622-8765-bbf4f70eba49.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/623a93c0-f0f8-46a2-98b3-2c5bcc5a91fa.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/6317a7c9-075a-4ab1-ae94-3f8e71ea8570.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/6343be15-1e61-4479-bde6-7b69ab736a42.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/63485fdf-214c-4adf-b8a2-34c9f63ee5a8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/63f274e4-686f-4efe-9665-9956ffcbb5e0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/652268d6-1477-4e56-bd9f-32262b49075f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/654a2b5d-c205-4702-b3a7-7bbf6bbc8859.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/65d0f0e9-daf2-4710-9333-b7eef8ceb7a7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/665b8c00-4164-4996-9bdd-649624fb1ac1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/383/034/00000/66ab6a73-2aac-4425-a680-34c385e7f13d.root',
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.options = cms.untracked.PSet(
    IgnoreCompletely = cms.untracked.vstring(),
    Rethrow = cms.untracked.vstring(),
    TryToContinue = cms.untracked.vstring(),
    accelerators = cms.untracked.vstring('*'),
    allowUnscheduled = cms.obsolete.untracked.bool,
    canDeleteEarly = cms.untracked.vstring(),
    deleteNonConsumedUnscheduledModules = cms.untracked.bool(True),
    dumpOptions = cms.untracked.bool(False),
    emptyRunLumiMode = cms.obsolete.untracked.string,
    eventSetup = cms.untracked.PSet(
        forceNumberOfConcurrentIOVs = cms.untracked.PSet(
            allowAnyLabel_=cms.required.untracked.uint32
        ),
        numberOfConcurrentIOVs = cms.untracked.uint32(0)
    ),
    fileMode = cms.untracked.string('FULLMERGE'),
    forceEventSetupCacheClearOnNewRun = cms.untracked.bool(False),
    holdsReferencesToDeleteEarly = cms.untracked.VPSet(),
    makeTriggerResults = cms.obsolete.untracked.bool,
    modulesToCallForTryToContinue = cms.untracked.vstring(),
    modulesToIgnoreForDeleteEarly = cms.untracked.vstring(),
    numberOfConcurrentLuminosityBlocks = cms.untracked.uint32(0),
    numberOfConcurrentRuns = cms.untracked.uint32(1),
    numberOfStreams = cms.untracked.uint32(0),
    numberOfThreads = cms.untracked.uint32(1),
    printDependencies = cms.untracked.bool(False),
    sizeOfStackForThreadsInKB = cms.optional.untracked.uint32,
    throwIfIllegalParameter = cms.untracked.bool(True),
    wantSummary = cms.untracked.bool(False)
)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('L1Ntuples nevts:-1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('file:./test.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run3_data', '')

# Path and EndPath definitions
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.raw2digi_step,process.L1simulation_step,process.endjob_step,process.RECOSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from L1Trigger.Configuration.customiseReEmul
from L1Trigger.Configuration.customiseReEmul import L1TReEmulFromRAW 

#call to customisation function L1TReEmulFromRAW imported from L1Trigger.Configuration.customiseReEmul
process = L1TReEmulFromRAW(process)

# Automatic addition of the customisation function from L1Trigger.L1TNtuples.customiseL1Ntuple
from L1Trigger.L1TNtuples.customiseL1Ntuple import L1NtupleRAWEMU 

#call to customisation function L1NtupleRAWEMU imported from L1Trigger.L1TNtuples.customiseL1Ntuple
process = L1NtupleRAWEMU(process)

# End of customisation functions


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
