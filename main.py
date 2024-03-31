#This line imports the Tkinter module and gives it the alias tk.
import tkinter as tk
import requests
from PIL import Image,ImageTk
# Python Imaging Library (PIL)
#The Image module provides a class for representing 
#images and a variety of functions for creating, modifying, and working 
#with images.
#The ImageTk module provides support for displaying images in Tkinter applications.
'''
This line creates the main window of the application. 
The Tk() function is used to create an instance of the Tkinter Tk class, which represents the main window of the application.
This instance is assigned to the variable root.
'''
root=tk.Tk()

root.title("Weather App")
# Giving the size of frame
root.geometry("600x500")

#For  formating response from api request
#Mainly formating json file to string
def format_response(weather):
    try:
        City=weather['name']
        Condition=weather['weather'][0]['description']
        temp=weather['main']['temp']
        final_str='City:%s\nCondition:%s\nTemperature:%s'%(City,Condition,temp)
    except:
        final_str='Threre was a problem in retrieving information'
    
    return final_str

### Here is function to find the weather of country and cities
#key: c9e1d01223df60a70c654340d166498c
# Api :https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def get_weather(city):
    weather_key='c9e1d01223df60a70c654340d166498c'
    url='https://api.openweathermap.org/data/2.5/weather'
    params={'appid':weather_key,'q':city,'units':'imperial'}
    response=requests.get(url,params)
    #weather is filled with json format data
    weather=response.json()
    # print(weather['name'])
    # print(weather['weather'][0]['description'])
    # print(weather['main']['temp'])\
    '''result is a Tkinter Label widget, and result['text'] is an attribute of that widget.'''
    result['text']=format_response(weather)
    icon_name=weather['weather'][0]['icon']
    open_image(icon_name)


def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size,size)))
    weather_icon.delete('all')
    #in can vas the image is placed
    weather_icon.create_image(0,0,anchor='nw',image=img)
    weather_icon.image=img


img=Image.open('./img/bg.png')
#Antilias converts high level image to low level image
#Image.ANTIALIAS specifies the resampling filter to use when resizing the image
img=img.resize((600,500),Image.ANTIALIAS)

'''
This line creates a Tkinter-compatible image object from the PIL image using the ImageTk.
PhotoImage() function from the PIL library.
'''
img_photo=ImageTk.PhotoImage(img)
#This line creates a Tkinter Label widget and associates it with the root window.
bg_lbl=tk.Label(root,image=img_photo)
#place() method to position and size the label within the window.
bg_lbl.place(x=0,y=0,width=600,height=500)

heading_title=tk.Label(bg_lbl,text="Today's Weather",fg='red',bg='#000063',font=("times new roman",16,'bold'))
heading_title.place(x=80,y=18)
#This line creates a Frame widget and associates it with the bg_lbl label widget.
frame_one=tk.Frame(bg_lbl,bg='light blue',bd=5)
#This line uses the place() method to position and size the frame within the window.
frame_one.place(x=80,y=60,width=450,height=50)
#This line creates an Entry widget and associates it with the frame_one frame. 
txt_box=tk.Entry(frame_one,font=("times new roman",25),width=17)

txt_box.grid(row=0,column=0,sticky='w')

'''
text='get weather': This sets the text displayed on the button to 'get weather'.
fg='green': This sets the foreground color of the button text to green.
font=('times new roman', 16, 'bold'): This sets the font style, size, and weight of the button text.

row=0: This specifies that the button should be placed in the first row of the grid within the frame.
column=1: This specifies that the button should be placed in the second column of the grid within the frame.
padx=10: This adds horizontal padding of 10 pixels around the button within its grid cell.

'''

btn=tk.Button(frame_one,text='get weather',fg='green',font=('times new roman',16,'bold'),command=lambda: get_weather(txt_box.get()))
#he button is then positioned within the frame using the grid() method 
btn.grid(row=0,column=1,padx=10)



#2nd frame should have to be created in where the result of weather will be 
#shown

#border width is set to 5 pixel
frame_two=tk.Frame(bg_lbl,bg="#42c2f4",bd=5)
frame_two.place(x=80,y=130,width=450,height=300)


'''
This code creates a Label widget for displaying the weather result within
the frame_two frame. The font size is set to 40, and the background color
of the label is set to white. The label is then placed within the frame 
to occupy its entire area using relative height and width.
'''

#anchor option for a Label widget specifies where the text or image should be positioned within the available space in the label widget.
#justify option specifies the horizontal alignment of the text within the label,
result=tk.Label(frame_two,font=40,bg='white',justify='left',anchor='nw')
result.place(relheight=1,relwidth=1)

#n the Tkinter place method, xrel and yrel are relative coordinates, and relwidth and relheight are relative dimensions.
#Here a can vas is created on which image icon will be placed canvas border is 0 (no border) and 
#Canvas will start at 75% of the parent's width, and its width will extend to cover the remaining 25%.
weather_icon=tk.Canvas(result,bg='white',bd=0,highlightthickness=0)
weather_icon.place(relx=0.75,rely=0,relwidth=1,relheight=0.5)



'''
This line starts the Tkinter event loop. The mainloop() function is a method of the Tk class, and 
it runs an event loop, which listens for events such as user input and updates the GUI accordingly.
'''
root.mainloop()


'''
In graphical user interface (GUI) programming, a widget is a graphical element or control that is part of the user interface. 
Widgets are the building blocks of a GUI and can include buttons, text boxes, labels, sliders, checkboxes, and various other interactive elements. 

Here are some common types of widgets:

Button: A clickable element that performs a specific action when pressed.

Label: A non-editable text element used for displaying information or providing instructions.

Entry: An editable text box that allows users to input text or data.

Checkbox: A small box that can be checked or unchecked to represent a binary choice.

Radio Button: A button that belongs to a group of radio buttons, where only one button in the group can be selected at a time.

Slider: A draggable control that allows users to select a value within a specified range.

Listbox: A list of selectable items from which users can make a choice.

Canvas: A drawing area where graphical elements can be drawn or displayed.


'''