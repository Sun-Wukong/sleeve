Feature: Generate ARM Template Parameter file
    In order to generate a parameter file for an ARM resource
    As a reader of a parameter file
    I want parameter file represented as a plain object
    according to either an imported file or constrictor function 

    Scenario: ARM Template Parameter file generation via class constructors
        Given I am creating a parameter file programatically
            |name                                                        |  properties|
        When I create a new parameter file factory object
            Then I add all parameter objects to a queued set of parameters
            Then I will store any unique parameters in a collection of scaffolds, according by name 
            Then I read and copy the most recent scaffold file, or a default
            Then I dequeue and push the queued parameter objects to the scaffold file copy
            Then I create a JSON file to be validated by Azure CLI
            Then I call Azure CLI to validate my template / parameter file combination
            Then the updated file is copied to a target location
         

    Scenario: ARM Template Parameter file generation via file import + append
        Given I am creating a new parameter file via file import
            
        When I create a new parameter file factory object
            Then I will provide a parameter file to create a scaffold
            Then I will create a copy of the parameter file
            Then I will copy a collection of parameters within the file, retaining all parameters with unique keys
            Then for each unique parameter, I will convert it's property values to the value's type, per property type
            Then I provide the parameter values I would like to update the file with as ParamProperty objects
            Then I evaluate the ParamProperty object, appending it to the parameter file copy, if valid
            Then I create a JSON file to be validated by Azure CLI
            Then I call Azure CLI to validate my template / parameter file combination
            Then the updated file is copied to a target location


Feature: Updating an ARM Template Parameter file
    In order to update a parameter file for an ARM resource
    As a reader of a parameter file
    I want a parameter file represented as a plain object
    according to either an imported file or constructor function 
    Scenario: Overwriting values within a parameter file
        Given I have successfully loaded in a JSON parameter file
            |uri                                                        |  mls|             
        When I choose to update the parameter file from the CLI
            Then I select the parameter name I want to update
                But if the selected parameter holds a singular value
                    Then I provide the new value to update the parameter
                    Then I continue with the update process
                But if the selected parameted holds a nested value
