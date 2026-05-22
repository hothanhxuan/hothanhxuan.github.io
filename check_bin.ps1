$Shell = New-Object -ComObject Shell.Application
$RecycleBin = $Shell.Namespace(0xA)
foreach($item in $RecycleBin.Items()) {
    if ($item.Name -match '(?i)assets|images') {
        Write-Output ($item.Name + ' | ' + $item.Path)
    }
}
