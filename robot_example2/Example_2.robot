*** Settings ***
Resource        setup_file.robot
Suite Setup         Login to Environment


*** Test Cases ***
Checking The Printing OF Variable
    Set Test Variable    ${test_variable}   testvarialbe1
    Log To Console      ${test_variable}
    Log To Console    ${test_variable}
    Log To Console    ${LOGIN_URL}
    Log To Console    ${large_wait}