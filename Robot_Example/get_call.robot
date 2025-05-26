*** Settings ***
Library     RequestsLibrary

*** Variables ***
${URL}          https://petstore.swagger.io/v2/store/
${INVENTORY_STORE_END_POINT}        inventory
${SCUESS_STATUS_CODE}               200
${ORDER_ID_END_POINT}               order/1

*** Keywords ***

GET CALL API
    [Arguments]        ${URL}       ${api_endpoint}
    ${response}=    Get    ${URL}${api_endpoint}
    ${json}=    To Json    ${response.content}
    Should Be Equal As Strings    ${response.status_code}    ${SCUESS_STATUS_CODE}
    Log To Console    ${json}
    Set Suite Variable    ${response}
    Set Suite Variable    ${json}

DELETE API CALL
    [Arguments]        ${URL}       ${api_endpoint}
    ${response}=    DELETE    ${URL}${api_endpoint}
    ${json}=    To Json    ${response.content}
    Should Be Equal As Strings    ${response.status_code}    ${SCUESS_STATUS_CODE}
    Log To Console    ${json}
    Set Suite Variable    ${response}
    Set Suite Variable    ${json}

*** Test Cases ***
Validate The Get Store Inventory
    GET CALL API        ${URL}      ${INVENTORY_STORE_END_POINT}
    Should Be Equal As Strings    ${json['AVAILABLE']}    6

Validate The Get store Order ID
    GET CALL API        ${URL}      ${ORDER_ID_END_POINT}
    Should Be Equal As Strings    ${json['id']}    1
    Should Be Equal As Strings    ${json['status']}    placed

Validate The Delete Order ID
    DELETE API CALL        ${URL}      ${ORDER_ID_END_POINT}
    Should Be Equal As Strings    ${json['message']}    1
    Should Be Equal As Strings    ${json['code']}    ${SCUESS_STATUS_CODE}
