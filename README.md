# Single-Finger Gripper for Scooping Object

We present our **Single-Finger Gripper for High-Speed Scooping**, an latest robotic end-effector designed to scoop objects quickly.
This project is inspired by and extends the work of [Direct-Drive-Gripper-with-Swivel-Fingertips](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips).\
\
<img width="1000" height="1000" alt="Image" src="https://github.com/user-attachments/assets/44b333e8-3319-4073-98d7-50a0dfb12ab4" />\
![Image](https://github.com/user-attachments/assets/085ccb89-bac7-4e0a-90ff-e5287afef652)

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
- [Gripper](#gripper)  
  - [Finger Assembly](#finger-assembly)  
  - [Gripper Assembly](#gripper-assembly)
- [Mounting](#mounting)  
  - [Customization](#customization)
- [Software](#software)  
  - [Versions](#versions)
  - [Virtual Environment Settings](#virtual-environment-settings)
  - [Motor Manipulation](#motor-manipulation)  
- [Experiments](#experiments)  
  - [Experiment ① : Test Object (10 g)](#experiment---test-object-10-g)  
  - [Experiment ② : Test Object (30 g)](#experiment---test-object-30-g)  
  - [Experiment ③ : Carton Box (63 g)](#experiment---carton-box-63-g)
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
<img width="539" height="560" alt="Image" src="https://github.com/user-attachments/assets/5da362db-3cf8-4530-8134-9ac9b487d681" />

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

# Gripper

## Finger Assembly
Insert bearings at the **red-circled** locations.  
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

## Versions
- Ubuntu: `22.04`  
- Python: `3.10.11`  
- ODrive control utility: `0.6.7`

Please refer to [JS-RML, Direct-Drive Gripper with Swivel Fingertips/Software/Getting started](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main?tab=readme-ov-file#getting-started) to get started.

if you finish [JS-RML, Direct-Drive Gripper with Swivel Fingertips/Software/Getting started](https://github.com/JS-RML/Direct-Drive-Gripper-with-Swivel-Fingertips/tree/main?tab=readme-ov-file#getting-started) part and before Run main.py, you have to set Virtual Enviroment.

## Virtual Environment Settings
Please open Visual Studio Code terminal and copy and paste the code below to set your virtual environment.  

```bash 
sudo apt-get install python3-venv
python3 -m venv myenv
source myenv/bin/activate
pip install --upgrade odrive
```

## Motor Manipulation
Our end-effector uses a **Coaxial 5-bar(Diamond) Linkage**. The controller accepts the endpoint position of the diamond tip, P(x,y) in (mm), and outputs the two motor commands 𝜃₁ and 𝜃₂. 

<img width="537" height="476" alt="Image" src="https://github.com/user-attachments/assets/efec12e7-182d-42e9-b0f4-5cdb923fbcd1" />

### Example : (-80,0) → (80,0) → (68,0) → (0,80) → (0,50) → (-80,0) → (-68,0)
![Image](https://github.com/user-attachments/assets/085ccb89-bac7-4e0a-90ff-e5287afef652)

# Experiments

## Experiment ① : Test Object (10 g)
![Image](https://github.com/user-attachments/assets/c4ebd16a-ba07-4b57-8cf1-6ba6bf7666ab)

## Experiment ② : Test Object (30 g)
![Image](https://github.com/user-attachments/assets/28eefbeb-4b33-4c8f-abf6-829790dbf17d)

## Experiment ③ : Carton Box (63 g)
![Image](https://github.com/user-attachments/assets/56f5fcad-eaad-489a-911b-5b9a04546464)


# Contributors
- **Ji-woong Choi**, chjwng@pusan.ac.kr
- **Yong-joo Ryu**, ryj01@pusan.ac.kr
- **Hyun-woo Seong**, zidlt@pusan.ac.kr
