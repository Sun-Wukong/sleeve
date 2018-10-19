from './src' import armParamGenerator

if __name__ == '__main__':
    try:
        myArmPrmGen = armParamGenerator()
        print( "Generating ARM Resource Parameter file" )
        myArmPrmGen.generateParameterFile()
    except:
        print( "Unforseen Error, backing out now" )
