import keyboard  # using module keyboard
import pyperclip as clip
import pyautogui as au
import time as t

def case_converter():
    t.sleep(0.3)
    au.press('delete')
    t.sleep(0.3)
    string_1 = clip.paste() #paste what you copy already
    clip.copy(string_1.lower()) # Transformed the copied sentence and then copy to boardclip
    t.sleep(0.3)
    au.hotkey('ctrl','v')
    print (string_1.lower()) # Show the transformed sentence
    
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('ctrl+c'):  # if key 'ctrl+c' is pressed 
            case_converter() # execute the defined function
        elif keyboard.is_pressed('end'):  # if key 'end' is pressed 
                break # Terminate the program
        
    except:
        break