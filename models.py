"""
This module contains the classes representing Near Earth Objects (NEOs) and their close approaches.

Classes:
- NearEarthObject: A class representing a near-Earth object (NEO).
- CloseApproach: A class representing a close approach to Earth by an NEO.
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        if not info.get('designation', False):
            raise ValueError('Insert NEO designation')

        self.designation = str(info.get('designation'))
        self.name = str(info.get('name')) if info.get('name') else None
        self.diameter = float(info.get('diameter')) if info.get('diameter') else float('nan')
        self.hazardous = bool(info.get('hazardous')) if info.get('hazardous') else False

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    @ property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name:
            return(f'{self.designation} ({self.name})')
        else:
            return(f'{self.designation}')

    def __str__(self):
        """Return `str(self)`."""
        hazardous_str = "is hazardous" if self.hazardous else "is not hazardous"
        return f"NEO {self.fullname} has a diameter of " \
               f"{self.diameter:.3f} km and {hazardous_str} "

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = info.get('designation')
        self.time = cd_to_datetime(info.get('time'))
        self.distance = float(info.get('distance'))
        self.velocity = float(info.get('velocity'))
        self.neo = None

    @ property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time."""
        return f'{datetime_to_str(self.time)}'

    def __str__(self):
        """Return `str(self)`."""
        return f"On {self.time_str}, '{self.neo.fullname}' approaches Earth at a distance of " \
               f"{self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
