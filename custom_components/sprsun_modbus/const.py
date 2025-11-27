"""Constants for SPRSUN Heat Pump Modbus integration."""

DOMAIN = "sprsun_modbus"

# Config options
CONF_MODBUS_TYPE = "modbus_type"
CONF_MODBUS_SERIAL = "serial"
CONF_MODBUS_TCP = "tcp"
CONF_MODBUS_UDP = "udp"
CONF_SERIAL_PORT = "serial_port"
CONF_BAUDRATE = "baudrate"
CONF_SLAVE_ID = "slave_id"
CONF_REGISTER_OFFSET = "register_offset"

# Default values
DEFAULT_PORT = "/dev/ttyUSB0"
DEFAULT_BAUDRATE = 19200
DEFAULT_SLAVE_ID = 1
DEFAULT_TCP_PORT = 4196
DEFAULT_SCAN_INTERVAL = 30
DEFAULT_REGISTER_OFFSET = 0

# ============================================================================
# HOLDING REGISTERS (40001+)
# ============================================================================

REG_WORK_MODE = 0  # 40001 - Mode setP
REG_HEATING_SETPOINT = 1  # 40002 - Heat SetP
REG_COOLING_SETPOINT = 2  # 40003 - Cool SetP
REG_HOTWATER_SETPOINT = 3  # 40004 - Hotwater SetP
REG_HW_START_DIFF = 4  # 40005 - hotwater_start_diff
REG_HW_STOP_DIFF = 5  # 40006 - hotwater_stop_diff
REG_CH_START_DIFF = 6  # 40007 - heat/cool start_Diff
REG_CH_STOP_DIFF = 7  # 40008 - heat/cool stop_Diff
REG_PUMP_START_INTERVAL = 8  # 40009 - Pump Start Interval
REG_PUMP_MODE = 11  # 40012 - Pump Mode
REG_FAN_MODE = 12  # 40013 - Fan Mode
REG_COMP_DELAY = 13  # 40014 - E/H comp.delay
REG_EXT_TEMP_SETP = 14  # 40015 - Ext.temp.setp.
REG_YEAR = 182  # 40183 - Year
REG_MONTH = 183  # 40184 - Month
REG_DAY = 184  # 40185 - Day
REG_HOUR = 185  # 40186 - Hour
REG_MINUTE = 186  # 40187 - Minute
REG_WEEK = 187  # 40188 - Week
REG_INLET_TEMP = 188  # 40189 - Inlet Temp.
REG_OUTLET_TEMP = 189  # 40190 - Outlet Temp.
REG_AMBIENT_TEMP = 190  # 40191 - Amb.Temp.
REG_DISCHARGE_TEMP = 191  # 40192 - Disch.gas Temp.
REG_SUCTION_TEMP = 192  # 40193 - Suct.gas Temp.
REG_DISCHARGE_PRESS = 193  # 40194 - Disch.press
REG_SUCTION_PRESS = 194  # 40195 - Suct.press
REG_HOTWATER_TEMP = 195  # 40196 - hotwater temp
REG_COIL_TEMP = 196  # 40197 - Coil Temp.
REG_FAN_OUTPUT = 197  # 40198 - Fan output(%)
REG_PUMP_OUTPUT = 198  # 40199 - Pump out(%)  
REG_DC_FAN1_OUTPUT = 199  # 40200 - Dc Fan1 Output
REG_DC_FAN1_FEEDBACK = 200  # 40201 - Fan2 RPM
REG_DC_FAN2_OUTPUT = 201  # 40202 - Dc Fan2 Output
REG_DC_FAN2_FEEDBACK = 202  # 40203 - Fan1 RPM
REG_REQUIRED_CAP = 203  # 40204 - Required Cap
REG_ACTUAL_CAP = 204  # 40205 - Actual Cap
REG_ACTUAL_SPEED = 205  # 40206 - COMP.RPM
REG_EEV_OPENING = 207  # 40208 - EEV1 Steps
REG_COMP_STATUS = 209  # 40210 - Comp Status
REG_COMP_PROTECTION = 210  # 40211 - Comp Protection
REG_SUCTION_SH = 211  # 40212 - Suction Sh
REG_UNIT_RUN_MODE = 215  # 40216 - unit run mode
REG_STATUS = 217  # 40218 - Status
REG_TZ1_MON_ON_HOUR = 218  # 40219 - Timezone1 Mon. ON: hour
REG_TZ1_MON_ON_MIN = 219  # 40220 - Timezone1 Mon. ON: minute
REG_TZ1_MON_OFF_HOUR = 220  # 40221 - Timezone1 Tue. ON: hour
REG_TZ1_MON_OFF_MIN = 221  # 40222 - Timezone1 Tue. ON: minute
REG_TZ1_TUE_ON_HOUR = 222  # 40223 - Timezone1 Wed. ON: hour
REG_TZ1_TUE_ON_MIN = 223  # 40224 - Timezone1 Wed. ON: minute
REG_TZ1_TUE_OFF_HOUR = 224  # 40225 - Timezone1 Thu. ON: hour
REG_TZ1_TUE_OFF_MIN = 225  # 40226 - Timezone1 Thu. ON: minute
REG_TZ1_WED_ON_HOUR = 226  # 40227 - Timezone1 Fri. ON: hour
REG_TZ1_WED_ON_MIN = 227  # 40228 - Timezone1 Fri. ON: minute
REG_TZ1_WED_OFF_HOUR = 228  # 40229 - Timezone1 Sat. ON: hour
REG_TZ1_WED_OFF_MIN = 229  # 40230 - Timezone1 Sat. ON: minute
REG_TZ1_THU_ON_HOUR = 230  # 40231 - Timezone1 Sun. ON: hour
REG_TZ1_THU_ON_MIN = 231  # 40232 - Timezone1 Sun. ON: minute
REG_TZ1_THU_OFF_HOUR = 232  # 40233 - Timezone1 Mon. OFF: hour
REG_TZ1_THU_OFF_MIN = 233  # 40234 - Timezone1 Mon. OFF: minute
REG_TZ1_FRI_ON_HOUR = 234  # 40235 - Timezone1 Tue. OFF: hour
REG_TZ1_FRI_ON_MIN = 235  # 40236 - Timezone1 Tue. OFF: minute
REG_TZ1_FRI_OFF_HOUR = 236  # 40237 - Timezone1 Wed. OFF: hour
REG_TZ1_FRI_OFF_MIN = 237  # 40238 - Timezone1 Wed. OFF: minute
REG_TZ1_SAT_ON_HOUR = 238  # 40239 - Timezone1 Thu. OFF: hour
REG_TZ1_SAT_ON_MIN = 239  # 40240 - Timezone1 Thu. OFF: minute
REG_TZ1_SAT_OFF_HOUR = 240  # 40241 - Timezone1 Fri. OFF: hour
REG_TZ1_SAT_OFF_MIN = 241  # 40242 - Timezone1 Fri. OFF: minute
REG_TZ1_SUN_ON_HOUR = 242  # 40243 - Timezone1 Sat. OFF: hour
REG_TZ1_SUN_ON_MIN = 243  # 40244 - Timezone1 Sat. OFF: minute
REG_TZ1_SUN_OFF_HOUR = 244  # 40245 - Timezone1 Sun. OFF: hour
REG_TZ1_SUN_OFF_MIN = 245  # 40246 - Timezone1 Sun. OFF: minute
REG_TZ_TEMP_HR1 = 246  # 40247 - TimezoneMng.TempHr1
REG_TZ_TEMP_MIN1 = 247  # 40248 - TimezoneMng.TempMin1
REG_TZ_S_SET_TEMP1 = 248  # 40249 - TimezoneMng.S_Set_Temp1
REG_TZ_W_SET_TEMP1 = 249  # 40250 - TimezoneMng.W_Set_Temp1
REG_TZ_TEMP_HR2 = 250  # 40251 - TimezoneMng.TempHr2
REG_TZ_TEMP_MIN2 = 251  # 40252 - TimezoneMng.TempMin2
REG_TZ_S_SET_TEMP2 = 252  # 40253 - TimezoneMng.S_Set_Temp2
REG_TZ_W_SET_TEMP2 = 253  # 40254 - TimezoneMng.W_Set_Temp2
REG_TZ_TEMP_HR3 = 254  # 40255 - TimezoneMng.TempHr3
REG_TZ_TEMP_MIN3 = 255  # 40256 - TimezoneMng.TempMin3
REG_TZ_S_SET_TEMP3 = 256  # 40257 - TimezoneMng.S_Set_Temp3
REG_TZ_W_SET_TEMP3 = 257  # 40258 - TimezoneMng.W_Set_Temp3
REG_TZ_TEMP_HR4 = 258  # 40259 - TimezoneMng.TempHr4
REG_TZ_TEMP_MIN4 = 259  # 40260 - TimezoneMng.TempMin4
REG_TZ_S_SET_TEMP4 = 260  # 40261 - TimezoneMng.S_Set_Temp4
REG_TZ_W_SET_TEMP4 = 261  # 40262 - TimezoneMng.W_Set_Temp4
REG_HEATER_TYPE = 323  # 40324 - Heater type
REG_VERSION_X = 325  # 40326 - GeneralMng.CurrVer.X
REG_VERSION_Y = 326  # 40327 - GeneralMng.CurrVer.Y
REG_VERSION_Z = 327  # 40328 - GeneralMng.CurrVer.Z
REG_UNIT_TYPE_A = 328  # 40329 - GeneralMng.UnitType_A
REG_UNIT_TYPE_B = 329  # 40330 - GeneralMng.UnitType_B
REG_BLDC_POWER = 333  # 40334 - BLDC_POwer
REG_BLDC_VAR = 334  # 40335 - BLDC_Var
REG_BLDC_CURRENT = 335  # 40336 - BLDC_Curret
REG_SG_MODE = 355  # 40356 - SG_Mode
REG_SG_MODE_CHANGE_HOLDTIME = 356  # 40357 - SG_Mode Change_HoldTime
REG_SG_MODE_W_TANK_SETP = 357  # 40358 - SG_Mode_W_Tank SetP
REG_SG_COOL_SETP_DIFF_1 = 358  # 40359 - SG_CoolSetP_Diff_1
REG_SG_HEAT_SETP_DIFF_1 = 359  # 40360 - SG_HeatSetP_Diff_1
REG_SG_W_TANK_SETP_DIFF_1 = 360  # 40361 - SG_W_TankSetP_Diff_1
REG_SG_COOL_SETP_DIFF_2 = 361  # 40362 - SG_CoolSetP_Diff_2
REG_SG_HEAT_SETP_DIFF_2 = 362  # 40363 - SG_HeatSetP_Diff_2
REG_SG_W_TANK_SETP_DIFF_2 = 363  # 40364 - SG_W_TankSetP_Diff_2
REG_WORKING_HOURS_PUMP = 364  # 40365 - WorkingHours.Pump
REG_WORKING_HOURS_COMP = 366  # 40367 - WorkingHours.Comp
REG_WORKING_HOURS_FAN = 368  # 40369 - WorkingHours.Fan
REG_WORKING_HOURS_3WAY = 370  # 40371 - WorkingHours.Three way valve
REG_WATER_FLOW = 372  # 40373 - Water Flow Value
REG_PHASE_VOLTAGE_A = 376  # 40377 - PhaseVoltage_A
REG_PHASE_VOLTAGE_B = 377  # 40378 - PhaseVoltage_B
REG_PHASE_VOLTAGE_C = 378  # 40379 - PhaseVoltage_C
REG_PHASE_CURRENT_A = 379  # 40380 - PhaseCurrent_A
REG_PHASE_CURRENT_B = 380  # 40381 - PhaseCurrent_B
REG_PHASE_CURRENT_C = 381  # 40382 - PhaseCurrent_C
REG_POWER_W = 382  # 40383 - Power_W
REG_TOTAL_POWER_CONSUMPTION = 384  # 40385 - Total power consumption
REG_UNIT_POWER = 387  # 40388 - Unit Power
REG_UNIT_COP = 389  # 40390 - Unit_COP
REG_RECORD_POWER_1 = 401  # 40402 - Record_PowerConsumption[1]
REG_RECORD_POWER_2 = 403  # 40404 - Record_PowerConsumption[2]
REG_RECORD_POWER_3 = 405  # 40406 - Record_PowerConsumption[3]
REG_RECORD_POWER_4 = 407  # 40408 - Record_PowerConsumption[4]
REG_RECORD_POWER_5 = 409  # 40410 - Record_PowerConsumption[5]
REG_RECORD_POWER_6 = 411  # 40412 - Record_PowerConsumption[6]
REG_RECORD_POWER_7 = 413  # 40414 - Record_PowerConsumption[7]
REG_TZ2_MON_ON_HOUR = 432  # 40433 - Timezone2 Mon. ON: hour
REG_TZ2_MON_ON_MIN = 433  # 40434 - Timezone2 Mon. ON: minute
REG_TZ2_MON_OFF_HOUR = 434  # 40435 - Timezone2 Tue. ON: hour
REG_TZ2_MON_OFF_MIN = 435  # 40436 - Timezone2 Tue. ON: minute
REG_TZ2_TUE_ON_HOUR = 436  # 40437 - Timezone2 Wed. ON: hour
REG_TZ2_TUE_ON_MIN = 437  # 40438 - Timezone2 Wed. ON: minute
REG_TZ2_TUE_OFF_HOUR = 438  # 40439 - Timezone2 Thu. ON: hour
REG_TZ2_TUE_OFF_MIN = 439  # 40440 - Timezone2 Thu. ON: minute
REG_TZ2_WED_ON_HOUR = 440  # 40441 - Timezone2 Fri. ON: hour
REG_TZ2_WED_ON_MIN = 441  # 40442 - Timezone2 Fri. ON: minute
REG_TZ2_WED_OFF_HOUR = 442  # 40443 - Timezone2 Sat. ON: hour
REG_TZ2_WED_OFF_MIN = 443  # 40444 - Timezone2 Sat. ON: minute
REG_TZ2_THU_ON_HOUR = 444  # 40445 - Timezone2 Sun. ON: hour
REG_TZ2_THU_ON_MIN = 445  # 40446 - Timezone2 Sun. ON: minute
REG_TZ2_THU_OFF_HOUR = 446  # 40447 - Timezone2 Mon. OFF: hour
REG_TZ2_THU_OFF_MIN = 447  # 40448 - Timezone2 Mon. OFF: minute
REG_TZ2_FRI_ON_HOUR = 448  # 40449 - Timezone2 Tue. OFF: hour
REG_TZ2_FRI_ON_MIN = 449  # 40450 - Timezone2 Tue. OFF: minute
REG_TZ2_FRI_OFF_HOUR = 450  # 40451 - Timezone2 Wed. OFF: hour
REG_TZ2_FRI_OFF_MIN = 451  # 40452 - Timezone2 Wed. OFF: minute
REG_TZ2_SAT_ON_HOUR = 452  # 40453 - Timezone2 Thu. OFF: hour
REG_TZ2_SAT_ON_MIN = 453  # 40454 - Timezone2 Thu. OFF: minute
REG_TZ2_SAT_OFF_HOUR = 454  # 40455 - Timezone2 Fri. OFF: hour
REG_TZ2_SAT_OFF_MIN = 455  # 40456 - Timezone2 Fri. OFF: minute
REG_TZ2_SUN_ON_HOUR = 456  # 40457 - Timezone2 Sat. OFF: hour
REG_TZ2_SUN_ON_MIN = 457  # 40458 - Timezone2 Sat. OFF: minute
REG_TZ2_SUN_OFF_HOUR = 458  # 40459 - Timezone2 Sun. OFF: hour
REG_TZ2_SUN_OFF_MIN = 459  # 40460 - Timezone2 Sun. OFF: minute
REG_ANTILEG_TEMP_SETP = 471  # 40472 - Anti-legionella temp.setp.
REG_ANTILEG_WEEKDAY = 473  # 40474 - Weekday of running antileg.
REG_ANTILEG_TIME_START_HR = 474  # 40475 - Timeband of runnig antileg.- hours (start)
REG_ANTILEG_TIME_START_MIN = 475  # 40476 - Timeband of runnig antileg. - minutes (start)
REG_ANTILEG_TIME_END_HR = 476  # 40477 - Timeband of runnig antileg. - hours (end)
REG_ANTILEG_TIME_END_MIN = 477  # 40478 - Timeband of runnig antileg. - minutes (end)

