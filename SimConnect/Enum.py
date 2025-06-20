from ctypes import c_char, c_double, c_int, c_ulong, c_int64, c_uint64, c_short, c_char_p
from ctypes.wintypes import WORD, BYTE, MAX_PATH, HANDLE
from _ctypes import Structure, POINTER, Union
from enum import IntEnum, auto, IntFlag

from .Constants import *


# ----------------------------------------------------------------------------
#        Enum definitions
# ----------------------------------------------------------------------------


# Define the types we need.
class CtypesEnum(IntEnum):
    """A ctypes-compatible IntEnum superclass."""

    @classmethod
    def from_param(cls, obj):
        return int(obj)


# Define the types we need.
class CtypesEn(IntFlag):
    """A ctypes-compatible Enum superclass."""

    @classmethod
    def from_param(cls, obj):
        return int(obj)


class AutoName(CtypesEnum):
    def _generate_next_value_(name, start, count, last_values):
        return count


# Receive data types
class SIMCONNECT_RECV_ID(CtypesEnum):
    SIMCONNECT_RECV_ID_NULL = 0x00
    SIMCONNECT_RECV_ID_EXCEPTION = 0x01
    SIMCONNECT_RECV_ID_OPEN = 0x02
    SIMCONNECT_RECV_ID_QUIT = 0x03
    SIMCONNECT_RECV_ID_EVENT = 0x04
    SIMCONNECT_RECV_ID_EVENT_OBJECT_ADDREMOVE = 0x05
    SIMCONNECT_RECV_ID_EVENT_FILENAME = 0x06
    SIMCONNECT_RECV_ID_EVENT_FRAME = 0x07
    SIMCONNECT_RECV_ID_SIMOBJECT_DATA = 0x08
    SIMCONNECT_RECV_ID_SIMOBJECT_DATA_BYTYPE = 0x09
    SIMCONNECT_RECV_ID_WEATHER_OBSERVATION = 0x0A
    SIMCONNECT_RECV_ID_CLOUD_STATE = 0x0B
    SIMCONNECT_RECV_ID_ASSIGNED_OBJECT_ID = 0x0C
    SIMCONNECT_RECV_ID_RESERVED_KEY = 0x0D
    SIMCONNECT_RECV_ID_CUSTOM_ACTION = 0x0E
    SIMCONNECT_RECV_ID_SYSTEM_STATE = 0x0F
    SIMCONNECT_RECV_ID_CLIENT_DATA = 0x10
    SIMCONNECT_RECV_ID_EVENT_WEATHER_MODE = 0x11
    SIMCONNECT_RECV_ID_AIRPORT_LIST = 0x12
    SIMCONNECT_RECV_ID_VOR_LIST = 0x13
    SIMCONNECT_RECV_ID_NDB_LIST = 0x14
    SIMCONNECT_RECV_ID_WAYPOINT_LIST = 0x15
    SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SERVER_STARTED = 0x16
    SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_CLIENT_STARTED = 0x17
    SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SESSION_ENDED = 0x18
    SIMCONNECT_RECV_ID_EVENT_RACE_END = 0x19
    SIMCONNECT_RECV_ID_EVENT_RACE_LAP = 0x1A
    SIMCONNECT_RECV_ID_EVENT_EX1 = 0x1B
    SIMCONNECT_RECV_ID_FACILITY_DATA = 0x1C
    SIMCONNECT_RECV_ID_FACILITY_DATA_END = 0x1D
    SIMCONNECT_RECV_ID_FACILITY_MINIMAL_LIST = 0x1E
    SIMCONNECT_RECV_ID_JETWAY_DATA = 0x1F
    SIMCONNECT_RECV_ID_CONTROLLERS_LIST = 0x20
    SIMCONNECT_RECV_ID_ACTION_CALLBACK = 0x21
    SIMCONNECT_RECV_ID_ENUMERATE_INPUT_EVENTS = 0x22
    SIMCONNECT_RECV_ID_GET_INPUT_EVENT = 0x23
    SIMCONNECT_RECV_ID_SUBSCRIBE_INPUT_EVENT = 0x24
    SIMCONNECT_RECV_ID_ENUMERATE_INPUT_EVENT_PARAMS = 0x25
    SIMCONNECT_RECV_ID_ENUMERATE_SIMOBJECT_AND_LIVERY_LIST = 0x26
    SIMCONNECT_RECV_ID_FLOW_EVENT = 0x27


# Data data types
class SIMCONNECT_DATATYPE(CtypesEnum):
    SIMCONNECT_DATATYPE_INVALID = 0x00  # invalid data type
    SIMCONNECT_DATATYPE_INT32 = 0x01  # 32-bit integer number
    SIMCONNECT_DATATYPE_INT64 = 0x02  # 64-bit integer number
    SIMCONNECT_DATATYPE_FLOAT32 = 0x03  # 32-bit floating-point number (float)
    SIMCONNECT_DATATYPE_FLOAT64 = 0x04  # 64-bit floating-point number (double)
    SIMCONNECT_DATATYPE_STRING8 = 0x05  # 8-byte string
    SIMCONNECT_DATATYPE_STRING32 = 0x06  # 32-byte string
    SIMCONNECT_DATATYPE_STRING64 = 0x07  # 64-byte string
    SIMCONNECT_DATATYPE_STRING128 = 0x08  # 128-byte string
    SIMCONNECT_DATATYPE_STRING256 = 0x09  # 256-byte string
    SIMCONNECT_DATATYPE_STRING260 = 0x0A  # 260-byte string
    SIMCONNECT_DATATYPE_STRINGV = 0x0B  # variable-length string

    SIMCONNECT_DATATYPE_INITPOSITION = 0x0C  # see SIMCONNECT_DATA_INITPOSITION
    SIMCONNECT_DATATYPE_MARKERSTATE = 0x0D  # see SIMCONNECT_DATA_MARKERSTATE
    SIMCONNECT_DATATYPE_WAYPOINT = 0x0E  # see SIMCONNECT_DATA_WAYPOINT
    SIMCONNECT_DATATYPE_LATLONALT = 0x0F  # see SIMCONNECT_DATA_LATLONALT
    SIMCONNECT_DATATYPE_XYZ = 0x10  # see SIMCONNECT_DATA_XYZ
    SIMCONNECT_DATATYPE_INT8 = 0x11 # 8-bit integer number

    SIMCONNECT_DATATYPE_MAX = 0x12  # enum limit


