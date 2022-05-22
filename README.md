# Large numbers

#### Technical task:
+ Using one of the existing libraries (you can make it yourself, but it's better to use the existing one to save time), print the number of key options that can be set 8-, 16-, 32-, 64-, 128-, 256-, 512- , 1024-, 2048-, 4096-bit sequence. *Example:* If the key length is 16 bits, then the key space is 65536. The keyspace is the number of unique keys that are in the given range.
+ For each of the options, it is necessary to generate a random key value that belongs to the range from 0x00…0 to 0xFF…F, depending on the selected key length.
+ Write a function to brute force values ​​from a range to find a key. The purpose of the function is to iterate over the key values from 0x00...0 until a value is found that is equal to the pre-generated key. The function should output the amount of time, in milliseconds, that it took to find the key.


# Program description
After starting, the program calculates the number of key options using the formula $2^n$, where $n$ is the length of the key in bits.

**Screenshots do not contain a full report of the program in order to save space!**

![Example](https://user-images.githubusercontent.com/47121348/169698195-5744c7bb-5c52-4e40-ba55-3544c4568b70.png)

The program then generates the keys. I used a pseudo-random sequence generator for **educational purposes (and only for them)**.

![Example](https://user-images.githubusercontent.com/47121348/169697206-c5c4608d-a19d-486c-9101-9a7605113ca3.png)


Brute force of the key starts from 0 and up to the maximum value within the given limits.

![Example](https://user-images.githubusercontent.com/47121348/169697313-177a92e1-3568-409d-9c4d-abd10d57ccac.png)


The screenshot shows that the 8-bit key was guessed in less than 1 millisecond, the 16-bit key took 15 milliseconds.
The 32-bit key was guessed in 273265 milliseconds (4 minutes 33 seconds).

To select a 64-bit key, it will take twice as much time, and so on.

Unfortunately, the brute force cycle will not be able to reach its logical end, as the time to select all 10 generated keys is approaching infinity.

**It is clearly seen how quickly the required time began to increase with increasing key length.**

*We can conclude that passwords containing less than 8-10 characters are not strong. Increasing the key length, using different registers, special characters, will increase the required time to guess your key!*