# ============================================================================
# DISCRETE INPUTS (10001+)
# ============================================================================

DISCRETE_UNIT_ON = 0  # 10001 - Unit On/OFF
DISCRETE_FLOW_SWITCH = 1  # 10002 - Flow switch
DISCRETE_AC_LINKAGE = 3  # 10004 - A/C linkage switch
DISCRETE_SG_SIGNAL = 4  # 10005 - SG_Signal
DISCRETE_DOUT_VAL_1 = 5  # 10006 - Outputs.DoutVal_1
DISCRETE_4WAY_VALVE = 7  # 10008 - Four way valve On/OFF status
DISCRETE_PUMP = 8  # 10009 - Pump On/OFF status
DISCRETE_3WAY_VALVE = 9  # 10010 - Three way valve On/OFF status
DISCRETE_CRANK_HEATER = 10  # 10011 - Crank.heater On/OFF status
DISCRETE_CHASSIS_HEATER = 11  # 10012 - chassis heater On/OFF status
DISCRETE_DOUT_VAL_9 = 12  # 10013 - Outputs.DoutVal_9
DISCRETE_TOO_MANY_MEM_WRITINGS = 13  # 10014 - Too many mem writings
DISCRETE_RETAIN_MEM_WRITE_ERROR = 14  # 10015 - Retain mem write error
DISCRETE_INLET_PROBE_ERROR = 15  # 10016 - Inlet probe error
DISCRETE_OUTLET_PROBE_ERROR = 16  # 10017 - Outlet probe error
DISCRETE_AMBIENT_PROBE_ERROR = 17  # 10018 - Ambient probe error
DISCRETE_CONDENSER_COIL_TEMP = 18  # 10019 - Condenser coil temp
DISCRETE_WATER_FLOW_SWITCH = 19  # 10020 - Water flow switch
DISCRETE_PHASE_SEQU_PROT_ALARM = 20  # 10021 - Phase sequ.prot.alarm
DISCRETE_UNIT_WORK_HOUR_WARNING = 21  # 10022 - Unit work hour warning
DISCRETE_PUMP_WORK_HOUR_WARNING = 22  # 10023 - Pump work hour warning
DISCRETE_COMP_WORK_HOUR_WARNING = 23  # 10024 - Comp.work hour warning
DISCRETE_COND_FAN_WORK_HOURWARN = 24  # 10025 - Cond.fan work hourWarn
DISCRETE_LOW_SUPERHEAT_VLV_A = 25  # 10026 - Low superheat - Vlv.A
DISCRETE_LOW_SUPERHEAT_VLV_B = 26  # 10027 - Low superheat - Vlv.B
DISCRETE_LOP_VLV_A = 27  # 10028 - LOP - Vlv.A
DISCRETE_LOP_VLV_B = 28  # 10029 - LOP - Vlv.B
DISCRETE_MOP_VLV_A = 29  # 10030 - MOP - Vlv.A
DISCRETE_MOP_VLV_B = 30  # 10031 - MOP - Vlv.B
DISCRETE_MOTOR_ERROR_VLV_A = 31  # 10032 - Motor error - Vlv.A
DISCRETE_MOTOR_ERROR_VLV_B = 32  # 10033 - Motor error - Vlv.B
DISCRETE_LOW_SUCT_TEMP_VLV_A = 33  # 10034 - Low suct.temp. - Vlv.A
DISCRETE_LOW_SUCT_TEMP_VLV_B = 34  # 10035 - Low suct.temp. - Vlv.B
DISCRETE_HIGH_CONDENS_TEMP_EVD = 35  # 10036 - High condens.temp.EVD
DISCRETE_PROBE_S1_ERROR_EVD = 36  # 10037 - Probe S1 error EVD
DISCRETE_PROBE_S2_ERROR_EVD = 37  # 10038 - Probe S2 error EVD
DISCRETE_PROBE_S3_ERROR_EVD = 38  # 10039 - Probe S3 error EVD
DISCRETE_PROBE_S4_ERROR_EVD = 39  # 10040 - Probe S4 error EVD
DISCRETE_BATTERY_DISCHARGE_EVD = 40  # 10041 - Battery discharge EVD
DISCRETE_EEPROM_ALARM_EVD = 41  # 10042 - EEPROM alarm EVD
DISCRETE_INCOMPLETE_CLOSING_EVD = 42  # 10043 - Incomplete closing EVD
DISCRETE_EMERGENCY_CLOSING_EVD = 43  # 10044 - Emergency closing EVD
DISCRETE_FW_NOT_COMPATIBLE_EVD = 44  # 10045 - FW not compatible EVD
DISCRETE_CONFIG_ERROR_EVD = 45  # 10046 - Config. error EVD
DISCRETE_EVD_DRIVER_OFFLINE = 46  # 10047 - EVD Driver offline
DISCRETE_BLDC_ALARM_HIGH_STARTUP_DELTAP = 47  # 10048 - BLDC-alarm:High startup DeltaP
DISCRETE_BLDC_ALARM_COMPRESSOR_SHUT_OFF = 48  # 10049 - BLDC-alarm:Compressor shut off
DISCRETE_BLDC_ALARM_OUT_OF_ENVELOPE = 49  # 10050 - BLDC-alarm:Out of Envelope
DISCRETE_BLDC_ALARM_STARTING_FAIL_WAIT = 50  # 10051 - BLDC-alarm:Starting fail wait
DISCRETE_BLDC_ALARM_STARTING_FAIL_EXCEEDED = 51  # 10052 - BLDC-alarm:Starting fail exceeded
DISCRETE_BLDC_ALARM_LOW_DELTA_PRESSURE = 52  # 10053 - BLDC-alarm:Low delta pressure
DISCRETE_BLDC_ALARM_HIGH_DISCARGE_GAS_TEMP = 53  # 10054 - BLDC-alarm:High discarge gas temp
DISCRETE_ENVELOPE_ALARM_HIGH_COMPRESSOR_RATIO = 54  # 10055 - Envelope-alarm:High compressor ratio
DISCRETE_ENVELOPE_ALARM_HIGH_DISCHARGE_PRESS = 55  # 10056 - Envelope-alarm:High discharge press.
DISCRETE_ENVELOPE_ALARM_HIGH_CURRENT = 56  # 10057 - Envelope-alarm:High current
DISCRETE_ENVELOPE_ALARM_HIGH_SUCTION_PRESSURE = 57  # 10058 - Envelope-alarm:High suction pressure
DISCRETE_ENVELOPE_ALARM_LOW_COMPRESSOR_RATIO = 58  # 10059 - Envelope-alarm:Low compressor ratio
DISCRETE_ENVELOPE_ALARM_LOW_PRESSURE_DIFF = 59  # 10060 - Envelope-alarm:Low pressure diff.
DISCRETE_ENVELOPE_ALARM_LOW_DISCHARGE_PRESSURE = 60  # 10061 - Envelope-alarm:Low discharge pressure
DISCRETE_ENVELOPE_ALARM_LOW_SUCTION_PRESSURE = 61  # 10062 - Envelope-alarm:Low suction pressure
DISCRETE_ENVELOPE_ALARM_HIGH_DISCHARGE_TEMP = 62  # 10063 - Envelope-alarm:High discharge temp.
DISCRETE_POWER_ALARM_01_OVERCURRENT = 63  # 10064 - Power+ alarm:01-Overcurrent
DISCRETE_POWER_ALARM_02_MOTOR_OVERLOAD = 64  # 10065 - Power+ alarm:02-Motor overload
DISCRETE_POWER_ALARM_03_DCBUS_OVERVOLTAGE = 65  # 10066 - Power+ alarm:03-DCbus overvoltage
DISCRETE_POWER_ALARM_04_DCBUS_UNDERVOLTAGE = 66  # 10067 - Power+ alarm:04-DCbus undervoltage
DISCRETE_POWER_ALARM_05_DRIVE_OVERTEMP = 67  # 10068 - Power+ alarm:05-Drive overtemp.
DISCRETE_POWER_ALARM_06_DRIVE_UNDERTEMP = 68  # 10069 - Power+ alarm:06-Drive undertemp.
DISCRETE_POWER_ALARM_07_OVERCURRENT_HW = 69  # 10070 - Power+ alarm:07-Overcurrent HW
DISCRETE_POWER_ALARM_08_MOTOR_OVERTEMP = 70  # 10071 - Power+ alarm:08-Motor overtemp.
DISCRETE_POWER_ALARM_09_IGBT_MODULE_ERROR = 71  # 10072 - Power+ alarm:09-IGBT module error
DISCRETE_POWER_ALARM_10_CPU_ERROR = 72  # 10073 - Power+ alarm:10-CPU error
DISCRETE_POWER_ALARM_11_PARAMETER_DEFAULT = 73  # 10074 - Power+ alarm:11-Parameter default
DISCRETE_POWER_ALARM_12_DCBUS_RIPPLE = 74  # 10075 - Power+ alarm:12-DCbus ripple
DISCRETE_POWER_ALARM_13_DATA_COMM_FAULT = 75  # 10076 - Power+ alarm:13-Data comm. Fault
DISCRETE_POWER_ALARM_14_THERMISTOR_FAULT = 76  # 10077 - Power+ alarm:14-Thermistor fault
DISCRETE_POWER_ALARM_15_AUTOTUNING_FAULT = 77  # 10078 - Power+ alarm:15-Autotuning fault
DISCRETE_POWER_ALARM_16_DRIVE_DISABLED = 78  # 10079 - Power+ alarm:16-Drive disabled
DISCRETE_POWER_ALARM_17_MOTOR_PHASE_FAULT = 79  # 10080 - Power+ alarm:17-Motor phase fault
DISCRETE_POWER_ALARM_18_INTERNAL_FAN_FAULT = 80  # 10081 - Power+ alarm:18-Internal fan fault
DISCRETE_POWER_ALARM_19_SPEED_FAULT = 81  # 10082 - Power+ alarm:19-Speed fault
DISCRETE_POWER_ALARM_20_PFC_MODULE_ERROR = 82  # 10083 - Power+ alarm:20-PFC module error
DISCRETE_POWER_ALARM_21_PFC_OVERVOLTAGE = 83  # 10084 - Power+ alarm:21-PFC overvoltage
DISCRETE_POWER_ALARM_22_PFC_UNDERVOLTAGE = 84  # 10085 - Power+ alarm:22-PFC undervoltage
DISCRETE_POWER_ALARM_23_STO_DETECTIONERROR = 85  # 10086 - Power+ alarm:23-STO DetectionError
DISCRETE_POWER_ALARM_24_STO_DETECTIONERROR = 86  # 10087 - Power+ alarm:24-STO DetectionError
DISCRETE_POWER_ALARM_25_GROUND_FAULT = 87  # 10088 - Power+ alarm:25-Ground fault
DISCRETE_POWER_ALARM_26_INTERNAL_ERROR_1 = 88  # 10089 - Power+ alarm:26-Internal error 1
DISCRETE_POWER_ALARM_27_INTERNAL_ERROR_2 = 89  # 10090 - Power+ alarm:27-Internal error 2
DISCRETE_POWER_ALARM_28_DRIVE_OVERLOAD = 90  # 10091 - Power+ alarm:28-Drive overload
DISCRETE_POWER_ALARM_29_UC_SAFETY_FAULT = 91  # 10092 - Power+ alarm:29-uC safety fault
DISCRETE_POWER_ALARM_98_UNEXPECTED_RESTART = 92  # 10093 - Power+ alarm:98-Unexpected restart
DISCRETE_POWER_ALARM_99_UNEXPECTED_STOP = 93  # 10094 - Power+ alarm:99-Unexpected stop
DISCRETE_POWER_SAFETY_ALARM_01_CURRENT_MEAS_FAULT = 94  # 10095 - Power+ safety alarm:01-Current meas.fault
DISCRETE_POWER_SAFETY_ALARM_02_CURRENT_UNBALANCED = 95  # 10096 - Power+ safety alarm:02-Current unbalanced
DISCRETE_POWER_SAFETY_ALARM_03_OVER_CURRENT = 96  # 10097 - Power+ safety alarm:03-Over current
DISCRETE_POWER_SAFETY_ALARM_04_STO_ALARM = 97  # 10098 - Power+ safety alarm:04-STO alarm
DISCRETE_POWER_SAFETY_ALARM_05_STO_HARDWARE_ALARM = 98  # 10099 - Power+ safety alarm:05-STO hardware alarm
DISCRETE_POWER_SAFETY_ALARM_06_POWERSUPPLY_MISSING = 99  # 10100 - Power+ safety alarm:06-PowerSupply missing
DISCRETE_POWER_SAFETY_ALARM_07_HW_FAULT_CMD_BUFFER = 100  # 10101 - Power+ safety alarm:07-HW fault cmd.buffer
DISCRETE_POWER_SAFETY_ALARM_08_HW_FAULT_HEATER_C = 101  # 10102 - Power+ safety alarm:08-HW fault heater c.
DISCRETE_POWER_SAFETY_ALARM_09_DATA_COMM_FAULT = 102  # 10103 - Power+ safety alarm:09-Data comm. Fault
DISCRETE_POWER_SAFETY_ALARM_10_COMPR_STALL_DETECT = 103  # 10104 - Power+ safety alarm:10-Compr. stall detect
DISCRETE_POWER_SAFETY_ALARM_11_DCBUS_OVER_CURRENT = 104  # 10105 - Power+ safety alarm:11-DCbus over current
DISCRETE_POWER_SAFETY_ALARM_12_HWF_DCBUS_CURRENT = 105  # 10106 - Power+ safety alarm:12-HWF DCbus current
DISCRETE_POWER_SAFETY_ALARM_13_DCBUS_VOLTAGE = 106  # 10107 - Power+ safety alarm:13-DCbus voltage
DISCRETE_POWER_SAFETY_ALARM_14_HWF_DCBUS_VOLTAGE = 107  # 10108 - Power+ safety alarm:14-HWF DCbus voltage
DISCRETE_POWER_SAFETY_ALARM_15_INPUT_VOLTAGE = 108  # 10109 - Power+ safety alarm:15-Input voltage
DISCRETE_POWER_SAFETY_ALARM_16_HWF_INPUT_VOLTAGE = 109  # 10110 - Power+ safety alarm:16-HWF input voltage
DISCRETE_POWER_SAFETY_ALARM_17_DCBUS_POWER_ALARM = 110  # 10111 - Power+ safety alarm:17-DCbus power alarm
DISCRETE_POWER_SAFETY_ALARM_18_HWF_POWER_MISMATCH = 111  # 10112 - Power+ safety alarm:18-HWF power mismatch
DISCRETE_POWER_SAFETY_ALARM_19_NTC_OVER_TEMP = 112  # 10113 - Power+ safety alarm:19-NTC over temp.
DISCRETE_POWER_SAFETY_ALARM_20_NTC_UNDER_TEMP = 113  # 10114 - Power+ safety alarm:20-NTC under temp.
DISCRETE_POWER_SAFETY_ALARM_21_NTC_FAULT = 114  # 10115 - Power+ safety alarm:21-NTC fault
DISCRETE_POWER_SAFETY_ALARM_22_HWF_SYNC_FAULT = 115  # 10116 - Power+ safety alarm:22-HWF sync fault
DISCRETE_POWER_SAFETY_ALARM_23_INVALID_PARAMETER = 116  # 10117 - Power+ safety alarm:23-Invalid parameter
DISCRETE_POWER_SAFETY_ALARM_24_FW_FAULT = 117  # 10118 - Power+ safety alarm:24-FW fault
DISCRETE_POWER_SAFETY_ALARM_25_HW_FAULT = 118  # 10119 - Power+ safety alarm:25-HW fault
DISCRETE_POWER_SAFETY_ALARM_26_RESEVED = 119  # 10120 - Power+ safety alarm:26-reseved
DISCRETE_POWER_SAFETY_ALARM_27_RESEVED = 120  # 10121 - Power+ safety alarm:27-reseved
DISCRETE_POWER_SAFETY_ALARM_28_RESEVED = 121  # 10122 - Power+ safety alarm:28-reseved
DISCRETE_POWER_SAFETY_ALARM_29_RESEVED = 122  # 10123 - Power+ safety alarm:29-reseved
DISCRETE_POWER_SAFETY_ALARM_30_RESEVED = 123  # 10124 - Power+ safety alarm:30-reseved
DISCRETE_POWER_SAFETY_ALARM_31_RESEVED = 124  # 10125 - Power+ safety alarm:31-reseved
DISCRETE_POWER_SAFETY_ALARM_32_RESEVED = 125  # 10126 - Power+ safety alarm:32-reseved
DISCRETE_POWER_ALARM_POWER_OFFLINE = 126  # 10127 - Power+ alarm:Power+ offline
DISCRETE_EEV_ALARM_LOW_SUPERHEAT = 127  # 10128 - EEV alarm:Low superheat
DISCRETE_EEV_ALARM_LOP = 128  # 10129 - EEV alarm:LOP
DISCRETE_EEV_ALARM_MOP = 129  # 10130 - EEV alarm:MOP
DISCRETE_EEV_ALARM_HIGH_CONDENS_TEMP = 130  # 10131 - EEV alarm:High condens.temp.
DISCRETE_EEV_ALARM_LOW_SUCTION_TEMP = 131  # 10132 - EEV alarm:Low suction temp.
DISCRETE_EEV_ALARM_MOTOR_ERROR = 132  # 10133 - EEV alarm:Motor error
DISCRETE_EEV_ALARM_SELF_TUNING = 133  # 10134 - EEV alarm:Self Tuning
DISCRETE_EEV_ALARM_EMERGENCY_CLOSING = 134  # 10135 - EEV alarm:Emergency closing
DISCRETE_EEV_ALARM_TEMPERATURE_DELTA = 135  # 10136 - EEV alarm:Temperature delta
DISCRETE_EEV_ALARM_PRESSURE_DELTA = 136  # 10137 - EEV alarm:Pressure delta
DISCRETE_EEV_ALARM_PARAM_RANGE_ERROR = 137  # 10138 - EEV alarm:Param.range error
DISCRETE_EEV_ALARM_SERVICEPOSIT_ERR = 138  # 10139 - EEV alarm:ServicePosit% err
DISCRETE_EEV_ALARM_VALVEID_PIN_ERROR = 139  # 10140 - EEV alarm:ValveID pin error
DISCRETE_LOW_PRESS_ALARM = 140  # 10141 - Low press alarm
DISCRETE_HIGH_PRESS_ALARM = 141  # 10142 - High press alarm
DISCRETE_DISC_TEMP_PROBE_ERROR = 142  # 10143 - Disc.temp.probe error
DISCRETE_SUCT_TEMP_PROBE_ERROR = 143  # 10144 - Suct.temp.probe error
DISCRETE_DISC_PRESS_PROBE_ERROR = 144  # 10145 - Disc.press.probe error
DISCRETE_SUCT_PRESS_PROBE_ERROR = 145  # 10146 - Suct.press.probe error
DISCRETE_TANK_TEMP_PROBE_ERROR = 146  # 10147 - Tank temp.probe error
DISCRETE_EVI_SUCTT_PROBE_ERROR = 147  # 10148 - EVI SuctT.probe error
DISCRETE_EVI_SUCTP_PROBE_ERROR = 148  # 10149 - EVI SuctP.probe error
DISCRETE_FLOW_SWITCH_ALARM = 149  # 10150 - Flow switch alarm
DISCRETE_HIGH_TEMP_ALARM = 150  # 10151 - High temp. alarm
DISCRETE_LOW_TEMP_ALARM = 151  # 10152 - Low temp. alarm
DISCRETE_TEMP_DELTA_ALARM = 152  # 10153 - Temp.delta alarm
DISCRETE_EVI_ALARM_PARAM_RANGE_ERROR = 153  # 10154 - EVI alarm:Param.range error
DISCRETE_EVI_ALARM_LOW_SUPERHEAT = 154  # 10155 - EVI alarm:Low superheat
DISCRETE_EVI_ALARM_LOP = 155  # 10156 - EVI alarm:LOP
DISCRETE_EVI_ALARM_MOP = 156  # 10157 - EVI alarm:MOP
DISCRETE_EVI_ALARM_HIGH_CONDENS_TEMP = 157  # 10158 - EVI alarm:High condens.temp.
DISCRETE_EVI_ALARM_LOW_SUCTION_TEMP = 158  # 10159 - EVI alarm:Low suction temp.
DISCRETE_EVI_ALARM_MOTOR_ERROR = 159  # 10160 - EVI alarm:Motor error
DISCRETE_EVI_ALARM_SELF_TUNING = 160  # 10161 - EVI alarm:Self Tuning
DISCRETE_EVI_ALARM_EMERGENCY_CLOSING = 161  # 10162 - EVI alarm:Emergency closing
DISCRETE_EVI_ALARM_SERVICEPOSIT_ERR = 162  # 10163 - EVI alarm:ServicePosit% err
DISCRETE_EVI_ALARM_VALVEID_PIN_ERROR = 163  # 10164 - EVI alarm:ValveID pin error
DISCRETE_SUPPLY_POWER_ERROR = 164  # 10165 - Supply power error
DISCRETE_FAN1_FAULT = 165  # 10166 - Fan1 fault
DISCRETE_FAN2_FAULT = 166  # 10167 - Fan2 fault
DISCRETE_FANS_OFFLINE = 167  # 10168 - Fans Offline
DISCRETE_SLAVE1_OFFLINE = 168  # 10169 - Slave1 Offline
DISCRETE_MASTER_OFFLINE = 169  # 10170 - Master Offline
DISCRETE_SLAVE2_OFFLINE = 170  # 10171 - Slave2 Offline
DISCRETE_SLAVE3_OFFLINE = 171  # 10172 - Slave3 Offline
DISCRETE_SLAVE4_OFFLINE = 172  # 10173 - Slave4 Offline
DISCRETE_SLAVE5_OFFLINE = 173  # 10174 - Slave5 Offline
DISCRETE_SLAVE6_OFFLINE = 174  # 10175 - Slave6 Offline
DISCRETE_SLAVE7_OFFLINE = 175  # 10176 - Slave7 Offline
DISCRETE_SLAVE8_OFFLINE = 176  # 10177 - Slave8 Offline
DISCRETE_SLAVE9_OFFLINE = 177  # 10178 - Slave9 Offline
DISCRETE_COMP_STATUS = 179  # 10180 - Comp  On/OFF status
DISCRETE_FAN_STATUS = 180  # 10181 - Fan On/OFF status
DISCRETE_EVU_SIGNAL = 187  # 10188 - EVU_Signal
DISCRETE_AL_OFFLINE_ELECTRICMETER_ACTIVE = 188  # 10189 - Al_Offline_ElectricMeter.Active

