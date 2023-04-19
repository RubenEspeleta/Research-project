name := report
fullname := latex/$(name)

LATEX := pdflatex -shell-escape -synctex=1
LATEXMK := latexmk -pdf -pdflatex="$(LATEX)"

# List here the files that are needed to compile the tex source and that are
# created by scripts. At the end of this file, you have to define the commands
# create these files.
figures := tmp/fig_R_vs_Fh_other_studies.png tmp/table_exps.tex \
           tmp/fig_simple.png


.PHONY: all clean cleanall figures startworking

all: $(name).pdf

clean:
	cd latex && rm -f *.log *.aux *.out *.bbl *.blg *.tmp *.toc

cleanpdf: clean
	rm -f $(name).pdf

cleanall: cleanpdf
	rm -rf tmp

figures: $(figures)

# dependencies and commands to create them

latex:
	cd latex && $(LATEXMK) $(name).tex

$(name).pdf: $(fullname).tex $(figures)
	cd latex && $(LATEXMK) $(name).tex && cp $(name).pdf ..

tmp/fig_R_vs_Fh_other_studies.png: python/make_fig_other_studies.py
	python python/make_fig_other_studies.py save_for_tex

tmp/table_exps.tex: python/make_table_exps.py
	python python/make_table_exps.py

tmp/fig_simple.png: python/make_fig_simple.py
	python python/make_fig_simple.py --no-show
