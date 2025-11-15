#pragma once

#include "esphome.h"

namespace esphome {
namespace inverter_sensor {

class InverterSensor : public PollingComponent {
 public:
  // 26 сенсорів
  sensor::Sensor *protocol_n{nullptr};
  sensor::Sensor *grid_voltage{nullptr};
  sensor::Sensor *grid_current{nullptr};
  sensor::Sensor *ac_output_voltage{nullptr};
  sensor::Sensor *ac_output_freq{nullptr};
  sensor::Sensor *ac_output_current{nullptr};
  sensor::Sensor *ac_apparent_power{nullptr};
  sensor::Sensor *ac_active_power{nullptr};
  sensor::Sensor *batt_rating_voltage{nullptr};
  sensor::Sensor *batt_recharge_voltage{nullptr};
  sensor::Sensor *batt_undervoltage{nullptr};
  sensor::Sensor *batt_bulk_voltage{nullptr};
  sensor::Sensor *batt_float_voltage{nullptr};
  sensor::Sensor *batt_type{nullptr};
  sensor::Sensor *max_ac_charge_current{nullptr};
  sensor::Sensor *max_charge_current{nullptr};
  sensor::Sensor *input_voltage_range{nullptr};
  sensor::Sensor *output_source_priority{nullptr};
  sensor::Sensor *charger_source_priority{nullptr};
  sensor::Sensor *parallel_max_num{nullptr};
  sensor::Sensor *machine_type{nullptr};
  sensor::Sensor *topology{nullptr};
  sensor::Sensor *output_mode{nullptr};
  sensor::Sensor *batt_redischarge_voltage{nullptr};
  sensor::Sensor *pv_ok_condition{nullptr};

  UARTComponent *uart_{nullptr};

  // Set-методи для кожного сенсора (для Python)
  void set_protocol_n(sensor::Sensor *protocol_n) { this->protocol_n = protocol_n; }
  void set_grid_voltage(sensor::Sensor *grid_voltage) { this->grid_voltage = grid_voltage; }
  void set_grid_current(sensor::Sensor *grid_current) { this->grid_current = grid_current; }
  void set_ac_output_voltage(sensor::Sensor *ac_output_voltage) { this->ac_output_voltage = ac_output_voltage; }
  void set_ac_output_freq(sensor::Sensor *ac_output_freq) { this->ac_output_freq = ac_output_freq; }
  void set_ac_output_current(sensor::Sensor *ac_output_current) { this->ac_output_current = ac_output_current; }
  void set_ac_apparent_power(sensor::Sensor *ac_apparent_power) { this->ac_apparent_power = ac_apparent_power; }
  void set_ac_active_power(sensor::Sensor *ac_active_power) { this->ac_active_power = ac_active_power; }
  void set_batt_rating_voltage(sensor::Sensor *batt_rating_voltage) { this->batt_rating_voltage = batt_rating_voltage; }
  void set_batt_recharge_voltage(sensor::Sensor *batt_recharge_voltage) { this->batt_recharge_voltage = batt_recharge_voltage; }
  void set_batt_undervoltage(sensor::Sensor *batt_undervoltage) { this->batt_undervoltage = batt_undervoltage; }
  void set_batt_bulk_voltage(sensor::Sensor *batt_bulk_voltage) { this->batt_bulk_voltage = batt_bulk_voltage; }
  void set_batt_float_voltage(sensor::Sensor *batt_float_voltage) { this->batt_float_voltage = batt_float_voltage; }
  void set_batt_type(sensor::Sensor *batt_type) { this->batt_type = batt_type; }
  void set_max_ac_charge_current(sensor::Sensor *max_ac_charge_current) { this->max_ac_charge_current = max_ac_charge_current; }
  void set_max_charge_current(sensor::Sensor *max_charge_current) { this->max_charge_current = max_charge_current; }
  void set_input_voltage_range(sensor::Sensor *input_voltage_range) { this->input_voltage_range = input_voltage_range; }
  void set_output_source_priority(sensor::Sensor *output_source_priority) { this->output_source_priority = output_source_priority; }
  void set_charger_source_priority(sensor::Sensor *charger_source_priority) { this->charger_source_priority = charger_source_priority; }
  void set_parallel_max_num(sensor::Sensor *parallel_max_num) { this->parallel_max_num = parallel_max_num; }
  void set_machine_type(sensor::Sensor *machine_type) { this->machine_type = machine_type; }
  void set_topology(sensor::Sensor *topology) { this->topology = topology; }
  void set_output_mode(sensor::Sensor *output_mode) { this->output_mode = output_mode; }
  void set_batt_redischarge_voltage(sensor::Sensor *batt_redischarge_voltage) { this->batt_redischarge_voltage = batt_redischarge_voltage; }
  void set_pv_ok_condition(sensor::Sensor *pv_ok_condition) { this->pv_ok_condition = pv_ok_condition; }

