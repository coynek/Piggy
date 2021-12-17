#!/usr/bin python3
from teacher import PiggyParent
import sys
import time

class Piggy(PiggyParent):

    '''
    *************
    SYSTEM SETUP
    *************
    '''

    def __init__(self, addr=8, detect=True):
        PiggyParent.__init__(self) # run the parent constructor

        ''' 
        MAGIC NUMBERS <-- where we hard-code our settings
        '''
        self.LEFT_DEFAULT = 78
        self.RIGHT_DEFAULT = 80
        self.MIDPOINT = 1475  # what servo command (1000-2000) is straight forward for your bot?
        self.set_motor_power(self.MOTOR_LEFT + self.MOTOR_RIGHT, 0)
        self.load_defaults()
        
    def load_defaults(self):
        """Implements the magic numbers defined in constructor"""
        self.set_motor_limits(self.MOTOR_LEFT, self.LEFT_DEFAULT)
        self.set_motor_limits(self.MOTOR_RIGHT, self.RIGHT_DEFAULT)
        self.set_servo(self.SERVO_1, self.MIDPOINT)

    def menu(self):
        """Displays menu dictionary, takes key-input and calls method"""
        ## This is a DICTIONARY, it's a list with custom index values. Python is cool.
        # Please feel free to change the menu and add options.
        print("\n *** MENU ***") 
        menu = {"n": ("Navigate", self.nav),
                "d": ("Dance", self.dance),
                "o": ("Obstacle count", self.obstacle_count),
                "s": ("Shy", self.shy),
                "f": ("Follow", self.follow),
                "c": ("Calibrate", self.calibrate),
                "q": ("Quit", self.quit),
                "v": ("Katie's Test", self.katie),
                "b": ("Katie's Square", self.square),
                "d": ("Katie's Dance", self.dance),
                "r": ("Katie's Endless Cycle of Running into Walls",self.backtoback),
                "m": ("Katie's Robot moves Around Box", self.move_around_box),
                "z": ("Katie's Slow Read", self.slow_read),
                "y": ("Katie's scanning and swerving", self.Choice),
                "k": ("Katie's Maze Mode", self.maze_mode)
                }
        # loop and print the menu...
        for key in sorted(menu.keys()):
            print(key + ":" + menu[key][0])
        # store the user's answer
        ans = str.lower(input("Your selection: "))
        # activate the item selected
        menu.get(ans, [None, self.quit])[1]()

    '''
    ****************
    STUDENT PROJECTS
    ****************
    '''



    def katie(self):
      self.closer_edge()

    def square(self):
      for num in range (4):
        self.turn_right(.85)
        self.go_fwd(1)
        

    def turn_right(self, second):
        self.right()
        time.sleep(second)
        self.stop()
    def turn_left(self, second):
        self.left()
        time.sleep(second)
        self.stop()
    def go_fwd(self, second):
        self.fwd()
        time.sleep(second)
        self.stop()
    def go_back(self, second):
        self.back()
        time.sleep(second)
        self.stop()

    def dance(self):
      for num in range (10):
        self.right(20)
        self.fwd()
        time.sleep(.4)
        self.back()
        time.sleep(.4)

    def safe_to_dance(self):
      """ Does a 360 distance check and returns true if safe """
      # lower-ordered example...
      self.right(primary=50, counter=50)
      time.sleep(2)
      self.stop()

    def shake(self):
        """ Another example move """
        self.deg_fwd(720)
        self.stop()


    def backtoback(self):
        """Robots reads wall and reverses"""
        while True:
          if self.read_distance() > 100:
            self.fwd()
          else:
            self.right()
            time.sleep(1.5)

    def move_around_box(self):
        if self.read_distance() > 100:
          self.right(.75)
          
          

    def example_move(self):
        """this is an example dance move that should be replaced by student-created content"""
        self.right() # start rotating right
        time.sleep(1) # turn for a second
        self.stop() # stop
        self.servo(1000) # look right
        time.sleep(.25) # give your head time to move
        self.servo(2000) # look left

    def scan(self):
        """Sweep the servo and populate the scan_data dictionary"""
        for angle in range(self.MIDPOINT-350, self.MIDPOINT+350, 3):
            self.servo(angle)
            self.scan_data[angle] = self.read_distance()

    def obstacle_count(self):
        """Does a 360 scan and returns the number of obstacles it sees"""
        pass

    def nav(self):
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        print("-------- [ Press CTRL + C to stop me ] --------\n")
        print("-----------! NAVIGATION ACTIVATED !------------\n")
        
        # TODO: build self.quick_check() that does a fast, 3-part check instead of read_distance
        while self.read_distance() > 250:  # TODO: fix this magic number
            self.fwd()
            time.sleep(.01)
        self.stop()

        # TODO: scan so we can decide left or right
        # TODO: average the right side of the scan dict
        # TODO: average the left side of the scan dict

    def slow_read(self):
        self.fwd()
        while True:
              self.servo(1475)
              time.sleep(.15)
              if self.read_distance() <200:
                self.swerve_right()

              self.servo(1675)
              time.sleep(.15)        
              self.servo(1275)
              time.sleep(.15)

    def swr(self, dir):
      self.stop()
      self.servo(self.MIDPOINT)
      if "left" in dir:
        self.stop()
        self.left(primary = 60, counter = 30)
        time.sleep(1.5)
        self.fwd()
        time.sleep(1.5)
        self.right(primary = 60, counter=30)
        time.sleep(1.5) 
        self.fwd()
      if "right" in dir:
        self.left(primary = 30, counter=60)
        time.sleep(1.5)
        self.fwd()
        time.sleep(1.5)
        self.right(primary = 30, counter = 60)
        time.sleep(1.5)
        self.fwd()
        time.sleep(1.5)





    #edward helped me with this the commented text was what I tried. why did it not work? 
    def turner(self):
      while True:
        if(self.read_distance() > 200):
          self.fwd()  
        elif(self.read_distance() < 199):
          self.right()
          time.sleep(1)
          self.fwd()
          time.sleep(1)
          self.left()
          time.sleep(1)
          self.fwd()

    def swerve_left(self):
        self.left(primary=90, counter=30)
        time.sleep(.8)
        self.right(primary=90, counter=30)
        time.sleep(.8)
        self.fwd()

    def swerve_right(self):
        self.right(primary=90, counter=30)
        time.sleep(.8)
        self.left(primary=90, counter=30)
        time.sleep(.8)
        self.fwd()

    def closer_edge(self):
        self.fwd()
        if self.read_distance() < 200:
          self.stop()
          self.servo(1000)
          right = self.read_distance()
          self.servo(1950)
          left = self.read_distance()
          if right > left:
            self.turn_right(.85)
            self.go_fwd(1)
            self.turn_left(.85)
            self.servo(1475)
            self.fwd()
          if right < left:
            self.turn_left(.85)
            self.go_fwd(1)
            self.turn_right(.85)
            self.servo(1475)

    
    def Choice(self):
      while True:
        self.fwd()
        self.servo(1000)
        time.sleep(.1)
        if self.read_distance() < 300:
          self.stop()
          self.servo(self.MIDPOINT)
          time.sleep(.1)
          if self.read_distance() > 300:
            self.swerve_left()
          else:
            self.closer_edge()  
        self.servo(2000)
        if self.read_distance() < 300:
          self.stop()
          self.servo(self.MIDPOINT)
          time.sleep(.1)
          if self.read_distance() > 300:
            self.swerve_right()
          else:
            self.closer_edge()
        time.sleep(.1)

    def maze_mode(self):
      while True:
        self.fwd()
        self.servo(self.MIDPOINT)
        if self.read_distance() < 100:
          self.stop()
          self.servo(2000)
          time.sleep(.1)
          if self.read_distance() > 100:
             self.stop()
             self.left()
             time.sleep(1.3)
             self.fwd(1.3)
          else:
            self.stop()
            self.right()
            time.sleep(1.3)
            self.fwd(1.3)



    






















###########
## MAIN APP
if __name__ == "__main__":  # only run this loop if this is the main file

      p = Piggy()
      if sys.version_info < (3, 0):
        sys.stdout.write("Sorry, requires Python 3.x\n")
        p.quit()

      try:
        while True:  # app loop
          p.menu()

      except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
          p.quit()  
