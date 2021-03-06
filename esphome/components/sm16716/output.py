import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import output
from esphome.const import CONF_CHANNEL, CONF_ID
from . import SM16716

DEPENDENCIES = ['sm16716']

Channel = SM16716.class_('Channel', output.FloatOutput)

CONF_SM16716_ID = 'sm16716_id'
CONFIG_SCHEMA = output.FLOAT_OUTPUT_SCHEMA.extend({
    cv.GenerateID(CONF_SM16716_ID): cv.use_id(SM16716),
    cv.Required(CONF_ID): cv.declare_id(Channel),
    cv.Required(CONF_CHANNEL): cv.int_range(min=0, max=65535),
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield output.register_output(var, config)

    parent = yield cg.get_variable(config[CONF_SM16716_ID])
    cg.add(var.set_parent(parent))
    cg.add(var.set_channel(config[CONF_CHANNEL]))
