# Eavesdrop (300 Pts)

### Description
> Download this packet capture and find the flag.

### Hints
- All we know is that this packet capture includes a chat conversation and a file transfer.

Opening the `.pcap` file with Wireshark and following the TCP stream reveals a chat conversation.
```
Hey, how do you decrypt this file again?
You're serious?
Yeah, I'm serious
*sigh* openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123
Ok, great, thanks.
Let's use Discord next time, it's more secure.
C'mon, no one knows we use this program like this!
Whatever.
Hey.
Yeah?
Could you transfer the file to me again?
Oh great. Ok, over 9002?
Yeah, listening.
Sent it
Got it.
You're unbelievable

```
What's important here apart from the decryption command is that they did the file transfer between "Yeah, listening." and "Sent it". Looking back at Wireshark this means that the file packet is somewhere between Packet No. 52 and Packet No. 59. In Packet No. 57, we see something interesting.
```
'Îs'¯9Ed¬@@uñ

Ü2#*^¢Ç@_Tmöi
Ñ§ôiAgSalted__e`XWó2çA»Ä(VRj:¯{ý*<nÔB[WÜ¾ûÞ_`j
```
The thing that started with "Salted" is the encrypted message they were talking about. Now copy the message (starting from "Salted...") as bytes into a file called `file.des3`. Running the decryption command `openssl des3 -d -salt -in file.des3 -out file.txt -k supersecretpassword123`, we get the flag. 

flag: `picoCTF{nc_73115_411_445e5629}`