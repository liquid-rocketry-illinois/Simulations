# NX 2306
#Exported files will match naming convention of the model with the .exp file appended
#Run by press Alt+F8 in the homescreen of NX and then selecting this .py file (may need to change extension dropdown from c to py)

#Name of nx file.
#MUST be located in "user"/documents/LRI CFD/NX/MODELS/
modelInputName = "fullrocket.prt"




import math
import NXOpen
import NXOpen.UF
import os
user_home = os.path.expanduser("~")
LRIPath = os.path.join(user_home, "Documents", "LRI CFD", "NX")
modelpath = os.path.join(LRIPath,"MODELS",modelInputName)
modelname = modelInputName[:-4]
#exp folder path:   (example: "C:/LRI/NX/EXP")
exppath = os.path.join(LRIPath, "EXPS")

#export file path:  (example: "C:/LRI/NX/EXPORTS")
exportpath = os.path.join(LRIPath, "EXPORTS")


def main() : 

    expfiles = os.listdir(exppath)
    # Filtering only the files.
    expfiles = [f for f in expfiles if os.path.isfile(exppath+'/'+f)]


    theSession  = NXOpen.Session.GetSession()
    markId1 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Load Part")
    theUfSession = NXOpen.UF.UFSession.GetUFSession()
    theUI = NXOpen.UI.GetUI()
    basePart1, partLoadStatus1 = theSession.Parts.OpenActiveDisplay(modelpath, NXOpen.DisplayPartOption.AllowAdditional)
    workPart = theSession.Parts.Work
    displayPart = theSession.Parts.Display
    partLoadStatus1.Dispose()
    theSession.ApplicationSwitchImmediate("UG_APP_MODELING")
    # ----------------------------------------------
    #   Menu: Tools->Utilities->Expressions...
    # ----------------------------------------------

    # For Loop:
    for i in range(len(expfiles)):
        markId2 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
        theSession.SetUndoMarkName(markId2, "Expressions Dialog")
        markId3 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Import Expressions")

        #exp files
        expModified1, errorMessages1 = workPart.Expressions.ImportFromFile(exppath+"/"+expfiles[i], NXOpen.ExpressionCollection.ImportMode.Replace)
        
        markId4 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
        theSession.DeleteUndoMark(markId4, None)
        markId5 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Expressions")
        markId6 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Make Up to Date")
        markId7 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "NX update")
        nErrs1 = theSession.UpdateManager.DoUpdate(markId7)
        theSession.DeleteUndoMark(markId7, "NX update")
        theSession.DeleteUndoMark(markId6, None)
        theSession.DeleteUndoMark(markId5, None)
        theSession.SetUndoMarkName(markId2, "Expressions")
        theSession.DeleteUndoMark(markId3, None)

        # ----------------------------------------------
        #   Menu: File->Export->Parasolid...
        # ----------------------------------------------

        markId8 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Visible, "Start")
        parasolidExporter1 = theSession.DexManager.CreateParasolidExporter()
        parasolidExporter1.ObjectTypes.Curves = True
        parasolidExporter1.ObjectTypes.Surfaces = True
        parasolidExporter1.ObjectTypes.Solids = True

        parasolidExporter1.InputFile = modelpath
        parasolidExporter1.OutputFile = exportpath+"/"+modelname+"_"+expfiles[i].replace('.exp','.x_t')

        parasolidExporter1.ParasolidVersion = NXOpen.ParasolidExporter.ParasolidVersionOption.Current
        theSession.SetUndoMarkName(markId8, "Export Parasolid Dialog")
        markId9 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Export Parasolid")
        theSession.DeleteUndoMark(markId9, None)
        markId10 = theSession.SetUndoMark(NXOpen.Session.MarkVisibility.Invisible, "Export Parasolid")

        parasolidExporter1.OutputFile = exportpath+"/"+expfiles[i][:-4]+"_"+modelname.replace('.exp','.x_t')

        nXObject1 = parasolidExporter1.Commit()
        theSession.DeleteUndoMark(markId10, None)
        theSession.SetUndoMarkName(markId8, "Export Parasolid")
        parasolidExporter1.Destroy()
        
    
if __name__ == '__main__':
    main()
    
