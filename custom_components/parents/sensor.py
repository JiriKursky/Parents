import logging
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import (
    CONF_SENSORS
)
from inspect import currentframe, getframeinfo
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity

DOMAIN = 'parents'
ENTITY_ID_FORMAT = 'sensor.{}'
_LOGGER = logging.getLogger(__name__)

def my_debug(s):
    cf = currentframe()
    line = cf.f_back.f_lineno
    if s is None:
        s = ''
    _LOGGER.debug("line: {} -> {}".format(line, s))

def kontrolaCasy(hodnota):
    return hodnota

SENSOR_SCHEMA = vol.Schema({
    vol.Required('school_end'): kontrolaCasy
})

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_SENSORS):  cv.schema_with_slug_keys(SENSOR_SCHEMA)
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    sensors = config.get(CONF_SENSORS)
    
    entities = []
    for object_id, pars in sensors.items():        
        entity = ParentSensor(hass, object_id, pars)
        entities.append(entity)
    async_add_entities(entities, True)
    

class ParentSensor(Entity):
    """Representation of a Parent Sensor."""

    def __init__(self, hass, object_id,  pars):        
        self.entity_id = ENTITY_ID_FORMAT.format(object_id)

    @property
    def should_poll(self):
        """If entity should be polled."""
        # Has its own timer for refreshing
        return True
    
    @property
    def state(self):
        """Return the state of the sensor."""
        return "yes"

    @property
    def available(self):
        """Return True if entity is available."""
        return True