# Exception error types
class SIMCONNECT_EXCEPTION(CtypesEnum):
    SIMCONNECT_EXCEPTION_NONE = 0x00

    SIMCONNECT_EXCEPTION_ERROR = 0x01
    SIMCONNECT_EXCEPTION_SIZE_MISMATCH = 0x02
    SIMCONNECT_EXCEPTION_UNRECOGNIZED_ID = 0x03
    SIMCONNECT_EXCEPTION_UNOPENED = 0x04
    SIMCONNECT_EXCEPTION_VERSION_MISMATCH = 0x05
    SIMCONNECT_EXCEPTION_TOO_MANY_GROUPS = 0x06
    SIMCONNECT_EXCEPTION_NAME_UNRECOGNIZED = 0x07
    SIMCONNECT_EXCEPTION_TOO_MANY_EVENT_NAMES = 0x08
    SIMCONNECT_EXCEPTION_EVENT_ID_DUPLICATE = 0x09
    SIMCONNECT_EXCEPTION_TOO_MANY_MAPS = 0x0A
    SIMCONNECT_EXCEPTION_TOO_MANY_OBJECTS = 0x0B
    SIMCONNECT_EXCEPTION_TOO_MANY_REQUESTS = 0x0C
    SIMCONNECT_EXCEPTION_WEATHER_INVALID_PORT = 0x0D
    SIMCONNECT_EXCEPTION_WEATHER_INVALID_METAR = 0x0E
    SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_GET_OBSERVATION = 0x0F
    SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_CREATE_STATION = 0x10
    SIMCONNECT_EXCEPTION_WEATHER_UNABLE_TO_REMOVE_STATION = 0x11
    SIMCONNECT_EXCEPTION_INVALID_DATA_TYPE = 0x12
    SIMCONNECT_EXCEPTION_INVALID_DATA_SIZE = 0x13
    SIMCONNECT_EXCEPTION_DATA_ERROR = 0x14
    SIMCONNECT_EXCEPTION_INVALID_ARRAY = 0x15
    SIMCONNECT_EXCEPTION_CREATE_OBJECT_FAILED = 0x16
    SIMCONNECT_EXCEPTION_LOAD_FLIGHTPLAN_FAILED = 0x17
    SIMCONNECT_EXCEPTION_OPERATION_INVALID_FOR_OBJECT_TYPE = 0x18
    SIMCONNECT_EXCEPTION_ILLEGAL_OPERATION = 0x18
    SIMCONNECT_EXCEPTION_ALREADY_SUBSCRIBED = 0x1A
    SIMCONNECT_EXCEPTION_INVALID_ENUM = 0x1B
    SIMCONNECT_EXCEPTION_DEFINITION_ERROR = 0x1C
    SIMCONNECT_EXCEPTION_DUPLICATE_ID = 0x1D
    SIMCONNECT_EXCEPTION_DATUM_ID = 0x1E
    SIMCONNECT_EXCEPTION_OUT_OF_BOUNDS = 0x1F
    SIMCONNECT_EXCEPTION_ALREADY_CREATED = 0x20
    SIMCONNECT_EXCEPTION_OBJECT_OUTSIDE_REALITY_BUBBLE = 0x21
    SIMCONNECT_EXCEPTION_OBJECT_CONTAINER = 0x22
    SIMCONNECT_EXCEPTION_OBJECT_AI = 0x23
    SIMCONNECT_EXCEPTION_OBJECT_ATC = 0x24
    SIMCONNECT_EXCEPTION_OBJECT_SCHEDULE = 0x25
    SIMCONNECT_EXCEPTION_JETWAY_DATA = 0x26
    SIMCONNECT_EXCEPTION_ACTION_NOT_FOUND = 0x27
    SIMCONNECT_EXCEPTION_NOT_AN_ACTION = 0x28
    SIMCONNECT_EXCEPTION_INCORRECT_ACTION_PARAMS = 0x29
    SIMCONNECT_EXCEPTION_GET_INPUT_EVENT_FAILED = 0x2A
    SIMCONNECT_EXCEPTION_SET_INPUT_EVENT_FAILED = 0x2B
    SIMCONNECT_EXCEPTION_INTERNAL = 0x2C


# Object types
class SIMCONNECT_SIMOBJECT_TYPE(CtypesEnum):
    SIMCONNECT_SIMOBJECT_TYPE_USER = 0x00
    SIMCONNECT_SIMOBJECT_TYPE_USER_AIRCRAFT = 0x00,
    SIMCONNECT_SIMOBJECT_TYPE_ALL = 0x01
    SIMCONNECT_SIMOBJECT_TYPE_AIRCRAFT = 0x02
    SIMCONNECT_SIMOBJECT_TYPE_HELICOPTER = 0x03
    SIMCONNECT_SIMOBJECT_TYPE_BOAT = 0x04
    SIMCONNECT_SIMOBJECT_TYPE_GROUND = 0x05
    SIMCONNECT_SIMOBJECT_TYPE_HOT_AIR_BALLOON = 0x06
    SIMCONNECT_SIMOBJECT_TYPE_ANIMAL = 0x07
    SIMCONNECT_SIMOBJECT_TYPE_USER_AVATAR = 0x08
    SIMCONNECT_SIMOBJECT_TYPE_USER_CURRENT = 0x09


# EventState values
class SIMCONNECT_STATE(CtypesEnum):
    SIMCONNECT_STATE_OFF = 0x00
    SIMCONNECT_STATE_ON = 0x01


# Object Data Request Period values
class SIMCONNECT_PERIOD(CtypesEnum):  #
    SIMCONNECT_PERIOD_NEVER = 0x00
    SIMCONNECT_PERIOD_ONCE = 0x01
    SIMCONNECT_PERIOD_VISUAL_FRAME = 0x02
    SIMCONNECT_PERIOD_SIM_FRAME = 0x03
    SIMCONNECT_PERIOD_SECOND = 0x04


