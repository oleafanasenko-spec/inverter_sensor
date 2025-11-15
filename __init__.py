import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_ID,
    CONF_NAME,
    UNIT_VOLT,
    UNIT_AMPERE,
    UNIT_HERTZ,
    UNIT_WATT,
    ICON_THERMOMETER,
    ICON_CURRENT_AC,
    ICON_FLASH,
    ICON_POWER,
    STATE_CLASS_MEASUREMENT,
)

CONF_UART_ID = "uart_id"

# Константи для ключів у YAML
CONF_PROTOCOL_N = "protocol_n"
CONF_GRID_VOLTAGE = "grid_voltage"
CONF_GRID_CURRENT = "grid_current"
CONF_AC_OUTPUT_VOLTAGE = "ac_output_voltage"
CONF_AC_OUTPUT_FREQ = "ac_output_freq"
CONF_AC_OUTPUT_CURRENT = "ac_output_current"
CONF_AC_APPARENT_POWER = "ac_apparent_power"
CONF_AC_ACTIVE_POWER = "ac_active_power"
CONF_BATT_RATING_VOLTAGE = "batt_rating_voltage"
CONF_BATT_RECHARGE_VOLTAGE = "batt_recharge_voltage"
CONF_BATT_UNDERVOLTAGE = "batt_undervoltage"
CONF_BATT_BULK_VOLTAGE = "batt_bulk_voltage"
CONF_BATT_FLOAT_VOLTAGE = "batt_float_voltage"
CONF_BATT_TYPE = "batt_type"
CONF_MAX_AC_CHARGE_CURRENT = "max_ac_charge_current"
CONF_MAX_CHARGE_CURRENT = "max_charge_current"
CONF_INPUT_VOLTAGE_RANGE = "input_voltage_range"
CONF_OUTPUT_SOURCE_PRIORITY = "output_source_priority"
CONF_CHARGER_SOURCE_PRIORITY = "charger_source_priority"
CONF_PARALLEL_MAX_NUM = "parallel_max_num"
CONF_MACHINE_TYPE = "machine_type"
CONF_TOPOLOGY = "topology"
CONF_OUTPUT_MODE = "output_mode"
CONF_BATT_REDISCHARGE_VOLTAGE = "batt_redischarge_voltage"
CONF_PV_OK_CONDITION = "pv_ok_condition"

