# daglog
a little python project that is like a personal diary, where you can write stuff and then encrypt it using a numeric key, and then decrypt using the inverse key.

commands:
- mklog: creates a log inside logs folder. after the command, you input the name, then the text and then the key.
- rdlog: reads a log from the logs folder. after the command, you input the name and then the key.

usage example:
- mklog
- first_file
- this is the text of this file!!!
- 121241
- 1 #(output saying it worked)
- rdlog first_file
- 0
- #(prints the encrypted text)
- rdlog
- first_file
- -121241
- #(prints the decrypted text)


I wanted to make it a bit hard to use, so only those who knows will be able to do so.