# ============================================================================
# COILS (00001+)
# ============================================================================


# ============================================================================
# MODE DEFINITIONS AND MAPS
# ============================================================================


# ============================================================================
# COIL ALIASES - Compatibility with code that uses COIL_ prefix
# ============================================================================
# NOTE: Many "coils" are actually discrete inputs (read-only)
# True coils for writing are only 00039, 00040, 00044, 00064-00069, 00106, 00110

# Discrete input aliases (read-only, referenced as COIL_ for compatibility)
COIL_FLOW_SWITCH = DISCRETE_FLOW_SWITCH
COIL_AC_LINKAGE = DISCRETE_AC_LINKAGE
COIL_FAN_HIGH = DISCRETE_DOUT_VAL_1
COIL_FAN_LOW = 6  # 10007 - Not in manufacturer table
COIL_4WAY_VALVE = DISCRETE_4WAY_VALVE
COIL_PUMP = DISCRETE_PUMP
COIL_THREE_VALVE = DISCRETE_3WAY_VALVE
COIL_CRANK_HEATER = DISCRETE_CRANK_HEATER
COIL_CHASSIS_HEATER = DISCRETE_CHASSIS_HEATER
COIL_HEATER = DISCRETE_DOUT_VAL_9
COIL_PHASE_SWITCH = DISCRETE_SG_SIGNAL
COIL_COOLING_LINKAGE = 181  # 10182 - Cooling linkage
COIL_HEATING_LINKAGE = 182  # 10183 - Heating linkage
COIL_TERMINAL_PUMP = 183  # 10184 - Terminal pump