class SIMCONNECT_MISSION_END(CtypesEnum):  #
    SIMCONNECT_MISSION_FAILED = 0x00
    SIMCONNECT_MISSION_CRASHED = 0x01
    SIMCONNECT_MISSION_SUCCEEDED = 0x02


# ClientData Request Period values
class SIMCONNECT_CLIENT_DATA_PERIOD(CtypesEnum):  #
    SIMCONNECT_CLIENT_DATA_PERIOD_NEVER = 0x00
    SIMCONNECT_CLIENT_DATA_PERIOD_ONCE = 0x01
    SIMCONNECT_CLIENT_DATA_PERIOD_VISUAL_FRAME = 0x02
    SIMCONNECT_CLIENT_DATA_PERIOD_ON_SET = 0x03
    SIMCONNECT_CLIENT_DATA_PERIOD_SECOND = 0x04


class SIMCONNECT_TEXT_TYPE(CtypesEnum):  #
    SIMCONNECT_TEXT_TYPE_SCROLL_BLACK = 0x00
    SIMCONNECT_TEXT_TYPE_SCROLL_WHITE = 0x01
    SIMCONNECT_TEXT_TYPE_SCROLL_RED = 0x02
    SIMCONNECT_TEXT_TYPE_SCROLL_GREEN = 0x03
    SIMCONNECT_TEXT_TYPE_SCROLL_BLUE = 0x04
    SIMCONNECT_TEXT_TYPE_SCROLL_YELLOW = 0x05
    SIMCONNECT_TEXT_TYPE_SCROLL_MAGENTA = 0x06
    SIMCONNECT_TEXT_TYPE_SCROLL_CYAN = 0x07
    SIMCONNECT_TEXT_TYPE_PRINT_BLACK = 0x100
    SIMCONNECT_TEXT_TYPE_PRINT_WHITE = 0x101
    SIMCONNECT_TEXT_TYPE_PRINT_RED = 0x102
    SIMCONNECT_TEXT_TYPE_PRINT_GREEN = 0x103
    SIMCONNECT_TEXT_TYPE_PRINT_BLUE = 0x104
    SIMCONNECT_TEXT_TYPE_PRINT_YELLOW = 0x105
    SIMCONNECT_TEXT_TYPE_PRINT_MAGENTA = 0x106
    SIMCONNECT_TEXT_TYPE_PRINT_CYAN = 0x107
    SIMCONNECT_TEXT_TYPE_MENU = 0x0200


class SIMCONNECT_TEXT_RESULT(CtypesEnum):  #
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_1 = 0x00
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_2 = 0x01
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_3 = 0x02
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_4 = 0x03
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_5 = 0x04
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_6 = 0x05
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_7 = 0x06
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_8 = 0x07
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_9 = 0x08
    SIMCONNECT_TEXT_RESULT_MENU_SELECT_10 = 0x09
    SIMCONNECT_TEXT_RESULT_DISPLAYED = 0x10000
    SIMCONNECT_TEXT_RESULT_QUEUED = 0x10001
    SIMCONNECT_TEXT_RESULT_REMOVED = 0x1002
    SIMCONNECT_TEXT_RESULT_REPLACED = 0x10003
    SIMCONNECT_TEXT_RESULT_TIMEOUT = 0x10004


class SIMCONNECT_WEATHER_MODE(CtypesEnum):  #
    SIMCONNECT_WEATHER_MODE_THEME = 0x00
    SIMCONNECT_WEATHER_MODE_RWW = 0x01
    SIMCONNECT_WEATHER_MODE_CUSTOM = 0x02
    SIMCONNECT_WEATHER_MODE_GLOBAL = 0x03


class SIMCONNECT_FACILITY_LIST_TYPE(CtypesEnum):  #
    SIMCONNECT_FACILITY_LIST_TYPE_AIRPORT = 0x00
    SIMCONNECT_FACILITY_LIST_TYPE_WAYPOINT = 0x01
    SIMCONNECT_FACILITY_LIST_TYPE_NDB = 0x02
    SIMCONNECT_FACILITY_LIST_TYPE_VOR = 0x03
    SIMCONNECT_FACILITY_LIST_TYPE_COUNT = 0x04  # invalid


class SIMCONNECT_FACILITY_DATA_TYPE(CtypesEnum):
    SIMCONNECT_FACILITY_DATA_AIRPORT = 0x00
    SIMCONNECT_FACILITY_DATA_RUNWAY = 0x01
    SIMCONNECT_FACILITY_DATA_START = 0x02
    SIMCONNECT_FACILITY_DATA_FREQUENCY = 0x03
    SIMCONNECT_FACILITY_DATA_HELIPAD = 0x04
    SIMCONNECT_FACILITY_DATA_APPROACH = 0x05
    SIMCONNECT_FACILITY_DATA_APPROACH_TRANSITION = 0x06
    SIMCONNECT_FACILITY_DATA_APPROACH_LEG = 0x07
    SIMCONNECT_FACILITY_DATA_FINAL_APPROACH_LEG = 0x08
    SIMCONNECT_FACILITY_DATA_MISSED_APPROACH_LEG = 0x09
    SIMCONNECT_FACILITY_DATA_DEPARTURE = 0x0A
    SIMCONNECT_FACILITY_DATA_ARRIVAL = 0x0B
    SIMCONNECT_FACILITY_DATA_RUNWAY_TRANSITION = 0x0C
    SIMCONNECT_FACILITY_DATA_ENROUTE_TRANSITION = 0x0D
    SIMCONNECT_FACILITY_DATA_TAXI_POINT = 0x0E
    SIMCONNECT_FACILITY_DATA_TAXI_PARKING = 0x0F
    SIMCONNECT_FACILITY_DATA_TAXI_PATH = 0x10
    SIMCONNECT_FACILITY_DATA_TAXI_NAME = 0x11
    SIMCONNECT_FACILITY_DATA_JETWAY = 0x12
    SIMCONNECT_FACILITY_DATA_VOR = 0x13
    SIMCONNECT_FACILITY_DATA_NDB = 0x14
    SIMCONNECT_FACILITY_DATA_WAYPOINT = 0x15
    SIMCONNECT_FACILITY_DATA_ROUTE = 0x16
    SIMCONNECT_FACILITY_DATA_PAVEMENT = 0x17
    SIMCONNECT_FACILITY_DATA_APPROACH_LIGHTS = 0x18
    SIMCONNECT_FACILITY_DATA_VASI = 0x19
    SIMCONNECT_FACILITY_DATA_VDGS = 0x1A
    SIMCONNECT_FACILITY_DATA_HOLDING_PATTERN = 0x1B
    SIMCONNECT_FACILITY_DATA_TAXI_PARKING_AIRLINE = 0x1C


