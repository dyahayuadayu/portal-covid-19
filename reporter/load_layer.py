import os
from django.contrib.gis.utils import LayerMapping
from .models import Counties

countie_mapping = {
    'gid_0': 'GID_0',
    'name_0': 'NAME_0',
    'gid_1': 'GID_1',
    'name_1': 'NAME_1',
    'gid_2': 'GID_2',
    'name_2': 'NAME_2',
    'gid_3': 'GID_3',
    'name_3': 'NAME_3',
    'gid_4': 'GID_4',
    'name_4': 'NAME_4',
    'varname_4': 'VARNAME_4',
    'type_4': 'TYPE_4',
    'engtype_4': 'ENGTYPE_4',
    'cc_4': 'CC_4',
    'geom': 'MULTIPOLYGON',
}

county_shp = os.path .abspath(os.path.join(os.path.dirname(__file__),'data/gadm36_IDN_4.shp'))

def run(verbose=True):
	lm = LayerMapping(Counties, county_shp, countie_mapping, transform= False, encoding='iso-8859-1')
	lm.save(strict=True,verbose=verbose)