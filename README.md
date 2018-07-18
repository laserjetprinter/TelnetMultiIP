# TelnetMultiIP
The following script and program are used to mass telnet IP addresses, and store their
resulting connection status in a .csv file.

The powershell script telnets each IP from an input .csv file. A log file from the resulting
command prompt is then generated and saved as a csv. Note: the input .csv file should contain 
the first IP address on row 2, because it skips the first.

The python program reads the .csv log file and formats a final .csv -- containing the telnet
IP and the corresponding connection status. Each row of the .csv file contains a separate 
telnet entry. Note: since the IPs are stored in a dictionary, no duplicate IPs will be stored
and any connection data will be overwritten by the most recent result.
