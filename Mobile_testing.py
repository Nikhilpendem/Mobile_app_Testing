# from appium import webdriver
# from appium.webdriver.common.appiumby import AppiumBy
# import time

# # Set up desired capabilities
# desired_caps = {
#     "platformName": "Android",
#     "deviceName": "emulator-5554",  # Change to your device name
#     "app": "C:\Users\nikhi\OneDrive\Desktop\Final app.apk",  # Change to your app's path
#     "automationName": "UiAutomator2"
# }

# # Start a session with Appium
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# # Wait for app to load
# time.sleep(5)

# # Example: Find a button and click it
# try:
#     button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "LoginButton")  # Use correct ID or selector
#     button.click()
#     print("Button clicked successfully.")
# except Exception as e:
#     print("Could not find or click button:", e)

# # Wait and check for a result
# time.sleep(3)

# # Example: Check if a label or success message appears
# try:
#     success_msg = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Welcome']")
#     print("Test passed. Found success message.")
# except Exception as e:
#     print("Test failed. Message not found:", e)

# # End session
# driver.quit()

# from appium import webdriver
# import time

# desired_caps = {
#     "platformName": "Android",
#     "platformVersion": "15",
#     "deviceName": "emulator-5554",
#     "app": r"C:\Users\nikhi\OneDrive\Desktop\Final app.apk",  # Update if stored elsewhere
#     "automationName": "UiAutomator2"
# }

# # Connect to Appium server
# driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

# # Wait to see the app launch
# time.sleep(5)

# # Close the app
# driver.quit()

from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

options = UiAutomator2Options()

# Set desired capabilities
options.platform_name = "Android"
options.platform_version = "15"
options.device_name = "emulator-5554"
options.app = r"D:\Testing\Test cases\Final_app.apk"  # Update path if needed
options.automation_name = "UiAutomator2"

# Start the session with Appium server
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Let the app open for 5 seconds
time.sleep(5)

# Close the session
driver.quit()

