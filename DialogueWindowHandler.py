import adsk.core, adsk.fusion, adsk.cam, traceback
import os
app = adsk.core.Application.get()
ui = app.userInterface
if app:
    ui  = app.userInterface
commandDefinitions = ui.commandDefinitions

class DialogueHandler:
        
    def DialogueOpener():
        dlg = ui.createFileDialog()
        dlg.title = 'Open DAT File'
        dlg.filter = 'CSV files (*.csv);;All Files (*.*)'
        if dlg.showOpen() != adsk.core.DialogResults.DialogOK :
            return
        filename = dlg.filename
        return filename
        
