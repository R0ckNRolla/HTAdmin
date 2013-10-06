import glob
import base64


# Encode all the .png files in the current directory as base64 and write
# the output to 'base64-output.txt'

outputfd = open( 'base64-output.txt', 'w' )

for f in glob.glob( "*.png" ):

	with open( f, 'rb' ) as i:
		encodedImage = base64.b64encode( i.read() )
		outputfd.write( f + '\n' )
		outputfd.write( str(encodedImage) + '\n\n' )

outputfd.close


