Baseconv
========

Converts hexadecimal, decimal and binary numbers into the other bases.

Copyright (c) 2019 Renato Montes, under Apache License 2.0.


Usage
-----

Usage, in the same directory:

        python3 baseconv.py

On Linux, you can set the executable bit on the file. The program is defined to use `/usr/bin/python3` in its first line of code.

        ./baseconv.py

Use `h` after a hexadecimal number, `b` after a binary number, `o` after an octal number. Example converting decimal 91 and hexadecimal 91:

![image showing decimal 91 and hexadecimal 91 converted to the other bases](/readme-img/output-all.png)


Filters
-------

Output filters can be given as an argument to show only some number bases. It is useful to cut down the output.

        #show only hexadecimal
        python3 baseconv.py h

        #show only decimal
        python3 baseconv.py d

        #show only binary
        python3 baseconv.py b

        #show only octal
        python3 baseconv.py o

        #only hexadecimal and decimal
        python3 baseconv.py hd

        #decimal, binary and hexadecimal (not octal)
        python3 baseconv.py dbh

A filter example would be calling the program as `python3 baseconv.py d` to translate IPv4 addresses in hexadecimal to decimal.

![image showing the hex address c0 a8 a5 87 converted to decimal 192.168.3.15](/readme-img/ipv4.png)

In this image, the program converts the hexadecimal IPv4 address `c0 a8 a5 87` to the normal decimal format `192.168.3.15`.



