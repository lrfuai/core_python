from Logical import LogicalFaccade;
import time;

navigator = LogicalFaccade.getNavigator();


navigator.moveForward();
time.sleep(1);
navigator.moveBackward();
time.sleep(1);
navigator.turnLeft();
time.sleep(1);
navigator.turnRight ();
time.sleep(1);
print "DONE VIEJA!!!";
