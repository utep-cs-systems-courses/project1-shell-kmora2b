import os,re,sys

def parse_command(cmdString):
    output_file = None
    input_file = None
    cmd = ''
 
    cmdString = re.sub(' +', ' ', cmdString)
    #print(cmdString)
 
    if '>' in cmdString:
        [cmd, output_file] = cmdString.split('>',1)
        output_file = output_file.strip()
 
    if '<' in cmdString:
        [cmd, input_file] = cmd.split('<', 1)
        input_file = input_file.strip()
    
    elif output_file != None and '<' in output_file:
        [output_file, input_file] = output_file.split('<', 1)
        
        output_file = output_file.strip()
        input_file = input_file.strip()
    else:
        cmd = cmdString
    return cmd.split(), output_file, input_file


def exec_command(command):
    cmd_process = parse_command(command)[0]
    #print(cmd_process)
    if cmd_process:
        if "cd" in cmd_process[0]:
            exec_cd(cmd_process[1])
            #print( exec_cd(cmd_process[1]))
            return 3
        if "exit" in cmd_process[0]:
            return 0
    return -1
    
def exec_cd(path):
    try:
        os.chdir(path)

    except:
        os.write(2, f"{path}: No such file or directory\n".encode())
    return os.getcwd()


def exec_fork(command):
    pid = os.getpid()

    os.write(1, ("About to fork (pid:%d)\n" % pid).encode())

    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())

    elif rc == 0:                   # child
        os.write(1, ("I am child.  My pid==%d.  Parent's pid=%d\n" % (os.getpid(), pid)).encode())
        return exec_command(command)
    else:                           # parent (forked ok)
        code_num = os.wait()
        os.write(1, ("Terminated Child's pid=%d\n" % (code_num[0])).encode())
        os.write(1, ("Signal number\n%d" % (code_num[1])).encode())
   
    return 0

        
    
