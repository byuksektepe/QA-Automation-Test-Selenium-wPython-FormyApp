from chrome_driver import chrome_driver
from sub import sub
from scenarios.keyboard_mouse_input import keyboard_mouse_input_scenario
from scenarios.autocomplete import autocomplete_scenario
from scenarios.scroll_to_element import scroll_to_element_scenario
from scenarios.switch_to_window import switch_to_window_scenario
from scenarios.switch_to_alert import switch_to_alert_scenario
from scenarios.execute_javascript import execute_javascript_scenario
import sys
sub = sub()

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
keyboard_mouse_input_scenario = keyboard_mouse_input_scenario()
keyboard_mouse_input_scenario.start(main.chrome_driver)

# Click Dropdown Menu then click autocomplete link
# instead, the url can be redirected directly with driver.get()
sub.click_element(find_element_mode="ID", item="navbarDropdownMenuLink", page_load_wait_id="null", driver=main.chrome_driver, require_wait=0)
sub.click_element(find_element_mode="LINK_TEXT", item="Autocomplete", page_load_wait_id="autocomplete", driver=main.chrome_driver)
# Start Autocomplete scenario
autocomplete_scenario = autocomplete_scenario()
autocomplete_scenario.start(main.chrome_driver)

# Click Dropdown Menu then click page scroll link
sub.click_element(find_element_mode="ID", item="navbarDropdownMenuLink", page_load_wait_id="null", driver=main.chrome_driver, require_wait=0)
sub.click_element(find_element_mode="LINK_TEXT", item="Page Scroll", page_load_wait_id="date", driver=main.chrome_driver)
# Start scroll to element scenario
scroll_to_element_scenario = scroll_to_element_scenario()
scroll_to_element_scenario.start(main.chrome_driver)

sub.click_element(find_element_mode="ID", item="navbarDropdownMenuLink", page_load_wait_id="null", driver=main.chrome_driver, require_wait=0)
sub.click_element(find_element_mode="LINK_TEXT", item="Switch Window", page_load_wait_id="new-tab-button", driver=main.chrome_driver)

switch_to_window_scenario = switch_to_window_scenario()
switch_to_window_scenario.start(main.chrome_driver)
#Stay same page
switch_to_alert_scenario = switch_to_alert_scenario()
switch_to_alert_scenario.start(main.chrome_driver)

sub.click_element(find_element_mode="ID", item="navbarDropdownMenuLink", page_load_wait_id="null", driver=main.chrome_driver, require_wait=0)
sub.click_element(find_element_mode="LINK_TEXT", item="Modal", page_load_wait_id="modal-button", driver=main.chrome_driver)

execute_javascript_scenario = execute_javascript_scenario()
execute_javascript_scenario.start(main.chrome_driver)
# Call This lAST!
sub.sleep_and_quit(2, main.chrome_driver)
