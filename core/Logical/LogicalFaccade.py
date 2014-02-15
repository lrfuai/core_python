from Navigator.SerialNavigator import SerialNavigator;
from Navigator.NoNavigator import NoNavigator;

_navigator = None;



def getNavigator():
    global _navigator;
    if(_navigator is None ):
        _navigator = NoNavigator();
        #_navigator = SerialNavigator ( 5, 19200, 8);
    return _navigator;



