import click
import describe
from datetime import datetime

template = r"""
\begin{figure}[t]
\includegraphics[width=0.9\textwidth]{{}/map.png}
\end{figure}
\input{{}/map}
"""

@click.command()
@click.argument("directory")
@click.option("-n", default=100)
def main(directory, n):
    describe.do_novel(directory, n)
    with open(directory + "/contents.tex", "w") as f:
        for i in range(n):
            start = datetime.now()
            f.write(template.format(i, i))
            print("")
            fin = datetime.now() - start
            print(fin.total_seconds())
            print("----")

if __name__ == '__main__':
    main()
