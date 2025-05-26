*** Settings ***
Library     BuiltIn
*** Variables ***

${value}        10

*** Keywords ***
Is Even
    [Arguments]    ${number}
    ${remainder}=    Evaluate    ${number} % 2
    Run Keyword If    ${remainder} == 0    Log    ${number} is even
    ...    ELSE    Log    ${number} is odd

*** Test Cases ***
TEST RUN KEYWORD EXAMPLE
    Run Keyword If    ${value} > 5    Log    The value is greater than 5
    Run Keyword If    ${value} < 5    Log    The value is less than 5
    Run Keyword If    ${value} == 10   Log    The value is exactly 10

Run Keyword If With Else
    ${x}=    Set Variable    20
    Run Keyword If    ${x} < 10    Log    Less than 10
    ...    ELSE IF    ${x} == 20    Log    Equal to 20
    ...    ELSE    Log    Something else

Multiple Actions If True
    ${num}=    Set Variable    5
    Run Keyword If    ${num} > 3    Run Keywords
    ...    Log    Number is greater than 3
    ...    AND    Log    Doing more things because it's true

Using Else If And Else
    ${age}=    Set Variable    18
    Run Keyword If    ${age} < 13    Log    Child
    ...    ELSE IF    ${age} < 20    Log    Teenager
    ...    ELSE    Log    Adult

Check Even Or Odd
    Is Even    8

Return Example
    ${x}=    Set Variable    100
    ${result}=    Run Keyword If    ${x} == 100    Return From Keyword    100 is OK
    Log    ${result}

Nested Run Keyword If
    ${x}=    Set Variable    10
    Run Keyword If    ${x} > 5
    ...    Run Keyword If    ${x} == 10    Log    Exactly 10
