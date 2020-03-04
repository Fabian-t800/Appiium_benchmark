from proj_lib.BaseLayer import BaseLayer
import re

class HelperClass:

    def __init__(self):
        self.window_handle = BaseLayer().ret_window_handle()

    def keyboard_typing(self, characters):
        self.window_handle.send_keys(characters)

    def read_results(self):
        return BaseLayer().result_window().read_result()

    def read_sci_results(self):
        return BaseLayer().result_window().read_sci_result()

    def click_number(self, number):
        BaseLayer().number_button(number).click()

    def click_symbol(self, symbol):
        BaseLayer().symbol_button(symbol).click()

    def click_scientific_symbol_button(self, sci_symbol):
        BaseLayer().sci_symbol_button(sci_symbol).click()

    def assert_result(self, result, expected_result):
        if result == float(expected_result):
            return True
        else:
            raise AssertionError(f"The expected ({float(expected_result)}) result did not match the actual result {result}!")

    def type_keys_keyboard(self, keytypes):
        BaseLayer().window_handle.send_keys(keytypes)

    def change_calculator_type(self, type_of_calculator):
        BaseLayer().menu_item(type_of_calculator).click()

    def click_calculator_type_menu(self):
        BaseLayer().menu_button().click()

    def click_sec_power_button(self):
        BaseLayer().symbol_button("xpower2").click()

    def click_trigonometry_button(self):
        BaseLayer().symbol_button("trig")

    def click_converter_type(self, uom):
        self.window_handle.find_element_by_name(uom).click()

    def click_uom(self, source_uom_field):
        BaseLayer().button.conv_elem_button(source_uom_field).click()

    def read_converter_input_1(self):
        p = BaseLayer().conv_res_1().text.split()
        return float(p[0])

    def read_converter_input_2(self):
        p = BaseLayer().conv_res_2().text[14:]
        return float(re.findall('[0-9]+', p)[0])

