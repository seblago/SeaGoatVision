#! /usr/bin/env python

#    Copyright (C) 2012  Octets - octets.etsmtl.ca
#
#    This file is part of SeaGoatVision.
#    
#    SeaGoatVision is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import inspect
import types
import SeaGoatVision.server.filters.implementation
from SeaGoatVision.commun.param import Param

def load_filters():
    #TODO on devrait utiliser implement au lieu de tout le nom?
    return {name: filtre
        for name, filtre in vars(SeaGoatVision.server.filters.implementation).items()
            if inspect.isclass(filtre)}

def create_filter(filter_name):
    for name, filtre in load_filters().items():
        if name == filter_name:
            return filtre()
    return None
 
def get_filter_from_filterName(filter_name):
    return load_filters().get(filter_name, None)