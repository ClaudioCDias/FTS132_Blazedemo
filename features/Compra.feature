@compra_passagem
Feature: Compra de Passagem Aérea
  # Descreve a compra pelo site Blazedemo.com
  # E2E = End to End = Início a Fim, etc
  Scenario: De São Paulo a Roma
    Given que acesso o site Blazedemo
    When seleciono a origem como "São Paolo"
    And seleciono a cidade de destino "Rome"
    And clico no botão Find Flights
    Then sou direcionado para a página de seleção de vôos
    When seleciono o primeiro vôo
    Then sou direcionado para a página de pagamento
    When preencho os dados para o pagamento
    And clico no botão Purchase Flight
    Then sou direcionado para a página de confirmação

  Scenario: De São Paulo a Roma Compacto
    Given que acesso o site Blazedemo
    When seleciono de "São Paolo" para "Rome"
    Then sou direcionado para a página de seleção de vôos
    When seleciono o primeiro vôo
    Then sou direcionado para a página de pagamento
    When preencho os dados para o pagamento
    And clico no botão Purchase Flight
    Then sou direcionado para a página de confirmação