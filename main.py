from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

class LoginScreen(Screen):
    def login(self):
        username = self.ids.username_input.text.strip()
        password = self.ids.password_input.text.strip()

        if username in ['jxta', 'nico', 'nj', 'rumel'] and password == 'tp2024':
            self.manager.current = 'calculator'
        else:
            self.ids.error_label.text = 'Invalid username or password'

class CalculatorScreen(Screen):
    def calculate_gpa(self):
        num_subjects_text = self.ids.num_subjects_input.text.strip()
        grades_text = self.ids.grades_input.text.strip()
        units_text = self.ids.units_input.text.strip()

        if not num_subjects_text or not grades_text or not units_text:
            self.ids.result_label.text = "Please fill in all fields."
            return

        try:
            num_subjects = int(num_subjects_text)
            grades = [float(x) for x in grades_text.split(',')]
            units = [float(x) for x in units_text.split(',')]

            total_grade_points = sum(grade * unit for grade, unit in zip(grades, units))
            total_units = sum(units)

            gpa = total_grade_points / total_units
            self.ids.result_label.text = f'Your GPA is: {gpa:.2f}'
        except Exception as e:
            self.ids.result_label.text = "Error: " + str(e)

class GPAApp(App):
    def build(self):
        Builder.load_file('my.kv')  # Load the Kv file
        self.sm = ScreenManager()
        self.sm.add_widget(LoginScreen(name='login'))
        self.sm.add_widget(CalculatorScreen(name='calculator'))
        return self.sm

if __name__ == '__main__':
    GPAApp().run()
