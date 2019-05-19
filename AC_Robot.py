import machine

class Robo:
    def __init__(self,machine):
        self.machine = machine
        self.LeftMotor1=machine.PWM(machine.Pin(14), freq =200 , duty = 1023)
        self.LeftMotor2=machine.PWM(machine.Pin(12), freq =200 , duty = 1023)
        self.RightMotor1=machine.PWM(machine.Pin(13), freq =200 , duty = 1023)
        self.RightMotor2=machine.PWM(machine.Pin(15), freq =200 , duty = 1023)

    def Stop(self):
        self.LeftMotor1.duty(1023)
        self.LeftMotor2.duty(1023)
        self.RightMotor1.duty(1023)
        self.RightMotor2.duty(1023)

    def Forwrad(self , duty = 0):
        self.LeftMotor1.duty(duty)
        self.RightMotor1.duty(duty)

    def Backward(self , duty = 0):
        self.LeftMotor2.duty(duty)
        self.RightMotor2.duty(duty)

    def Left(self):
        self.Stop()
        self.RightMotor1.duty(0)

    def Right(self):
        self.Stop()
        self.LeftMotor1.duty(0)

    def Upleft(self):
        self.Stop()
        self.RightMotor1.duty(0)
        self.LeftMotor2.duty(100)


    def Upright(self):
        self.Stop()
        self.LeftMotor1.duty(0)
        self.RightMotor2.duty(100)

    def Downleft(self):
        self.Stop()
        self.RightMotor2.duty(0)
        self.LeftMotor1.duty(100)


    def Downright(self):
        self.Stop()
        self.LeftMotor2.duty(0)
        self.RightMotor1.duty(100)
