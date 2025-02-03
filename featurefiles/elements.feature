Feature: select element in demoqa webpage
  Scenario:select element tab
    Given click element tab
    Then verify the element tab

  Scenario:go to the textbox in elements tab
    Given select the textbox
    When enter the textbox fields
    And submit the textbox
    Then verify the textbox

  @checkbox
  Scenario: go to the checkbox in elements tab
    Given select the checkbox
    When choose the checkboxes
    Then verify the checkboxes

  Scenario: go to the radiobutton in elements tab
    Given click the radio button option
    When select the radio button
    Then verify the radio button

  Scenario:go to the webtables in element tab
    Given click the webtables option
    When add user details in webtable
    Then verify user details added or not

  Scenario: go to the buttons in element tab
    Given click the button option
    When double click the button
    Then verify the button is double clicked or not
    When right click the button
    Then verify the right click button
    When clik the button
    Then verify the click button

  Scenario: go to links in element tab
    Given click the link option
    When click the link that direct to new tab
    Then verify the page are open or not
    When open the api call links
    Then verify api links

  Scenario: go to broken links in element tab
    Given click the broken link tab
    When open the valid link
    Then verify the vallid link
    Given open the broken link
    Then verify the broken link