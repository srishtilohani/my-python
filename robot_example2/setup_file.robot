*** Settings ***

Library     SeleniumLibrary

*** Variables ***
${LOGIN_URL}    https://dfl.${BASE_URL}/login
${large_wait}  60s
${medium_wait}  50s
${small_wait}  15s
${BASE_URL}             wewuwydui
${SELENIUM_BROWSER}
${LoginUsernameInputBox}        hello   srishti     lohani
${LoginUsernameInputBox}        kumari  atul
${LoginPasswordInputBox}
${PASS}
${LoginButton}
${page_title}

*** Keywords ***
Login to Environment
    [Documentation]       This keyword logs into the specified environment using provided credentials.
    [Tags]    Smoke       Regression          ui
    Set Global Variable    ${LOGIN_URL}         globalvariable_update
    Log To Console    ${LOGIN_URL}
    Set Suite Variable    ${large_wait}
    Log To Console    ${large_wait}
    ${hi} =    Set Variable    Hello, world!
    Log To Console    ${hi}
    ${hi2} =    Set Variable    I said: ${hi}
    Log To Console    ${hi2}
    ${var1}    ${var2} =    Set Variable    Hello    world
    Log To Console    ${var1}    ${var2}
    @{list} =    Set Variable    ${LoginUsernameInputBox}            hello   srishti     lohani
#    ${item1}    ${item2} =    Set Variable    ${LoginUsernameInputBox}
#    Log To Console    ${item1}    ${item2}


