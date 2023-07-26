# combine_annotation_report
combine the interproscan, eggnog annotation output file, then display summary stat.


**interproscan interproscan_only statstistics
**
python interproscan_only_gene_count.py --interproscan interproscan_output.xlsx 

**interproscan and eggnog statstictics
**
python combine_eggnog_interpro.py --interpro Tx_ips_output.xlsx --eggnog Tx_wj.emapper.annotations.xlsx 
