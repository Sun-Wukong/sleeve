import behave
import json

@given( 'We have an existing file for the target environment' )

@when( 'We load our parameter file, we can locate the values for the "websites.values" parameter' )

@then( 'We generate new value objects, appending them to the "website.values" list key' )

@given( 'We finished adding new values, we may create a JSON object' )

@when( 'We create a new json file, we test it against Azure Template tools' )

@then( 'We copy the file to a "Collateral" folder' )