*** Settings ***
Library         proj_lib/SetupTeardown.py
Suite Setup     setup_suite
Suite Teardown  teardown_suite
Resource        helper_kw.robot
Resource        keywords.robot

*** Test Cases ***
Sum two numbers
    [Documentation]       https://trello.com/c/8cWgKHQZ/1-tc1-sum-two-numbers
    When A number is clicked     ${first_number}
    And The plus sign is clicked
    And Another number is clicked   ${second_number}
    And The equals symbol is clicked
    When The result is read
    Then The result is asserted for test case sum two numbers

Divide two numbers
    [Documentation]     https://trello.com/c/fQxu0Y7Y/2-tc2-divide-two-numbers
    When A number is clicked    ${first_number}
    And The divide sign is clicked
    And Another number is clicked   ${second_number}
    And The equals symbol is clicked
    When The result is read
    Then The result is asserted for test case divide two numbers

Multiply two numbers
    [Documentation]     https://trello.com/c/bBhmkZo7/3-tc3-multiply-two-numbers
    When A number is typed  ${first_keytype}
    And The asterix is clicked
    And Another number is typed  ${second_keytype}
    And The equals symbol is clicked
    When The result is read
    Then The result is asserted for the test case multiply two numbers

Subtract two numbers
    [Documentation]     https://trello.com/c/ykAM5cme/4-tc4-subtract-two-numbers
    When A number is clicked     ${first_number}
    And The minus sign is clicked
    And Another number is clicked   ${second_number}
    And The equals symbol is clicked
    When The result is read
    Then The result is asserted for the test case subtract two numbers

Multiply four numbers
    [Documentation]     https://trello.com/c/jpH9Tvgu/7-tc5-multiply-4-numbers
    When A number is clicked    ${first_number}
    And The asterix is clicked
    And a number is typed   ${second_number}
    And The asterix is clicked
    And Another number is typed  ${third_number}
    And The asterix is clicked
    And Another number is clicked  ${fourth_number}
    And The equals symbol is clicked
    When The result is read
    Then The result is asserted for the test case multiply four numbers

Calculate the log of a number
    [Documentation]  https://trello.com/c/SrxJZJCQ/6-tc6-calculate-the-log-of-a-number
    [Setup]  Set Calculator to  ${calculator_type}
    When A number is clicked  ${log_number}
    And The log button is pressed
    When The result is read
    Then The result is asserted for the test case calculate the log a number
    [Teardown]  Set Calculator to  Standard

Read the number pi
    [Documentation]  https://trello.com/c/L9kZmba6/5-tc7-read-the-number-pi
    [Setup]  Set Calculator to  ${calculator_type}
    When Pi is clicked
    When The scientific calculator result is read
    Then The result is asserted for the test case read the number pi
    [Teardown]  Set Calculator to  Standard

Bring number to the 2nd power
    [Documentation]  https://trello.com/c/rVLnP8Fu/8-tc8-bring-number-to-the-2nd-power
    [Setup]  Set Calculator to  ${calculator_type}
    When A number is typed  ${x2number}
    And The x2 symbol is clicked
    When The scientific calculator result is read
    Then The result is asserted for the test case bring number to the 2nd power
    [Teardown]  Set Calculator to  Standard

Calculate the sin of a number
    [Documentation]  https://trello.com/c/6exygbed/9-tc9-calculate-the-sin-of-a-number
    [Setup]  Set Calculator to  ${calculator_type}
    When A number is typed  ${for_sin_number}
    And The Trigonometry button is clicked
    And The sin button is clicked
    When The scientific calculator result is read
    Then The result is asserted for the test case calculate the sin of a number
    [Teardown]  Set Calculator to  Standard

Convert Celsius to Fahrenheit
    [Documentation]  https://trello.com/c/JWCbokho/10-tc10-convert-celsius-to-fahrenheit
    [Setup]  Set Calculator to  ${calculator_type_conv}
    When The source temperature UoM is set to   ${s_temp_uom}
    And The target temperature UoM is set to    ${t_temp_uom}
    And A number is typed  ${conv_num}
    When The converter result is read
    Then The result is asserted for the test case convert celsius to fahrenheit
    [Teardown]  Set Calculator to  Standard