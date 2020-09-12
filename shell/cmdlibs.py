import os,re,sys

def create_command():
    


def exec_cd(cd_path):
    try:
        os.chdir(cd_path)
    except:
        os.write(2, "{cd-path}: No such file or directory/n".encode())
    return os.getcwd()

def exec_fork():
    pid = os.getpid()

    os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)
    elif rc == 0:                   # child
        os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
    else:                           # parent (forked ok)
        os.write(1, ("I am parent.  My pid=%d.  Child's pid=%d\n" % (pid, rc)).encode())

def exec_shell_cmd(usr_input):
    if usr_input == "exit":
        sys.exit(0)
    if usr_input != "":
        exec_fork()
   
        
    
