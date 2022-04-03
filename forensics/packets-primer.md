# Packets Primer (100 Pts)

### Description
> Download the packet capture file and use packet analysis software to find the flag.

### Hints
- Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

We were given a `.pcap` file. Looking into the file with Wireshark, we can see some packets with TCP protocol. Following the TCP stream, we get the flag.

flag: `picoCTF{p4ck37_5h4rk_d0565941}`