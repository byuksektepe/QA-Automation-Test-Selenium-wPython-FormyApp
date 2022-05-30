from chrome_driver import chrome_driver
from sub import sub
from scenarios.keyboard_mouse_input import keyboard_mouse_input_scenario
from scenarios.autocomplete import autocomplete_scenario
import sys
sub = sub()
keyboard_mouse_input_scenario = keyboard_mouse_input_scenario()
autocomplete_scenario = autocomplete_scenario()
class main:
    chrome_driver = chrome_driver().set()
    chrome_driver.get('https://formy-project.herokuapp.com/')

    def Get_Formy_App():

        main.chrome_driver.maximize_window()

        if not "Formy" in main.chrome_driver.title:
            raise Exception("Page Could Not Load, Check Title Text")


main.Get_Formy_App()
sub.click_element(find_element_mode="XPATH", item="/html/body/div/div/li[9]/a", page_load_wait_id="name", driver=main.chrome_driver)

# Start scenarios in order
keyboard_mouse_input_scenario.start(main.chrome_driver)
# Click Dropdown Menu then click autocomplete link
sub.click_element(find_element_mode="ID", item="navbarDropdownMenuLink", page_load_wait_id="name", driver=main.chrome_driver)
sub.click_element(find_element_mode="LINK_TEXT", item="Autocomplete", page_load_wait_id="autocomplete", driver=main.chrome_driver)
# Start Autocomplete scenario
autocomplete_scenario.start(main.chrome_driver)

# Call This lAST!
sub.sleep_and_quit(2, main.chrome_driver)
