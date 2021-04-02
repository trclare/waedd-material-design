"""
bls_data_gather.py
Written by: Aaron Finocchiaro

Retrieves data from the Bureau of Labor Statistics API and formats it into Pandas Dataframes
"""
import yaml
from pybls.bls_data import BlsData

# read in yaml file
with open('bls_config.yaml') as bls_yaml:
    bls_list = yaml.load(bls_yaml, Loader=yaml.FullLoader)

for waedd_section in bls_list:
    section_data = BlsData(
        waedd_section['seriesIDs'],
        waedd_section['start_year'],
        waedd_section['end_year'],
    )
    #create graph and table
    fig = section_data.create_graph(waedd_section['graph_name'],
                                    graph_type=waedd_section['graph_type'],
                                    custom_column_names=waedd_section.get('custom_column_names'),
                                    transpose=waedd_section.get('transpose'),
    )
    table = section_data.create_table(
            custom_column_names=waedd_section.get('custom_column_names'),
            index_color='orange',
    )

    #save graph and table to html files
    fig.write_html(f"./graphs/{waedd_section['filename']}.html", include_plotlyjs='cdn')
    table.write_html(f"./tables/{waedd_section['filename']}.html", include_plotlyjs='cdn')