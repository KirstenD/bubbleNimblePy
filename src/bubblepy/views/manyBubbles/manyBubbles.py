
import nimble
from nimble import cmds
from pyglass.widgets.PyGlassWidget import PyGlassWidget
import random

def drawBubble( radius , xpoint , ypoint , zpoint , name,time ):
    """
    Arguments: radius is the size of the overall shape
    Return: None
    """

    y = (0, 1, 0)

    c = cmds.polySphere( r=radius , ax = y , cuv = 2 , ch = 1 , n = name )[0]
   # cmds.setAttr( "lambert1.transparency" ,0.470085 0.470085 0.470085,)
    rate = float(random.randrange(1,8))/16
    print rate

    i=1
    positive = True
    positivez = True
    if (xpoint < 0):
        positive = False
    if (zpoint <0):
        positivez = False
    radius_long = radius
    while ypoint <=19.9:
      # figure out best time step
        cmds.setKeyframe( name , t=i)
        radius_long = radius*(1+rate)
        cmds.scale( 1, 1, radius_long )
        cmds.move(xpoint , ypoint , zpoint , relative = False)
        cmds.select(name)


        response = nimble.createRemoteResponse(globals())
        response.put('name', name)

        if (xpoint -radius*2<-13):
            xpoint +=rate
            positive = True
        elif (xpoint + radius*2>13):
            xpoint -=rate
            positive = False
        else:

            if (positive == True):
                xpoint +=rate
            else:
                xpoint -=rate
        if (zpoint - radius_long*2<-13):
            zpoint +=rate
            positivez = True
        elif (zpoint +radius_long*2>13):
            zpoint -=rate
            positivez = False
        else:

            if (positivez == True):
                zpoint +=rate
            else:
                zpoint -=rate

        if ypoint >=19.9:
            ypoint = 20

            print ("pop")
            break
        else:
            ypoint = (rate+ float(ypoint) )

        i+=3
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
#___________________________________________________________________________________________________ ManyBubblesWidget
class ManyBubblesWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of ManyBubblesWidget."""
        super(ManyBubblesWidget, self).__init__(parent, **kwargs)
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)
        #self.NumBubbles.clicked.connect(self._handleReturnHome)
#===================================================================================================
#                                                                                 H A N D L E R S
    def _handleExampleButton(self):
        time =120
        d = cmds.polyCylinder( r=15, h=20, sx=40, sy=10, sz=1, ax=(0,0,0), rcp=0, cuv=2, ch=1, n='CylinderContainer')[0]
        cmds.move(0,10,0)
        cmds.select(d)
        response = nimble.createRemoteResponse(globals())
        response.put('name', d)
        num =self.NumBubbles.value()
        bubble = "bubble"
        for i in range(num):

            randomX = random.randrange(-10,10)
            randomY = random.randrange(0,2)
            randomZ = random.randrange(-10, 10)
            circleShape( randomX , randomY , randomZ ,bubble  , 1 , None, time )
            bubble = "bubble" + str(i)
#_________________________________________________________________________________________ _handleReturnHome


    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
