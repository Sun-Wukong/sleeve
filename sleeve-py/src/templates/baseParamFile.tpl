{
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        {{ armR.CDNProfile.parameters }}
        
        "CDNProfile": {
            "value": "cdnstaticspauk1"
        },
        "CDNLocation": {
            "value": "NorthEurope"
        },
        "Endpoints": {
            "value": [
                {
                    "name": "account-staticspa-prod-uk",
                    "originPath": "/account",
                    "originHost": "prod-account-staticspa.trafficmanager.net"
                },
                {
                    "name": "expert-staticspa-prod-uk",
                    "originPath": "/expert",
                    "originHost": "prod-account-staticspa.trafficmanager.net"
                },
                {{ endpoint in armR.CDNProfile.endpoints }}
            ]
        }
    }
}