"""
a=radius
    volumeS = 4.0*3.14*(a**3)/3.0
    volumeC = 3.14*(20.0**2)*5.0
    velocityY = 1.0
    height = 20
    ystart= float(1/6)
    print( ystart, "ystart")
playstuff
"""
import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget

import random

time = 0
def drawBubble( radius , xpoint , ypoint , zpoint , name,time ):
    """
    Arguments: radius is the size of the overall shape
    Return: None
    """

    y = (0, 1, 0)
    d = cmds.polyCylinder( r=10, h=20, sx=40, sy=10, sz=1, ax=(0,0,0), rcp=0, cuv=2, ch=1, n='CylinderContainer')[0]
    cmds.move(0,10,0)
    cmds.select(d)
    response = nimble.createRemoteResponse(globals())
    response.put('name', d)
    c = cmds.polySphere( r=radius , ax = y , cuv = 2 , ch = 1 , n = name )[0]

    xpoint = 0
    for i in range(1,time+1,3):  # figure out best time step
        cmds.setKeyframe( name , t=i)
        cmds.move(xpoint , ypoint , zpoint , relative = False)
        cmds.select(name)
        response = nimble.createRemoteResponse(globals())
        response.put('name', name)
        xpoint =xpoint +.1   # need to do some physics for theses
        print (ypoint, i)
        if ypoint >=19.5:
            ypoint = 20
            print ("pop")
            break
        else:
            ypoint = (.55+ float(ypoint) )
        zpoint = zpoint+.001
    #cmds.setKeyframe( name , at="translateY", t=time, v=xpoint + 3)
    return None


def circleShape( xpoint , ypoint , zpoint , name ,   radius = .1 ,deformer = None, time=0):
    """
      create a bubble
      Arguments: radius is the size of the overall shape
                 deformer is tells if bubble is deformed in anyway.
      Return:    None
    """

    if deformer == None:
        drawBubble( radius , xpoint , ypoint , zpoint , name,time )
    else:
        pass

    return None

#_________________________________________________________________________________ OneBubbleWidget
class OneBubbleWidget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of OneBubbleWidget."""
        super(OneBubbleWidget, self).__init__(parent, **kwargs)
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleExampleButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        time  = 120
        listBubbles = [ "bubble1" ]
        for i in listBubbles:

            randomX = random.randrange(-15,15)
            randomY = random.randrange(0,2)
            randomZ = random.randrange(-15, 15)
            circleShape( randomX , randomY , randomZ , i , 1 , None, time )



#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
