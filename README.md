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

I did do a (shallow) comparison to IDA 6.95 by going over all exes in `/bin/` and comparing runtime, number of functions found and overall number of bytes found and disassembled. The resulsts show that R2 is on par when it comes to run time and finding blocks, but it assigns them to significantly less functions (so i guess IDA is better at finding function..).





