from kivy.app import App
from kivy.core.window import Window

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class GridLayouttExample(GridLayout):
    def print_this(self):
        print("this button is "+str(self.text))
        pass

    def add_buttons(self, number):
        i = 0
        while(i<number):
            b = Button(text=str(i))
            b.bind(on_press=GridLayouttExample.print_this)
            self.add_widget(b)
            print("another button "+str(i))
            i+=1
            pass
        pass    
          

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        GridLayouttExample.add_buttons(self, 100)
        pass

      



class BoxLayoutExample(BoxLayout):
    pass
    """
    #structure to display boxlayout with buttons
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")

        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)

    #funtion that create and display varius buttons
    def add_buttons(self, number):
        i = 0
        while(i<number):
        b = Button(text=str(i))
        self.add_widget(b)
        print("another button "+str(i))
        i+=1
        pass
    pass """

class MainWidget(Widget):
    pass


class MainApp(App):
    pass

MainApp().run()