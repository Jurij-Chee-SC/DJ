from abaqus import *
from abaqusConstants import *
from viewerModules import *
from driverUtils import executeOnCaeStartup
import os
file_name = 'JOB-55.odb'
syntaxpath = os.getcwd()	
#------------------
try:
	os.makedirs('result')
except:
	print 'This folder extisted already'

executeOnCaeStartup()
o2 = session.openOdb(name=file_name)
session.viewports['Viewport: 1'].setValues(displayedObject=o2)
leaf = dgo.LeafFromElementSets(elementSets=('PILE-1.SET-2', ))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Z-Plane'].setValues(
    showFreeBodyCut=True)
session.viewports['Viewport: 1'].odbDisplay.setValues(viewCutNames=('Z-Plane', 
    ), viewCut=ON)
session.viewports['Viewport: 1'].odbDisplay.viewCuts['Z-Plane'].setValues(
    position=16.44)
session.viewports['Viewport: 1'].odbDisplay.viewCutOptions.setValues(
    numCutFreeBody=64, cutFreeBodyMax=15, cutFreeBodyMin=4.44, csysName='(Global)')
odb = session.odbs[file_name]
lastframe = len(odb.steps['pull'].frames)-1
print lastframe
session.freeBodyReportOptions.setValues(reportFormat=COMMA_SEPARATED_VALUES)
for i in range (0,lastframe):
	session.writeFreeBodyReport(fileName='result/fm'+str(i)+'.csv', append=OFF, 
		step=1, frame=i, stepFrame=SPECIFY, odb=odb)

leaf = dgo.Leaf(leafType=DEFAULT_MODEL)
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
leaf = dgo.LeafFromModelNodeLabels(nodeLabels=(	
('SOIL-1', ('4', )),('SOIL-1', ('1292', )),('SOIL-1', ('1293', )),('SOIL-1', ('1294', )),\
('SOIL-1', ('1295', )),('SOIL-1', ('1296', )),('SOIL-1', ('1297', )),\
('SOIL-1', ('1298', )),('SOIL-1', ('1299', )),('SOIL-1', ('1300', )),('SOIL-1', ('1301', )),\
('SOIL-1', ('1302', )),('SOIL-1', ('1303', )),('SOIL-1', ('1304', )),('SOIL-1', ('1305', )),\
('SOIL-1', ('1306', )),('SOIL-1', ('1307', )),('SOIL-1', ('1308', )),('SOIL-1', ('1309', )),\
('SOIL-1', ('1310', )),('SOIL-1', ('1311', )),('SOIL-1', ('1312', )),\
('SOIL-1', ('1313', )),('SOIL-1', ('1314', )),('SOIL-1', ('1315', )),\
('SOIL-1', ('1316', )),('SOIL-1', ('1317', )),('SOIL-1', ('1318', )),\
('SOIL-1', ('1319', )),('SOIL-1', ('1320', )),('SOIL-1', ('1321', )),\
('SOIL-1', ('1322', )),('SOIL-1', ('51', ))
))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
odb = session.odbs[file_name]
session.fieldReportOptions.setValues(printTotal=OFF, printMinMax=OFF)
session.writeFieldReport(syntaxpath+'\\Result\\su.csv', append=OFF, 
		sortItem='Node Label', odb=odb, step=1, frame=lastframe, outputPosition=NODAL, 
		variable=(('COORD', NODAL, ( (COMPONENT, 'COOR3'), )), ('FV1', INTEGRATION_POINT), ))
with open ('result/su.csv', 'r') as yi:
	yi_ori = yi.readlines()
	yi_ori = yi_ori[26:]
with open ('result/su.csv', 'w') as g:
	g.writelines(yi_ori)
		
		
		
leaf = dgo.Leaf(leafType=DEFAULT_MODEL) 
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
leaf = dgo.LeafFromModelNodeLabels(nodeLabels=(			
('PILE-1', ('2', )),('PILE-1', ('5', )),('PILE-1', ('9', )),('PILE-1', ('28', )),\
('PILE-1', ('64', )),('PILE-1', ('65', )),('PILE-1', ('66', )),('PILE-1', ('67', )),\
 ('PILE-1', ('68', )),('PILE-1', ('69', )),('PILE-1', ('70', )),\
('PILE-1', ('71', )),('PILE-1', ('72', )),('PILE-1', ('73', )),('PILE-1', ('74', )),\
('PILE-1', ('75', )),('PILE-1', ('76', )),('PILE-1', ('77', )),('PILE-1', ('78', )),\
('PILE-1', ('79', )),('PILE-1', ('80', )),('PILE-1', ('81', )),('PILE-1', ('82', )),\
('PILE-1', ('83', )),('PILE-1', ('84', )),('PILE-1', ('85', )),('PILE-1', ('86', )),\
('PILE-1', ('87', )),('PILE-1', ('88', )),('PILE-1', ('89', )),('PILE-1', ('90', )),\
('PILE-1', ('91', )),('PILE-1', ('92', )),('PILE-1', ('93', )),('PILE-1', ('94', )),\
('PILE-1', ('95', )),('PILE-1', ('96', )),('PILE-1', ('97', )),('PILE-1', ('98', )),\
('PILE-1', ('99', )),('PILE-1', ('100', )),('PILE-1', ('101', )),('PILE-1', ('102', )),\
('PILE-1', ('103', )),('PILE-1', ('104', )),('PILE-1', ('105', )),('PILE-1', ('106', )),\
('PILE-1', ('107', )),('PILE-1', ('108', )),('PILE-1', ('109', )),('PILE-1', ('110', )),\
('PILE-1', ('111', )),('PILE-1', ('112', )),('PILE-1', ('113', )),('PILE-1', ('114', )),\
('PILE-1', ('115', )),('PILE-1', ('116', ))
))
session.viewports['Viewport: 1'].odbDisplay.displayGroup.replace(leaf=leaf)
odb = session.odbs[file_name]
session.fieldReportOptions.setValues(printTotal=OFF, printMinMax=OFF)

for i in range(0,lastframe):
	session.writeFieldReport(syntaxpath+'\\Result\\PILE'+str(i)+'.csv', append=OFF, 
			sortItem='Node Label', odb=odb, step=1, frame=i, outputPosition=NODAL, 
			variable=(('COORD', NODAL, ( (COMPONENT, 'COOR3'), )), ('U', NODAL, ((COMPONENT, 'U1'), ))))
	with open ('result/PILE'+str(i)+'.csv', 'r') as yi:
		yi_ori = yi.readlines()
		yi_ori = yi_ori[19:]
	with open ('result/PILE'+str(i)+'.csv', 'w') as g:
		g.writelines(yi_ori)
