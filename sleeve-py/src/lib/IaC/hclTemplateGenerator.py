import json
import jinja2

''' 
Goals of this:
- Create scripted process of generating Hashicorp Configuration Language files
- Produce a template( Jinja2 for PoC ), for creating new Hashicorp product configurations
- Test for the QA cases( Functional )
 
Not Goals of this:
- Testing integration into CD Pipeline( Let's allow Powershell, VSTS to handle that )
'''

class hclTemplateGenerator( dict ):
""" 
ARM Parameter file generator. Contains a list of values to be inserted into a given parameter file

name(string): the name of the resource, composed of resourceType, enviornmentTier, businessRegion
resourceType(string): The type of resource, according to the Azure ARM Spec
enviornmentTier(string): The envirionment this parameter file applies to
businessRegion(string): The region we are deploying the resource to

parameters(dict): a dictionary of parameters, where each parameter may be a `atomic` or `composite` complexity

Construction flow:
- Compose configurations for necessary Hashicorp tools
- Validate configuration object schema against HCL spec
- Create new json file with Jinja
"""

    
# Base class values, organizaed by Resource Type name( according to Templates Directory of repo )
    def generateParamFile( self ):
    # Generates the parameter file, according to the contents of our properties
        pass


    def getEnvironmentStub(self):
    # Retrieves a stub to insert into various ARM Template Parameter values.
        pass


    def getRegionStub(self):
    # Retrieves a stub...
        pass 


    def __init__( self, resourceType, environmentTier, businessRegion ):
    # Basic introspection of constructor kwargs / setting instance properties
        if isinstance( resourceType, basestring ):
            self._resourceType = resourceType
        if isinstance( environmentTier, basestring ):
            self.envirionmentTier = environmentTier
        if isinstance( businessRegion, basestring ):
            self.businessRegion = businessRegion
    
    # Set the inital container for parameter injection
        if isinstance( baseParameters, dict ):
            try:
                for value in baseParameters["resourceType"].values():
                    if resourceType == value
                        self.parameters = baseParameters["resourceType"][resourceType]
                        break
                    else:
                        # raise Exception
                        raise ValueError
            except( ValueError, TypeError ):
                print( "Invalid data type or value used, let's try again" )        