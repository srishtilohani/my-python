*** Settings ***

*** Variables ***
${global_var}      global_var
*** Test Cases ***

test case 1
    [Tags]      123
    Set Suite Variable    ${suite_var}  suite_var1
    Set Suite Variable    ${global_var}  global_var_updated
    Set Test Variable    ${test_var}  test_varl_1
    Log To Console    ${suite_var}      #   Log 1
    Log To Console    ${global_var}    #   Log 2
    Log To Console     ${test_var}    #   Log 3

test case 2
    [Tags]      123
    Set Suite Variable    ${SUITEVAR}    suite_var13e23
    Log To Console    ${suite_var}    #   Log 4
    Log To Console    ${global_var}    #   Log 4
#    Log To Console     ${test_var}    #   Log 5
