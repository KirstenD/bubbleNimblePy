# Assignment1Widget.py
# (C)2013
# Scott Ernst

import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import random
ime = 0
def drawBubble( radius , xpoint , ypoint , zpoint , name ):
    """
    Arguments: radius is the size of the overall shape
    Return: None
    """

    y = (0, 1, 0)
    c = cmds.polySphere( r=radius , ax = y , cuv = 2 , ch = 1 , n = name )[0]
    cmds.move(xpoint , ypoint , zpoint , relative = True)
    cmds.select(name)
    response = nimble.createRemoteResponse(globals())
    response.put('name', name)
    #cmds.setKeyframe( name , at="translateY", t=time, v=xpoint + 3)
    return None


def circleShape( xpoint , ypoint , zpoint , name ,   radius = .1 ,deformer = None):
    """
      create a bubble
      Arguments: radius is the size of the overall shape
                 deformer is tells if bubble is deformed in anyway.
      Return:    None
    """

    if deformer == None:
        drawBubble( radius , xpoint , ypoint , zpoint , name )
    else:
        pass

    return None
#___________________________________________________________________________________________________ OneBubbleWidget
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
        time = 0
        listBubbles = [ "bubble1" , "bubble2" , "bubble3" , "bubble4" , "bubble5" ]
        for i in listBubbles:
            for p in range(20):
                randomX = random.randrange(-20,21)
                randomY = random.randrange(0,2+p)
                randomZ = random.randrange(-20,21)
                circleShape( randomX , randomY , randomZ , i , 1 , None )
                cmds.setKeyframe( i , at="translateY", t=time, v=randomX + 3)
                time += 10
                
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
