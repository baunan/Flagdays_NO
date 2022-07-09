CONF_CLIENT = "client"
CONF_FLAGS = "flags"
CONF_FLAGS_DAYS = "flagdays"
CONF_HIDE_PAST = "hide_past"
CONF_TIME_OFFSET = "time_offset"
CONF_PLATFORM = "sensor"
DEFAULT_COORDINATES = {"lat": 59.2181, "lon": 10.9298}
DEFAULT_FLAG = "norge"
DEFAULT_TIME_OFFSET = 10
DOMAIN = "flagdays_no"
FLAGDAY_URL = "http://www.flaggdager.no/"
UPDATE_INTERVAL = 60

CREDITS = [
    {"Created by": "J-Lindvig (https://github.com/J-Lindvig)"},
    {"Redeveloped by": "B. Aunan"},
    {"Data provided by": "Flaggdager (" + FLAGDAY_URL + ")"},
    {"Sunrise/sunset provided by": "Sunrise-Sunset (https://sunrise-sunset.org/api)"},
]
