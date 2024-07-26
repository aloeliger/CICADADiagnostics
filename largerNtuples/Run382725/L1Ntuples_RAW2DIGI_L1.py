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
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/001537ef-a421-4b1c-9665-e926706dd390.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/01218857-620b-4b7f-8ab7-431051a17527.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/02194218-0f8c-43fd-b97d-431cac44c781.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/023556cb-2642-4396-a0ad-f316a5e03fb1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/039feb9f-dc91-48c0-bcc4-022ec918e558.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/05e1739a-c4c1-436a-ac34-87b2042a7eb0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/0667d10b-4fa1-4ba8-9864-22668ea38fa5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/0699c64d-2f0f-4ee0-af9c-2c39313133b7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/086eb686-6d06-4289-8ea2-0191721908b1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/087cdc76-f547-4cb8-8241-8c46d7021176.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/0e3c2b84-dca0-4c98-b40f-d3dcb3105fef.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/0f9bda79-2aca-4394-b461-ec281f32c6c3.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/10142e41-f20d-40d1-9546-0ad7a99f0305.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1059c455-5ea6-4a0a-928c-ddd789673a3f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/15bd0527-1b55-4167-88da-c127cd515e4e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/15f8f32b-9eaa-4293-b566-c1d0c78088ec.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/17584f18-0b94-485d-8840-54d4db76a9e9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1a7cb438-3a8f-47b6-81a3-5e2940b635b4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1b81f425-d8f0-4f8f-80fa-12f7942ba208.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1c8fbabf-c56a-4c57-bbea-827c4b3653a1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1ca5be12-bbff-4a2d-923f-7f3850cb2a14.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1d2421f7-f725-4b47-a581-fd095bb524df.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/1dd0d605-789d-403d-a8f4-7463ab267038.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/21dbcd9b-e8d0-49bd-b41c-dee21dfe9e90.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/27691d2f-f26d-4f0f-872f-7ee4c9fbf65e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/298f0ec7-bc42-466a-95e0-a16a619d5ee6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2bca2974-184b-486f-9966-459454b6b68f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2cc8260a-0dd5-4c23-b9f9-6a82d3b636e1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2d9d18fe-15bc-4b1e-a192-156e71232fb6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2e838e68-f57d-40b3-ad5e-5cab70bafbd4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2edab1e9-9760-4a08-bde9-3e7b76b080f2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/2f708649-2fd1-4559-92e9-ebdd66862029.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/301caaf8-fba4-4394-b60b-3e42e98cadaa.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/305748bc-14af-4ed5-be9f-20e010566145.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/30beaaa0-f061-4991-84cb-7a00c28f3fe8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/325b2e54-596b-44fd-a6b7-f8fb2a949663.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3385d1f2-36d0-4870-aeac-75f7a9d6da8d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/36f1fbee-a9c8-414d-9996-3c368d4852ec.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/37033ec1-ee6b-427a-9df9-dac9b7610944.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/371ab874-20ed-4b5d-b743-d63eb3358fe6.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/38d29826-1c57-4886-a7c7-48e96efce92e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/39486060-cedc-4878-a786-0bc48a6e553c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3ae63922-2f44-4e12-ac85-c533f52d4b37.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3b164235-cc5d-4f9a-906a-43af5089319d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3cde746b-a675-4613-b720-9973eb201356.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3cf0def3-5106-40bf-9f3d-70c85e2d9de8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/3e1ebecf-291a-470f-aa64-c42f7407a274.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/41d463c2-a7b6-4e3a-8f15-39056d779989.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/441d0752-79dd-4777-983f-2623e783c95b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/494acefa-1f93-4ce8-b702-51aebd9fc752.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/49c25440-c0c4-45f1-aa6d-3fbc4cefdc62.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4a11b90a-d137-4c4d-bb1d-c1c230ccec2b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4bad0a85-9879-4906-8db3-d6e8bb8eaf98.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4c327462-6329-4744-a16d-271eb0ec4c9d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4cf86f3c-0c0b-4efc-99c5-c1c2dcfc166f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4d17bdf2-a57a-4ab0-a95c-f20daf4cb79f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4d26c20a-0a53-4559-ae6c-ac4b706a96e8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4d9e378c-bd6c-465f-9452-c94936674083.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/4ee88582-a104-4c53-beba-ae10f8b31c23.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/578c4f03-da43-4f76-91a9-35d7d6d8d83c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/57f090b4-b045-40c1-85d4-c9bfb4049a09.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/58bc4676-654a-4515-92d1-b5b0d6442e62.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/59b536d5-2142-4ad5-ac71-2db6f77c28b8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/59bb056f-8499-4086-b794-148203070300.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/5ab879e2-82d1-42bb-bf50-07b67d718c17.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/5c4560fb-ef2a-4729-bcab-7f7fc0b58f2d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/5df9f074-243e-4c7f-ba0d-a356034ecfab.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/609767b5-52ed-4b74-9dce-a8c7e65dcc2e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/626b165c-69c0-4218-b8a0-94585a628208.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6482465f-fccf-46b7-b8d9-74cec7851da9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/66f06011-3f04-4bb9-a0bc-59ab6bde2597.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6719dc06-2352-4d25-b426-9d9abf907ea9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/67be9f52-cb94-42f3-a23a-eebc0344423c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/68594965-fa52-4516-8b37-86c12b7f98fa.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6956cf06-17b8-411b-8c7a-df6d916b8cd1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/69b17e02-5871-46b8-ab61-ee8017e7fe3d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6a6ea757-728e-4bf7-b064-48be8d95c825.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6ac19fd3-04f1-4ea3-8a19-cce91f4c0269.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6d801b8a-2165-415f-85f4-2dbaebaf7bef.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/6ec31a05-e261-429a-9d59-f08d90ed31f0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/737ffe61-5191-4d35-977c-a2b5bbe945c4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/77b89d28-28ef-4678-b242-e3dae8a1742d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/7aa81d6e-dcf8-46c1-b779-bdcafd33fbb4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/7b9a8de0-8ab1-446d-85ff-d3137265fbb1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/7bf39f26-5d71-4062-a667-2226108bec43.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/7d994894-b015-4b2c-800b-7f728e48a1f5.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/7fad814c-9407-4bfa-b5a7-4c5afd8aaf60.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/80b00541-2105-4dd4-9972-b1df66ba77ab.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/80eae298-9c0e-4220-a8bd-78d09a249481.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/81dfcbde-f2c0-481e-87ef-15e41211e3ec.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/863379a4-bd13-46cf-b840-b4028747c7a2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/8839ec75-d9dc-4a0c-8afc-9e489459f1ec.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/8e9bbdc8-a355-4845-a923-c145da363d54.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/8ecf432e-8832-4ce1-a770-c1cee86ae0de.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/90da2f6a-8bff-4822-aa54-373df6f5ff6b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/918b2562-d61b-4e81-aace-01d70c4d6f10.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/92b967a6-5a0a-4180-99e0-b6eb2360b2f4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/930e53b9-590f-499b-bed5-b8af5971162a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/9896f661-d9b7-4780-b247-c43e5a8df99c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/99991019-ea72-4ead-88ad-31b6fdb1fe42.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/9a1ce4ce-7c1d-4bd6-a248-c2191ac9db8f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/9c8d81d9-ec1f-4ec3-a818-347501575704.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/9cfcb6d6-4497-4375-8ce0-50676d639614.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/9d69ea5b-9af3-44b0-a308-1fd32bb0257e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a0da919d-ef7b-4abe-8692-b5b5fda8fb49.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a0db2971-ca32-428c-a1b4-4986447f71b7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a2eaa507-8c47-43ba-914e-bbde5c27b451.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a5dc515f-ab1c-4e2b-9a29-33853441faba.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a883e666-40da-454b-a034-2dff5b69912e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a8c41289-8c27-460c-9d70-67d9be6d04de.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/a98610c2-ed72-4c47-9fe8-b7eed8facad7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/aa8fdb2a-193e-474b-aa31-28f1f8a51eec.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/aaf9cdd4-e68b-479d-94c4-c3b865642efb.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/abcb6bd2-b9a3-4674-9a82-e5fa8119b33b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ac24fa66-a47d-4b7c-911f-a784aea6851f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ae928d41-907d-4d2f-a3d8-91e14826aa2a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b0458ef0-a078-468b-a57b-f7683d64cb97.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b067dab3-799d-4442-9085-428472f3759d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b1175220-8268-4191-aa6c-48700231b9d9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b183b41f-817b-429b-996c-fb87f54e3a03.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b450e2e9-4b45-45f6-a9c8-68352973a9c4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b4883463-616f-4bcf-bea0-26a9253a07f9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/b78de906-a9da-404e-9a4d-9cf6fd33031a.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ba58aebb-509a-4b3a-9fed-c2953873f394.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/bb00b5ce-dcb3-472c-9d68-6d1a11017181.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/bde23107-8d32-4abe-bfbe-c88fbea27fe3.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/bdf8e658-27cf-45c9-b6ea-4f9c2f199741.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/bf80e503-4e1b-45fc-99f1-bd20ff09bbdd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c04af091-ce26-4a02-ad5b-a60ca0be7d99.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c1fee45d-8575-4598-914e-87f100248d0f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c28b7dd9-9834-45d0-a7fe-e6a1305cb27d.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c2a185b9-4e0e-409c-9b39-be64e54b416e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c45f528b-d990-4973-a2d0-57a189af6236.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c545a554-696e-475c-a1dc-8c8b5ad2fd20.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c54de8e5-d3a4-47a6-88d0-74e2eaf07815.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c73b0754-a064-4273-8a17-6ec65e231fcd.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/c89da10f-8f1b-478b-be8f-549759675356.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/caefad16-87dd-4311-93ab-03d427fc801e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/cb85345e-1263-4936-b98e-ffc1b4666f3b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/cd6828b0-a43b-472a-b5ce-94acd5bb6cbe.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/cdbca6ee-0844-45a2-952f-b64a103a7d26.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ce57e7c2-8040-4490-836e-9344091e1fea.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ce6eecb5-24ab-40fc-bc3c-adc8fc6ad2b8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/cfa1a3b9-b91a-4cfd-a113-0567287a27d0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d27708cf-94b8-4701-89a2-ec42b1f46bc0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d4a767ac-cce0-4406-8d8f-c40849acb717.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d6793201-26ef-44d9-8acc-632e3b27dfd4.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d6f4b741-8052-4c78-ab99-8373f0b68e73.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d8c6f965-4684-4203-ac2b-011dcf4c2b1b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/d933253e-4cea-41ed-a8ee-8e8a3e84cf0f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/dc11a4fe-04b7-4fe6-93a0-b3b5d62f530f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/dc4dc135-86f5-4d50-8aeb-5bac45d593a0.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/dff32c2c-8d17-4431-ae47-d566339adfe3.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e024f644-7468-4aa9-9c6c-4c6f21170e41.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e30f245e-da9d-44ba-b081-380660bb8c92.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e3851e4b-796d-43ae-acb4-e71f2be44a82.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e3d0dfde-8e7b-4790-a939-faea9ac83fe9.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e4447864-ae70-4779-b432-6ce2beb8a17e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e4ad1de4-bb6a-4ecd-9c2a-f5cc142bf360.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e4cac1fa-d0d9-46c3-af3f-8fab8aa55574.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e50235e2-074b-4e19-8650-d36405dfc4e8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e5ab57a9-ddb3-46f6-a720-639ece30e9e2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e66fe2b9-c34e-4052-9c76-3c60c9b6e768.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e80b58c6-8cdb-469b-bedc-8a3e68f48c7c.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/e909a03e-a8d5-47b0-adc3-384edec6d16f.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ea7bbe1f-f66f-4856-89b4-94bffec46c5b.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ec076523-4201-4495-9f58-6804b8b9d578.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ec72e4f9-e5c9-4dcf-85c9-1510104aaec2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/eeec315d-08b5-4d6a-98b3-f5b4018fe2cf.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/ef683f0d-b200-4970-b370-889f55351d69.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f0818f2c-ea0f-47f3-9bf6-078a87ced5a7.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f10cfd38-e33f-4ab0-a674-e03d56e8c719.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f25073f6-183a-4dd6-96f3-8d583dd81bdf.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f316ba1c-3547-4594-80bf-22fb0e944798.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f334d9b9-906e-44be-b2cf-c16258a301d2.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f3e27b91-5849-477d-b451-ae9f78442e53.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f5f328aa-52c9-479f-95c8-7a22ded58a20.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f727b183-5a07-4442-a7d9-c3a83561e589.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f89d29bf-28e1-4765-b94a-92dc7eb472c8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f974eb81-423e-419d-89be-a99fd2989f8e.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/f9d17afe-3cee-4bc4-9b7d-fe755feaf8c8.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/fb394ee5-cca1-4580-b643-be276cbc1ba1.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/fcf64f52-7814-4004-944f-7d8e17b33543.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/fde673cb-6980-4e13-a488-47139a1db039.root',
        '/store/data/Run2024F/ZeroBias/RAW/v1/000/382/725/00000/fe0ae3b7-5025-4c1a-8de1-e7292bbdcbd7.root',
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
