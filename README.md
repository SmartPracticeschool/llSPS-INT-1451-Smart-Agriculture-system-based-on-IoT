# llSPS-INT-1451-Smart-Agriculture-system-based-on-IoT
### **Smart Agriculture System Based On IoT**

- Smart Agriculture System based on IoT can monitor soil moisture and climatic conditions to grow and yield a good crop.

- The farmer can also get the realtime weather forecasting data by using external platforms like Open Weather API.

- Farmer is provided with a mobile app using which he can monitor the temperature, humidity and soil moisture parameters along with weather forecasting details.

![smart-farming_800x500](https://user-images.githubusercontent.com/59228357/84514282-624fab80-ace8-11ea-8e56-2933e9f6dd59.jpg)


- Based on all the parameters he can water his crop by controlling the motors using the mobile application.

- Even if the farmer is not present near his crop he can water his crop by controlling the motors using the mobile application from anywhere.

- Here we are using the Online IoT simulator for getting the Temperature, Humidity and Soil Moisture values.

### **Simulator**

- The data of the farm like soil moisture, humidity and temperature are collected from sensors and then need to be sent to the cloud but here I am using a simulator in which we are going to connect it to the IBM cloud account and send data to the cloud.

- The simulator I used is here

![Watson IOT Sensor Simulator](https://user-images.githubusercontent.com/59228357/84513663-65966780-ace7-11ea-8221-6862f57fff25.png)

### **WebApp User Interface**

- Web App is created using NodeRed.

- There are two tabs in this Web App :

1.Home tab

- This tab contains measured and online weather forecast data displayed in gauges.

- I used OpenWeather to collect weather forecast data.

![sensor 1](https://user-images.githubusercontent.com/59228357/84514835-47ca0200-ace9-11ea-9ad0-3254c496030a.png)

2.Open Weather Map Info

- This Tab Displays the Current Weather Data

![sensor2](https://user-images.githubusercontent.com/59228357/84515005-83fd6280-ace9-11ea-9d40-668c8e2f9f7d.png)

### **Node-Red Program Flow**

 
- program flow of the web app created using NodeRed.

- Flow 1

![NodeRed Flow 1](https://user-images.githubusercontent.com/59228357/84515380-05ed8b80-acea-11ea-86be-f4e020f5502e.png)

- Flow 2

![NodeRed Flow 2](https://user-images.githubusercontent.com/59228357/84515417-11d94d80-acea-11ea-825d-ba9356079db6.png)

- Flow 3

![NodeRed Flow 3](https://user-images.githubusercontent.com/59228357/84515469-23225a00-acea-11ea-9f34-d8e04ebd1f45.png)

- ### **Virtual Farm Command Receiver on Python**

- Commands from the NodeRed are sent to the cloud and the following commands are received using Raspberry Pi or any other device with the following python code.

- Below image contains the python console showing the received commands

![python code output (2)](https://user-images.githubusercontent.com/59228357/84515814-975cfd80-acea-11ea-95ef-df4a3e1e6058.png)

For a detailed view of the project, read 
[Project Report.docx](https://github.com/SmartPracticeschool/llSPS-INT-1451-Smart-Agriculture-system-based-on-IoT/files/4771507/Project.Report.docx)




Project Demo Video Link:https://youtu.be/s1yjd9djOLk


Project Internship FeedBack Video Link:https://drive.google.com/file/d/1-uhAXC-gzZ0PeBs3we38EoWFn5M071e-/view?usp=sharing



Project Demo Video Using PPT Link:https://drive.google.com/file/d/1a7LRWGGq5FqD_0Rv8gOkfR-7q9pJm8Uy/view?usp=sharing



