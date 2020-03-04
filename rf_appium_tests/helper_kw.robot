*** Settings ***
Library  appium_tests/HelperClass.py
Resource  keywords.robot

*** Keywords ***


A number is clicked
    [Arguments]  ${first_number}
    click_number    ${first_number}

The plus sign is clicked
    click_symbol    plus

Another number is clicked
    [Arguments]  ${second_number}
    click_number    ${second_number}

The result is read
    ${result}   read_results
    Set global variable    ${result}

The scientific calculator result is read
    ${result}   read_sci_results
    Set global variable    ${result}

The result is asserted for test case sum two numbers
    assert_result   ${result}   ${expected_result_tc1}

The divide sign is clicked
    click_symbol    divide

The result is asserted for test case divide two numbers
    assert_result   ${result}   ${expected_result_tc2}

The asterix is clicked
    click_symbol    multiply

The equals symbol is clicked
    click_symbol    equal

The result is asserted for the test case multiply two numbers
    assert_result   ${result}   ${expected_result_tc3}

The result is asserted for the test case subtract two numbers
    assert_result   ${result}   ${expected_result_tc4}

The result is asserted for the test case multiply four numbers
    assert_result   ${result}   ${expected_result_tc5}

The result is asserted for the test case calculate the log a number
    assert_result   ${result}   ${expected_result_tc6}

The result is asserted for the test case read the number pi
    assert_result   ${result}   ${expected_result_tc7}

The result is asserted for the test case bring number to the 2nd power
    assert_result   ${result}   ${expected_result_tc8}

The result is asserted for the test case calculate the sin of a number
    assert_result   ${result}   ${expected_result_tc9}

The result is asserted for the test case convert celsius to fahrenheit
    assert_result   ${result}   ${expected_result_tc10}

A number is typed
    [Arguments]  ${first_keytype}
    type_keys_keyboard  ${first_keytype}

The minus sign is clicked
    click_symbol    minus

Another number is typed
    [Arguments]  ${third_number}
    type_keys_keyboard  ${third_number}

The log button is pressed
    click_scientific_symbol_button    logBase10Button

Set Calculator to
    [Arguments]  ${calculator_type}
    click_calculator_type_menu
    change_calculator_type  ${calculator_type}

Pi is clicked
    click_symbol    pi

The x2 symbol is clicked
    click_sec_power_button

The Trigonometry button is clicked
    click_symbol    trig

The sin button is clicked
    click_symbol    sin

The source temperature UoM is set to
    [Arguments]  ${s_temp_uom}
    click_uom   Units1
    click_converter_type    ${s_temp_uom}

The target temperature UoM is set to
    [Arguments]  ${t_temp_uom}
    click_uom   Units2
    click_converter_type    ${t_temp_uom}

The converter result is read
    ${result}=      read_converter_input_2
    Set global variable     ${result}