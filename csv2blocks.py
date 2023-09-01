#Author-24 yamagishi
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
from . import SolidManager as So
from . import csvReader as Cr
from . import DialogueWindowHandler as Dw

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        fil = Dw.DialogueHandler.DialogueOpener()
        lst = Cr.csvReader.Reader(fil)
        ui.messageBox(format(fil))
        check = Cr.csvReader.FileFormatCertification(lst)
        if check == False:
            ui.messageBox('Wrong csv file!')
            exit()
        del lst[0]
        ##Initializationとしてまとめたい###################################################
        Original = Cr.csvReader.ReadOriginal(lst)
        for ii in range(len(Original)):
            Original[ii] = float(Original[ii])
        Newplane = So.planeTools.plane_builder(float(0))
        Opoint = [0,0,0]
        sent2Excrude = So.planeTools.Points2Rectangle(Opoint,Original,Newplane)
        So.BlockTools.ExtrudeInterface(sent2Excrude, Original[2],0)
        #################################################################################

        for ii in range(len(lst) -1):
            Newplane = So.planeTools.plane_builder(float(lst[ii +1][2] ))
            startPoint = [float(lst[ii +1][0]),float(lst[ii +1][1]),float(lst[ii +1][2])]
            partsize = []
            for jj in range(3):
                partsize.append(float(lst[ii +1][jj +3]))
            sent2Excrude =  So.planeTools.Points2Rectangle(startPoint,partsize,Newplane)
            So.BlockTools.ExtrudeInterface(sent2Excrude, partsize[2],1)
            So.BlockTools.ExtrudeInterface(sent2Excrude, partsize[2],0)



    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
