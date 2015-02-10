# bubblePyHomeWidget.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.widgets.PyGlassWidget import PyGlassWidget

from bubblepy.enum.UserConfigEnum import UserConfigEnum
from bubblepy.views.home.NimbleStatusElement import NimbleStatusElement

#___________________________________________________________________________________________________ bubblePyHomeWidget
class bubblePyHomeWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of bubblePyHomeWidget."""
        super(bubblePyHomeWidget, self).__init__(parent, **kwargs)
        self._firstView = True

        self.OneBubbleBtn.clicked.connect(self._handleOneBubble)
        self.ManyBubblesBtn.clicked.connect(self._handleManyBubbles)

        self._statusBox, statusLayout = self._createElementWidget(self, QtGui.QVBoxLayout, True)
        statusLayout.addStretch()

        self._nimbleStatus = NimbleStatusElement(
            self._statusBox,
            disabled=self.mainWindow.appConfig.get(UserConfigEnum.NIMBLE_TEST_STATUS, True) )
        statusLayout.addWidget(self._nimbleStatus)
#===================================================================================================
#                                                                               P R O T E C T E D

#___________________________________________________________________________________________________ _activateWidgetDisplayImpl
    def _activateWidgetDisplayImpl(self, **kwargs):
        if self._firstView:
            self._nimbleStatus.refresh()
            self._firstView = False

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleOneBubble
    def _handleOneBubble(self):
        self.mainWindow.setActiveWidget('oneBubble')

#___________________________________________________________________________________________________ _handlemanyBubbles
    def _handleManyBubbles(self):
        self.mainWindow.setActiveWidget('manyBubbles')
