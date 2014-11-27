Feature: Google simple query

  Scenario: query for python
     Given main page loaded
      When type "python" and press enter
      Then results page should have "Welcome to Python.org" link

  Scenario: query for starcraft
     Given main page loaded
      When type "starcraft" and press enter
      Then results page should have "Site oficial de StarCraft II - Battle.net" link
