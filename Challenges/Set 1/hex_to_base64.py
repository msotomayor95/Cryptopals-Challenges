import sys
import codecs
import base64

string = sys.argv[1].encode('utf-8')
decoded_string = codecs.decode(string, "hex")
print(base64.b64encode(decoded_string))