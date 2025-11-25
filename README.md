# Single-Finger Gripper for Scooping Object

We present our spatula-type **Direct-Drive End-Effector** that rapidly inserts beneath an object and scoops it without ejection.
This project is inspired by and extends the work of [Direct-Drive-Gripper-with-Swivel-Fingertips](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips).

<img width="1000" height="615" alt="Image" src="https://github.com/user-attachments/assets/2f29c692-15a6-46a8-bbcc-e8a3e211f1c3" />　
<img width="1000" height="500" alt="Image" src="https://github.com/user-attachments/assets/690a4544-f94f-4f63-9928-05304e68aa5d" />
<img width="1000" height="380" alt="Image" src="https://github.com/user-attachments/assets/658a1eda-8ab0-41ec-b8e5-abd862391134" />

**Related repos**
* [**High-Speed Scooping (2024)**](https://github.com/JS-RML/Advanced-high-speed-scooping)
* [**Direct-Drive Gripper (2024)**](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips)
* [**High-Speed Scooping (2022)**](https://github.com/JS-RML/high_speed_scooping)
* [**Direct-Drive Gripper (2022)**](https://github.com/JS-RML/ddh_hardware)
  
# Table of Contents
- [Parts](#parts)  
  - [Bill of Materials (BOM)](#bill-of-materials-bom)  
      - [Off-the-Shelf Parts](#off-the-shelf-parts)  
      - [3D Printing](#3d-printing)
- [Motors](#motors)
  - [Wiring](#wiring)
    - [Encoder Connection](#encoder-connection)
    - [Motor Connection](#motor-connection)  
  - [Motor Calibration](#motor-calibration)
    - [Calibrate ODrives](#calibrate-odrive)
    - [Calibrate Zero Position](#calibrate-zero-position)
- [Gripper](#gripper)  
  - [Finger Assembly](#finger-assembly)  
  - [Gripper Assembly](#gripper-assembly)
- [Mounting](#mounting)  
  - [Customization](#customization)
- [Software](#software)
  - [Prerequisites](#prerequisites)
    - [Versions](#versions)
    - [Virtual Environment Settings](#virtual-environment-settings)
  - [Run Single-Finger Gripper for Scooping Object](#run-single-finger-gripper-for-scooping-object)
    - [Before running the code](#before-running-the-code)
    - [Let the robot Single-Finger Gripper for Scooping Object](#let-the-robot-single-finger-gripper-for-scooping-object)
    - [How to customize control parameters](#how-to-customize-control-parameters)
  - [Motor Manipulation](#motor-manipulation)  
- [Experiments](#experiments)  
  - [Experiment ① : Test Object (10 g)](#experiment---test-object-30-g)  
  - [Experiment ② : Test Object (30 g)](#experiment---test-object-50-g)  
  - [Experiment ③ : Carton Box (63 g)](#experiment---carton-box-63-g)
  - [Experiment ④ : iphone13 mini (155 g)](#experiment---carton-box-63-g)
- [Contributors](#contributors)
---
# Parts

## Bill of Materials (BOM)
### Off-the-Shelf Parts
- [T-Motor GB54-2](https://store.tmotor.com/goods-445-GB54-2.html) × 4  
- [ODrive S1](https://shop.odriverobotics.com/products/odrive-s1) × 4  
- [AS5048A magnetic encoder + solid magnet](https://ko.aliexpress.com/item/1005001686457940.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.16.79211d4aZISBpE&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=d12cc80d-7f2f-4472-b774-95bc286dbf2c&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:d12cc80d-7f2f-4472-b774-95bc286dbf2c,tpp_buckets:668%232846%238116%232002&pdp_ext_f=%7B%22order%22%3A%225%22%2C%22eval%22%3A%221%22%2C%22sceneId%22%3A%2230050%22%2C%22fromPage%22%3A%22recommend%22%7D&pdp_npi=6%40dis%21KRW%2125633%2117724%21%21%2117.86%2112.35%21%40213ba0c517586181047795086e8a83%2112000017134313267%21rec%21KR%21%21ABXZ%211%210%21n_tag%3A-29910%3Bd%3A7e1d6246%3Bm03_new_user%3A-29895%3BpisId%3A5000000182996635&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A%7Cx_object_id%3A1005001686457940%7C_p_origin_prod%3A#nav-review) × 4
- [Bearings — OD 100 mm / ID 6 mm](https://kr.misumi-ec.com/vona2/detail/221000058378/?KWSearch=%eb%b2%a0%ec%96%b4%eb%a7%81&searchFlow=results2products) × 3  
- [Wire terminal box](https://freeship.co.kr/goods/content.asp?guid=14063350&cate=&sitecate=mini) × 1  
- [Shielded cable](https://smartstore.naver.com/bantolmarket/products/10633794496) × 1  
- [3-phase cable](https://smartstore.naver.com/shipdiy/products/7890381050?) × 3

### 3D Printing
- **Gripper**
<img width="1000" height="500" alt="Image" src="https://github.com/user-attachments/assets/690a4544-f94f-4f63-9928-05304e68aa5d" />

  - [distal_link](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/distal_link.stl) × 2  
  - [distal_tip_cap](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/distal_tip.stl) × 1  
  - [distal_tip](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/distal_tip_cap.stl) × 1  
  - [finger_tip](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/finger_tip.stl) × 2  
  - [motor_shell](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/motor_shell.stl) × 1  
  - [motor_plate](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/motorplate.stl) × 2  
  - [proximal_link](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/proximal_link.stl) × 1
  - [proximal_link_cap](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/proximal_link_cap.stl) × 1
  - [proximal_link_pillar](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Gripper/proximal_link_pillar.stl) × 1

- **Mounting**
  - **Robotic Arm** : RB5-850
    - [adapter_plate](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Mounting/RB5/adapter_plate.stl) × 1
    - [coupler](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Mounting/RB5/coupler.stl)× 1
    - [coupling](https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object/blob/main/STL/Mounting/RB5/coupling.stl)× 1

  - **Drone** : DJI Matrice 400
    - to be added

# Motors
Please refer to [JS-RML, Direct-Drive Gripper with Swivel Fingertips/Motors](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main?tab=readme-ov-file#motors).
We need two motor subassemblies. Each one can be assembled as follows.

<img width="512" height="508" alt="Image" src="https://github.com/user-attachments/assets/48826f68-7391-4c78-9f94-8025019ff439" />
<img width="600" height="515" alt="Image" src="https://github.com/user-attachments/assets/92949678-feb1-4e81-b83c-a3e7a012e38f" />
<img width="512" height="528" alt="Image" src="https://github.com/user-attachments/assets/eb5de35e-2d01-4f72-b3d5-c253eea90626" />

## Wiring
The components should be connected following the diagram below. For power supply, the system supports an input range of DC 12-48V. In our setup, we supplied 24V. The encoder connection will be further elaborated. 
<img width="1744" height="973" alt="Image" src="https://github.com/user-attachments/assets/88c62bc8-fbec-463a-b960-22034f1697e2" />

### Encoder Connection
For the encoder connection, we fabricated a cable assembly as shown in the schematic below.

The wires were joined using heat-shrinkable tube (3.0 × 45 mm) instead of soldering.
After aligning the wires inside the tube, apply heat with a heat gun or lighter to shrink the tube and secure the connection.

And Finally, insert the connector into the Odrive S1 as shown in the figure below.
<img width="1837" height="1189" alt="Image" src="https://github.com/user-attachments/assets/dfc7c40a-b6ca-4473-9a47-8eb678853f31" />
<img width="1869" height="863" alt="Image" src="https://github.com/user-attachments/assets/650155c4-d2ad-46cc-8736-15eb1a2ce3d7" />

### Motor Connection
Keep the 3-phase connection consistent as shown below.
<img width="1641" height="831" alt="Image" src="https://github.com/user-attachments/assets/5a307f72-e21f-43be-b147-1bf35b271d80" />

## Motor Calibration
Each actuator module require calibration before use. This step can not be done after the gripper is assembled, so do not postpone this step.

We explicitly define the direction of the rotor to be the direction the hexagonal logo on the rotor is pointing at, and the zero position of the motor to be when the direction of the motor is pointing at the opposite direction of the power port on the stator.
<img width="1500" height="1200" alt="motor_frame" src="https://github.com/user-attachments/assets/932ef56f-18b9-42e8-9efb-6a105ce4e6b5" />




### Calibrate Odrive
ODrive provides a GUI service for setting up the motordriver. [Odrive GUI](https://gui.odriverobotics.com/inspector) In the configuration tab in this GUI, You can set up the motordriver's configuration. (this step need motor move freely so you don't set like Calibrate Zero Position diagram)
- **Power source**
  - DC bus overvoltage trip level: 26
  - DC bus undervoltage trip level: 22
  - DC max positive current: 'Leave it blank'
  - DC max negative current: -0.5

- **Motor**
  - Type: Gimbal
  - Phase resistance: 2.675
  - Pole pairs: 7
  - KV: 26
  - Current limit: 1
  - Motor calib current: 10
  - Motor calib voltage: 2
  - Lock-in spin current: 10

- **Encoder**
  - Type: SPI (AMS protocol)
  - nCS pin: GPIO 12

- **Control mode**
  - control mode: Position Control
  - Soft velocity limit: 10
  - Hard velocity limit: 13.75
  - Torque limit: 0.192

- **Interface**
  - UART (115200)



### Calibrate Zero Position
Here we calibrate the zero position of the motor. Mount the actuator on the calibration stand and install the calibration arm onto the actuator according to the diagram
<img width="1000" height="1200" alt="motor-calib-stand" src="https://github.com/user-attachments/assets/ed182651-2a10-4a5d-a702-55116d22c98d" />
Put the motor into zero position as show in the diagram below. Press down the calibration arm to make sure the stand and arm touch tightly.
<img width="1000" height="1200" alt="calib-zero" src="https://github.com/user-attachments/assets/3be51595-16b0-4aeb-8c0c-2c59aba9a498" />
when your motor is zero position you go to (ODrive0, ODrive1) in the 'inspector' tab of the [Odrive GUI](https://gui.odriverobotics.com/inspector) and set like picture below.(when you finish First step, Second step is you have to click save_configuration variable call button)
<img width="1200" height="677" alt="guirrreaaaal" src="https://github.com/user-attachments/assets/e2494c2e-048a-4bb4-ab56-a25cfc9466ab" />






# Gripper

## Finger Assembly  
<img width="1000" height="1189" alt="Image" src="https://github.com/user-attachments/assets/1a8166db-eabc-4d4d-bfb1-378a043d2473" />

## Gripper Assembly
<img width="800" height="1030" alt="Image" src="https://github.com/user-attachments/assets/8e4ec863-8d67-47b9-b2ad-74216baeeba6" />


# Mounting
Standard interface: **30 mm PCD**, **4 × M4**.  
<img width="771" height="1735" alt="Image" src="https://github.com/user-attachments/assets/631a1e19-9ad4-454e-9977-7efd8571f48a" />

## Customization
If the default mounting does not work for you, it's very easy to make a custom mount. The gripper has a 30 mm PCD with 4 ⨉ M4 mounting interface, as shown in the drawing below.

The gripper is designed to be compatible with **ISO 9409-1-50-4-M6 Flange** (applied Rainbow robotics RB5, Universal Robots UR10e, Universal Robots UR5, etc.). For other robot systems, it would be better to customize the adapter plate and coupling.

<img width="850" height="847" alt="Image" src="https://github.com/user-attachments/assets/ddd6ba45-ca68-44aa-a905-427b5f352a76" />

<img width="450" height="600" alt="Image" src="https://github.com/user-attachments/assets/ac228425-be4f-4dbd-9b15-36e9f07012d9" />

# Software
Implemented in **Python 3** on **Ubuntu**. For ODrive basics, see official docs.
## Prerequisites

### Versions
- Ubuntu: `22.04`  
- Python: `3.10.11`  
- ODrive control utility: `0.6.7`

Git clone our software.

```bash 
https://github.com/taehwaru/Single-Finger-Gripper-for-Scooping-Object.git
```

### Virtual Environment Settings
Please open Visual Studio Code terminal and copy and paste the code below to set your virtual environment.  

```bash 
sudo apt-get install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade odrive
```
if you finish Virtual Environment Settings part, Please refer to [JS-RML, Direct-Drive Gripper with Swivel Fingertips/Software/Getting started](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main?tab=readme-ov-file#getting-started) to get started.

## Run Single-Finger Gripper for Scooping Object
### Before running the code
Modify GRIPPER/Spatula.py as follows.

(1) Define the variables SN_M1, SN_M2 using the serial numbers of each odrive.
```bash 
SN_M1 = '383F34723539'
SN_M2 = '00E848E15413'
```
(2) Create odrive objects using those SN_M1, SN_M2.
```bash 
odrv0 = odrive.find_any(serial_number=SN_M1)
odrv1 = odrive.find_any(serial_number=SN_M2)
```
(3) Create Actuator objects using the odrive objects above. 
```bash 
MOTOR1 = Actuator(odrv0, 0, 1, 45) 
MOTOR2 = Actuator(odrv1, 0, 1, 45)
```
(4) Select controlSignal in GRIPPER/mainGripper.py. 
```bash 
controlSignal = 'Scoop'
#controlSignal = 'testFinger'
#controlSignal = 'testEdge'
#controlSignal = 'testGetTheta'
#controlSignal = 'testGetEdge'
#controlSignal = 'testGetFingerTip'
#controlSignal = 'testMotionStop'
```
### Let the robot Single-Finger Gripper for Scooping Object
Run main.py.
```bash 
python3 main.py
```
### How to customize control parameters
There are a set of control parameters that you can customize for different objects to scoop.
- **initialConfiguration**: Initial configuration
- **goalConfiguration**: Goal configuration
- **pgain**: Motor P-gains after collision.
- **softmax**: Motor current limit
- **torque_soft_max**: Motor positive torque limit(this variable not contain at code so if you want to fix it, you can use odrive gui) 
- **torque_soft_min**: Motor negative torque limit(this variable not contain at code so if you want to fix it, you can use odrive gui) 
- **sensi**: Motor angle Error range

for instance. In the code, the parameters are preset as follows, to scoop a iphone 13 mini (155g).
```bash
#Example code
x0=-40 ,y0=130
shoulder01, shoulder02 = ik_5bar_fingerTip(x0, y0)
initialConfiguration=[shoulder01,shoulder02]

x1=100,y1=10
shoulder11, shoulder12 = ik_5bar_fingerTip(x1, y1)
goalConfiguration=[shoulder11, shoulder12]

pgain=[15,15]
softmax=[4,4]
torque_soft_max=[0.8,0.8]
torque_soft_min=[-0.8,-0.8]
sensi=5
```
## Motor Manipulation
Our end-effector uses a **Coaxial 5-bar (Diamond) Linkage**. The system can be controlled in two modes — either based on the linkage edge point E(xₑ, yₑ) or the fingertip point T(xₜ, yₜ), depending on the desired level of precision. The controller accepts the endpoint position (either E or T) and outputs the two motor commands 𝜃₁ and 𝜃₂.

<img width="747" height="581" alt="Image" src="https://github.com/user-attachments/assets/e0bc0add-03d9-4288-acfd-0520875f1575" />
<img width="747" height="581" alt="Image" src="https://github.com/user-attachments/assets/95959932-0af7-49fd-b938-f4be5eea828d" />

### Example ① : input E
![Image](https://github.com/user-attachments/assets/f394a5d9-2902-4c3a-8db1-625cd441564b)

### Example ② : input T
![Image](https://github.com/user-attachments/assets/edb17581-2bad-49e1-a695-a0d018088105)

# Experiments

## Experiment ① : Test Object (30 g)
![Image](https://github.com/user-attachments/assets/8e143c2e-c073-407b-bec9-ceb2e2c65446)

## Experiment ② : Test Object (50 g)
![Image](https://github.com/user-attachments/assets/ee2b3c5d-b702-479b-9f97-769e5a075928)

## Experiment ③ : Carton Box (63 g)
![Image](https://github.com/user-attachments/assets/af97a3cc-2167-4f34-87b2-e2fcbdd92bf5)

## Experiment ④ : iphone13 mini (155 g)
![Image](https://github.com/user-attachments/assets/b9216237-a5b9-4b81-b98c-ca86de7b9b4e)

# Contributors
- **Ji-woong Choi**, chjwng@pusan.ac.kr
- **Yong-joo Ryu**, ryj01@pusan.ac.kr
- **Hyun-woo Sung**, zidlt@pusan.ac.kr
