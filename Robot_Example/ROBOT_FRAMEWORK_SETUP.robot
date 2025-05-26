*** Settings ***
Library         SeleniumLibrary
Library         RequestsLibrary

*** Variables ***
${URL}      https://robotframework.org/#getting-started
${PAGE_TILTLE}
${CHROME_BROWSER}       chrome
${PAGE_TITLE}           ROBOT FRAMEWORK
${GET_API_URL}          https://jsonplaceholder.typicode.com
${get_endpoint}         /todos/1

*** Keywords ***
OPEN THE BROWSER AND VALIDATE THE HOMEPAGE
    Open Browser        ${URL}          ${CHROME_BROWSER} 
    Page Should Contain    ${PAGE_TITLE}
    Location Should Be    ${URL}

GET API CALL
    [Arguments]         ${api}      ${api_end_point}
    ${response}=    GET    ${api}${api_end_point}
    ${json}=    To Json    ${response.content}
    Set Suite Variable    ${response}
    Set Suite Variable    ${json}

POST API CALL
    [Arguments]     ${api}      ${api_end_point}        ${RESPONSE_BODY}
    ${payload}=    Create Dictionary    title=Robot Test    body=This is a test post.    userId=101

    ${headers}=    Create Dictionary    Content-Type=application/json

    ${response}=    POST   ${api}${api_end_point}      json=${payload}    headers=${headers}
    Should Be Equal As Strings    ${response.status_code}    201

    ${resp_body}=    Evaluate    ${response.json()}    modules=requests
    Log    ${resp_body['title']}
    Should Be Equal As Strings    ${resp_body['title']}    Robot Test


*** Test Cases ***
LOGIN INTO THE ENV
    OPEN THE BROWSER AND VALIDATE THE HOMEPAGE

VALIDATE API CALL
    GET API CALL        ${GET_API_URL}  ${get_endpoint}
    Should Be Equal As Strings    ${response.status_code}    200
    Log    ${json['title']}
    Should Be Equal As Strings    ${json['title']}    delectus aut autem