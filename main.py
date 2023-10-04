

# from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.screenmanager import ScreenManager, Screen
#
# Builder.load_file("QuizPage.kv")
# class QuizPageApp(App):
#     def build(self):
#         return QuizManager()
#
#
# class QuizManager(ScreenManager):
#     pass
# class Question1Screen(Screen,BoxLayout):
#     def answer_question(self,bool):
#         if bool:
#             self.manager.current = "correct"
#         else:
#             self.manager.current = "incorrect"
#
# class Question2Screen(Screen):
#     def answer_question(self, text):
#         if text == "red":
#             self.ids.test.text = "correct"
#             self.ids.test.font_size = 50
#             #self.manager.current = "correct"
#         else:
#             self.ids.test.text = "WRONG"
#             self.ids.test.font_size = 80
#
#             #self.manager.current = "incorrect"
#
# class CorrectScreen(Screen,BoxLayout):
#     def advance(self):
#         self.manager.current="question two"
# class IncorrectScreen(Screen,BoxLayout):
#     def advance(self):
#         self.manager.current="question two"
#
#
# QuizPageApp().run()

class LoginScreen(Screen,BoxLayout):
    pass
class NewAccount(Screen,BoxLayout):
    pass
class WelcomePage(Screen,BoxLayout):
    pass


class LoginPageApp(App):
    pass


LoginPageApp().run()