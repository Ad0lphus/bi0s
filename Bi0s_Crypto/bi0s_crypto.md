**Intro1**

Just copy pasted the flag

**Intro2- GREAT SNAKES**

Just tried to run the py code and got the flag!

**Intro3**

In the py code , "buy": "clothes" to "buy": "flag" and  then tried to run request through the program!

And got the flag

![](bi0s\_crypto.001.png)

**General : encoding** 

**ascii**

using chr I converted the particular number to character and joined all the converted charecters to string to get the flag!

![](bi0s\_crypto.002.png)

**Hex**

I’ve imported unhexlify from binascii module which return the binary data represented by the hexadecimal string.![](bi0s\_crypto.003.png)

**Base64**

To make bytes like object unhexlify from binascii is used And to convert to base64, we can use a library function from base62 i.e b643ncode().




![](bi0s\_crypto.004.png)

**XOR**

**XOR Starter**

Tried to read character by character using for loop and did the xor between the integer value of each character and 13

![](bi0s\_crypto.005.png)

**o/p**

![](bi0s\_crypto.006.png)

