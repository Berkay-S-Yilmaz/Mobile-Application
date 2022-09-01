#Kivy Framework for the Mobile Application
from kivy.app import App #App class
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button

#Designing GUI in this class
class MainGrid(GridLayout): #child class of Gridlayout, allows inheritance of methods 
    def __init__(self, **kwargs): # ** allows unlimited attributes
        super(MainGrid, self).__init__(**kwargs)
        self.cols = 1 #Dividing screen into columns
        
        #Adding Nested Grid Layout
        self.inner = GridLayout()
        self.inner.cols = 2

        #Adding widgets (Texts, Input Boxes etc)
        self.inner.add_widget(Label(text = "Forename: ")) #1) Create Label
        self.forename = TextInput(multiline = False) #2) Add input box
        self.inner.add_widget(self.forename) #Add the label as widget

        self.inner.add_widget(Label(text="Surname: "))
        self.surname = TextInput(multiline = False)
        self.inner.add_widget(self.surname)

        self.inner.add_widget(Label(text = "Email: "))
        self.email = TextInput(multiline=False)
        self.inner.add_widget(self.email)

        #Adding inner to class
        self.add_widget(self.inner)

        #Button Widget (outside of .inner gridlayout column)
        self.submit = Button(text = "Submit", font_size=30)
        self.submit.bind(on_press = self.btn_pressed)
        self.add_widget(self.submit)

    def btn_pressed(self, instantce):
        #variables using text input
        forename = self.forename.text
        surname = self.surname.text
        email = self.email.text
        print(f"Forename: {forename} /  Surname: {surname}  /  Email: {email}")
        #clearing input text after submission
        self.forename.text = ""
        self.surname.text = ""
        self.email.text = ""


#Creating class to run the program
class MainApp(App):  
    def build(self):
        return MainGrid() 

#If script is run directly, run the App
if __name__== "__main__":
    MainApp().run() 