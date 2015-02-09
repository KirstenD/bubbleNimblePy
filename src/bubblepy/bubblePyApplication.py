# bubblePyApplication.py
# (C)2013
# Scott Ernst

from pyglass.app.PyGlassApplication import PyGlassApplication

#___________________________________________________________________________________________________ bubblePyApplication
class bubblePyApplication(PyGlassApplication):

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: debugRootResourcePath
    @property
    def debugRootResourcePath(self):
        return ['..', '..', 'resources']

#___________________________________________________________________________________________________ GS: splashScreenUrl
    @property
    def splashScreenUrl(self):
        return 'splashscreen.png'

#___________________________________________________________________________________________________ GS: appID
    @property
    def appID(self):
        return 'bubblePy'

#___________________________________________________________________________________________________ GS: appGroupID
    @property
    def appGroupID(self):
        return 'bubblePy'

#___________________________________________________________________________________________________ GS: mainWindowClass
    @property
    def mainWindowClass(self):
        from bubblepy.bubblePyMainWindow import bubblePyMainWindow
        return bubblePyMainWindow

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    bubblePyApplication().run()
