$path = "C:\Users\natalie.davis\Documents\TelnetScriptLogs\ExampleIPs.csv"
$csv = Import-csv -path $path
$python="C:\Users\natalie.davis\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.7\Python 3.7 (32-bit).lnk"
$PythonScript="C:\Users\natalie.davis\Documents\TelnetScriptLogs\telnetLogSort.py"

Import-Csv $path | Foreach-Object { 

    foreach ($property in $_.PSObject.Properties)
    {
        $property.Value >>C:\Users\natalie.davis\Documents\TelnetScriptLogs\telnetLog.csv 
        New-Object System.Net.Sockets.TcpClient($property.Value , 3246) >>C:\Users\natalie.davis\Documents\TelnetScriptLogs\telnetLog.csv 
    } 

}

 
& $python $PythonScript