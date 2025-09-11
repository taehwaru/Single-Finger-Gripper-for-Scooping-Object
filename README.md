# Single-Finger Gripper for Scooping Object
## 1. Overview

We present our **Single-Finger Gripper for High-Speed Scooping**, a new robotic end-effector designed to scoop objects quickly.
This project is inspired by and extends the work of [Direct-Drive-Gripper-with-Swivel-Fingertips](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips).\
\
![Image](https://github.com/user-attachments/assets/ff8aee65-1ade-4aa5-98c2-da446d936d9f)
**Related repos**
* [High-Speed Scooping (2024)](https://github.com/JS-RML/Advanced-high-speed-scooping/tree/main)
* [Direct-Drive Gripper (2024)](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips)
* [High-Speed Scooping (2022)](https://github.com/JS-RML/high_speed_scooping)
* [High-Speed Scooping (2022)](https://github.com/JS-RML/ddh_hardware)

## 2. Hardware Design

* **CAD Models**: Available in `/STL/`

* **Key Components**:

  * Motor: GB54-2

  * Encoder: AS5048A magnetic encoder

  * Driver: ODrive S1

  * Assembly Example:


## 3. Electronics & Control

* **Control Board:** ODrive S1

* **Encoder Feedback:** AS5048A for angular position

* **Communication:** USB / CAN interface

* **Wiring Diagram:** (to be added in `/Media/`)

## 4. Software

* **Programming Environment:** Python 3 + ROS2 (Humble)

* **Key Scripts:**

  * `main.py` → Main experiment loop

  * `gripper_controller.py` → Torque & position control

* **Installation:**

```bash
git clone https://github.com/username/Advanced-High-Speed-Scooping.git cd Advanced-High-Speed-Scooping pip install -r requirements.txt 
cd Single-Finger-Gripper-for-Scooping-Object
pip install -r requirements.txt
```

* **Execution:**

```bash 
python3 main.py
```
  
## 5. Experiments
### Experiment ① : Object (10 g)
![Image](https://github.com/user-attachments/assets/c4ebd16a-ba07-4b57-8cf1-6ba6bf7666ab)
## Experiment ② : Object (30 g)

(to be added)

### Experiment ③ : Drone-Mounted Test

(planned)

## 6. Results

* **Scooping Success Rate:** XX %

* **Average Reaction Time:** XXX ms

* **Payload Tested:** up to XXX g

## 7. Five-Bar Linkage Code

A kinematic simulation of the gripper was implemented using a **coaxial five-bar linkage model**.
Source code can be found in `/src/five_bar_linkage.py`.

```python
# Example snippet
from five_bar_linkage import simulate
```

simulate(lengths=[100, 80, 60, 80, 100], top_point=(0, 200))

## 8. Future Work

* Optimize lightweight fingertip design

* Improve force/torque control

* Integration with autonomous drone systems
