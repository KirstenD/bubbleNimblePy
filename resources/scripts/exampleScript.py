import math

import nimble
from nimble import cmds

#cmds.doSomethingHere
r = 50
a = 2.0*r
y = (0, 1, 0)
c = cmds.polyCylinder(
            r=r, h=5, sx=40, sy=1, sz=1, ax=y, rcp=0, cuv=2, ch=1, n='exampleCylinder')[0]
cmds.select(c)
response = nimble.createRemoteResponse(globals())
response.put('name', c)
