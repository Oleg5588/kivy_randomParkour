from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
import random
a=['манки', 'вал ран+рол', 'тиктак в акур', 'манки с выходом на акуроси', 'манки+рол', 'прокрутка возле перипятствия на 360', 'сальто с земли на ноги', 'ревёрс', 'двайной манки', 'вал ран в акур', 'манки на кетлип', 'сальто с трубы на картоны', 'акуроси', 'вал ап на акураси', 'лач на манки', 'тик-так', 'вал ап', 'вал ран', 'кеш', 'конг']


class MyApp(App):
    def build(self):
        bl = BoxLayout(orientation = 'vertical')
        self.label = Label()
        self.button = Button(text = 'Trick', on_press=self.click)
        bl.add_widget(self.label)
        bl.add_widget(self.button)

        return bl
    def click(self, event ):
        self.label.text = random.choice(a)

if __name__ == "__main__":
    MyApp().run()