# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Hxl
                                 A QGIS plugin
 Plugin for working with Humanitarian Exchange Language (HXL) data
                             -------------------
        begin                : 2017-05-19
        copyright            : (C) 2017 by 510
        email                : info@510.global
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Hxl class from file Hxl.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .hxl import Hxl
    return Hxl(iface)