class SIMCONNECT_INPUT_EVENT_TYPE(CtypesEnum):
    SIMCONNECT_INPUT_EVENT_TYPE_DOUBLE = 0x00
    SIMCONNECT_INPUT_EVENT_TYPE_STRING = 0x01


class SIMCONNECT_FLOW_EVENT(CtypesEnum):
    SIMCONNECT_FLOW_EVENT_NONE = 0x00
    SIMCONNECT_FLOW_EVENT_FLT_LOAD = 0x01
    SIMCONNECT_FLOW_EVENT_FLT_LOADED = 0x02
    SIMCONNECT_FLOW_EVENT_TELEPORT_START = 0x03
    SIMCONNECT_FLOW_EVENT_TELEPORT_DONE = 0x04
    SIMCONNECT_FLOW_EVENT_BACK_ON_TRACK_START = 0x05
    SIMCONNECT_FLOW_EVENT_BACK_ON_TRACK_DONE = 0x06
    SIMCONNECT_FLOW_EVENT_SKIP_START = 0x07
    SIMCONNECT_FLOW_EVENT_SKIP_DONE = 0x08
    SIMCONNECT_FLOW_EVENT_BACK_TO_MAIN_MENU = 0x09
    SIMCONNECT_FLOW_EVENT_RTC_START = 0x0A
    SIMCONNECT_FLOW_EVENT_RTC_END = 0x0B
    SIMCONNECT_FLOW_EVENT_REPLAY_START = 0x0C
    SIMCONNECT_FLOW_EVENT_REPLAY_END = 0x0D
    SIMCONNECT_FLOW_EVENT_FLIGHT_START = 0x0E
    SIMCONNECT_FLOW_EVENT_FLIGHT_END = 0x0F
    SIMCONNECT_FLOW_EVENT_PLANE_CRASH = 0x10


class SIMCONNECT_VOR_FLAGS(CtypesEn):  # flags for SIMCONNECT_RECV_ID_VOR_LIST
    SIMCONNECT_RECV_ID_VOR_LIST_HAS_NAV_SIGNAL = 0x00000001  # Has Nav signal
    SIMCONNECT_RECV_ID_VOR_LIST_HAS_LOCALIZER = 0x00000002  # Has localizer
    SIMCONNECT_RECV_ID_VOR_LIST_HAS_GLIDE_SLOPE = 0x00000004  # Has Nav signal
    SIMCONNECT_RECV_ID_VOR_LIST_HAS_DME = 0x00000008  # Station has DME


# bits for the Waypoint Flags field: may be combined
class SIMCONNECT_WAYPOINT_FLAGS(CtypesEn):  #
    SIMCONNECT_WAYPOINT_NONE = 0x00  #
    SIMCONNECT_WAYPOINT_SPEED_REQUESTED = 0x04  # requested speed at waypoint is valid
    SIMCONNECT_WAYPOINT_THROTTLE_REQUESTED = 0x08  # request a specific throttle percentage
    SIMCONNECT_WAYPOINT_COMPUTE_VERTICAL_SPEED = 0x10  # compute vertical to speed to reach waypoint altitude when crossing the waypoint
    SIMCONNECT_WAYPOINT_ALTITUDE_IS_AGL = 0x20  # AltitudeIsAGL
    SIMCONNECT_WAYPOINT_ON_GROUND = 0x00100000  # place this waypoint on the ground
    SIMCONNECT_WAYPOINT_REVERSE = 0x00200000  # Back up to this waypoint. Only valid on first waypoint
    SIMCONNECT_WAYPOINT_WRAP_TO_FIRST = 0x00400000
    SIMCONNECT_WAYPOINT_ALWAYS_BACKUP = 0x00800000  # Go from first waypoint to last one moving only backwards
    SIMCONNECT_WAYPOINT_KEEP_LAST_HEADING = 0x01000000  # Object doesn't only go from waypoint to waypoint using position but it will also keep the same heading computed on the last 2 waypoints
    SIMCONNECT_WAYPOINT_YIELD_TO_USER = 0x02000000  # Object will never be too close to the player. If waypoints pass too close to the player, the object will stop and wait
    SIMCONNECT_WAYPOINT_CAN_REVERSE = 0x04000000  # This flag handles the behavior of the object if it can't reach a waypoint. By default, it will take another way and try to reach this point again. With this flag, the object will try some other methods to reach this waypoint in better condition (e.g., moving backwards)


class SIMCONNECT_EVENT_FLAG(CtypesEn):  #
    SIMCONNECT_EVENT_FLAG_DEFAULT = 0x00000000  #
    SIMCONNECT_EVENT_FLAG_FAST_REPEAT_TIMER = 0x00000001  # set event repeat timer to simulate fast repeat
    SIMCONNECT_EVENT_FLAG_SLOW_REPEAT_TIMER = 0x00000002  # set event repeat timer to simulate slow repeat
    SIMCONNECT_EVENT_FLAG_GROUPID_IS_PRIORITY = 0x00000010  # interpret GroupID parameter as priority value


class SIMCONNECT_DATA_REQUEST_FLAG(CtypesEn):  #
    SIMCONNECT_DATA_REQUEST_FLAG_DEFAULT = 0x00000000
    SIMCONNECT_DATA_REQUEST_FLAG_CHANGED = 0x00000001  # send requested data when value(s) change
    SIMCONNECT_DATA_REQUEST_FLAG_TAGGED = 0x00000002  # send requested data in tagged format


class SIMCONNECT_DATA_SET_FLAG(CtypesEn):  #
    SIMCONNECT_DATA_SET_FLAG_DEFAULT = 0x00000000
    SIMCONNECT_DATA_SET_FLAG_TAGGED = 0x00000001  # data is in tagged format


