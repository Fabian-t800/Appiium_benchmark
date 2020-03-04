from proj_lib.Element import Element


class Button(Element):

    def number_button(self, number):
        """
        :param number: integer containing a single-digit number
        :return:
        """
        return self.ret_element().find_element_by_accessibility_id(f"num{int(number)}Button")

    def symbol_button(self, symbol):
        return self.ret_element().find_element_by_accessibility_id(f"{symbol.lower()}Button")

    def sci_symbol_button(self, sci_symbol):
        return self.ret_element().find_element_by_accessibility_id(sci_symbol)

    def conv_elem_button(self, input_field):
        return self.ret_element().find_element_by_accessibility_id(input_field)

class MenuIcon(Element):

    def get_name(self):
        return self.ret_element().text

    def click_menu_icon(self):
        self.ret_element().click()


class Menu(Element):

    def ret_menu(self, element_name):
        return self.ret_element().find_element_by_accessibility_id(element_name)

    def click_menu_item(self, element_name):
        self.ret_element().find_element_by_accessibility_id(element_name).click()


class Window(Element):

    def ret_entire_window(self):
        return self.ret_element()

    def ret_window_text(self):
        return self.ret_element().text


class ResultsWindow(Window):

    def read_result(self):
        return float(self.ret_window_text()[10:])

    def read_sci_result(self):
        return float(self.ret_window_text()[10:19])


class ConversionResWindow(Window):
    def input_window_value(self):
        return self.ret_entire_window().find_element_by_accessibility_id("Value1")

    def result_window_value(self):
        return self.ret_entire_window().find_element_by_accessibility_id("Value2")


class BaseLayer:

    def __init__(self):
        self.button = Button()
        self.window_handle = Element(locator_strategy="name", locator="Calculator").ret_element()

    def ret_window_handle(self):
        return self.window_handle

    def number_button(self, number):
        return self.button.number_button(number)

    def symbol_button(self, symbol):
        return self.button.symbol_button(symbol)

    @staticmethod
    def result_window():
        return ResultsWindow(locator_strategy="accessibility_id", locator="CalculatorResults")

    def menu_button(self):
        return MenuIcon(locator_strategy="accessibility_id", locator="TogglePaneButton").ret_element()

    def menu_item(self, menu_item_name):
        return Menu().ret_menu(menu_item_name)

    def sci_symbol_button(self, sci_symbol_element_id):
        return self.button.sci_symbol_button(sci_symbol_element_id)

    def conv_menu(self, input_f):
        return self.button.conv_elem_button(input_field=input_f)

    def conv_res_1(self):
        return ConversionResWindow().input_window_value()

    def conv_res_2(self):
        return ConversionResWindow().result_window_value()

# if __name__ == '__main__':
#     BaseLayer().number_button(1).click()
#     BaseLayer().symbol_button("plus").click()
#     BaseLayer().number_button(4).click()
#     BaseLayer().symbol_button("equal").click()
#     print(BaseLayer().result_window().read_result())
#     # BaseLayer().keyboard(145)
