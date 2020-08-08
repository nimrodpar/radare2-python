import sys
import os
import r2pipe
from typing import Tuple, List

if (sys.version_info.major, sys.version_info.minor) < (3, 6):
    exit("Run me with Python3.6 (or above) please.")


class FunctionDescriptor(dict):
    """ A wrapper for functions in executables, with additions for blocks binary and disassembly and properties
    for important stuff """

    class Keys:
        name = "name"
        address = "offset"
        size = "size"

    @property
    def name(self) -> str:
        return self[self.Keys.name]

    @property
    def address(self) -> int:
        return int(self[self.Keys.address])

    @property
    def size(self) -> int:
        return int(self[self.Keys.size])


class BlockDescriptor(dict):
    """ A wrapper for blocks, with additions and properties for important stuff """

    class Keys:
        address = "addr"
        size = "size"
        dsm = "dsm"
        binary = "binary"

    @property
    def address(self) -> int:
        return int(self[self.Keys.address])

    @property
    def size(self) -> int:
        return int(self[self.Keys.size])

    @property
    def dsm(self) -> List[Tuple[int, str, int]]:
        return self[self.Keys.dsm]

    @dsm.setter
    def dsm(self, value):
        self[self.Keys.dsm] = value

    @property
    def binary(self) -> List[int]:
        return self[self.Keys.binary]

    @binary.setter
    def binary(self, value):
        self[self.Keys.binary] = value


def disassmeble(filepath):
    """ Disassmles an exe using radare2, :returns A dict {function address} -> {block address} """
    r2 = r2pipe.open(filepath)

    r2.cmd("aaa")  # do an analysis to find functions
    functions = r2.cmdj("aflj")  # get all functions

    print(f"Disassembling {len(functions)} functions in {filepath}")

    result = {}
    for function in functions:
        function = FunctionDescriptor(function)
        next_address = function.address

        print(f"Disassembling Function {function.name} ({function.size} bytes)")

        if function.size != int(function["realsz"]):
            print(f"Function @{function.address} size is different from 'real size' "
                  f"({function.size} != {function['realsz']})")

        overall_block_size, blocks = 0, {}
        while True:
            r2.cmd(f"s {next_address}")  # seek to block
            try:
                block = BlockDescriptor(r2.cmdj("pdfj"))  # get block info
            except:
                print(f"Couldn't get block info for block @{next_address} in function {function.name}, Stopping.")
                break

            if next_address != block.address:
                print(f"Discrepancy @function {function.name}, Seek to block {next_address}, "
                      f"but block is at {block.address}. Stopping disassembly for this function")
                break

            overall_block_size += block.size
            block.binary = r2.cmdj(f"pcj {block.size}")  # get binary of block

            ops = block["ops"]
            # print(f"{len(ops)} instructions in block @{block.address}")
            if not ops:
                break

            block.dsm = []
            for o in ops:
                if o["type"] == "invalid":
                    continue
                block.dsm += (int(o["offset"]), o["disasm"], int(o["size"]))

            if o["type"] == "invalid":
                print(f"Invalid instruction @{block.address + int(o['offset'])} @ block {block.address} "
                      f"@ function {function.name}. SKipping block")
                break

            blocks[block.address] = block
            if o["type"] == "jmp":
                jump_address = int(o["jump"])
                if jump_address in blocks.keys():
                    break
                next_address = jump_address
                continue

            break

        if overall_block_size < function["realsz"]:
            print(f"Only {overall_block_size} bytes successfully disassembled out of {function.size} @ function "
                  f"{function.name}")
        result[function.address] = blocks

    return result


if len(sys.argv) != 2 or not os.path.isfile(sys.argv[1]):
    exit(f"python3 Usage: {sys.argv[0]} <path/to/exe>")

disassmeble(sys.argv[1])