# Special alias for switch.py (even though Unit ON/OFF is controlled via register, not coil)
COIL_UNIT_ON = DISCRETE_UNIT_ON  # Note: This is READ-ONLY discrete input!


WORK_MODE_COOLING = 0
WORK_MODE_HEATING = 1
WORK_MODE_HOT_WATER = 2
WORK_MODE_HW_COOLING = 3
WORK_MODE_HW_HEATING = 4

WORK_MODE_MAP = {
    WORK_MODE_COOLING: "Cooling",
    WORK_MODE_HEATING: "Heating",
    WORK_MODE_HOT_WATER: "Hot Water",
    WORK_MODE_HW_COOLING: "Hot Water + Cooling",
    WORK_MODE_HW_HEATING: "Hot Water + Heating"
}

# ============================================================================
# STATUS VALUES
# ============================================================================
STATUS_MAP = {
    0: "Not Ready",
    1: "Unit ON",
    2: "OFF by Alarm",
    3: "OFF by Timezone",
    4: "OFF by SuperV",
    5: "OFF by Linkage",
    6: "OFF by Keyboard",
    7: "Manual Mode",
    8: "Anti Freeze",
    9: "OFF by AC linkage",
    10: "OFF by Change"
}

# ============================================================================
# UNIT RUN MODE
# ============================================================================
UNIT_RUN_MODE_COOLING = 0
UNIT_RUN_MODE_HEATING = 1
UNIT_RUN_MODE_DHW = 2

