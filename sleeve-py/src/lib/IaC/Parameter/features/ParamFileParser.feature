Feature: Ingesting Parameter file
    In order to consume and parse parameter files
    As a reader of a parameter file
    I want parameter files to be in JSON / YAML format
    The file needs to have a "parameters" property

    Scenario: Parameter file ingest
        Given I am creating a parameter file programatically
            |name         |  properties|
        When I create a new parameter file factory object
            Then I add all parameter objects to a queued set of parameters
            Then I will store any unique parameters in a collection of scaffolds, according by name 
            Then I read and copy the most recent scaffold file, or a default
            Then I dequeue and push the queued parameter objects to the scaffold file copy
            Then I create a JSON file to be validated by Azure CLI
            Then I call Azure CLI to validate my template / parameter file combination
            Then the updated file is copied to a target location