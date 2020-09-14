import os,re,sys, cmdlibs

def init_ps1(usr_ps1=None):
    if usr_ps1:
        os.environ['PS1'] = usr_ps1
    elif 'PS1' not in os.environ:
        os.environ['PS1'] = "$ "
    else:
        os.environ['PS1'] = "$ "


def shell():
    init_ps1()
    os.write(2,(os.environ['PS1']).encode())

    while 1:
        try:
            usr_input = input()
        except EOFError:
            pass

        s = cmdlibs.exec_fork(usr_input)
        if s == 0 or usr_input == "exit":
            sys.exit(0)
        else:
            os.write(2, (os.environ['PS1']).encode())

shell()
