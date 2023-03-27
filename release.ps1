$match = (Get-Content milsymb.tex) | Select-String -pattern "\\vhEntry{(.*?)}{.*?}{.*?}{(.*?}.*)}" | Select-Object -Last 1
$ver = $match.Matches[0].Groups[1].Value
$desc = $match.Matches[0].Groups[2].Value
$lastmod = git log -1 --format=%cs

(Get-Content milsymb.sty) | Foreach-Object {
    $_ -replace "\\ProvidesPackage{milsymb}\[(.*?)\]", "\ProvidesPackage{milsymb}[$lastmod v$ver]" `
       -replace "%% Version: (?:.*?)(\s*?)%%\n","%% Version: ${ver}${1}%%\n" `
       -replace "%% Last Modified: (?:.*?)(\s*?)%%\n","%% Last Modified: ${lastmod}${1}%%\n"
}  | Set-Content milsymb.sty
(Get-Content milsymb.tex) | Foreach-Object {
    $_ -replace "%% Version: (?:.*?)(\s*?)%%\n","%% Version: ${ver}${1}%%\n" `
       -replace "%% Last Modified: (?:.*?)(\s*?)%%\n","%% Last Modified: ${lastmod}${1}%%\n" `
       -replace "\\vhEntry{$ver}{(.*?)}{(.*?}{.*?)}\n", "\vhEntry{$ver}{$lastmod}{$2}\n"
}  | Set-Content milsymb.tex

Copy-Item -Path "LICENCE.md","README.md","milsymb.sty","milsymb.pdf","milsymb.tex","manual_examples" -Destination (New-Item -Type Directory "milsymb") -Recurse
Set-Location -Path "milsymb"
"LICENCE.md","README.md","milsymb.sty","milsymb.tex","manual_examples/mef.tex" | ForEach-Object -Process {((Get-Content $_) -join "`n") + "`n" | Set-Content -NoNewline $_}
Set-Location -Path "..\"
Compress-Archive -Path "milsymb" -Destination "milsymb.zip" -Update
Remove-Item -Recurse ".\milsymb\"

Set-Content release_${ver}_description.txt -Value "$ver $lastmod $desc"

