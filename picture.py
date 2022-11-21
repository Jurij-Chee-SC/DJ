# -*- coding: mbcs -*-
#
# Abaqus/Viewer Release 6.14-1 replay file
# Internal Version: 2014_06_05-06.11.02 134264
# Run by Administrator on Mon Sep 26 17:52:51 2022
#

# from driverUtils import executeOnCaeGraphicsStartup
# executeOnCaeGraphicsStartup()
#: Executing "onCaeGraphicsStartup()" in the site directory ...
from abaqus import *
from abaqusConstants import *
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=189.133850097656, 
    height=126.424072265625)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
from viewerModules import *
from driverUtils import executeOnCaeStartup
executeOnCaeStartup()
o2 = session.openOdb(name='Job-55.odb')
#: Model: D:/xsj/dj/Job-55.odb
#: Number of Assemblies:         1
#: Number of Assembly instances: 0
#: Number of Part instances:     3
#: Number of Meshes:             4
#: Number of Element Sets:       9
#: Number of Node Sets:          15
#: Number of Steps:              2
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCut=ON)
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCut=OFF)
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Y-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(session.views['Front'])
session.viewports['Viewport: 1'].view.setProjection(projection=PARALLEL)
leaf = dgo.LeafFromElementSets(elementSets=('BEAM-1.SET-2', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromElementSets(elementSets=('PILE-1.SET-2', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromElementSets(elementSets=('PILE-1.SET-2', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.remove(leaf=leaf)
leaf = dgo.LeafFromOdbElementPick(elementPick=(('SOIL-1', 1676, (
    '[#0:5 #e0792480 #70381c0 #49240000 #92492492 #c0e07924 #70381', 
    ' #fc92400 #3e007c0 #49200000 #2 #0:37 #801f0000 #ffffc00f', 
    ' #ffffffff #1f #0:2 #fff80000 #ffffffff #3ff #0:36', 
    ' #1f0000 #2492 #0:9 #24000000 #49249249 #92492492 #24924924', 
    ' #49249249 #12492492 #0:10 #49249200 #92492492 #24924924 #49249249', 
    ' #92492492 #924 #0:271 #fc000000 #f800001f #f000003f #e000007f', 
    ' #c00000ff #800001ff #3ff #7ff #ffe #1ffc #3ff8', 
    ' #7ff0 #ffe0 #1ffc0 #3ff80 #7ff00 #ffe00 #49249000', 
    ' #fe492492 #3ff #3fffc00 #fc000000 #3ff #3fffc00 #fc000000', 
    ' #3ff #3fffc00 #fc000000 #3ff #3fffc00 #fc000000 #3ff', 
    ' #3fffc00 #fc000000 #3ff #3fffc00 #0:425 #92492490 #92424924', 
    ' #24924924 #49249249 #92492492 #24924924 #49249249 #92492492 #24924924', 
    ' #49249249 #92492492 #24924924 #49249249 #92492492 #24924924 #49249249', 
    ' #92492492 #24924924 #9 #0:32 #ffff0 #fff00000 #ffffffff:5', 
    ' #f #0:294 #ff000000 #ffffffff:6 #ffffff #0:55 #ff000000', 
    ' #ffffffff #3fffffff #0:17 #ffffc000 #ffffffff:6 #3fff #0:253', 
    ' #7f00000 #0 #3f80000 #0 #1fc0000 #0 #fe0000', 
    ' #0 #7f0000 #0 #3f8000 #0 #1fc000 #0', ' #fe000 #0 #7f000 #0 #3f800 ]', 
    )), ('ASSEMBLY', 1, ('[#1 ]', )), ), )
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    SYMBOLS_ON_UNDEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.5658, 
    farPlane=61.7323, width=45.6153, height=21.3855, cameraPosition=(-32.4066, 
    -14.28, 16.1044), cameraTarget=(15.1092, 4.92851, 8.71624))
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelOnCut=False)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelBelowCut=False)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelBelowCut=True)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelBelowCut=False)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelOnCut=True)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelAboveCut=False)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelAboveCut=True)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelOnCut=False)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelOnCut=True)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelBelowCut=True)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelAboveCut=False)
session.viewports['Viewport: 1'].view.setValues(nearPlane=35.1013, 
    farPlane=59.1968, width=18.0313, height=8.45351, cameraPosition=(-33.1227, 
    -11.3144, 19.2091), cameraTarget=(14.3931, 7.89413, 11.821))
session.viewports['Viewport: 1'].view.setValues(nearPlane=34.7457, 
    farPlane=61.0472, cameraPosition=(-33.3147, -6.20704, 25.942), 
    cameraUpVector=(0.350469, -0.248353, 0.903046), cameraTarget=(14.412, 
    7.39235, 11.1595))
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    position=4.98222)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    position=4.99778)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    position=4.94444)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    position=2.5)
leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(nearPlane=32.2835, 
    farPlane=63.5678, width=34.0481, height=15.9625, cameraPosition=(-34.0305, 
    -4.31183, 25.3746), cameraTarget=(13.6962, 9.28756, 10.5921))
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    position=5)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Y-Plane'].setValues(
    showModelBelowCut=False)
leaf = dgo.LeafFromPartInstance(partInstanceName=('SOIL-1', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].view.setValues(session.views['Bottom'])
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.7269, 
    farPlane=62.2534, width=40.9408, height=19.194, cameraPosition=(7.75681, 
    -48.4902, 8.68018), cameraTarget=(7.75681, 2.5, 8.68018))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    ORIENT_ON_DEF, ))
