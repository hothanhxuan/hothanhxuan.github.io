Add-Type -AssemblyName System.Drawing
$imgPath = "C:\Users\Admin\.gemini\antigravity-ide\brain\4d543e23-e53d-4233-82b5-7ecfbfdf893f\media__1783597711681.jpg"
$img = [System.Drawing.Image]::FromFile($imgPath)
Write-Output "Width: $($img.Width), Height: $($img.Height)"
