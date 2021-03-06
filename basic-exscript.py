import Exscript


from Exscript.util.start import quickstart
from Exscript.util.file  import get_hosts_from_file


def do_something(job, host, conn):
    conn.execute('conf t')
    conn.execute('interface lo4')
    conn.execute('des exscript')
    conn.execute('end')


hosts = get_hosts_from_file('hosts.txt')
quickstart(hosts, do_something, max_threads = 3)


#quickstart does the following:
#1.It prompts the user for a username and a password.
#2.It connects to the specified host, using the specified protocol.
#3.It logs in using the given login details.
#4.It calls our do_something() function.
#5.When do_something() completes, it closes the connection.


#max_threads = 3 does the following:
#This tells Exscript to open three network connections in parallel.

