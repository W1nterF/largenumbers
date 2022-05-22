# Large numbers

#### Technical task:
+ Using one of the existing libraries (you can make it yourself, but it's better to use the existing one to save time), print the number of key options that can be set 8-, 16-, 32-, 64-, 128-, 256-, 512- , 1024-, 2048-, 4096-bit sequence. *Example:* If the key length is 16 bits, then the key space is 65536. The keyspace is the number of unique keys that are in the given range.
+ For each of the options, it is necessary to generate a random key value that belongs to the range from 0x00…0 to 0xFF…F, depending on the selected key length.
+ Write a function to brute force values ​​from a range to find a key. The purpose of the function is to iterate over the key values from 0x00...0 until a value is found that is equal to the pre-generated key. The function should output the amount of time, in milliseconds, that it took to find the key.


# Program description
After starting, the program calculates the number of key options using the formula $2^n$, where $n$ is the length of the key in bits.
**Screenshots do not contain a full report on the program in order to save space!**
![Example](https://user-images.githubusercontent.com/47121348/169697147-8f7ccb9a-6fb0-49f6-a42d-a101edeb3cdf.png)


The program then generates the keys. I used a pseudo-random sequence generator for **educational purposes (and only for them)**.
![Example](https://user-images.githubusercontent.com/47121348/169697206-c5c4608d-a19d-486c-9101-9a7605113ca3.png)

