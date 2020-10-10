# radare2-python
Python script(s) for interacting with radare2:
- disassemble.py - find and iterate over all functions in the exe and extract all block locations, binary and disassembly.

### Prerequisites
- radare2 (tested on v4.6.0-git)
- r2pipe

## Usage
`python3 disassemble.py <path/to/exe>`

## Notes
Couldn't find a python script for this, so wrote one. I have very little experience with radare2 so feel free to suggest corrections and share insights. This [CS](https://scoding.de/uploads/r2_cs.pdf) helped a bit.

## Testing

Tested on ELFs only so far, on a Ubuntu 18 machine.

I did do a (shallow) comparison to IDA 6.95 by going over all exes in `/bin/` and comparing runtime, number of functions found and overall number of bytes found and disassembled. **I did not check or compare the contents of the blocks or the quality of the disassembly, as of yet**.

The resulsts show that R2 is on par when it comes to run time and finding blocks, but it assigns them to significantly less functions (so i guess IDA is better at finding function..).

![Recovered Bytes](https://github.com/nimrodpar/radare2-python/raw/master/IDA%20v%20R2%20-%20Bytes.png)
![Run Time](https://github.com/nimrodpar/radare2-python/raw/master/IDA%20v%20R2%20-%20Runtime.png)

EXE| Radare2 Time| IDA Time| Radare2 #Functions| IDA #Functions| Radare2 #Bytes| IDA #Bytes
---|---------|-------------|---------------|-------------------|-----------|---------------
chown| 2.1s| 1.8s| 162| 248| 31870| 31811
systemd-notify| 0.34s| 0.95s| 34| 66| 2457| 2347
rmdir| 1.3s| 1.5s| 93| 158| 19447| 20384
systemctl| 4.6s| 3.5s| 343| 662| 60897| 96410
systemd-inhibit| 0.36s| 0.98s| 42| 80| 2901| 2806
sh.distrib| 3.8s| 2.7s| 289| 418| 56290| 64006
bzgrep| 0.056s| 0.74s| 1| 0| 2| 0
ntfssecaudit| 3.1s| 2.0s| 148| 247| 46985| 47276
dmesg| 1.7s| 1.6s| 161| 277| 18822| 23218
ntfsfix| 1.1s| 1.3s| 76| 142| 13616| 14351
kmod| 4.4s| 3.1s| 339| 469| 67375| 87091
loginctl| 0.85s| 1.4s| 103| 212| 9271| 20086
dd| 2.4s| 1.9s| 151| 240| 39015| 39223
ed| 1.6s| 1.6s| 105| 218| 28298| 28127
df| 2.8s| 2.2s| 191| 288| 46820| 46634
mount| 1.2s| 1.2s| 154| 279| 10965| 11644
bzegrep| 0.057s| 0.72s| 1| 0| 2| 0
more| 1.3s| 1.4s| 120| 209| 19583| 20535
red| 0.054s| 0.73s| 1| 0| 4| 0
umount| 0.73s| 1.1s| 109| 206| 6441| 7257
hostname| 0.43s| 0.99s| 55| 102| 3723| 3734
ntfscluster| 0.81s| 1.2s| 65| 113| 10643| 11574
ntfs-3g| 3.4s| 3.0s| 348| 639| 42767| 77679
bzmore| 0.054s| 0.71s| 1| 0| 2| 0
cp| 5.2s| 3.0s| 347| 513| 83014| 82030
unicode_start| 0.056s| 0.72s| 1| 0| 2| 0
mt-gnu| 2.3s| 1.9s| 159| 249| 38140| 39578
su| 1.3s| 1.3s| 144| 257| 11175| 16104
stty| 2.0s| 1.8s| 111| 184| 32778| 33344
sync| 0.87s| 1.2s| 81| 143| 11532| 12008
sh| 3.7s| 2.7s| 289| 418| 56290| 64006
rnano| 9.2s| 4.6s| 560| 802| 153904| 143483
zgrep| 0.06s| 0.72s| 1| 0| 2| 0
setfacl| 0.85s| 1.3s| 43| 187| 15675| 14066
lsblk| 2.3s| 1.8s| 250| 417| 29465| 32747
ntfstruncate| 0.7s| 1.1s| 69| 124| 8474| 8954
ping6| 1.7s| 1.7s| 138| 251| 27565| 33813
bzdiff| 0.056s| 0.72s| 1| 0| 2| 0
chvt| 0.27s| 0.92s| 30| 56| 1691| 1701
udevadm| 1.2e+01s| 7.7s| 706| 1044| 187625| 258075
kbd_mode| 0.25s| 0.93s| 31| 57| 2084| 2094
lowntfs-3g| 2.6s| 2.3s| 266| 503| 33653| 54875
ulockmgr_server| 0.18s| 0.97s| 8| 90| 2790| 3609
btrfstune| 1.1e+01s| 5.3s| 761| 928| 181764| 178036
ntfs-3g.probe| 0.18s| 0.91s| 20| 38| 1142| 1163
cpio| 4.6s| 3.2s| 324| 460| 75269| 84276
egrep| 0.054s| 0.72s| 1| 0| 2| 0
lessecho| 0.21s| 0.93s| 18| 34| 2139| 1856
mkdir| 2.7s| 2.0s| 208| 318| 41735| 42424
mkfs.btrfs| 1.2e+01s| 5.8s| 798| 985| 193138| 192815
uncompress| 0.057s| 0.71s| 1| 0| 2| 0
nc| 0.98s| 1.3s| 84| 151| 14973| 15570
ntfsusermap| 0.63s| 1.1s| 72| 133| 7230| 8109
ls| 3.8s| 2.8s| 265| 444| 62675| 67831
zless| 0.057s| 0.72s| 1| 0| 2| 0
Error  when doing /bin/static-sh| skipping
tempfile| 0.22s| 0.96s| 27| 51| 1677| 1833
netcat| 0.99s| 1.3s| 84| 151| 14973| 15570
mknod| 2.2s| 1.8s| 185| 287| 32799| 33081
zfgrep| 0.063s| 0.76s| 1| 0| 2| 0
touch| 2.9s| 2.2s| 152| 237| 48842| 49444
uname| 0.93s| 1.3s| 82| 142| 11933| 11953
which| 0.061s| 0.74s| 1| 0| 4| 0
ip| 1.6e+01s| 1e+01s| 672| 932| 272609| 335387
pidof| 0.66s| 1.1s| 76| 138| 7836| 8020
zdiff| 0.069s| 0.77s| 1| 0| 2| 0
Error  when doing /bin/busybox| skipping
networkctl| 1.1s| 1.3s| 134| 241| 12263| 12935
nano| 8.9s| 4.7s| 560| 802| 153904| 143483
ss| 3.4s| 2.4s| 249| 367| 53788| 56678
bash| 4e+01s| 1.9e+01s| 2151| 2473| 672194| 614308
loadkeys| 2.5s| 2.1s| 171| 231| 36181| 38910
fgconsole| 0.28s| 0.96s| 31| 57| 2149| 2159
dnsdomainname| 0.43s| 1.1s| 55| 102| 3723| 3734
systemd-tty-ask-password-agent| 0.87s| 1.1s| 96| 190| 9368| 10174
tar| 1.4e+01s| 7.8s| 848| 1164| 222776| 243105
getfacl| 0.39s| 1.1s| 22| 128| 6491| 7308
vdir| 3.8s| 2.8s| 265| 444| 62675| 67831
nisdomainname| 0.42s| 1.0s| 55| 102| 3723| 3734
grep| 6.4s| 4.3s| 278| 411| 119336| 134205
rbash| 4e+01s| 1.8e+01s| 2151| 2473| 672194| 614308
ntfsmove| 0.76s| 1.2s| 70| 128| 9503| 10100
bzless| 0.061s| 0.73s| 1| 0| 2| 0
fgrep| 0.055s| 0.73s| 1| 0| 2| 0
bzip2recover| 0.36s| 0.97s| 36| 63| 4056| 3878
sed| 3.4s| 2.5s| 252| 365| 56118| 56457
readlink| 1.1s| 1.4s| 108| 171| 16490| 17178
setupcon| 0.12s| 0.79s| 1| 0| 2| 0
false| 0.78s| 1.2s| 74| 128| 10248| 10664
date| 3.3s| 2.3s| 152| 237| 57064| 57092
btrfs| 1.9e+01s| 1.1e+01s| 1108| 1470| 338776| 378926
dir| 3.8s| 2.9s| 265| 444| 62675| 67831
bunzip2| 0.91s| 1.2s| 83| 139| 13490| 13812
systemd-sysusers| 1.4s| 1.4s| 123| 229| 20598| 21372
systemd-machine-id-setup| 0.48s| 1.0s| 53| 101| 5077| 5262
gzip| 2.9s| 2.5s| 105| 283| 55944| 54709
zmore| 0.062s| 0.74s| 1| 0| 2| 0
zegrep| 0.057s| 0.73s| 1| 0| 2| 0
ntfscat| 0.6s| 1.1s| 62| 110| 6772| 5864
zcmp| 0.061s| 0.73s| 1| 0| 2| 0
mv| 5.4s| 3.0s| 346| 516| 83029| 81965
btrfs-map-logical| 1.1e+01s| 5.4s| 763| 934| 181386| 177473
zforce| 0.06s| 0.74s| 1| 0| 2| 0
setfont| 1.3s| 1.4s| 107| 172| 20795| 21173
ntfsls| 0.61s| 1.1s| 67| 120| 7041| 6795
wdctl| 0.74s| 1.1s| 82| 150| 8113| 8475
whiptail| 0.91s| 1.2s| 101| 185| 11357| 11683
ps| 1.9s| 2.1s| 146| 424| 24492| 41032
kill| 0.66s| 1.1s| 74| 135| 7597| 8025
journalctl| 1.9s| 1.5s| 194| 369| 21642| 26218
open| 0.52s| 1.0s| 61| 113| 4930| 5204
zcat| 0.058s| 0.73s| 1| 0| 2| 0
ntfsrecover| 4.0s| 2.5s| 135| 201| 64927| 65473
systemd-escape| 0.25s| 0.98s| 31| 60| 1978| 2271
sleep| 0.93s| 1.2s| 84| 143| 12070| 12156
btrfs-image| 1.2e+01s| 5.8s| 804| 995| 193530| 192119
systemd| 3.4e+01s| 2.2e+01s| 2020| 3464| 530260| 749876
lsmod| 4.3s| 3.1s| 339| 469| 67375| 87091
bzcmp| 0.061s| 0.74s| 1| 0| 2| 0
ping4| 1.7s| 1.8s| 138| 251| 27565| 33813
ntfsfallocate| 0.72s| 1.1s| 74| 135| 8197| 8425
nc.openbsd| 0.98s| 1.3s| 84| 151| 14973| 15570
dumpkeys| 1.4s| 1.5s| 107| 141| 15248| 15956
ntfscmp| 0.84s| 1.1s| 87| 142| 9244| 9537
ntfsinfo| 1.6s| 1.4s| 86| 151| 22101| 22781
chmod| 2.0s| 1.7s| 146| 220| 29280| 29163
findmnt| 1.6s| 1.5s| 202| 358| 16097| 23531
btrfs-zero-log| 1.1e+01s| 5.3s| 757| 926| 179369| 175750
gunzip| 0.061s| 0.73s| 1| 0| 2| 0
netstat| 2.2s| 2.5s| 90| 360| 45744| 59531
ln| 2.0s| 1.7s| 179| 274| 29195| 30080
lessfile| 0.072s| 0.73s| 1| 0| 2| 0
btrfs-find-root| 1.1e+01s| 5.4s| 759| 926| 179811| 176209
systemd-hwdb| 2.7s| 2.0s| 216| 336| 42167| 41024
bzip2| 0.91s| 1.2s| 83| 139| 13490| 13812
systemd-tmpfiles| 2.4s| 1.8s| 175| 337| 33000| 34343
bzexe| 0.064s| 0.74s| 1| 0| 2| 0
cat| 1.0s| 1.3s| 90| 155| 13838| 14536
domainname| 0.43s| 1.0s| 55| 102| 3723| 3734
ping| 1.7s| 1.7s| 138| 251| 27565| 33813
mountpoint| 0.31s| 0.96s| 43| 82| 2026| 2393
bzcat| 0.91s| 1.3s| 83| 139| 13490| 13812
rm| 2.0s| 1.7s| 162| 241| 30434| 30380
echo| 0.85s| 1.3s| 75| 131| 11743| 12016
fsck.btrfs| 0.059s| 0.75s| 1| 0| 2| 0
openvt| 0.52s| 1.0s| 61| 113| 4930| 5204
login| 1.8s| 1.5s| 187| 305| 23012| 23112
btrfs-select-super| 1.1e+01s| 5.5s| 759| 929| 179524| 175674
chacl| 0.2s| 1.0s| 10| 77| 3328| 3778
lesspipe| 0.07s| 0.75s| 1| 0| 2| 0
pwd| 1.0s| 1.3s| 95| 163| 13423| 13426
systemd-ask-password| 0.21s| 0.94s| 25| 48| 1497| 1565
plymouth| 0.98s| 1.2s| 103| 189| 11262| 13165
lesskey| 0.35s| 1.0s| 32| 55| 3272| 4340
run-parts| 0.48s| 1.0s| 61| 115| 5165| 5663
znew| 0.066s| 0.75s| 1| 0| 2| 0
bzfgrep| 0.061s| 0.75s| 1| 0| 2| 0
less| 5.8s| 3.2s| 425| 529| 84300| 83028
btrfsck| 2e+01s| 1.1e+01s| 1108| 1470| 338776| 378926
chgrp| 2.0s| 1.7s| 160| 242| 30590| 30503
gzexe| 0.065s| 0.74s| 1| 0| 2| 0
mt| 2.4s| 1.9s| 159| 249| 38140| 39578
btrfs-debug-tree| 1.1e+01s| 5.5s| 765| 931| 182678| 178508
mktemp| 1.2s| 1.3s| 110| 188| 16611| 16969
fusermount| 0.66s| 1.3s| 23| 171| 11838| 13321
dash| 3.6s| 2.7s| 289| 418| 56290| 64006
fuser| 1.1s| 1.3s| 89| 148| 15563| 15752
ypdomainname| 0.43s| 1.0s| 55| 102| 3723| 3734
true| 0.78s| 1.2s| 74| 128| 10239| 10655
ntfswipe| 0.96s| 1.4s| 79| 145| 11593| 20035





