#Kivy Framework for the Mobile Application
from kivy.app import App #Application class
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#Creating class to run the program
class MainApp(App):
    def build(self):
        self.icon = "calc.png"
        self.operators = ["*", "/", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        layout = BoxLayout(orientation = "vertical")
        #Variable for displaying soluting
        self.result = TextInput(background_color = "black",foreground_color = "white",
        multiline=False, halign="right", font_size=55, readonly=True)
        #passing result into the layout
        layout.add_widget(self.result)
        buttons = [["7", "8", "9", "*"], ["4", "5", "6", "-"],
        ["1", "2", "3", "+"], [".", "0", "C", "/"]]

        for row in buttons:
            b_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color="grey",
                    pos_hint={"center_x": 0.5, "center_y": 0.5})
                button.bind(on_press=self.on_button_press)
                b_layout.add_widget(button)
            layout.add_widget(b_layout)

        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5})
        equal_button.bind(on_press=self.on_result)
        layout.add_widget(equal_button)
        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.result.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators


    def on_result(self, instance):
        text = self.result.text
        if text:
            result = str(eval(self.result.text))
            self.result.text = result

if __name__ == "__main__":
    MainApp().run()