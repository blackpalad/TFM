set title 'Radial Distribution Function'
set xlabel 'r / A'
set ylabel 'g(r)'

plot 'gr.dat' w l smooth csplines
