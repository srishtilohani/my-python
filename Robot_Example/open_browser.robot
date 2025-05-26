*** Settings ***
Library    SeleniumLibrary
Suite Setup     Open Browser Example
Suite Teardown      Close Browser


*** Variables ***
${BROWSER}    chrome
${URL}        https://www.google.com

*** Keywords ***
Open Browser Example
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s


*** Test Cases ***
Open Browser To Check Anythings
    Log To Console     login
