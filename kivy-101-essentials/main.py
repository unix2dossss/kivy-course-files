from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.graphics.context_instructions import Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

class WidgetsExample(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)
    my_text = StringProperty(str(count))
    text_input_str = StringProperty("foo")
    # slider_value_txt = StringProperty("Slider Value")
    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled:
            self.count+=1
            self.my_text = str(self.count)

    def on_toggle_button_state(self, widget):
        print(f"toggle state: {widget.state}")
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_switch_active(self, widget):
        print(f"Switch: {widget.active}")

    def on_slider_value(self, widget):
        # self.slider_value_txt = str(int(widget.value))
        print(f"Slider Value: {str(int(widget.value))}")

    def on_text_validate(self, widget):
        self.text_input_str = widget.text


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        # self.padding =
        for i in range(0,100):
            # size = dp(100) + i*10
            size = dp(100)
            b = Button(text=str(i+1), size_hint=(None, None), size=(size, size))
            self.add_widget(b)

# No need to do this -> can also be done in .kv file for example: <GridLayoutExample@GridLayout>:
# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass

class BoxLayoutExample(BoxLayout):
    pass
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.orientation = "vertical"
    #     b1 = Button(text="A")
    #     b2 = Button(text="B")
    #     b3 = Button(text="C")
    #     self.add_widget(b1)
    #     self.add_widget(b2)
    #     self.add_widget(b3)

class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

class CanvasExample1(Widget):
    pass

class CanvasExample2(Widget):
    pass

class CanvasExample3(Widget):
    pass

class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Make Canvas like this:
        with self.canvas:
            my_line = Line(points=(100, 100, 400, 500), width=2)
            new_color = Color(0, 1, 0)
            my_circle = Line(circle=(400, 200, 80), width=2)
            my_rectangle = Line(rectangle=(700, 500, 150, 100), width=5)
            self.my_filled_rectangle = Rectangle(pos=(700, 200), size=(150, 200))

    def move_rectangle_button(self):
        # print("FOO")

        x, y = self.my_filled_rectangle.pos
        w, h = self.my_filled_rectangle.size
        # inc = dp(10)
        space_to_rightmost = self.width - (x+w)
        inc = dp(10)

        if space_to_rightmost < inc:
            inc = space_to_rightmost

        x += inc

        # Remember, Tuple is immutable, it cannot be changed.
        self.my_filled_rectangle.pos = (x, y)

class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        self.vx = dp(3)
        self.vy = dp(4)
        # Make Canvas like this:
        with self.canvas:
            self.ball = Ellipse(pos=self.center, size=(self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1/60)

    def on_size(self, *args):
        # print(f'On Size: {str(self.width)}, {str(self.height)}')
        self.ball.pos = (self.center_x-self.ball_size/2, self.center_y-self.ball_size/2)

    def update(self, dt):
        x, y = self.ball.pos

        x += self.vx
        y += self.vy

        # Conditions:
        # x and y are the lower left part of the ball.
        # right part = self.ball_size

        if y + self.ball_size > self.height:
            y = self.height - self.ball_size
            # inverting velocity in the Y direction
            self.vy = -self.vy

        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            # inverting velocity in the X direction
            self.vx = -self.vx

        if y<0:
            y = 0
            self.vy = -self.vy

        if x<0:
            x = 0
            self.vx = -self.vx

        self.ball.pos = (x, y)


class CanvasExample6(BoxLayout):
    pass

TheLabApp().run()