UNIT_RUN_MODE_MAP = {
    UNIT_RUN_MODE_COOLING: "Cooling",
    UNIT_RUN_MODE_HEATING: "Heating",
    UNIT_RUN_MODE_DHW: "DHW"
}

# ============================================================================
# FAN MODES
# ============================================================================
FAN_MODE_DAYTIME = 0
FAN_MODE_NIGHT = 1
FAN_MODE_ECO = 2
FAN_MODE_PRESSURE = 3

FAN_MODE_MAP = {
    FAN_MODE_DAYTIME: "Daytime",
    FAN_MODE_NIGHT: "Night",
    FAN_MODE_ECO: "ECO Mode",
    FAN_MODE_PRESSURE: "Pressure"
}

# ============================================================================
# HEATER TYPE
# ============================================================================
HEATER_TYPE_DISABLE = 0
HEATER_TYPE_HOTWATER = 1
HEATER_TYPE_HEATING = 2
HEATER_TYPE_ALL = 3
HEATER_TYPE_INDEPENDENT = 4

HEATER_TYPE_MAP = {
    HEATER_TYPE_DISABLE: "Disable",
    HEATER_TYPE_HOTWATER: "Hot Water",
    HEATER_TYPE_HEATING: "Heating",
    HEATER_TYPE_ALL: "All",
    HEATER_TYPE_INDEPENDENT: "Independent"
}

