Feature: Generate Parameter file parameter objects as a set
    In order to generate a collection of parameter objects
    As a parameter object factory
    I want to consume a valid parameter template file,
    extract all items in the "parameters" property of the file,
    convert each parameter into an object with a name, type, value, and example property
    Scenario: Parameter object generation
        Given I am generating parameter objects
            |  parameterSet|
        When I iterate through the parameterSet passed in
            Then I create a Parameter object, per item within the parameterSet
            Then I will store the Parameter objects in an ordered collection of parameter objects 
            Then I yield the collection of the collection of parameters