class SIMCONNECT_CREATE_CLIENT_DATA_FLAG(CtypesEn):  #
    SIMCONNECT_CREATE_CLIENT_DATA_FLAG_DEFAULT = 0x00000000  #
    SIMCONNECT_CREATE_CLIENT_DATA_FLAG_READ_ONLY = 0x00000001  # permit only ClientData creator to write into ClientData


class SIMCONNECT_CLIENT_DATA_REQUEST_FLAG(CtypesEn):  #
    SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_DEFAULT = 0x00000000  #
    SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_CHANGED = 0x00000001  # send requested ClientData when value(s) change
    SIMCONNECT_CLIENT_DATA_REQUEST_FLAG_TAGGED = 0x00000002  # send requested ClientData in tagged format


class SIMCONNECT_CLIENT_DATA_SET_FLAG(CtypesEn):  #
    SIMCONNECT_CLIENT_DATA_SET_FLAG_DEFAULT = 0x00000000  #
    SIMCONNECT_CLIENT_DATA_SET_FLAG_TAGGED = 0x00000001  # data is in tagged format


class SIMCONNECT_VIEW_SYSTEM_EVENT_DATA(CtypesEn):  # dwData contains these flags for the "View" System Event
    SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_COCKPIT_2D = 0x00000001  # 2D Panels in cockpit view
    SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_COCKPIT_VIRTUAL = 0x00000002  # Virtual (3D) panels in cockpit view
    SIMCONNECT_VIEW_SYSTEM_EVENT_DATA_ORTHOGONAL = 0x00000004  # Orthogonal (Map) view


class SIMCONNECT_SOUND_SYSTEM_EVENT_DATA(CtypesEn):  # dwData contains these flags for the "Sound" System Event
    SIMCONNECT_SOUND_SYSTEM_EVENT_DATA_MASTER = 0x00000001  # Sound Master


class SIMCONNECT_PICK_FLAGS(CtypesEn):
    SIMCONNECT_PICK_GROUND = 0x01  # pick ground/ pick result item is ground location
    SIMCONNECT_PICK_AI = 0x02  # pick AI    / pick result item is AI, (dwSimObjectID is valid)
    SIMCONNECT_PICK_SCENERY = 0x04  # pick scenery/ pick result item is scenery object (hSceneryObject is valid)
    SIMCONNECT_PICK_ALL = 0x04 | 0x02 | 0x01  # pick all / (not valid on pick result item)
    SIMCONNECT_PICK_COORDSASPIXELS = 0x08  #


# ----------------------------------------------------------------------------
#        User-defined enums
# ----------------------------------------------------------------------------
class SIMCONNECT_NOTIFICATION_GROUP_ID(
    AutoName
):  # client-defined notification group ID
    pass


class SIMCONNECT_INPUT_GROUP_ID(AutoName):  # client-defined input group ID
    pass


class SIMCONNECT_DATA_DEFINITION_ID(AutoName):  # client-defined data definition ID
    pass


class SIMCONNECT_DATA_REQUEST_ID(AutoName):  # client-defined request data ID
    pass


class SIMCONNECT_CLIENT_EVENT_ID(AutoName):  # client-defined client event ID
    EVENT_SIM_START = auto()
    EVENT_SIM_STOP = auto()
    EVENT_SIM_PAUSED = auto()
    EVENT_SIM_UNPAUSED = auto()
    EVENT_SIM_AIRCRAFT_LOADED = auto()
    pass


class SIMCONNECT_CLIENT_DATA_ID(AutoName):  # client-defined client data ID
    pass


class SIMCONNECT_CLIENT_DATA_DEFINITION_ID(
    AutoName
):  # client-defined client data definition ID
    pass


# ----------------------------------------------------------------------------
#        Struct definitions
# ----------------------------------------------------------------------------

class Struct1(Structure):
    _pack_ = 1  # implement the pragma(push, 1)


class SIMCONNECT_GUID(Structure):
    _pack_ = 1
    _fields_ = [
        ("Data1", DWORD),
        ("Data2", WORD),
        ("Data3", WORD),
        ("Data4", BYTE * 8)
    ]


class SIMCONNECT_RECV(Structure):
    _pack_ = 1
    _fields_ = [
        ("dwSize", DWORD),  # record size
        ("dwVersion", DWORD),  # interface version
        ("dwID", DWORD),  # see SIMCONNECT_RECV_ID
    ]


