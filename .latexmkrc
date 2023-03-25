$pdf_mode = 1;
$latex = 'latex  %O  --shell-escape %S';
$pdflatex = 'lualatex --shell-escape %S';
sub pythontex {return system("pythontex --interpreter \"python:py -3.9\" \"$_[0]\"");}
add_cus_dep("pytxcode", "tex", 0, "pythontex");