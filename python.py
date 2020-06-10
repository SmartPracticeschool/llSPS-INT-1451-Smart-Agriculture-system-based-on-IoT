import time
import sys
import ibmiotf.application # to install pip install ibmiotf
import ibmiotf.device

#Provide your IBM Watson Device Credentials
organization = "jv9gu9" #replace the ORG ID
deviceType = "IOTPROJECT"#replace the Device type wi
deviceId = "smart_agriculture"#replace Device ID
authMethod = "token"
authToken = "123456789" #Replace the authtoken

def myCommandCallback(cmd): # function for Callback
        print("Command received: %s" % cmd.data)
        if cmd.data['command']=='motoron':
                print("MOTOR ON IS RECEIVED")
                #time.sleep(1)
                #print("Motor Started")
        elif cmd.data['command']=='motoroff':
                print("MOTOR OFF IS RECEIVED")
                #time.sleep(1)
                #print("Motor Stopped")
        #elif cmd.data['command'] == 'runfor30minutes':
                #print("Motor Runs For 30 Minutes")
                #print("Motor Started")
                #for i in range(1,31):
                        #print("%d minutes to stop "%(30-i))
                        #print("Motor Stopped")
                
        if cmd.command == "setInterval":
                
                if 'interval' not in cmd.data:
                        print("Error - command is missing required information: 'interval'")
                else:
                        interval = cmd.data['interval']
        elif cmd.command == "print":
                if 'message' not in cmd.data:
                        print("Error - command is missing required information: 'message'")
                else:
                        output=cmd.data['message']
                        print(output)

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
              
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()