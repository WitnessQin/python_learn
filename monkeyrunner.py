import sys  
from com.android.monkeyrunner import MonkeyRunner as mr  
from com.android.monkeyrunner import MonkeyDevice as md  
from com.android.monkeyrunner import MonkeyImage as mi  
   
#connect device 连接设备  
#第一个参数为等待连接设备时间  
#第二个参数为具体连接的设备  
device = mr.waitForConnection(1.0,'80QBCPF2262H') 
device.press('KEYCODE_ENTER') 