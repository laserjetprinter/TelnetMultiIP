$path = "EXAMPLE-IP-CSV-FILEPATH"
$csv = Import-csv -path $path
$python="PYTHON-EXE-FILEPATH"
$PythonScript="PYTHON-TELNETLOGSORT-FILEPATH"

Import-Csv $path | Foreach-Object { 

    foreach ($property in $_.PSObject.Properties)
    {
        $property.Value >>TELNET-LOG-FILEPATH
        New-Object System.Net.Sockets.TcpClient($property.Value , 80) >>TELNET-LOG-FILEPATH
    } 

}

 
& $python $PythonScript