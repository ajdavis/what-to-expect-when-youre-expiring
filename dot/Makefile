src = $(wildcard *.dot)
pdf = $(src:.dot=.dot.pdf)

all: $(pdf)

%.dot.pdf: %.dot
	dot -O -Tpdf $<

.PHONY: clean
clean:
	rm -f $(pdf)
