import maya.cmds as cmds
import json

def GenerateCurve(selectedIn):
	curveName = selectedIn[1:]
	cv0 = cmds.getAttr(curveName + '.cv[0]')

	cmds.polyPlane( n='CurvePlane', sx=1, sy=1, w=1, h=1)
	cmds.move( cv0[0][0] - .5, cv0[0][1], cv0[0][2], 'CurvePlane', absolute=True )

	
	cmds.polyExtrudeEdge( 'CurvePlane.e[2]', kft=True, d=100, inc=curveName)
	# Edges are extruded then scaled together
	cmds.delete( 'CurvePlane.f[0]' )

	WriteCurveJSON('C:/Users/jacks/Documents/Ada_Assets/' + curveName + '.json')

	cmds.delete()

def WriteCurveJSON (address):
	data = {}

	data = []

	curvePointsX = []
	curvePointsY = []
	curvePointsZ = []

	for i in range(0, 100):
		pos = cmds.pointPosition( 'CurvePlane.vtx[' + str(i) + ']', w=True)

		curvePointsX.append(
			pos[0]
		)
		curvePointsY.append(
			pos[1]
			)
		curvePointsZ.append(
			pos[2]
		)
	data.append({
			'Name' : 'NurbCurve',
			'p_count' : 100,
			'p_x' : curvePointsX,
			'p_y' : curvePointsY,
			'p_z' : curvePointsZ
		})

	with open(address, 'w') as outfile:  
		json.dump(data, outfile)

selected = cmds.ls(sl=True,long=True) or []
for eachSel in selected:	
	GenerateCurve(eachSel)
