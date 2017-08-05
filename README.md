# Todo List
* Research [OpenBTS](http://openbts.org) for use with PlutoSDR
* Research [OpenLTE](http://openlte.sourceforge.net/) for use with PlutoSDR
* OpenCV Image Recognition on top of Tensorflow
* Support PlutoSDR in gr-osmosdr (So gr-scan works out of the box)
* IPv6 tunnel in Chicago
* AWS Certification (All three levels)

[August 5th, 2017](https://github.com/blurbdust/blurbdust.github.io#august-5th-2017)

[August 4th, 2017](https://github.com/blurbdust/blurbdust.github.io#august-4th-2017)

# August 5th, 2017
## Morning Coffee at noon
I still have a ways to go to get this all updated. I need to still go over my plans for distributed computing utilizing all the servers I currently own and can set up (Free AWS instances!) as well as the build log for my NAS. I have the server as well as the drives but I haven't put them in it yet since I was keeping that server as a Tensorflow node for now. I really am not too sure how I want to set it up either. I would like a shell and the ability to run some code on it and I'm not sure if FreeNAS or unRAID supports that. That being said, the hardware I will use is the following.

| Part | Name | Cost |
|------|------|------|
| CPU  | i3-4150 | \* |
| RAM  | 8GB PC3-128000 ECC | \* |
| Hard Drives | 4x 8TB WB Red (shucked) | $640 |
| GPU  | GTX 750 (Just got a GTX 1050Ti) | $30 |

\* This came as one [system](https://www.newegg.com/Product/Product.aspx?Item=2RC-001A-000S2) for $200.

I'm slowly working towards my own homelab. I'd like to be able to spin up a VM whenever from wherever and have the install automated and post install mostly automated. A friend showed me [checkinstall](https://wiki.debian.org/CheckInstall) where I could easily host the package somewhere and use that to facilitate postinstall stuff. I've been paying for VPSs for awhile now and I'd like to free up some of my monthly expenses so hosting my own hardware would be a good way to do that. The only issue is the network though. The same friend has essentially datacenter grade networking capabilities. I won't go into detail about his setup because that's how vulnerabilities can be found. 

Speaking of vulnerabilities, I really want to setup [syskaller](https://github.com/google/syzkaller). One of my life goals is to get a CVE attributed to me. I'd be fine if a computer found it for me since I'd still get all the glory. Who knows, maybe I'll set it up during my free week at my apartment.

Jumping topics yet again, my apartment. My roommate bought a 55" TV for the living room and this year we have two couches so it should be a pretty fun weekend hangout place. I need to get speakers for it though since I will want to keep my big speakers in my room. Actually, maybe I'll go for studio monitors in my room and put the big guys out there? Amazon usually has a certain brand on sale for ~$60 so I will probably do that. That way I also get a little bit more room in my room. I am not sure about a coffee table yet, either in my room or in the living room. I like privacy and sometimes you just want to binge watch a TV show and not have anyone look at you while you're sprawled out on a futon downing the whole bag of chips. (Favorite kind is kettle cooked in case you were wondering.)

# August 4th, 2017
## Merry Christmas everyone. 
Yes in ~~July~~ August. I made yet another blog. This time I fully intend to keep it going or at least edited more than once a year. Why do you have [blurbdust.com](http://blurbdust.com) you ask? Well that's more of a professional blog, like an online resume that also contains my resume. 

## Who are you? What are you doing in my house?
I'm a student in Computer Engineering at Iowa State University. If you're not one of the few people that stay up to date on all things me, (shoutout to those who do, you're great), then you won't know I **really** enjoy breaking things. I purposefully take things apart basically as soon as I get them because it adds a bit of excitement to getting new things. By breaking things I generally learn how they work but not all the time. Since I'm writing this in markdown I can get fancy while still being lazy! So how about a bulleted list of things I like/like to do?

* Python and C programming
* All things AI (Artificial Intelligence)
* SDR (Software Defined Radio)
* Linux Sysadmin and security
* CTFs (Capture the Flag (on a computer not outside))
* [Random challenges on the internet](https://twitter.com/argonne/status/840383280079855616)

~~Once I figure out how I want to structure this page I'll update this again. See you within 6 hours?~~
I think decided how I want to do this. I will make it one giant page where I add in new stuff at the top. With a table of index by date? Nah, we'll do it by day. Linearly within the day with the most recent day at the top. Cool? Cool.

## Do I know you? Have you made something I've used?
Probably not, at least not yet. I got two [PlutoSDRs](http://www.analog.com/en/design-center/evaluation-hardware-and-software/evaluation-boards-kits/adalm-pluto.html) and will be doing a lot of hacking things together to get it working with other things. The standard block provided by Analog Devices for use in GNURadio was broken so I ~~fixed~~ worked around that. See [gr-iio](https://github.com/blurbdust/gr-iio) here. Some of the README from that repo will be copied here so sorry, not sorry. Fun fact, this is the fourth time eating Chinese food within 24 hours. Occasionally I live off fried rice. As far as I'm aware, I got my PkutoSDR very early and not many people have them or have gotten them working yet. Gr-iio lets you use the radio within GNURadio. For those of you who don't know, GNURadio is an open source framework that allows you to connect blocks together to model radios and use them immediately. This is great because it lets you model things and test it instantly, no soldering required. Another thing you can do it see the pretty waterfall of the radio spectrum. Don't believe me?
![](https://i.imgur.com/OS8F2oq.png)

Yes that is Kali Linux. Yes I do need a hacking distro occasionally. I participate in the [Cyber Defense Competition](https://cdc.iseage.org/) at ISU plus basically every major online CTF. No I'm not very good at CTFs but I'm learning and having fun and that's the part that counts, right? I am pretty decent at the CDC though. I like knowing who or what is using a system that I am also using so I've been locking things down for a few years now and somethings are scripted while others aren't because installing things at 3:00am is oh so fun! Sometimes I do it correctly and TSB gets first in the [National Cyber Defense Competition](https://cdc.iseage.org/769-2/).

## What did you have to do in order to get your PlutoSDR working?
Good question. Out of the box gr-iio was installed to the wrong directory or at least was being imported incorrectly. I decided to fix it. So one of the ways I thought I could fix it was by setting the install directory to something else so it's easier to import it. This sort of worked but I was missing "_iio_swig.py" so I pulled a fresh copy of gr-iio, built, installed, then reinstalled my fork and it worked! Copied from my fork of [gr-iio](https://github.com/blurbdust/gr-iio):

First and foremost, let's list dependencies because someone thought listing dependencies was too hard.

```
git clone https://github.com/analogdevicesinc/libiio.git
cd libiio
mkdir build
cd build
cmake ..
make
sudo make install

git clone https://github.com/analogdevicesinc/libad9361-iio.git
cd libad9361-iio
mkdir build
cd build
cmake ..
make
sudo make install
```

Secondly, I had a ton of trouble getting this to compile and then eventually actually running in the latest GNURadio.
The way it is laid out made sense however eventually failed. When installed I could not run the block. 

The error was "ImportError: cannot import name iio".

/usr/local/lib/python2.7/dist-packages/gnuradio/iio did exist and as far as I am aware that is how one would import something from inside a folder. Maybe gnuradio.iio would have worked? ~~I'll test in a bit.~~ Tested, no go.

```
cd /usr/local/lib/python2.7/dist-packages/
sudo cp -r gnuradio/iio/* .
```
But still no luck. Different error libgnuradio-iio.so not being found. Instead of trying to symlink that everywhere I ran in to errors, I instead decided to change the install path from "/usr/local/lib/python2.7/dist-packages/gnuradio/iio" to "/usr/local/lib/python2.7/dist-packages/iio".

```
git clone https://github.com/analogdevicesinc/gr-iio.git
cd gr-iio
mkdir build
cd build
cmake ..
make
sudo make install
cd ..
rm -r build
mv include/gnuradio/iio include/iio
rm -r include/gnuradio
sed -i 's/gnuradio\/iio/iio/g' CMakeLists.txt
sed -i 's/gnuradio\/iio/iio/g' swig/*
sed -i 's/gnuradio\/iio/iio/g' include/iio/*
sed -i 's/gnuradio\/iio/iio/g' lib/*
sed -i 's/gnuradio\/iio/iio/g' python/iio/*
sed -i 's/from\ gnuradio\ import\ iio/import\ iio/g' grc/iio_pluto_sink.xml
sed -i 's/from\ gnuradio\ import\ iio/import\ iio/g' grc/iio_pluto_source.xml
mkdir build
cd build
cmake ..
make
sudo make install
````

Then I was able to get my PlutoSDR working in GNURadio. This is a terrible way of doing it. And I will look into an actual fix instead of a bandaid. One benefit to doing it this is the ability to install only this block from source and not GNURadio itself as with pyBOMBS so it'd be possible to use a prebuilt GNURadio like on a RPi. Or if you are like me and have a lot of issues with pyBOMBS.

## What are you doing tonight and or what is next?
I may make an up to date list of everything I want to do/make and cross things off when/if I accomplish the task or not. Tonight I have been writing a script to dump the whole frequency range of the PlutoSDR to a file and then modifying [gr-scan](https://github.com/blurbdust/gr-scan) to look through the file for center frequencies so I can look at them later. Actually yeah I will make a list because it'd feel good to cross things off the list. It actually uses two scripts: one is auto generated from GNURadio and the other was written (and partially generated) by me. Partially generated? Yeah sometimes I get ~~lazy~~ efficient and write another script to write part of a different script.

gen_freq.py generates the frequency list.
```
max = 3800 # 3.8GHz
min = 325 # 325 MHz
step = 20 # 20 MHz
freq = []
while (min < max):
	freq.append(str(min) + "000000") # Append zeros to go to Hz
	min = min + step
print("freq = " + str(freq).replace('\'', '')) #If you want this to be ints. It is replacing all ' with nothing
#print("freq = " + str(freq)) #If you want this to be strings.
print(len(freq))
```
auto_scan.py is a bit large since it's generated from the GNURadio flow graph so I included it [here](PlutoSDR/scripts/auto_scan.py)

scan.py takes the generated list (copy pasted, nothing fancy) and then calls auto_scan.py in the worst way possible, a system call. Kids, don't try this at home. At least not the system call because seriously this is bad for security. Make sure scan.py and auto_scan.py are in the same directory.
```
import time, sys, os
from subprocess import call
freq = ['325000000', '345000000', '365000000', '385000000', '405000000', '425000000', '445000000', '465000000', '485000000', '505000000', '525000000', '545000000', '565000000', '585000000', '605000000', '625000000', '645000000', '665000000', '685000000', '705000000', '725000000', '745000000', '765000000', '785000000', '805000000', '825000000', '845000000', '865000000', '885000000', '905000000', '925000000', '945000000', '965000000', '985000000', '1005000000', '1025000000', '1045000000', '1065000000', '1085000000', '1105000000', '1125000000', '1145000000', '1165000000', '1185000000', '1205000000', '1225000000', '1245000000', '1265000000', '1285000000', '1305000000', '1325000000', '1345000000', '1365000000', '1385000000', '1405000000', '1425000000', '1445000000', '1465000000', '1485000000', '1505000000', '1525000000', '1545000000', '1565000000', '1585000000', '1605000000', '1625000000', '1645000000', '1665000000', '1685000000', '1705000000', '1725000000', '1745000000', '1765000000', '1785000000', '1805000000', '1825000000', '1845000000', '1865000000', '1885000000', '1905000000', '1925000000', '1945000000', '1965000000', '1985000000', '2005000000', '2025000000', '2045000000', '2065000000', '2085000000', '2105000000', '2125000000', '2145000000', '2165000000', '2185000000', '2205000000', '2225000000', '2245000000', '2265000000', '2285000000', '2305000000', '2325000000', '2345000000', '2365000000', '2385000000', '2405000000', '2425000000', '2445000000', '2465000000', '2485000000', '2505000000', '2525000000', '2545000000', '2565000000', '2585000000', '2605000000', '2625000000', '2645000000', '2665000000', '2685000000', '2705000000', '2725000000', '2745000000', '2765000000', '2785000000', '2805000000', '2825000000', '2845000000', '2865000000', '2885000000', '2905000000', '2925000000', '2945000000', '2965000000', '2985000000', '3005000000', '3025000000', '3045000000', '3065000000', '3085000000', '3105000000', '3125000000', '3145000000', '3165000000', '3185000000', '3205000000', '3225000000', '3245000000', '3265000000', '3285000000', '3305000000', '3325000000', '3345000000', '3365000000', '3385000000', '3405000000', '3425000000', '3445000000', '3465000000', '3485000000', '3505000000', '3525000000', '3545000000', '3565000000', '3585000000', '3605000000', '3625000000', '3645000000', '3665000000', '3685000000', '3705000000', '3725000000', '3745000000', '3765000000', '3785000000']
for fr in freq: # for each fr in freq
	call(["python", "./auto_scan.py", "-f", fr])
	print("Done with " + str(fr))
```