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
      | Name | Number | Pictures |
      |  --- | --- | --- |
      | ATMEGA2560-16AU | 1 |![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/d63b3f7da24ce03e0000dabeccd7ed70caecaaaf/Mega2560.jpeg)|
      | Raspberry Pi Model 3B+ | 1 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/b04889b4c000208db660323e5e8df1ffa59d043f/Raspberrypi.png) |
      | DC 3V-5V Water Level Sensor | 1 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/DC%203V-5V%20Water%20Level%20Sensor.jpeg) |
      | Encoder/DC Motor Driver | 2 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Encoder:DC%20Motor%20Driver.jpeg) |
      | IR Proximity Sensor | 2 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/IR%20Proximity%20Sensor.jpeg) |
      | Impact Switch | 2 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)|
      | Lithium AA Battery (1.5V) | 6 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/b04889b4c000208db660323e5e8df1ffa59d043f/battery.png) |
      | MakeBlock mbot mega Chassis | 1 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/MakeBlock%20mbot%20mega%20Chassis.png) |
      | Custom 10-pin Wiring Harness | 1 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Custom%2010-pin%20Wiring%20Harness.jpeg)|
      | RGB LED | 2 |![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/b04889b4c000208db660323e5e8df1ffa59d043f/RGB%20LED.png) |
      | HD USB Webcamera | 1 | ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/HD%20USB%20Webcamera.png) |
      

  - __Fall-back Plan__:
    - Plan 1: Paper model of Roosevelt island/Cornell Tech with smart features (weather, transportation, night lights etc.)
    - Plan 2: Reduce the features in our bud


- __Functioning Project__: 



    The completed project is a robotic plant that functions as a pet and has the following features:
      - Zommie 1: https://youtu.be/gFXpq3ll_io
      - Zommie 2:https://youtu.be/Q4AVnUg-z1g
      - Sunlight Chasing: https://youtu.be/p_VLosO4qjc
      - I want water dance: https://youtu.be/mdTZZOwKOjE
      - Stay away from Stranger: https://youtu.be/u5x-O6yp5lo
      - Butt Scratch: https://youtu.be/7XOs2DJO2yg
      - Recognize Owner: https://youtu.be/gSTwQe7AVko

    

- Documentation of design process
  - Ideation:
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)
    
  - Sketch Designs:
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)
    
  - Prototyping/Wizarding:
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)
    ![This is an image](https://github.com/JMortonTan/bud-cornell-tech-idd-final/blob/main/Impact%20Switch.jpeg)

  - Software designs:
    Here is a link to our code: https://github.com/JMortonTan/bud-cornell-tech-idd-final/tree/main/code
    We used 

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
    Building the plant-like robot "BUD" was the fascinating project I have ever built. That allowed me to explore the hardware (Ex. Raspberry Pi), software, and tools used for building interactive devices. My teammate Jon and I are both plant and cat lovers. Thus, the goal of our project was to make an interactive pet-like plant plot. To achieve our goals, we decided to use the technics we learned in classes to combine plants with robots. 

    One of the main challenges we faced during this project was the high energy consumption of our robot. Initially, we relied on a plug-in power source, but this limited the mobility of the robot. As a solution, we created a battery pack for the robot. However, the added weight of the battery pack made the robot kits heavy, and the six-battery pack only allowed the robot to run for 20 minutes before running out of energy. This time, we could not overcome this limitation on time. We will continue to experiment with self-sustaining energy sources in an effort to improve the energy consumption issue.

    Additionally, this was my first time working with maker tools, such as soldering and wire-cutting tools. To familiarize myself with these tools, I watched numerous YouTube tutorials. I found the experience of using these tools to be very interesting and would like to continue learning more about them in the future.

    Overall, the project was a success, and the plant-like robot could move and behave in a manner that was remarkably similar to a real cat. It was a great learning experience, and I feel that I gained a greater understanding of both engineering and interactive devices as a result.

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
