# bud-cornell-tech-idd-final
CS5424-Final Project

- __Project Plan__
  - __Big idea__:

    The "bud" is a hybrid plant-robot that turns your indoor potted plant into a house pet. It has features such as water monitoring and sunlight chasing, as well as additional pet-like characteristics. With "bud," your plant becomes a 100% companion.

  - __Timeline__:
    - Sketch Designs 11/20
    - Begin wizarding/prototyping 11/25
    - Complete laser cutting or 3D printing of assembly 11/30
    - Debugging sofware 12/3
    - Preparing demo videos 12/5
    - Final Writeup 12/12
    - Project Reflection 12/14
 
  - __Parts Needed__:
      | Name| Description |
      | Picture | --- |
      | git status | List all new or modified files |
      | git diff | Show file differences that haven't been staged |
    - ATMEGA2560-16AU x1
    - Raspberry Pi Model 3B+ x1
    - DC 3V-5V Water Level Sensor
    - Encoder/DC Motor Driver x2
    - IR Proximity Sensor x2
    - Impact Switch x2
    - Lithium AA Battery (1.5V) x6
    - MakeBlock mbot mega Chassis x1
    - Custom 10-pin Wiring Harness x1
    - RGB LED x2
    - HD USB Webcamera x1
    
  - __Fall-back Plan__:
    - Plan 1: Paper model of Roosevelt island/Cornell Tech with smart features (weather, transportation, night lights etc.)
    - Plan 2: Reduce the features in our bud


- Functioning project: The finished project should be a device, system, interface, etc. that people can interact with.

- Documentation of design process
  - Ideation:
  - Sketch Designs:
  - Prototyping/Wizarding:
  - Software designs:
  - Hardware designs:
  - Tools:

- Archive of all code, design patterns, etc. used in the final design. (As with labs, the standard should be that the documentation would allow you to recreate your project if you woke up with amnesia.)

- Video of someone using your project

- Reflections on process (What have you learned or wish you knew at the start?)
  - Jonathan Tan:
    
    In this project we started with a unique idea, to combine the actions of raising plants, and raising pets.

    This was unique because it was a very open ended proposition.  What kind of interactions should, would and are required in order to properly raise a plant?

    To quickly get to the point, I really wish I understood more about robotics at the beginning of the project.

    We spent a ton of time understanding how to interface Arduino and Raspberry Pi in order to allow Raspberry Pi to handle computing functions such as CV, and Arduino to handle controlling the motors.  We also spent a ton of time learning about robotics kits, power requirements and what kind of chassis we should purchase in order to fulfill basic functions such as mobility rotation, and expandability to add sensors.  Then, it was another journey to research and understand what type of sensors we were interested in using.

    Only after this was handled, were we able to begin ideating "What kinds of behaviors would a mechanized plant require in order to survive?" "What type of personality would it have or try to mimic?" "What are some typical interactions between a human and a pet?"

    Here we were most able to apply the ideation processing, storyboarding, and interactions that we had reviewed in the class.  We really wish we hadn't underestimated the basic knowledge required in robotics, such as calculating voltage and amperage requirements for various kits.  Especially since in the end, we decided to purchase a kit that had a power system predesigned for the chassis.  We also utilized much of the time soldering and creating a wiring harness that allowed the Pi and Arduino to interact with one another.  Although the kit was compatible, it required significant modification in order to physically bridge the two "brains".

    All in all, we really discovered that robotics is not as simple as a python script to set a motor to move a certain distance.  There are in fact several different types of motors for different types of movement as well (servo etc.).  Even two motors of the same model and type may not perform the same.

    We wish we had known this a bit earlier, and perhaps would have directly purchased a kit without wasting time believing it was possible to do on our own.  This way we could quickly focus on developing features and interactions, which was the most important aspect of the project.
  - Peggy Pei:

- Group work distribution questionnaire:

  Jon:
  - Sketch Ideation
  - Coding Logic
  - Hardware Selection
  - Motorization coding
  - Arduino and Pi Integration
  
  Peggy (Yiru):
  - Wiring Harness Soldering
  - Device Design
  - Laser Cut
  - Hardware Assembly
  - CV Programming and Implementation
