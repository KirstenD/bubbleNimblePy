# bubblePyMainWindow.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.windows.PyGlassWindow import PyGlassWindow

from bubblepy.views.home.bubblePyHomeWidget import bubblePyHomeWidget
from bubblepy.views.oneBubble.oneBubble import OneBubbleWidget
from bubblepy.views.manyBubbles.manyBubbles import ManyBubblesWidget

#___________________________________________________________________________________________________ bubblePyMainWindow
class bubblePyMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home':bubblePyHomeWidget,
                'oneBubble':OneBubbleWidget,
                'manyBubbles':ManyBubblesWidget },
            title='bubblePy',
            **kwargs )

        self.setMinimumSize(1024,480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        self.setActiveWidget('home')

