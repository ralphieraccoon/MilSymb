$pdf_mode = 1;
$latex = 'latex  %O  --shell-escape %S';
$pdflatex = 'lualatex %O --shell-escape %S';
sub pythontex {return system("pythontex --interpreter \"python:py -3.11\" \"$_[0]\"");}
add_cus_dep("pytxcode", "tex", 0, "pythontex");
