from proj_lib.SetupTeardown import connect_to_application


class Element:

    def __init__(self, locator_strategy=None, locator=None):
        self.driver = connect_to_application("Microsoft.WindowsCalculator_8wekyb3d8bbwe!App")
        self.locator_strategy = locator_strategy
        self.locators = locator

    def ret_element(self):
        if self.locator_strategy is None and self.locators is None:
            return self.driver
        else:
            if self.locator_strategy.lower() == "accessibility_id":
                return self.driver.find_element_by_accessibility_id(self.locators)
            else:
                return self.driver.find_element(by=self.locator_strategy.lower(), value=self.locators)

    def read_element_name(self):
        return self.ret_element().text

    def click_element(self):
        self.ret_element().click()

    def toggle_state(self):
        pass

    def toggle_action(self):
        self.click_element()



# if __name__ == '__main__':
#     pass
#     # n1 = Button(locator_strategy="accessibility_id", locator="num1Button")
#     # n2 = Button(locator_strategy="accessibility_id", locator="num2Button")
#     # n5 = Button(locator_strategy="accessibility_id", locator="num5Button")
#     # menu = MenuIcon(locator_strategy="accessibility_id", locator="TogglePaneButton")
#     # conversion_menu = Menu(locator_strategy="accessibility_id", locator="MenuItemsHost")
#     # equal_button = Button(locator_strategy="accessibility_id", locator="equalButton")
#     # multiply_button = Button(locator_strategy="accessibility_id", locator="multiplyButton")
#     # results = ResultsWindow(locator_strategy="accessibility_id", locator="CalculatorResults")
#     # conv_result = ConversionResWindow(locator_strategy="name", locator="Calculator")
#     #
#     # menu.click_menu_icon()
#     # conversion_menu.click_menu_item("Temperature")
#     # n1.click_button()
#     # n2.click_button()
#     # n5.click_button()
#     # print(conv_result.input_window_value())
#     # print(conv_result.result_window_value())
#     # # multiply_button.click_button()
#     # # n2.click_button()
#     # # equal_button.click_button()