  void set_uart(UARTComponent *uart) { uart_ = uart; }

  void setup() override {
    // Нічого не створюй тут — сенсори вже зареєстровані з Python
    // Якщо потрібно, ініціалізуй UART: uart_->setup();
  }

  void update() override {
    // Тут читай UART і парси дані. Приклад з тестовим парсингом:
    // uint8_t data[256];
    // size_t len = uart_->read_bytes(data, 256, 1000);  // Читай з таймаутом
    // Якщо len > 0, парси data (залежно від протоколу інвертора, наприклад Modbus)
    // Заміни на реальний парсинг, наприклад:
    // float grid_volt = parse_grid_voltage(data);
    // if (grid_voltage) grid_voltage->publish_state(grid_volt);
    
    // Тестові значення для перевірки (заміни на реальні)
    if (protocol_n) protocol_n->publish_state(1.0f);  // Приклад для protocol_n
    if (grid_voltage) grid_voltage->publish_state(230.5f);
    if (grid_current) grid_current->publish_state(10.2f);
    if (ac_output_voltage) ac_output_voltage->publish_state(220.0f);
    if (ac_output_freq) ac_output_freq->publish_state(50.0f);
    if (ac_output_current) ac_output_current->publish_state(5.1f);
    if (ac_apparent_power) ac_apparent_power->publish_state(1122.0f);
    if (ac_active_power) ac_active_power->publish_state(1000.0f);
    if (batt_rating_voltage) batt_rating_voltage->publish_state(48.0f);
    if (batt_recharge_voltage) batt_recharge_voltage->publish_state(54.0f);
    if (batt_undervoltage) batt_undervoltage->publish_state(42.0f);
    if (batt_bulk_voltage) batt_bulk_voltage->publish_state(56.4f);
    if (batt_float_voltage) batt_float_voltage->publish_state(54.0f);
    if (batt_type) batt_type->publish_state(1.0f);  // Приклад для типу (enum-like)
    if (max_ac_charge_current) max_ac_charge_current->publish_state(20.0f);
    if (max_charge_current) max_charge_current->publish_state(100.0f);
    if (input_voltage_range) input_voltage_range->publish_state(0.0f);  // Приклад для range (enum)
    if (output_source_priority) output_source_priority->publish_state(0.0f);  // Enum
    if (charger_source_priority) charger_source_priority->publish_state(2.0f);  // Enum
    if (parallel_max_num) parallel_max_num->publish_state(6.0f);
    if (machine_type) machine_type->publish_state(0.0f);  // Enum
    if (topology) topology->publish_state(1.0f);  // Enum
    if (output_mode) output_mode->publish_state(0.0f);  // Enum
    if (batt_redischarge_voltage) batt_redischarge_voltage->publish_state(52.0f);
    if (pv_ok_condition) pv_ok_condition->publish_state(1.0f);  // Enum
  }
};

}  // namespace inverter_sensor
}  // namespace esphome