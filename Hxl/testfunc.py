from hxl_tools import HxlDataSet
import csv

hxl_remote_json = 'https://proxy.hxlstandard.org/data.json?url=https%3A//data.humdata.org/dataset/3cb60971-0dc7-4743-a7ae-e65744b2dbba/resource/968202f1-856a-4906-ae87-c730e9b1dd27/download/PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv'
hxl_remote_csv = 'https://proxy.hxlstandard.org/data.csv?url=https%3A//data.humdata.org/dataset/3cb60971-0dc7-4743-a7ae-e65744b2dbba/resource/968202f1-856a-4906-ae87-c730e9b1dd27/download/PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv'
#hxl_remote_csv = 'https://proxy.hxlstandard.org/data/z82Fye/download/data.csv'

hxlfilename = '/home/raymond/git/HXLQGISscript/data/PHL_haima_houses_damaged_pcoded_ndrrmc_sitrep_9_20161025.csv'

hds = HxlDataSet()
print(hds)

hds.remote_file = hxl_remote_csv
print(hds)

hds.download()
print(hds)
