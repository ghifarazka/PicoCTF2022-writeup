# morse-code (100 Pts)

### Description
> Morse code is well known. Can you decrypt this? Download the file here. Wrap your answer with picoCTF{}, put underscores in place of pauses, and use all lowercase.

### Hints
- Audacity is a really good program to analyze morse code audio.

I tried using [online decoder](https://morsecode.world/international/decoder/audio-decoder-expert.html) the first time and it failed. I then tried looking up on Audacity and do it by hand and also failed. So, I went back to the online decoder, and realized that it gives different results everytime you try to decode it. I input the file again and try decoding it until I get a message that make sense and sounds like a good English.

Here are some of the failed attempts by the way.
```
EMH47 H47H 90D W9H7
WH47 H47H 90D W20U9
WH47 H47H 9ÑDS20U9H7
WH47H47HÐ0DU20U9H7
WH55 H47H 90D W20U9H
```
The correct one was `WH47 H47H 90D W20U9H7`.

flag: `picoCTF{wh47_h47h_90d_w20u9h7}`