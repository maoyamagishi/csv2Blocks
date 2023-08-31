import adsk.core, adsk.fusion, traceback

handlers = []
ui = None
app = adsk.core.Application.get()
if app:
    ui  = app.userInterface

product = app.activeProduct
design = adsk.fusion.Design.cast(product)
rootComp = design.rootComponent
planes = rootComp.constructionPlanes

class BaseTools:
    def createNewComponent(app):
    # Get the active design.
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)
        rootComp = design.rootComponent
        allOccs = rootComp.occurrences
        newOcc = allOccs.addNewComponent(adsk.core.Matrix3D.create())
        return newOcc.component



class plane_tools():

    def plane_builder(dist):     
        try:           #offset平面の生成（一枚分）
           distance = adsk.core.ValueInput.createByReal(dist)
           xyplane = rootComp.xYConstructionPlane
           planeInput = planes.createInput()
           planeInput.setByOffset(xyplane, distance)
           PlaneOne = planes.add(planeInput)
           return PlaneOne
        except:
            if ui:
               ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

    def Points2Rectangle(pointlist1,pointlist2,plane):
        basecomp = BaseTools.createNewComponent(app)
        sketches = basecomp.sketches
        sketch = sketches.add(plane)
        lines = sketch.sketchCurves.sketchLines
        sketchPoint1 = adsk.core.Point3D.create(pointlist1[0],pointlist1[1],pointlist1[2])
        sketchPoint2 = adsk.core.Point3D.create(pointlist2[0],pointlist2[1],pointlist2[2])
        rectangle = lines.addTwoPointRectangle(sketchPoint1,sketchPoint2)
        prof = sketch.profiles.item(0)
        return prof, basecomp
    
    def ExtrudeAndCut(item,dist):
        basecomp = plane_tools.createNewComponent(app)
        distance = adsk.core.ValueInput.createByReal(dist)
        extrudes = basecomp.features.extrudeFeatures
        operation = adsk.fusion.FeatureOperations.CutFeatureOperation
        extrudes.addSimple(item,distance,operation)

    def ExtrudeNew(sent,thickness):
        ui.messageBox(format(type(sent)))
        profile = sent[0]
        basecomp = sent[1]
        dist = adsk.core.ValueInput.createByReal(5)
        extrudes = basecomp.features.extrudeFeatures
        operation = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
        ext = extrudes.addSimple(profile,dist,operation)


#Help me... I can't made it by using Override.
#    def ExtrudeNew(self,prof,thickness):
#        newcomp = super(blockBuilder,self).createNewComponent(app)
#        dist = adsk.core.ValueInput.createByReal(thickness)
#        extrudes = newcomp.features.extrudeFeatures
#        operation = adsk.fusion.FeatureOperations.NewBodyFeatureOperation
#        ext = extrudes.addSimple(prof,dist,operation)
#        return None