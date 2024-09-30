class Car():
    def __init__(self):
        self.acc= False
        self.clutch= False
        self.brk= False 
    
    def start(self):
        print("Car started!Press clutch and start incognition") 
        while not self.clutch:
            action=input('enter C to start the car').lower()
            if action=='c':
                self.clutch= True
                print('Car is ready to move')

    def accelerate(self):
        if self.clutch:
            print('now you can accelerate')
            while not self.acc:
                action= input('enter A to accelerate').lower()
                if action=='a': 
                    self.acc= True
                    print('Now the car is accelerated')

    def brake(self):
        if self.acc:
            print("Now prepare to brake.")
            while not self.brk:
                action = input("Press 'B' to brake smoothly: ").lower()
                if action == 'b':
                    self.brk = True
                    print("Braking smoothly...")  
class DrivingLesson():
    def __init__(self):
        self.steps=["1. Sit in the car.",
            "2. Wear your seatbelt.",
            "3. Make the rearview mirrors open.",
            "4. Press the clutch and start the car.",
            "5. Accelerate gently.",
            "6. Brake smoothly."
        ]  
        self.current_step = 0
        self.car = Car()
        
    def next_step(self):
        if self.current_step < len(self.steps):
            print(self.steps[self.current_step])
            self.current_step += 1
        else:
            print('Congratulations! You now know the basics of driving.')

    def start_lesson(self):
        print('Welcome to your driving class!!')
        
        # Step 1: Sit in the car
        input('Press Enter after you sit in the car.')
        self.next_step()
        
        # Step 2: Wear your seatbelt
        input('Press Enter after you wear your seatbelt.')
        self.next_step()

        # Step 3: Open rearview mirrors
        input('Press Enter after adjusting the rearview mirrors.')
        self.next_step()

        # Step 4: Start the car by pressing the clutch
        self.car.start()
        self.next_step()
        
        # Step 5: Accelerate gently
        self.car.accelerate()
        self.next_step()
        
        # Step 6: Brake smoothly
        self.car.brake()
        self.next_step()

        print('Thank you for participating in this driving lesson!')

lesson = DrivingLesson()
lesson.start_lesson()


         


    