#!/usr/bin/python3
# Name: Arjun Singh Brar
# ID: 1001189

import shlex
from subprocess import Popen, PIPE

def get_exitcode_stdout_stderr(cmd):
    """
    Execute the external command and get its exitcode, stdout and stderr.
    """
    args = shlex.split(cmd)

    proc = Popen(args, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()
    exitcode = proc.returncode
    #
    return exitcode, out, err


for i in range(256):
	cmd = "python3 shiftcipher_binary.py -i flag -o flag_d"+str(i)+" -m d -k " + str(i)
	exitcode, out, err = get_exitcode_stdout_stderr(cmd)
	cmd = "file flag_d" + str(i)
	exitcode, out, err = get_exitcode_stdout_stderr(cmd)
	str_png = "PNG"
	if bytes(str_png, "utf-8") in out:
		print(i, out)
	else:
		cmd = "rm flag_d"+str(i)
		exitcode, out, err = get_exitcode_stdout_stderr(cmd)