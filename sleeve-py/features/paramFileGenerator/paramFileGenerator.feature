Feature: Generate ARM Template Parameter file
    In order to generate a parameter file for an ARM resource
    As a reader of a parameter file
    I want parameter file represented as a plain object
    according to either an imported file or constrictor function 

    Scenario: ARM Template Parameter file generation via class constructors
        Given the MLS data source is able to be scrubbed
            |uri                                                        |  mls|
            |https://5436b264-b5b0-434f-8fe7-9301c3b4de79.mock.pstmn.io/|REBNY|
            |https://dade36c9-2cce-4bc9-ad08-f92bc7d69b08.mock.pstmn.io/|GSMLS|
            |https://d4347e55-8214-4e9a-b944-1c737638436c.mock.pstmn.io/|BNYMLS|

             
        When we post a new fullscrub job request
        Then the MLS Listing Scrubber service should return a "Successful" response, with a status code of 200, and a an object

    Scenario: ARM Template Parameter file generation via 
        Given the MLS data source is unable to be scrubbed
            |uri                                                        |  mls|
            |https://5436b264-b5b0-434f-8fe7-9301c3b4de79.mock.pstmn.io/|REBNY|
            |https://dade36c9-2cce-4bc9-ad08-f92bc7d69b08.mock.pstmn.io/|GSMLS|
            |https://d4347e55-8214-4e9a-b944-1c737638436c.mock.pstmn.io/|BNYMLS|
        When we post a new fullscrub job request
        Then the MLS Listing Scrubber service should return an "Unprocessable Entity" response, with a status code of 422

Feature: Updating an ARM Template Parameter file
    In order to update a parameter file for an ARM resource
    As a reader of a parameter file
    I want a parameter file represented as a plain object
    according to either an imported file or constructor function 
    Scenario: Successful post of a full scrub job
        Given the MLS data source is able to be scrubbed
            |uri                                                        |  mls|
            |https://5436b264-b5b0-434f-8fe7-9301c3b4de79.mock.pstmn.io/|REBNY|
            |https://dade36c9-2cce-4bc9-ad08-f92bc7d69b08.mock.pstmn.io/|GSMLS|
            |https://d4347e55-8214-4e9a-b944-1c737638436c.mock.pstmn.io/|BNYMLS|

             
        When we post a new fullscrub job request
        Then the MLS Listing Scrubber service should return a "Successful" response, with a status code of 200, and a an object

    Scenario: Failure to post a full scrub job to the MLS listing scrubber
        Given the MLS data source is unable to be scrubbed
            |uri                                                        |  mls|
            |https://5436b264-b5b0-434f-8fe7-9301c3b4de79.mock.pstmn.io/|REBNY|
            |https://dade36c9-2cce-4bc9-ad08-f92bc7d69b08.mock.pstmn.io/|GSMLS|
            |https://d4347e55-8214-4e9a-b944-1c737638436c.mock.pstmn.io/|BNYMLS|
        When we post a new fullscrub job request
        Then the MLS Listing Scrubber service should return an "Unprocessable Entity" response, with a status code of 422
