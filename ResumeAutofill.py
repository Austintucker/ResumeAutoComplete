import pyautogui as pya
import cv2, time

pya.FAILSAFE = True

print("\nBegin 5 sec Countdown!\n")
count = 5
for i in range(count):
    print(str(count - i) + "." * (count - i))
    time.sleep(1)        
print("\nExecute\n")

pya.click(pya.locateCenterOnScreen('captures\\0-email.png', grayscale=True, confidence=.5))
pya.move(1000, 0)
time.sleep(.5)


# Enter user credentials
pya.typewrite("Student@resilientresumes.com")
pya.press("tab")
time.sleep(.25)
pya.typewrite("thisisatemppassword")
pya.press("tab")
time.sleep(.25)
pya.press("enter")


# Start filling personal details
pya.move(1000, 0)
time.sleep(1)
pya.press("tab")
pya.typewrite("Bryan")
time.sleep(.25)
pya.press("tab")
pya.typewrite("Cruz")
time.sleep(.25)
pya.press("tab")
pya.press("tab")
pya.typewrite("123-456-9988") # phone number has an incrementation button?
time.sleep(.25)
pya.press("tab")
pya.typewrite("Student@resilientresumes.com")
time.sleep(.25)
pya.press("tab")


# Start filling address
pya.typewrite("123 Main St")
pya.press("tab")
pya.press("tab")
time.sleep(.25)
pya.typewrite("Reading")
pya.press("tab")
time.sleep(.25)
pya.typewrite("PA")
pya.press("tab")
time.sleep(.25)
pya.typewrite("19605")
pya.press("tab")
time.sleep(.25)
pya.typewrite("United States")
time.sleep(.25)
pya.press("tab")
time.sleep(.25)
pya.press("enter")



# Start Filling Objective
time.sleep(1)
pya.press("tab")
pya.typewrite("Junior Developer")
pya.press("tab")
time.sleep(.25)
pya.press("tab")
pya.press("tab")
time.sleep(.25)
pya.press("enter")



# Start Filling Social Profiles
time.sleep(1)
pya.press("tab")
pya.typewrite("https://www.linkedin.com/in/bryan-cruz/")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
time.sleep(.25)
pya.press("enter")



# Start Filling Education
time.sleep(1)
pya.press("tab")
pya.typewrite("UPR")
pya.press("tab")
time.sleep(.25)
pya.typewrite("Bayamon")
pya.press("tab")
time.sleep(.25)
pya.typewrite("PR")
pya.press("tab")
time.sleep(.25)
pya.typewrite("United States")
pya.press("tab")
time.sleep(.25)
pya.press("pgdn")
pya.press("tab")
time.sleep(.25)
pya.typewrite("Computer Science")
pya.press("tab")
pya.press("tab")
time.sleep(.25)
pya.typewrite("3.8")
pya.press("tab")
time.sleep(.25)
pya.typewrite("m")
pya.typewrite("m")
pya.press("tab")
pya.typewrite("2018")
pya.press("tab")
pya.press("enter")


pya.click(pya.locateCenterOnScreen('captures\\6-Institution.png', grayscale=True, confidence=.8))
pya.move(1000, 0)
pya.press("pgdn")
pya.typewrite("Reading Area Community College")
pya.press("tab")
time.sleep(.25)
pya.typewrite("Reading")
pya.press("tab")
time.sleep(.25)
pya.typewrite("PA")
pya.press("tab")
time.sleep(.25)
pya.typewrite("United States")
pya.press("tab")
time.sleep(.25)
pya.press("pgdn")
pya.press("tab")
time.sleep(.25)
pya.typewrite("Web Development")
pya.press("tab")
pya.press("tab")
time.sleep(.25)
pya.typewrite("3.5")
pya.press("tab")
time.sleep(.25)
pya.typewrite("m")
pya.typewrite("m")
pya.press("tab")
pya.typewrite("2018")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("enter")



# Start Filling Relevant Courses
time.sleep(1)
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("enter")



# Start Filling Experience
time.sleep(1)
pya.press("tab")
pya.typewrite("P")
pya.press("down")
pya.press("tab")
pya.typewrite("Yiftee")
pya.press("tab")
pya.typewrite("Web Development Intern")
pya.press("tab")
pya.typewrite("Menlo Park")
pya.press("tab")
pya.typewrite("CA")
pya.press("tab")
pya.typewrite("United States")
pya.press("tab")
pya.press("tab")
pya.typewrite("Responsive Website")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.typewrite("j")
pya.press("tab")
pya.typewrite("2014")
pya.press("tab")
pya.typewrite("j")
pya.typewrite("j")
pya.press("tab")
pya.typewrite("2014")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("enter")


# Start Filling Skills

# will manual fill these

print("\nBegin 20 sec Countdown!\n")
count = 20
for i in range(count):
    print(str(count - i) + "." * (count - i))
    time.sleep(1)        
print("\nExecute\n")


# Start Filling Acheivements
time.sleep(1)
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("enter")


# Start Filling Activities
time.sleep(1)
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("tab")
pya.press("enter")


# feedback
time.sleep(1)
pya.click(pya.locateCenterOnScreen('captures\\ContactInfo-Feedback.png', grayscale=True, confidence=.8))
time.sleep(5)
pya.press("pagedown")
time.sleep(5)
pya.press("pagedown")