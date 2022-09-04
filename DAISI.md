
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


#### Screenshots:
Testing - Integer Values:

<img width="1018" alt="Screenshot 2022-09-04 at 2 42 11 PM" src="https://user-images.githubusercontent.com/112493795/188306234-37f20e28-1f63-4f35-972f-10a6e8dc2dc9.png">

Testing - Float Values:
<img width="1018" alt="Screenshot 2022-09-04 at 2 32 34 PM" src="https://user-images.githubusercontent.com/112493795/188306208-e31539a4-6c6b-43c4-9f95-d0d7d54edd5c.png">


#### Conclusion:

This function will be used in data compression, encode and decode algorithm.Similar kind of functions are available in market but those are not help us for data compression. this function will helpful for data compression.We can use this function for integer and float values.
#### This function is reducing your data and saving approx 50% of space and cost.



