# bubblePyCompiler.py
# (C)2013
# Scott Ernst

from pyglass.compile.PyGlassApplicationCompiler import PyGlassApplicationCompiler
from pyglass.compile.SiteLibraryEnum import SiteLibraryEnum

from bubblepy.bubblePyApplication import bubblePyApplication

#___________________________________________________________________________________________________ bubblePyCompiler
class bubblePyCompiler(PyGlassApplicationCompiler):
    """A class for..."""

#===================================================================================================
#                                                                                   G E T / S E T

#___________________________________________________________________________________________________ GS: siteLibraries
    @property
    def siteLibraries(self):
        return [SiteLibraryEnum.PYSIDE]

#___________________________________________________________________________________________________ GS: binPath
    @property
    def binPath(self):
        return ['..', '..', 'bin']

#___________________________________________________________________________________________________ GS: appFilename
    @property
    def appFilename(self):
        return 'bubblePy'

#___________________________________________________________________________________________________ GS: appDisplayName
    @property
    def appDisplayName(self):
        return 'bubblePy'

#___________________________________________________________________________________________________ GS: applicationClass
    @property
    def applicationClass(self):
        return bubblePyApplication

#___________________________________________________________________________________________________ GS: iconPath
    @property
    def iconPath(self):
        return ['apps', 'bubblePy']

####################################################################################################
####################################################################################################

if __name__ == '__main__':
    bubblePyCompiler().run()