class SIMCONNECT_RECV_EXCEPTION(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_EXCEPTION
    UNKNOWN_SENDID = 0
    UNKNOWN_INDEX = DWORD_MAX
    _pack_ = 1
    _fields_ = [
        ("dwException", DWORD),  # see SIMCONNECT_EXCEPTION
        ("dwSendID", DWORD),  # see SimConnect_GetLastSentPacketID
        ("dwIndex", DWORD),  # index of parameter that was source of error
    ]


class SIMCONNECT_RECV_OPEN(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_OPEN
    _pack_ = 1
    _fields_ = [
        ("szApplicationName", c_char * 256),
        ("dwApplicationVersionMajor", DWORD),
        ("dwApplicationVersionMinor", DWORD),
        ("dwApplicationBuildMajor", DWORD),
        ("dwApplicationBuildMinor", DWORD),
        ("dwSimConnectVersionMajor", DWORD),
        ("dwSimConnectVersionMinor", DWORD),
        ("dwSimConnectBuildMajor", DWORD),
        ("dwSimConnectBuildMinor", DWORD),
        ("dwReserved1", DWORD),
        ("dwReserved2", DWORD),
    ]


class SIMCONNECT_RECV_QUIT(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_QUIT
    pass


class SIMCONNECT_RECV_EVENT(SIMCONNECT_RECV):  # when dwID == SIMCONNECT_RECV_ID_EVENT
    UNKNOWN_GROUP = DWORD_MAX
    _pack_ = 1
    _fields_ = [
        ("uGroupID", DWORD),
        ("uEventID", DWORD),
        ("dwData", DWORD),  # uEventID-dependent context
    ]


class SIMCONNECT_RECV_EVENT_FILENAME(
    SIMCONNECT_RECV_EVENT
):  # when dwID == SIMCONNECT_RECV_ID_EVENT_FILENAME
    _pack_ = 1
    _fields_ = [
        ("zFileName", c_char * MAX_PATH),  # uEventID-dependent context
        ("dwFlags", DWORD),
    ]


class SIMCONNECT_RECV_EVENT_OBJECT_ADDREMOVE(
    SIMCONNECT_RECV_EVENT
):  # when dwID == SIMCONNECT_RECV_ID_EVENT_FILENAME
    eObjType = SIMCONNECT_SIMOBJECT_TYPE


class SIMCONNECT_RECV_EVENT_FRAME(
    SIMCONNECT_RECV_EVENT
):  # when dwID == SIMCONNECT_RECV_ID_EVENT_FRAME
    _pack_ = 1
    _fields_ = [
        ("fFrameRate", c_float),
        ("fSimSpeed", c_float)
    ]


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_SERVER_STARTED(SIMCONNECT_RECV_EVENT):
    # when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SERVER_STARTED
    # No event specific data, for now
    pass


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_CLIENT_STARTED(SIMCONNECT_RECV_EVENT):
    # when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_CLIENT_STARTED
    # No event specific data, for now
    pass


class SIMCONNECT_RECV_EVENT_MULTIPLAYER_SESSION_ENDED(SIMCONNECT_RECV_EVENT):
    # when dwID == SIMCONNECT_RECV_ID_EVENT_MULTIPLAYER_SESSION_ENDED
    # No event specific data, for now
    pass


class SIMCONNECT_RECV_EVENT_EX1(SIMCONNECT_RECV):
    UNKNOWN_GROUP = DWORD_MAX
    # Doesn't support array so, let's list
    _pack_ = 1
    _fields_ = [
        ("uGroupID", DWORD),
        ("uEventID", DWORD),
        ("dwData0", DWORD),
        ("dwData1", DWORD),
        ("dwData2", DWORD),
        ("dwData3", DWORD),
        ("dwData4", DWORD),
    ]


# SIMCONNECT_DATA_RACE_RESULT
class SIMCONNECT_DATA_RACE_RESULT(Structure):
    _pack_ = 1
    _fields_ = [
        ("dwNumberOfRacers", DWORD),  # The total number of racers
        ("szPlayerName", c_char * MAX_PATH),  # The name of the player
        ("szSessionType", c_char * MAX_PATH),  # The type of the multiplayer session: "LAN", "GAMESPY")
        ("szAircraft", c_char * MAX_PATH),  # The aircraft type
        ("szPlayerRole", c_char * MAX_PATH),  # The player role in the mission
        ("fTotalTime", c_double),  # Total time in seconds, 0 means DNF
        ("fPenaltyTime", c_double),  # Total penalty time in seconds
        ("MissionGUID", SIMCONNECT_GUID),  # The name of the mission to execute, NULL if no mission
        ("dwIsDisqualified", c_double),  # non 0 - disqualified, 0 - not disqualified
    ]


class SIMCONNECT_RECV_EVENT_RACE_END(
    SIMCONNECT_RECV_EVENT
):  # when dwID == SIMCONNECT_RECV_ID_EVENT_RACE_END
    RacerData = SIMCONNECT_DATA_RACE_RESULT
    _pack_ = 1
    _fields_ = [("dwRacerNumber", DWORD)]  # The index of the racer the results are for


class SIMCONNECT_RECV_EVENT_RACE_LAP(
    SIMCONNECT_RECV_EVENT
):  # when dwID == SIMCONNECT_RECV_ID_EVENT_RACE_LAP
    RacerData = SIMCONNECT_DATA_RACE_RESULT
    _pack_ = 1
    _fields_ = [("dwLapIndex", DWORD)]  # The index of the lap the results are for


class SIMCONNECT_RECV_SIMOBJECT_DATA(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwObjectID", DWORD),
        ("dwDefineID", DWORD),
        ("dwFlags", DWORD),
        ("dwentrynumber", DWORD),
        ("dwoutof", DWORD),
        ("dwDefineCount", DWORD),
        ("dwData", POINTER(DWORD)),
    ]


class SIMCONNECT_RECV_SIMOBJECT_DATA_BYTYPE(SIMCONNECT_RECV_SIMOBJECT_DATA):
    _pack_ = 1
    _fields_ = []


class SIMCONNECT_RECV_CLIENT_DATA(
    SIMCONNECT_RECV_SIMOBJECT_DATA
):  # when dwID == SIMCONNECT_RECV_ID_CLIENT_DATA
    _pack_ = 1
    _fields_ = []


class SIMCONNECT_RECV_WEATHER_OBSERVATION(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_WEATHER_OBSERVATION
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        (
            "szMetar",
            c_char * MAX_METAR_LENGTH.value,
        ),  # Variable length string whose maximum size is MAX_METAR_LENGTH
    ]


class SIMCONNECT_RECV_CLOUD_STATE(SIMCONNECT_RECV):
    # when dwID == SIMCONNECT_RECV_ID_CLOUD_STATE
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwArraySize", DWORD),
        # SIMCONNECT_FIXEDTYPE_DATAV(BYTE,    rgbData, dwArraySize, U1 /*member of UnmanagedType enum*/ , System::Byte /*cli type*/);
    ]


class SIMCONNECT_RECV_ASSIGNED_OBJECT_ID(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_ASSIGNED_OBJECT_ID
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwObjectID", DWORD)
    ]


class SIMCONNECT_RECV_RESERVED_KEY(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_RESERVED_KEY
    _pack_ = 1
    _fields_ = [
        ("szChoiceReserved", c_char * 30),
        ("szReservedKey", c_char * 50)
    ]


class SIMCONNECT_RECV_SYSTEM_STATE(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_SYSTEM_STATE
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwInteger", DWORD),
        ("fFloat", c_float),
        ("szString", c_char * MAX_PATH),
    ]


class SIMCONNECT_RECV_CUSTOM_ACTION(SIMCONNECT_RECV_EVENT):  #
    _pack_ = 1
    _fields_ = [
        ("guidInstanceId", SIMCONNECT_GUID),  # Instance id of the action that executed
        ("dwWaitForCompletion", DWORD),  # Wait for completion flag on the action
        ("szPayLoad", c_char),  # Variable length string payload associated with the mission action.
    ]


class SIMCONNECT_RECV_EVENT_WEATHER_MODE(SIMCONNECT_RECV_EVENT):  #
    _pack_ = 1
    _fields_ = []  # No event specific data - the new weather mode is in the base structure dwData member.


# SIMCONNECT_RECV_FACILITIES_LIST
class SIMCONNECT_RECV_FACILITIES_LIST(SIMCONNECT_RECV):  #
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwArraySize", DWORD),
        ("dwEntryNumber", DWORD),  # when the array of items is too big for one send, which send this is (0..dwOutOf-1)
        ("dwOutOf", DWORD),  # total number of transmissions the list is chopped into
    ]


class SIMCONNECT_RECV_LIST_TEMPLATE(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("dwArraySize", DWORD),
        ("dwEntryNumber", DWORD),  # when the array of items is too big for one send, which send this is (0..dwOutOf-1)
        ("dwOutOf", DWORD),  # total number of transmissions the list is chopped into
    ]


# SIMCONNECT_DATA_FACILITY_AIRPORT
class SIMCONNECT_DATA_FACILITY_AIRPORT(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("Ident", c_char * 9),  # ICAO of the object
        ("Region", c_char * 3),  # ICAO of the object
        ("Latitude", c_double),  # degrees
        ("Longitude", c_double),  # degrees
        ("Altitude", c_double),  # meters
    ]


# SIMCONNECT_RECV_AIRPORT_LIST
class SIMCONNECT_RECV_AIRPORT_LIST(SIMCONNECT_RECV_FACILITIES_LIST):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_DATA_FACILITY_AIRPORT),
    ]


