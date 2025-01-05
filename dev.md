# inital pi setup
start by scanning ur network for pi's ip
```bash
ip a
```
look for inet 192.168.X.X/XX

```bash
sudo nmap 192.168.1.0/24

```
now just grab the ip of the pi using its mac address
vid tutorial- https://www.youtube.com/watch?v=1t3vCc-hlNg

# connecting to pi
```bash
ssh neb@192.168.1.5
```

neb is the name I selected for pi while installing its os on sd card and  192.168.1.5 is the ip i got from scanning my network


## recording audio using pi
connect usb mic to the pi

```bash
arecord -l
```
This will list all the devices available for recording audio

```bash
arecord -D hw:3,0 -f S16_LE -t wav -d 10 -r 44100 -c 1 test.wav
```
this command will record a 10sec audio file and save it as test.wav in pwd


