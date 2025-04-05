class Smartphone:
    def _init_(self, brand, model, screen_size, storage_capacity, battery_capacity):
        """
        Constructor to initialize a Smartphone object.

        Args:
            brand (str): The brand of the smartphone.
            model (str): The model name of the smartphone.
            screen_size (float): The screen size in inches.
            storage_capacity (int): The storage capacity in GB.
            battery_capacity (int): The battery capacity in mAh.
        """
        self.brand = brand
        self.model = model
        self.screen_size = screen_size
        self.storage_capacity = storage_capacity
        self.battery_capacity = battery_capacity
        self.battery_level = 100  # Initial battery level
        self.is_locked = True
        self.installed_apps = []

    def power_on(self):
        """Powers on the smartphone."""
        print(f"{self.brand} {self.model} is powering on...")
        self.is_locked = True  # When powered on, it's usually locked
        print("Screen is on. Device locked.")

    def power_off(self):
        """Powers off the smartphone."""
        print(f"{self.brand} {self.model} is powering off...")
        self.is_locked = True
        print("Screen is off.")

    def lock(self):
        """Locks the smartphone."""
        if not self.is_locked:
            self.is_locked = True
            print("Smartphone locked.")
        else:
            print("Smartphone is already locked.")

    def unlock(self):
        """Unlocks the smartphone."""
        if self.is_locked:
            print("Unlocking smartphone...")
            self.is_locked = False
            print("Smartphone unlocked.")
        else:
            print("Smartphone is already unlocked.")

    def install_app(self, app_name):
        """Installs a new app."""
        if app_name not in self.installed_apps:
            self.installed_apps.append(app_name)
            print(f"{app_name} installed successfully.")
        else:
            print(f"{app_name} is already installed.")

    def uninstall_app(self, app_name):
        """Uninstalls an existing app."""
        if app_name in self.installed_apps:
            self.installed_apps.remove(app_name)
            print(f"{app_name} uninstalled successfully.")
        else:
            print(f"{app_name} is not installed.")

    def call(self, phone_number):
        """Simulates making a call."""
        if not self.is_locked:
            print(f"Calling {phone_number}...")
        else:
            print("Unlock the phone to make a call.")

    def send_message(self, phone_number, message):
        """Simulates sending a message."""
        if not self.is_locked:
            print(f"Sending message to {phone_number}: '{message}'")
        else:
            print("Unlock the phone to send a message.")

    def check_battery(self):
        """Checks the current battery level."""
        print(f"Battery level: {self.battery_level}%")

    def charge(self, duration_hours):
        """Simulates charging the phone."""
        if self.battery_level < 100:
            charge_amount = duration_hours * 20  # Example charge rate
            self.battery_level = min(100, self.battery_level + charge_amount)
            print(f"Charged for {duration_hours} hours. Battery level is now {self.battery_level}%.")
        else:
            print("Battery is already full.")

    def open_app(self, app_name):
        """Opens an installed app."""
        if not self.is_locked:
            if app_name in self.installed_apps:
                print(f"Opening {app_name}...")
            else:
                print(f"{app_name} is not installed.")
        else:
            print("Unlock the phone to open apps.")

# Creating instances of the Smartphone class
my_phone = Smartphone("Samsung", "Galaxy S23", 6.1, 256, 3900)
another_phone = Smartphone("Apple", "iPhone 15", 6.1, 128, 3870)

# Using the methods of the Smartphone class
my_phone.power_on()
my_phone.unlock()
my_phone.install_app("WhatsApp")
my_phone.install_app("Instagram")
my_phone.open_app("WhatsApp")
my_phone.call("07XXXXXXXX")
my_phone.check_battery()
my_phone.send_message("07YYYYYYYY", "Hello!")
my_phone.lock()
my_phone.open_app("Instagram") # This won't work as the phone is locked
my_phone.charge(1)
my_phone.check_battery()
my_phone.power_off()