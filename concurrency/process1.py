import os
"""
windows not have fork
too low level ,used rarely, use multiprocessing
"""
pid_list = []

def main():
    pid_list.append(os.getpid())
    child_pid = os.fork()

    if child_pid == 0:
        pid_list.append(os.getpgid())
        print()
        print("CHILD:hey, I am the child process")
        print("CHILD: all the pids i know %" % pid_list)
    else:
        pid_list.append(os.getpid())
        print()
        print("PRINT: hey, I am the parent")
        print("PRINT: the child is pid %d " % child_pid)
        print("PRINT: all the pids i know %s" % pid_list)

if __name__ == '__main__':
    main()