# ============================================================================
# PUMP MODES
# ============================================================================
PUMP_MODE_NORMAL = 0
PUMP_MODE_DEMAND = 1
PUMP_MODE_INTERVAL = 2
PUMP_MODE_ALWAYS = 3

PUMP_MODE_MAP = {
    PUMP_MODE_NORMAL: "Normal",
    PUMP_MODE_DEMAND: "Demand",
    PUMP_MODE_INTERVAL: "Interval",
    PUMP_MODE_ALWAYS: "Always"
}

# ============================================================================
# COMPRESSOR STATUS
# ============================================================================
COMP_STATUS_OK = 0
COMP_STATUS_CONTROLLED = 1
COMP_STATUS_LIMITED = 2

COMP_STATUS_MAP = {
    COMP_STATUS_OK: "OK",
    COMP_STATUS_CONTROLLED: "Controlled",
    COMP_STATUS_LIMITED: "Limited"
}

# ============================================================================
# ALARM REGISTERS (Discrete Inputs 10014+)
# ============================================================================
ALARM_REGISTERS = {
    13: "AL001 Too many mem writings",
    14: "AL002 Retain mem write error",
    15: "AL003 Inlet probe error",
    16: "AL004 Outlet probe error",
    17: "AL005 Ambient probe error",
    18: "AL006 Condenser coil temp",
    19: "AL007 Water flow switch",
    20: "AL008 Phase sequ.prot.alarm",
    21: "AL009 Unit work hour warning",
    22: "AL010 Pump work hour warning",
    23: "AL011 Comp.work hour warning",
    24: "AL012 Cond.fan work hourWarn",
    25: "AL013 Low superheat - Vlv.A",
    26: "AL014 Low superheat - Vlv.B",
    27: "AL015 LOP - Vlv.A",
    28: "AL016 LOP - Vlv.B",
    29: "AL017 MOP - Vlv.A",
    30: "AL018 MOP - Vlv.B",
    31: "AL019 Motor error - Vlv.A",
    32: "AL020 Motor error - Vlv.B",
    33: "AL021 Low suct.temp. - Vlv.A",
    34: "AL022 Low suct.temp. - Vlv.B",
    35: "AL023 High condens.temp.EVD",
    36: "AL024 Probe S1 error EVD",
    37: "AL025 Probe S2 error EVD",
    38: "AL026 Probe S3 error EVD",
    39: "AL027 Probe S4 error EVD",
    40: "AL028 Battery discharge EVD",
    41: "AL029 EEPROM alarm EVD",
    42: "AL030 Incomplete closing EVD",
    43: "AL031 Emergency closing EVD",
    44: "AL032 FW not compatible EVD",
    45: "AL033 Config. error EVD",
    46: "AL034 EVD Driver offline",
    47: "AL035 BLDC: High startup DeltaP",
    48: "AL036 BLDC: Compressor shut off",
    49: "AL037 BLDC: Out of Envelope",
    50: "AL038 BLDC: Starting fail wait",
    51: "AL039 BLDC: Starting fail exceeded",
    52: "AL040 BLDC: Low delta pressure",
    53: "AL041 BLDC: High discarge gas temp",
    54: "AL042 Envelope: High compressor ratio",
    55: "AL043 Envelope: High discharge press",
    56: "AL044 Envelope: High current",
    57: "AL045 Envelope: High suction pressure",
    58: "AL046 Envelope: Low compressor ratio",
    59: "AL047 Envelope: Low pressure diff",
    60: "AL048 Envelope: Low discharge pressure",
    61: "AL049 Envelope: Low suction pressure",
    62: "AL050 Envelope: High discharge temp",
    63: "AL051 Power+: 01-Overcurrent",
    64: "AL052 Power+: 02-Motor overload",
    65: "AL053 Power+: 03-DCbus overvoltage",
    66: "AL054 Power+: 04-DCbus undervoltage",
    67: "AL055 Power+: 05-Drive overtemp",
    68: "AL056 Power+: 06-Drive undertemp",
    69: "AL057 Power+: 07-Overcurrent HW",
    70: "AL058 Power+: 08-Motor overtemp",
    71: "AL059 Power+: 09-IGBT module error",
    72: "AL060 Power+: 10-CPU error",
    73: "AL061 Power+: 11-Parameter default",
    74: "AL062 Power+: 12-DCbus ripple",
    75: "AL063 Power+: 13-Data comm. Fault",
    76: "AL064 Power+: 14-Thermistor fault",
    77: "AL065 Power+: 15-Autotuning fault",
    78: "AL066 Power+: 16-Drive disabled",
    79: "AL067 Power+: 17-Motor phase fault",
    80: "AL068 Power+: 18-Internal fan fault",
    81: "AL069 Power+: 19-Speed fault",
    82: "AL070 Power+: 20-PFC module error",
    83: "AL071 Power+: 21-PFC overvoltage",
    84: "AL072 Power+: 22-PFC undervoltage",
    85: "AL073 Power+: 23-STO DetectionError",
    86: "AL074 Power+: 24-STO DetectionError",
    87: "AL075 Power+: 25-Ground fault",
    88: "AL076 Power+: 26-Internal error 1",
    89: "AL077 Power+: 27-Internal error 2",
    90: "AL078 Power+: 28-Drive overload",
    91: "AL079 Power+: 29-uC safety fault",
    92: "AL080 Power+: 98-Unexpected restart",
    93: "AL081 Power+: 99-Unexpected stop",
    94: "AL082 Power+ safety: 01-Current meas.fault",
    95: "AL083 Power+ safety: 02-Current unbalanced",
    96: "AL084 Power+ safety: 03-Over current",
    97: "AL085 Power+ safety: 04-STO alarm",
    98: "AL086 Power+ safety: 05-STO hardware alarm",
    99: "AL087 Power+ safety: 06-PowerSupply missing",
    100: "AL088 Power+ safety: 07-HW fault cmd.buffer",
    101: "AL089 Power+ safety: 08-HW fault heater c.",
    102: "AL090 Power+ safety: 09-Data comm. Fault",
    103: "AL091 Power+ safety: 10-Compr. stall detect",
    104: "AL092 Power+ safety: 11-DCbus over current",
    105: "AL093 Power+ safety: 12-HWF DCbus current",
    106: "AL094 Power+ safety: 13-DCbus voltage",
    107: "AL095 Power+ safety: 14-HWF DCbus voltage",
    108: "AL096 Power+ safety: 15-Input voltage",
    109: "AL097 Power+ safety: 16-HWF input voltage",
    110: "AL098 Power+ safety: 17-DCbus power alarm",
    111: "AL099 Power+ safety: 18-HWF power mismatch",
    112: "AL100 Power+ safety: 19-NTC over temp",
    113: "AL101 Power+ safety: 20-NTC under temp",
    114: "AL102 Power+ safety: 21-NTC fault",
    115: "AL103 Power+ safety: 22-HWF sync fault",
    116: "AL104 Power+ safety: 23-Invalid parameter",
    117: "AL105 Power+ safety: 24-FW fault",
    118: "AL106 Power+ safety: 25-HW fault",
    119: "AL107 Power+ safety: 26-reserved",
    120: "AL108 Power+ safety: 27-reserved",
    121: "AL109 Power+ safety: 28-reserved",
    122: "AL110 Power+ safety: 29-reserved",
    123: "AL111 Power+ safety: 30-reserved",
    124: "AL112 Power+ safety: 31-reserved",
    125: "AL113 Power+ safety: 32-reserved",
    126: "AL114 Power+: Power+ offline",
    127: "AL115 EEV: Low superheat",
    128: "AL116 EEV: LOP",
    129: "AL117 EEV: MOP",
    130: "AL118 EEV: High condens.temp",
    131: "AL119 EEV: Low suction temp",
    132: "AL120 EEV: Motor error",
    133: "AL121 EEV: Self Tuning",
    134: "AL122 EEV: Emergency closing",
    135: "AL123 EEV: Temperature delta",
    136: "AL124 EEV: Pressure delta",
    137: "AL125 EEV: Param.range error",
    138: "AL126 EEV: ServicePosit% err",
    139: "AL127 EEV: ValveID pin error",
    140: "AL128 Low press alarm",
    141: "AL129 High press alarm",
    142: "AL130 Disc.temp.probe error",
    143: "AL131 Suct.temp.probe error",
    144: "AL132 Disc.press.probe error",
    145: "AL133 Suct.press.probe error",
    146: "AL134 Tank temp.probe error",
    147: "AL135 EVI SuctT.probe error",
    148: "AL136 EVI SuctP.probe error",
    149: "AL137 Flow switch alarm",
    150: "AL138 High temp. alarm",
    151: "AL139 Low temp. alarm",
    152: "AL140 Temp.delta alarm",
    153: "AL141 EVI: Param.range error",
    154: "AL142 EVI: Low superheat",
    155: "AL143 EVI: LOP",
    156: "AL144 EVI: MOP",
    157: "AL145 EVI: High condens.temp",
    158: "AL146 EVI: Low suction temp",
    159: "AL147 EVI: Motor error",
    160: "AL148 EVI: Self Tuning",
    161: "AL149 EVI: Emergency closing",
    162: "AL150 EVI: ServicePosit% err",
    163: "AL151 EVI: ValveID pin error",
    164: "AL152 Supply power error",
    165: "AL153 Fan1 fault",
    166: "AL154 Fan2 fault",
    167: "AL155 Fans Offline",
    168: "AL165 Slave1 Offline",
    169: "AL166 Master Offline",
    170: "AL167 Slave2 Offline",
    171: "AL168 Slave3 Offline",
    172: "AL169 Slave4 Offline",
    173: "AL170 Slave5 Offline",
    174: "AL171 Slave6 Offline",
    175: "AL172 Slave7 Offline",
    176: "AL173 Slave8 Offline",
    177: "AL174 Slave9 Offline",
    188: "AL177 Electric Meter Offline",
}

# ============================================================================
# SG READY MODES
# ============================================================================
SG_MODE_NORMAL = 0
SG_MODE_MINUS = 1
SG_MODE_PLUS = 2
SG_MODE_PLUS_PLUS = 3

SG_MODE_MAP = {
    SG_MODE_NORMAL: "Normal",
    SG_MODE_MINUS: "SG-",
    SG_MODE_PLUS: "SG+",
    SG_MODE_PLUS_PLUS: "SG++"
}

# ============================================================================
# WEEKDAY MAP
# ============================================================================
WEEKDAY_MAP = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    7: "Sunday"
}