# SIMCONNECT_DATA_FACILITY_WAYPOINT
class SIMCONNECT_DATA_FACILITY_WAYPOINT(SIMCONNECT_DATA_FACILITY_AIRPORT):  #
    _pack_ = 1
    _fields_ = [("fMagVar", c_float)]  # Magvar in degrees


class SIMCONNECT_RECV_WAYPOINT_LIST(SIMCONNECT_RECV_FACILITIES_LIST):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_DATA_FACILITY_WAYPOINT),
    ]


# SIMCONNECT_DATA_FACILITY_NDB
class SIMCONNECT_DATA_FACILITY_NDB(SIMCONNECT_DATA_FACILITY_WAYPOINT):  #
    _pack_ = 1
    _fields_ = [("fFrequency", DWORD)]  # frequency in Hz


# SIMCONNECT_RECV_NDB_LIST
class SIMCONNECT_RECV_NDB_LIST(SIMCONNECT_RECV_FACILITIES_LIST):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_DATA_FACILITY_NDB),
    ]


# SIMCONNECT_DATA_FACILITY_VOR
class SIMCONNECT_DATA_FACILITY_VOR(SIMCONNECT_DATA_FACILITY_NDB):  #
    _pack_ = 1
    _fields_ = [
        ("Flags", DWORD),  # SIMCONNECT_VOR_FLAGS
        ("fLocalizer", c_float),  # Localizer in degrees
        ("GlideLat", c_double),  # Glide Slope Location (deg, deg, meters)
        ("GlideLon", c_double),  #
        ("GlideAlt", c_double),  #
        ("fGlideSlopeAngle", c_float),  # Glide Slope in degrees
    ]


# SIMCONNECT_RECV_VOR_LIST
class SIMCONNECT_RECV_VOR_LIST(SIMCONNECT_RECV_FACILITIES_LIST):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_DATA_FACILITY_VOR),
    ]


class SIMCONNECT_RECV_FACILITY_DATA(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("UserRequestId", DWORD),
        ("UniqueRequestId", DWORD),
        ("ParentUniqueRequestId", DWORD),
        ("Type", DWORD),
        ("IsListItem", DWORD),
        ("ItemIndex", DWORD),
        ("ListSize", DWORD),
        ("Data", DWORD),
    ]


class SIMCONNECT_RECV_FACILITY_DATA_END(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("RequestId", DWORD),
    ]


class ICAO(Structure):
    _pack_ = 1
    _fields_ = [
        ("Type", c_char),
        ("Ident", c_char * (8 + 1)),
        ("Region", c_char * (2 + 1)),
        ("Airport", c_char * (4 + 1)),
    ]


# SIMCONNECT_DATA_LATLONALT
class SIMCONNECT_DATA_LATLONALT(Structure):
    _pack_ = 1
    _fields_ = [
        ("Latitude", c_double),
        ("Longitude", c_double),
        ("Altitude", c_double),
    ]


class SIMCONNECT_DATA_PBH(Structure):
    _pack_ = 1
    _fields_ = [
        ("Pitch", c_float),
        ("Bank", c_float),
        ("Heading", c_float),
    ]


class SIMCONNECT_FACILITY_MINIMAL(Structure):
    _pack_ = 1
    _fields_ = [
        ("icao", ICAO),
        ("lla", SIMCONNECT_DATA_LATLONALT),
    ]


class SIMCONNECT_RECV_FACILITY_MINIMAL_LIST(SIMCONNECT_RECV_LIST_TEMPLATE):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_FACILITY_MINIMAL),
    ]


class SIMCONNECT_RECV_PICK(
    SIMCONNECT_RECV
):  # when dwID == SIMCONNECT_RECV_ID_RESERVED_KEY
    _pack_ = 1
    _fields_ = [
        ("hContext", HANDLE),
        ("dwFlags", DWORD),
        ("Latitude", c_double),  # degrees
        ("Longitude", c_double),  # degrees
        ("Altitude", c_double),  # feet
        ("xPos", c_int),  # reserved
        ("yPos", c_int),  # reserved
        ("dwSimObjectID", DWORD),
        ("hSceneryObject", HANDLE),
        ("dwentrynumber", DWORD),  # if multiple objects returned, this is number <entrynumber> out of <outof>.
        ("dwoutof", DWORD),  # note:  starts with 1, not 0.
    ]


