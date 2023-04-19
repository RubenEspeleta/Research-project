# A latex template for reports on research projects

This repository contains files to produce a pdf file for the report of a
research project with LaTeX (pdflatex and bibtex), Python and a Makefile.

To setup the environment to compile the pdf, follow the instructions in the
file
[install.md](https://gricad-gitlab.univ-grenoble-alpes.fr/augierpi/coursem1_pa_instabilities_turbulence/-/blob/master/install.md).

### Create your onw repository and start working on it locally

Fork this repo
https://gricad-gitlab.univ-grenoble-alpes.fr/augierpi/report_research_project_template.
You should have a new repo
https://gricad-gitlab.univ-grenoble-alpes.fr/myusername/report_research_project_template.

Clone your own repository with the program ``hg``:

```bash
hg clone https://gricad-gitlab.univ-grenoble-alpes.fr/myusername/report_research_project_template.git
```

### Compile to produce the pdf document

Finally, to compile the pdf, use the command `make`. (You can have a look at
the Makefile to understand what it does.)

This should produce a pdf file `report.pdf` that can be viewed for example with
the command `evince report.pdf &`.

You have to make sure that the pdf is produced from a clean directory. Try this:

```bash
make cleanall
make
```

### Description of the main files

The main files are:

- `README.rst`: file containing this text.

- `Makefile`: describes how to build the pdf; is used by the program
  `make`.

- In the directory `latex`:

  - `report.tex`: file containing the latex code.
  - `biblio.bib`: file containing the bibliography entries.
  - `jfm.bst`: file containing the style for the bibliography.

- In the directory `fig` (all figures that are not produced by scripts):

  - `logo_UGA.png`: the logo of the university.

- The directory `python` contains python scripts to make figures and tables.
