# Copyright 2017 John Curci jcurci92@bu.edu


import unittest
import subprocess


AUTHORS = ['jcurci92@bu.edu']

PROGRAM_TO_TEST = "collision.py"

def runprogram(program, args, inputstr):
    try:
        coll_run = subprocess.run(
            ["python", program, *args],
            input=inputstr.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=0.1)
    except:
        print("problem in test.py")
    ret_code = coll_run.returncode
    program_output = coll_run.stdout.decode()
    program_errors = coll_run.stderr.decode()
    return (ret_code, program_output, program_errors)


class CollisionTestCase(unittest.TestCase):

   def test_same_number_newline(self):
        try:
            strin = "1 0 0 0 0\n2 0 0 0 0"
            (rc,out,errs) = runprogram("collision.py",["b", "0", "2", "1", "a", "$", "!", "_", "0.1"],strin)
   
        except:
            print("got here")
            pass
        print("return code:-->",rc,"<--")
        print("errors:-->",errs,"<--")
        print("output:-->",out,"<--")  


def main():
    unittest.main()

if __name__ == '__main__':
    main()

# implement "set up" and "tear down"??
# check to make sure the files are python??
# try "brushing" the things by eachother to find minimum distance