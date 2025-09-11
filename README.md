# Single-Finger Gripper for Scooping Object

We present our **Single-Finger Gripper for High-Speed Scooping**, a new robotic end-effector designed to scoop objects quickly.
This project is inspired by and extends the work of [Direct-Drive-Gripper-with-Swivel-Fingertips](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips).\
\
![Image](https://github.com/user-attachments/assets/ff8aee65-1ade-4aa5-98c2-da446d936d9f)
**Related repos**
* [**High-Speed Scooping (2024)**](https://github.com/JS-RML/Advanced-high-speed-scooping/tree/main)
* [**Direct-Drive Gripper (2024)**](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips)
* [**High-Speed Scooping (2022)**](https://github.com/JS-RML/high_speed_scooping)
* [**Direct-Drive Gripper (2022)**](https://github.com/JS-RML/ddh_hardware)
  
## Table of Contents
- [Parts](#parts)  
  - [Bill of Materials (BOM)](#bill-of-materials-bom)  
    - [Off-the-Shelf Parts](#off-the-shelf-parts)  
    - [3D Printing](#3d-printing)
- [Motors](#motors)  
  - [Motor Subassembly](#motor-subassembly)  
  - [Wiring](#wiring)  
    - [Power Supply](#power-supply)  
    - [Encoder Connection](#encoder-connection)  
    - [Motor Connection](#motor-connection)  
    - [ODrive S1 Pin Map](#odrive-s1-pin-map)
- [Motor Calibration](#motor-calibration)  
  - [Calibrate ODrives](#calibrate-odrives)  
  - [Calibrate Zero Position](#calibrate-zero-position)
- [Gripper](#gripper)  
  - [Finger Assembly ×2](#finger-assembly-2)  
  - [Gripper Assembly](#gripper-assembly)
- [Mounting](#mounting)  
  - [Customization](#customization)
- [Software](#software)  
  - [Versions](#versions)  
  - [Getting Started](#getting-started)
- [Experiments](#experiments)  
  - [Experiment ① : Object (10 g)](#experiment---object-10-g)  
  - [Experiment ② : Object (30 g)](#experiment---object-30-g)  
  - [Experiment ③ : Drone-Mounted Test (planned)](#experiment---drone-mounted-test-planned)
- [Five-Bar Linkage Code](#five-bar-linkage-code)  
- [Contributors](#contributors)
---
## Parts

### Bill of Materials (BOM)
### Off-the-Shelf Parts
- [T-Motor GB54-2](https://store.tmotor.com/goods-445-GB54-2.html) × 4  
- [ODrive S1](https://shop.odriverobotics.com/products/odrive-s1) × 4  
- [AS5048A magnetic encoder + solid magnet](https://ko.aliexpress.com/item/1005004239532357.html?spm=a2g0o.ppclist.product.16.189a33gr33grC1&pdp_npi=2%40dis%21KRW%21%E2%82%A9%2020%2C299%21%E2%82%A9%2020%2C299%21%21%21%21%21%402103011616813606980156478ed18f%2112000028490990365%21btf&_t=pvid%3A1729ba70-2e9e-4e62-ae44-2781def9d2bc&afTraceInfo=1005004239532357__pc__pcBridgePPC__xxxxxx__1681360698&gatewayAdapt=glo2kor) × 4  
- [Bearings — OD 100 mm / ID 6 mm](https://kr.misumi-ec.com/vona2/detail/221000058378/?KWSearch=%eb%b2%a0%ec%96%b4%eb%a7%81&searchFlow=results2products) × 12  
- [Wire terminal box](https://freeship.co.kr/goods/content.asp?guid=14063350&cate=&sitecate=mini) × 1  
- [Shielded cable](https://smartstore.naver.com/bantolmarket/products/10633794496) × 1  
- [3-phase cable](https://smartstore.naver.com/shipdiy/products/7890381050?) × 3

### 3D Printing
- **Gripper**
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

## Motors
Overall motor-related parts are assembled as follows:

![Motor Overview](docs/motor_overview.png)

### Motor Subassembly
Build **four** identical actuator modules:
```
[motor_with_magnet] + [motor_plate] → [actuator_module]
```
![Motor Plate](docs/motor_plate.png)  
![Actuator Module](docs/actuator_module.png)

---

## Wiring
Follow the system diagram. **Black = encoder**, **Green = power**.

![Wiring](docs/wiring.png)

### Power Supply
1) Connect the DC power supply to the outlet.  
2) Distribute **positive ↔ positive**, **negative ↔ negative** to all four ODrives.  
3) Boards have **no power switch**: plug = on, unplug = off.  
![Power Supply](docs/power_supply.png)

### Encoder Connection
Fabricate the encoder cable per schematic; verify **continuity**/**resistance** and **label** connectors.  
![Encoder Wiring](docs/encoder_wiring.png)  
![Encoder → ODrive](docs/encoder_odrive.png)

### Motor Connection
Keep **3-phase** order consistent across modules.  
![Motor ↔ ODrive](docs/motor_odrive.png)

### ODrive S1 Pin Map
![ODrive Power](docs/odrive_power.png)  
![ODrive Pin Map](docs/odrive_pinmap.png)

---

## Motor Calibration
Calibrate **each** actuator **before** assembling the full gripper.

**Rotor direction**: direction of the hex-logo on the rotor.  
**Zero position**: that direction pointing **opposite** to the stator power port.  
![Motor Zero](docs/motor_zero.png)

### Calibrate ODrives
Use **ODrive GUI** to configure your drivers (power, motor, encoder, control-mode, interface).  
> Follow your hardware’s safe limits; values in our experiments may differ.

### Calibrate Zero Position
Mount the actuator on the **calibration stand** and install the **calibration arm** as shown. Press down for solid contact.  
![Calibration Stand](docs/calibration_stand.png)  
![Zero Stop](docs/zero_stop.png)

In **Inspector**, read each ODrive’s `pos_estimate` and **record** it—used later as a **motor offset** when creating the `Actuator`.

![Motor Offset in GUI](docs/motor_offset_gui.png)

---

## Gripper

### Finger Assembly ×2
Insert bearings at the **red-circled** locations.  
![Finger](docs/finger.png)

### Gripper Assembly
![Gripper Shell](docs/gripper_shell.png)  
![Gripper](docs/gripper.png)

---

## Mounting
Standard interface: **60 mm PCD**, **4 × M4**.  
![Base Mount](docs/base_mount.png)  
![Mounted](docs/gripper_mounted.png)

### Customization
Default mounting targets **Rainbow Robotics RB5**. For other robots, customize the **adapter plate** and **coupling** (drawings in `docs/base_mount.dxf`).

---

## Software
Implemented in **Python 3** on **Ubuntu**. For ODrive basics, see official docs.

### Versions
- Ubuntu: `20.04`  
- Python: `3.10.11`  
- ODrive control utility: `0.6.7`

### Getting Started

**Clone & install**
```bash
git clone https://github.com/username/Single-Finger-Gripper-for-Scooping-Object.git
cd Single-Finger-Gripper-for-Scooping-Object
pip install -r requirements.txt
```

**Install ODrive tool**
```bash
pip install --upgrade odrive
```

**Set USB permissions**
```bash
sudo bash -c "curl https://cdn.odriverobotics.com/files/odrive-udev-rules.rules > /etc/udev/rules.d/91-odrive.rules && udevadm control --reload-rules && udevadm trigger"
```

**Launch & check bus voltage**
```bash
odrivetool
# In the prompt:
# In [1]: odrv0.vbus_voltage
```

---

## Experiments

### Experiment ① : Object (10 g)
![Image](https://github.com/user-attachments/assets/c4ebd16a-ba07-4b57-8cf1-6ba6bf7666ab)

### Experiment ② : Object (30 g)
*(to be added)*

### Experiment ③ : Drone-Mounted Test (planned)
*(planned)*

---

## Five-Bar Linkage Code
Kinematic simulation for the fingertip mechanism lives in `src/five_bar_linkage.py`.

```python
from five_bar_linkage import simulate
simulate(lengths=[100, 80, 60, 80, 100], top_point=(0, 200))
```

---

## Contributors
- **Jiwoong Choi** — <chjwng@pusan.ac.kr>  
- **Yongju Ryu** — <ryj01@naver.com>
- **Hyunwoo Seong** - <zidlt@pusan.ac.kr>