inverter_sensor_ns = cg.esphome_ns.namespace("inverter_sensor")
InverterSensor = inverter_sensor_ns.class_("InverterSensor", cg.PollingComponent)

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(InverterSensor),
        cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
        # Сенсори з defaults (створюються з дефолтним name, якщо не в YAML)
        cv.Optional(CONF_PROTOCOL_N, default={CONF_NAME: "Protocol N"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_GRID_VOLTAGE, default={CONF_NAME: "Grid Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_THERMOMETER,
            accuracy_decimals=1,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_GRID_CURRENT, default={CONF_NAME: "Grid Current"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=2,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_AC_OUTPUT_VOLTAGE, default={CONF_NAME: "AC Output Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            icon=ICON_THERMOMETER,
            accuracy_decimals=1,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_AC_OUTPUT_FREQ, default={CONF_NAME: "AC Output Frequency"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_HERTZ,
            icon=ICON_FLASH,
            accuracy_decimals=1,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_AC_OUTPUT_CURRENT, default={CONF_NAME: "AC Output Current"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=2,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_AC_APPARENT_POWER, default={CONF_NAME: "AC Apparent Power"}): sensor.sensor_schema(
            unit_of_measurement="VA",
            icon=ICON_POWER,
            accuracy_decimals=0,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_AC_ACTIVE_POWER, default={CONF_NAME: "AC Active Power"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_WATT,
            icon=ICON_POWER,
            accuracy_decimals=0,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional(CONF_BATT_RATING_VOLTAGE, default={CONF_NAME: "Battery Rating Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_BATT_RECHARGE_VOLTAGE, default={CONF_NAME: "Battery Recharge Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_BATT_UNDERVOLTAGE, default={CONF_NAME: "Battery Undervoltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_BATT_BULK_VOLTAGE, default={CONF_NAME: "Battery Bulk Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_BATT_FLOAT_VOLTAGE, default={CONF_NAME: "Battery Float Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_BATT_TYPE, default={CONF_NAME: "Battery Type"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_MAX_AC_CHARGE_CURRENT, default={CONF_NAME: "Max AC Charge Current"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_MAX_CHARGE_CURRENT, default={CONF_NAME: "Max Charge Current"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_INPUT_VOLTAGE_RANGE, default={CONF_NAME: "Input Voltage Range"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_OUTPUT_SOURCE_PRIORITY, default={CONF_NAME: "Output Source Priority"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_CHARGER_SOURCE_PRIORITY, default={CONF_NAME: "Charger Source Priority"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_PARALLEL_MAX_NUM, default={CONF_NAME: "Parallel Max Num"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_MACHINE_TYPE, default={CONF_NAME: "Machine Type"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_TOPOLOGY, default={CONF_NAME: "Topology"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_OUTPUT_MODE, default={CONF_NAME: "Output Mode"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional(CONF_BATT_REDISCHARGE_VOLTAGE, default={CONF_NAME: "Battery Redischarge Voltage"}): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
        ),
        cv.Optional(CONF_PV_OK_CONDITION, default={CONF_NAME: "PV OK Condition"}): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
    }
).extend(cv.polling_component_schema("10s"))

async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    # Підключаємо UART
    uart_comp = await cg.get_variable(config[CONF_UART_ID])
    cg.add(var.set_uart(uart_comp))
    
    # Створюємо сенсори (завжди, з дефолтом якщо не в YAML)
    sens = await sensor.new_sensor(config.get(CONF_PROTOCOL_N))
    cg.add(var.set_protocol_n(sens))
    sens = await sensor.new_sensor(config.get(CONF_GRID_VOLTAGE))
    cg.add(var.set_grid_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_GRID_CURRENT))
    cg.add(var.set_grid_current(sens))
    sens = await sensor.new_sensor(config.get(CONF_AC_OUTPUT_VOLTAGE))
    cg.add(var.set_ac_output_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_AC_OUTPUT_FREQ))
    cg.add(var.set_ac_output_freq(sens))
    sens = await sensor.new_sensor(config.get(CONF_AC_OUTPUT_CURRENT))
    cg.add(var.set_ac_output_current(sens))
    sens = await sensor.new_sensor(config.get(CONF_AC_APPARENT_POWER))
    cg.add(var.set_ac_apparent_power(sens))
    sens = await sensor.new_sensor(config.get(CONF_AC_ACTIVE_POWER))
    cg.add(var.set_ac_active_power(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_RATING_VOLTAGE))
    cg.add(var.set_batt_rating_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_RECHARGE_VOLTAGE))
    cg.add(var.set_batt_recharge_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_UNDERVOLTAGE))
    cg.add(var.set_batt_undervoltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_BULK_VOLTAGE))
    cg.add(var.set_batt_bulk_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_FLOAT_VOLTAGE))
    cg.add(var.set_batt_float_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_TYPE))
    cg.add(var.set_batt_type(sens))
    sens = await sensor.new_sensor(config.get(CONF_MAX_AC_CHARGE_CURRENT))
    cg.add(var.set_max_ac_charge_current(sens))
    sens = await sensor.new_sensor(config.get(CONF_MAX_CHARGE_CURRENT))
    cg.add(var.set_max_charge_current(sens))
    sens = await sensor.new_sensor(config.get(CONF_INPUT_VOLTAGE_RANGE))
    cg.add(var.set_input_voltage_range(sens))
    sens = await sensor.new_sensor(config.get(CONF_OUTPUT_SOURCE_PRIORITY))
    cg.add(var.set_output_source_priority(sens))
    sens = await sensor.new_sensor(config.get(CONF_CHARGER_SOURCE_PRIORITY))
    cg.add(var.set_charger_source_priority(sens))
    sens = await sensor.new_sensor(config.get(CONF_PARALLEL_MAX_NUM))
    cg.add(var.set_parallel_max_num(sens))
    sens = await sensor.new_sensor(config.get(CONF_MACHINE_TYPE))
    cg.add(var.set_machine_type(sens))
    sens = await sensor.new_sensor(config.get(CONF_TOPOLOGY))
    cg.add(var.set_topology(sens))
    sens = await sensor.new_sensor(config.get(CONF_OUTPUT_MODE))
    cg.add(var.set_output_mode(sens))
    sens = await sensor.new_sensor(config.get(CONF_BATT_REDISCHARGE_VOLTAGE))
    cg.add(var.set_batt_redischarge_voltage(sens))
    sens = await sensor.new_sensor(config.get(CONF_PV_OK_CONDITION))
    cg.add(var.set_pv_ok_condition(sens))