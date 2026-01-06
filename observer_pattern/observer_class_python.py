class WeatherStation():
    def __init__(self):
        self._temperature = 0
        self._observers =[]
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        self._temperature = value
        self.notify_observers()
    def add_observer(self,observer):
        self._observers.append(observer)
    def notify_observers(self):
        for observer in self._observers:
            observer.update(self._temperature)
class PhoneDisplay:
    def update(self,temperature):
        print(f"Phone Display: {temperature}°C")

class WindowDisplay:
    def update(self, temperature):
        print(f"Window Display: {temperature}°C")

ws = WeatherStation()

phone = PhoneDisplay()
window = WindowDisplay()

ws.add_observer(phone)
ws.add_observer(window)

ws.temperature = 25
ws.temperature = 30