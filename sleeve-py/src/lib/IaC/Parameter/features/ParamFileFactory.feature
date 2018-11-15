Feature: Generate Template Parameter file via factory builders
    In order to generate template parameter files
    As parameter file generator
    I want to ingest a given JSON file, representing a set of deployment parameters
    I want to extract the parameter values, modifying them as needed
    I want to write the updated values into a copy of a file template
    I want the file template to be deployed as a new parameter file


    Scenario: Parameter file generation
        Given I am generating a parameter file programatically
            |name                                                        |  properties|
        When I need to produce a brand new parameter file
            Then I create a file reader
            Then I create a file writer
            Then I create a parameter object factory
            Then I produce as many parameters as needed
            Then I write a parameter file to a directory
