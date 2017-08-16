#   Ewia - A tool to calculate astrophysical object positions.
#   Copyright (C) 2017-2017 Johannes Bauer
#
#   This file is part of Ewia.
#
#    Ewia is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; this program is ONLY licensed under
#    version 2 of the License, later versions are explicitly excluded.
#
#    Ewia is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Ewia; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
#   Johannes Bauer <JohannesBauer@gmx.de>

class ApparentPosition(object):
	_COMPASS_ROSE = {
		0:		"N",
		22.5:	"NNE",
		45:		"NE",
		67.5:	"ENE",
		90:		"E",
		112.5:	"ESE",
		135:	"SE",
		157.5:	"SSE",
		180:	"S",
		202.5:	"SSW",
		225:	"SW",
		247.5:	"WSW",
		270:	"W",
		292.5:	"WNW",
		315:	"NW",
		337.5:	"NNW",
	}

	def __init__(self, altitude, azimuth, observed_object = None, observer_location = None, observation_time = None):
		assert(isinstance(altitude, float))
		assert(isinstance(azimuth, float))
		assert(-90 < altitude <= 90)
		assert(0 <= azimuth < 360)
		self.__altitude = altitude
		self.__azimuth = azimuth
		self.__observed_object = observed_object
		self.__observer_location = observer_location
		self.__observation_time = observation_time

	@property
	def altitude(self):
		return self.__altitude

	@property
	def azimuth(self):
		return self.__azimuth

	@property
	def observed_object(self):
		return self.__observed_object

	@property
	def observer_location(self):
		return self.__observer_location

	@property
	def observation_time(self):
		return self.__observation_time

	@property
	def azimuth_compass(self):
		return "MOO"

	def __str__(self):
		return "%s observed from %s at %s: altitude %.1f° azimuth %.1f (%s)" % (self.observed_object, self.observer_location, self.observation_time, self.altitude, self.azimuth, self.azimuth_compass)