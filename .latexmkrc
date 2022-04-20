$ENV{'TEXINPUTS'}='./:' . $ENV{'TEXINPUTS'}; 
$pdf_mode = 1;
$latex = 'latex  %O  --shell-escape %S';
$pdflatex = 'lualatex  %O  --shell-escape %S';