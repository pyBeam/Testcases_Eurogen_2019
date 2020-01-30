#!/usr/bin/env python3

import os
import subprocess


def UnifyStructure(config,YOUNG):

    configfile2 = open(config + '_temp', "w")
    with open(config, 'r') as configfile:
        while 1:
           line = configfile.readline()
           string = line
           if not line:
             break
           # remove line returns
           line = line.strip('\r\n')
           # make sure it has useful data
           if (not "=" in line) or (line[0] == '%'):
              configfile2.write(string)
           else:
              # split across equal sign
              line = line.split("=", 1)
              this_param = line[0].strip()
              this_value = line[1].strip()

              #float values
              if this_param == "Y_MODULUS":
                    stringalt = 'Y_MODULUS = '+ str(40000000000*(1+YOUNG)) + '   \r\n'
                    configfile2.write(stringalt)

              else:
                    configfile2.write(string)

    configfile.close()
    configfile2.close()
    # the file is now replaced
    os.remove(config )
    os.rename(config + '_temp', config )


def main():

    #deltaE = [1,10,50,100,150,200,500,100]
    #deltaE = [1.0e-05, 5.0e-05, 1.0e-04, 5.0e-04, 1.0e-03, 5.0e-03, 1.0e-02, 5.0e-02, 1.0e-01]
    deltaE = [1.0e-05, 5.0e-05,]
    config = 'configBeam.cfg'
    for i in range(len(deltaE)):
        for j in range(2):
            if j ==0:
               UnifyStructure(config, deltaE[i])
               Output_file = './Output_FD/' + 'FDeplus' + str(deltaE[i]) + '.txt'


            else:
                UnifyStructure(config, -deltaE[i])
                Output_file = './Output_FD/' + 'FDeminus' + str(deltaE[i]) + '.txt'

            Command_file = 'mpirun -n 4 pyBeamFSI.py -f config.cfg >' + Output_file
            process = subprocess.Popen(Command_file, shell=True, stdout=subprocess.PIPE)
            process.wait()


# -------------------------------------------------------------------
#  Run Main Program
# -------------------------------------------------------------------

# --- This is only accessed if running from command prompt --- #
if __name__ == '__main__':
    main()
