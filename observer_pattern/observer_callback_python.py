class WeatherStation():
    def __init__(self):
        self._temperature = 0
        self._observers =[] #keep reocrds of observers 
    def add_observer(self,callback):
        # registers observer as callback function
        self._observers.append(callback)
    @property
    def temperature(self):
        return self._temperature
    @temperature.setter
    def temperature(self,value):
        self._temperature = value
        self._notify_observers()

    def _notify_observers(self):
        for callback in self._observers:
            callback(self._temperature)
def phone_display(temp):
    print(f"Phone Display: Temperature updated to {temp}°C")
    
def window_display(temp):
    print(f"Window Display: Temperature updated to {temp}°C")

weather_station = WeatherStation()
weather_station.add_observer(phone_display)
weather_station.add_observer(window_display)

weather_station.temperature = 25  # triggers callbacks
weather_station.temperature = 30
