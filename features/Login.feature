@Login
Feature: Login
  Scenario: Login com Sucesso
    Given que acesso o site Blazedemo
    When clico em home
    And preencho "<email>" "<senha>" e clico no botão Login
    Then visualizo a mensagem de confirmação