from enum import Enum

DOMAIN = "de-occupancy"
CONF_GYMS = 'gyms'
OCCUPANCY_API_URL = "https://www.delirescalade.com/web/wp-json/api/occupancy?skipcache=1&code={code}"


class Gym(Enum):
    BPT = 'Beauport'
    DPB = 'Pierre Bertrand'
    DLE = 'Ste-Foy'