# SIMCONNECT_DATATYPE_INITPOSITION
class SIMCONNECT_DATA_INITPOSITION(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("Latitude", c_double),  # degrees
        ("Longitude", c_double),  # degrees
        ("Altitude", c_double),  # feet
        ("Pitch", c_double),  # degrees
        ("Bank", c_double),  # degrees
        ("Heading", c_double),  # degrees
        ("OnGround", DWORD),  # 1=force to be on the ground
        ("Airspeed", DWORD),  # knots
    ]


# SIMCONNECT_DATATYPE_MARKERSTATE
class SIMCONNECT_DATA_MARKERSTATE(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("szMarkerName", c_char * 64),
        ("dwMarkerState", DWORD)
    ]


# SIMCONNECT_DATATYPE_WAYPOINT
class SIMCONNECT_DATA_WAYPOINT(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("Latitude", c_double),  # degrees
        ("Longitude", c_double),  # degrees
        ("Altitude", c_double),  # feet
        ("Flags", c_ulong),
        ("ktsSpeed", c_double),  # knots
        ("percentThrottle", c_double),
    ]


# SIMCONNECT_DATA_LATLONALT
class SIMCONNECT_DATA_LATLONALT(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("Latitude", c_double),
        ("Longitude", c_double),
        ("Altitude", c_double)
    ]


# SIMCONNECT_DATA_XYZ
class SIMCONNECT_DATA_XYZ(Structure):  #
    _pack_ = 1
    _fields_ = [
        ("x", c_double),
        ("y", c_double),
        ("z", c_double)
    ]


class SIMCONNECT_JETWAY_DATA(Structure):
    _pack_ = 1
    _fields_ = [
        ("AirportIcao", c_char * 8),
        ("ParkingIndex", c_int),
        ("Lla", SIMCONNECT_DATA_LATLONALT),
        ("Pbh", SIMCONNECT_DATA_PBH),
        ("Status", c_int),
        ("Door", c_int),
        ("ExitDoorRelativePos", SIMCONNECT_DATA_XYZ),
        ("MainHandlePos", SIMCONNECT_DATA_XYZ),
        ("SecondaryHandle", SIMCONNECT_DATA_XYZ),
        ("WheelGroundLock", SIMCONNECT_DATA_XYZ),
        ("JetwayObjectId", DWORD),
        ("AttachedObjectId", DWORD),
    ]


class SIMCONNECT_RECV_JETWAY_DATA(SIMCONNECT_RECV_LIST_TEMPLATE):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_JETWAY_DATA),
    ]


class SIMCONNECT_RECV_ACTION_CALLBACK(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("szActionID", c_char * (MAX_PATH)),
        ("cbRequestId", DWORD),
    ]


class SIMCONNECT_INPUT_EVENT_DESCRIPTOR(Structure):
    _pack_ = 1
    _fields_ = [
        ("Name", c_char * 64),  # Input event name
        ("Hash", c_uint64),  # Hash
        ("eType", DWORD),
    ]


class SIMCONNECT_RECV_ENUMERATE_INPUT_EVENTS(SIMCONNECT_RECV_LIST_TEMPLATE):
    _pack_ = 1
    _fields_ = [
        ("rgData", POINTER(SIMCONNECT_INPUT_EVENT_DESCRIPTOR)),
    ]


class SIMCONNECT_DATAV(Union):
    _fields_ = [
        ("flt_value", c_double),  # For DOUBLE type
        ("str_value", c_char_p)  # For STRING type
    ]


class SIMCONNECT_RECV_GET_INPUT_EVENT(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("dwRequestID", DWORD),
        ("eType", DWORD),
        ("Value", SIMCONNECT_DATAV),
    ]


class SIMCONNECT_RECV_SUBSCRIBE_INPUT_EVENT(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("Hash", c_uint64),
        ("eType", DWORD),
        ("Value", POINTER(DWORD)),
    ]


class SIMCONNECT_RECV_ENUMERATE_INPUT_EVENT_PARAMS(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("Hash", c_uint64),
        ("Value", c_char * (MAX_PATH)),
    ]


class SIMCONNECT_VERSION_BASE_TYPE(Structure):
    _pack_ = 1
    _fields_ = [
        ("Major", c_short),
        ("Minor", c_short),
        ("Revision", c_short),
        ("Build", c_short),
    ]


class SIMCONNECT_CONTROLLER_ITEM(Structure):
    _pack_ = 1
    _fields_ = [
        ("DeviceName", c_char * 256),
        ("DeviceId", c_int),
        ("ProductId", c_int),
        ("CompositeID", c_int),
        ("HardwareVersion", SIMCONNECT_VERSION_BASE_TYPE),
    ]


class SIMCONNECT_RECV_CONTROLLERS_LIST(SIMCONNECT_RECV_LIST_TEMPLATE):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_CONTROLLER_ITEM),
    ]


class SIMCONNECT_ENUMERATE_SIMOBJECT_LIVERY(Structure):
    _pack_ = 1
    _fields_ = [
        ("AircraftTitle", c_char * 256),
        ("LiveryName", c_char * 256),
    ]


class SIMCONNECT_RECV_ENUMERATE_SIMOBJECT_AND_LIVERY_LIST(SIMCONNECT_RECV_LIST_TEMPLATE):
    _pack_ = 1
    _fields_ = [
        ("rgData", SIMCONNECT_ENUMERATE_SIMOBJECT_LIVERY),
    ]


class SIMCONNECT_RECV_FLOW_EVENT(SIMCONNECT_RECV):
    _pack_ = 1
    _fields_ = [
        ("FlowEvent", SIMCONNECT_FLOW_EVENT),
        ("FltPath", c_char * 256),
    ]


SIMCONNECT_DATATYPE_MAP = {
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT32: c_int,  # 32-bit integer
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_INT64: c_int64,  # 64-bit integer
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT32: c_float,  # 32-bit float
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_FLOAT64: c_double,  # 64-bit float (double)
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING8: c_char * 8,  # 8-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING32: c_char * 32,  # 32-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING64: c_char * 64,  # 64-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING128: c_char * 128,  # 128-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING256: c_char * 256,  # 256-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRING260: c_char * 260,  # 260-byte string
    SIMCONNECT_DATATYPE.SIMCONNECT_DATATYPE_STRINGV: c_char * 1,  # Variable-length string (placeholder)
}
