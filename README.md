# animated_graph_plotter
```console
Creating animated graph from csv table 

usage: main.py [-h] [-o O] [-p P] [--dpi DPI] [--update UPDATE] [--time_col TIME_COL] [--nogrid] [--figx FIGX] [--figy FIGY]
               [--pcx PCX] [--pcy PCY]
               data_path

animated graph plotter

positional arguments:
  data_path            path to csv table

optional arguments:
  -h, --help           show this help message and exit
  -o O                 output filename
  -p P                 path to video
  --dpi DPI            dpi for video
  --update UPDATE      time of showing each frame
  --time_col TIME_COL  number of column with time
  --nogrid             render without grid
  --figx FIGX          horizontal figure size in inches
  --figy FIGY          vertical figure size in inches
  --pcx PCX            horizontal plots count
  --pcy PCY            vertical plots count
  ```