#: Warning: Material orientation information is not available in the current frame for any elements in the current display group.  Please make sure the primary variable is element-based AND orientations had been defined in the pertinent solid/shell sections.
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Pressure'), )
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    UNDEFORMED, CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, SYMBOLS_ON_UNDEF, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.165, 
    farPlane=61.8154, width=40.9408, height=19.194, cameraPosition=(7.78025, 
    -48.4902, 8.75679), cameraTarget=(7.78025, 2.5, 8.75679))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Tresca'), )
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='S', outputPosition=INTEGRATION_POINT, refinement=(INVARIANT, 
    'Pressure'), )
session.viewports['Viewport: 1'].view.setValues(nearPlane=45.3389, 
    farPlane=61.6415, width=34.2836, height=16.0729, cameraPosition=(8.05123, 
    -48.4902, 9.90872), cameraTarget=(8.05123, 2.5, 9.90872))
session.viewports['Viewport: 1'].odbDisplay.setPrimaryVariable(
    variableLabel='FV1', outputPosition=INTEGRATION_POINT, )
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.3369, 
    farPlane=62.6435, width=51.1365, height=23.9739, cameraPosition=(12.6519, 
    -48.4902, 6.68731), cameraTarget=(12.6519, 2.5, 6.68731))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    intervalType=USER_DEFINED, intervalValues=(6, 7, 8, 9, 10, 11, 12, 13, 14, 
    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, ))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    intervalType=USER_DEFINED, intervalValues=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, ))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    intervalType=USER_DEFINED, intervalValues=(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
    10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, ))
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.0356, 
    farPlane=62.9448, width=48.4624, height=22.7203, cameraPosition=(10.0592, 
    -48.4902, 8.71039), cameraTarget=(10.0592, 2.5, 8.71039))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, SYMBOLS_ON_DEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_DEF, SYMBOLS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.display.setValues(plotState=(
    CONTOURS_ON_UNDEF, SYMBOLS_ON_UNDEF, ))
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    vectorColorSpectrum='Black to white', vectorMaxValue=0.388536, 
    vectorMinValue=0)
session.viewports['Viewport: 1'].view.setValues(nearPlane=43.8473, 
    farPlane=63.1331, width=50.511, height=23.6807, cameraPosition=(11.6483, 
    -48.4902, 9.06312), cameraTarget=(11.6483, 2.5, 9.06312))
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    tensorIntervalNumber=11)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    tensorArrowheadStyle=FILLED)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=5)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=7)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    vectorColor='#FFC9C8')

session.viewports['Viewport: 1'].view.setValues(nearPlane=45.1244, 
    farPlane=61.856, width=36.6169, height=17.1668, cameraPosition=(12.3912, 
    -48.4902, 7.98184), cameraTarget=(12.3912, 2.5, 7.98184))
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=10)
session.viewports['Viewport: 1'].view.setValues(nearPlane=44.9096, 
    farPlane=62.0708, width=44.0857, height=20.6684, cameraPosition=(12.0672, 
    -48.4902, 7.84399), cameraTarget=(12.0672, 2.5, 7.84399))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Black to white', maxValue=20.79, minValue=0.33)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Blue to red')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Red to blue')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Wrap around')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='White to black')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Reversed rainbow')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Red to blue')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Black to white')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Rainbow')
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    outsideLimitsMode=SPECTRUM)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    outsideLimitsMode=SPECIFY)
session.Spectrum(name="Geo", colors =('#2B83BA', '#419AB2', '#56B1AB', 
    '#6CC4A5', '#82CDA5', '#98D6A4', '#AEDEA3', '#C1E69F', '#D5EE9C', 
    '#E7F599', '#EFF9A6', '#F7FCB2', '#FFFFBF', '#FFF5AE', '#FEEA9C', 
    '#FEE08B', '#FECF7D', '#FDBF6F', '#FDAF62', '#FA9957', '#F7844D', 
    '#F46E43', '#EB5D3B', '#E14D32', '#D73C28', ))
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Geo')
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=18)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=4)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    arrowSymbolSize=8)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    tensorIntervalNumber=7)
session.viewports['Viewport: 1'].odbDisplay.contourOptions.setValues(
    spectrum='Geo')
session.viewports['Viewport: 1'].odbDisplay.setSymbolVariable(
    variableLabel='U', outputPosition=NODAL, vectorQuantity=RESULTANT, )
session.viewports['Viewport: 1'].viewportAnnotationOptions.setValues(triad=OFF, 
    legend=OFF, title=OFF, state=OFF, annotations=OFF, compass=OFF)
session.graphicsOptions.setValues(backgroundStyle=SOLID, 
    backgroundColor='#FFFFFF', translucencyMode=2)
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    visibleEdges=NONE)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    vectorMaxValueAutoCompute=OFF, vectorMaxValue=0.6, 
    vectorMinValueAutoCompute=OFF, vectorMinValue=0.02, tensorMaxValue=41.7764, 
    tensorMinValue=-147.051)
session.viewports['Viewport: 1'].odbDisplay.symbolOptions.setValues(
    vectorColorSpectrum='Blue to red')
session.viewports['Viewport: 1'].odbDisplay.commonOptions.setValues(
    renderStyle=FILLED, )
session.epsOptions.setValues(resolution=DPI_600)
session.printToFile(fileName='123', format=EPS, canvasObjects=(
    session.viewports['Viewport: 1'], ))


