
### Convert Base10 to Base64 or Base10 to Base64

Base64 is an encoding method for handling multibyte characters and binary data in a communication environment that uses only 64 types of printable alphanumeric characters and cannot handle other characters 

Since this encoding greatly increases the amount of data, especially when sending and receiving large files, it may be much faster to use means other than e-mail. Also, for text sentences in which special characters are mixed in English, data efficiency is better if only the special characters are encoded, and there is an advantage that most of the data can be read without decoding.

Please refer this link https://ja.wikipedia.org/wiki/Base64 for more details 

#### How will use this function?

##### STEP 1: 
import pydaisi as pyd

base10_to_base64 = pyd.Daisi("chinnappar/base10_to_base64")

##### STEP 2: (Parameter 1: Pass the Base10 integer or float value and Parameter 2: Pass "f" char if your are passing floating value)

base10_to_base64.base64_to_base10(b64dec, datatype=None).value

##### STEP 3: (Parameter 1: Pass the Base64 integer or float value and Parameter 2: Pass "f" char if your are passing floating value)

base10_to_base64.base10_to_base64(decimal, datatype=None).value


#### Conclusion:

This function will be used in data compression, encode and decode algorithm and this is reduce the characters and save approx 50% of space and cost.


