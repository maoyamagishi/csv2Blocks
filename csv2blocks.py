#Author-24 yamagishi
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
from . import SolidManager as So

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        Newplane = So.plane_tools.plane_builder(float(3))
        a = [0,0,0]
        b = [2,2,0]
        sent2Excrude = So.plane_tools.Points2Rectangle(a,b,Newplane)
        So.plane_tools.ExtrudeNew(sent2Excrude, 3.0)


    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
