
// Delcare all constants and variables
volatile unsigned long last_time = 0;
volatile unsigned long delta_t;
volatile float UV_Dose_0,  UV_Dose_1,  UV_Dose_2,  UV_Dose_3,
         UV_Dose_4,  UV_Dose_5,  UV_Dose_6,  UV_Dose_7,
         UV_Dose_8,  UV_Dose_9,  UV_Dose_10, UV_Dose_11,
         UV_Dose_12, UV_Dose_13, UV_Dose_14;//, UV_Dose_15;

float V_conversion = 0.725;

void setup() {
  // Set baud rate
  Serial.begin(19200);
}

void loop() {
  // Compute actual polling time difference
  delta_t = millis() - last_time;

  // Compute the diode current of the sensors with diode_current function
  float Di_0  = diode_current(analogRead(A0));
  float Di_1  = diode_current(analogRead(A1));
  float Di_2  = diode_current(analogRead(A2));
  float Di_3  = diode_current(analogRead(A3));
  float Di_4  = diode_current(analogRead(A4));
  float Di_5  = diode_current(analogRead(A5));
  float Di_6  = diode_current(analogRead(A6));
  float Di_7  = diode_current(analogRead(A7));
  float Di_8  = diode_current(analogRead(A8));
  float Di_9  = diode_current(analogRead(A9));
  float Di_10 = diode_current(analogRead(A10));
  float Di_11 = diode_current(analogRead(A11));
  float Di_12 = diode_current(analogRead(A12));
  float Di_13 = diode_current(analogRead(A13));
  float Di_14 = diode_current(analogRead(A14));
  //  float Di_15 = diode_current(analogRead(A15));

  // Compute Irradiance at sensor with mapfloat function //Convert the voltage to a UV intensity level
  float Ir_0  = mapfloat(Di_0,  0.0, 1.0, 0.0, 9.0);
  float Ir_1  = mapfloat(Di_1,  0.0, 1.0, 0.0, 9.0);
  float Ir_2  = mapfloat(Di_2,  0.0, 1.0, 0.0, 9.0);
  float Ir_3  = mapfloat(Di_3,  0.0, 1.0, 0.0, 9.0);
  float Ir_4  = mapfloat(Di_4,  0.0, 1.0, 0.0, 9.0);
  float Ir_5  = mapfloat(Di_5,  0.0, 1.0, 0.0, 9.0);
  float Ir_6  = mapfloat(Di_6,  0.0, 1.0, 0.0, 9.0);
  float Ir_7  = mapfloat(Di_7,  0.0, 1.0, 0.0, 9.0);
  float Ir_8  = mapfloat(Di_8,  0.0, 1.0, 0.0, 9.0);
  float Ir_9  = mapfloat(Di_9,  0.0, 1.0, 0.0, 9.0);
  float Ir_10 = mapfloat(Di_10, 0.0, 1.0, 0.0, 9.0);
  float Ir_11 = mapfloat(Di_11, 0.0, 1.0, 0.0, 9.0);
  float Ir_12 = mapfloat(Di_12, 0.0, 1.0, 0.0, 9.0);
  float Ir_13 = mapfloat(Di_13, 0.0, 1.0, 0.0, 9.0);
  float Ir_14 = mapfloat(Di_14, 0.0, 1.0, 0.0, 9.0);
  //  float Ir_15 = mapfloat(Di_15, 0.0, 1.0, 0.0, 9.0);

  // Update UV dosage at sensor. 
  // Multiply by 10 to convert to mW/cm^2 to W/m^2 and
  // divide by 1000 to convert ms to s
  UV_Dose_0  += 10 * Ir_0  * delta_t / 1000.0;
  UV_Dose_1  += 10 * Ir_1  * delta_t / 1000.0;
  UV_Dose_2  += 10 * Ir_2  * delta_t / 1000.0;
  UV_Dose_3  += 10 * Ir_3  * delta_t / 1000.0;
  UV_Dose_4  += 10 * Ir_4  * delta_t / 1000.0;
  UV_Dose_5  += 10 * Ir_5  * delta_t / 1000.0;
  UV_Dose_6  += 10 * Ir_6  * delta_t / 1000.0;
  UV_Dose_7  += 10 * Ir_7  * delta_t / 1000.0;
  UV_Dose_8  += 10 * Ir_8  * delta_t / 1000.0;
  UV_Dose_9  += 10 * Ir_9  * delta_t / 1000.0;
  UV_Dose_10 += 10 * Ir_10 * delta_t / 1000.0;
  UV_Dose_11 += 10 * Ir_11 * delta_t / 1000.0;
  UV_Dose_12 += 10 * Ir_12 * delta_t / 1000.0;
  UV_Dose_13 += 10 * Ir_13 * delta_t / 1000.0;
  UV_Dose_14 += 10 * Ir_14 * delta_t / 1000.0;
  //  UV_Dose_15 += 10 * Ir_15 * delta_t/1000.0;

  // Serial print the irradiance and uv dosage at sensor
  //  Serial.print(Ir_0);
  Serial.print(UV_Dose_0);
  Serial.print(", ");
  Serial.print(UV_Dose_1);
  Serial.print(", ");
  Serial.print(UV_Dose_2);
  Serial.print(", ");
  Serial.print(UV_Dose_3);
  Serial.print(", ");
  Serial.print(UV_Dose_4);
  Serial.print(", ");
  Serial.print(UV_Dose_5);
  Serial.print(", ");
  Serial.print(UV_Dose_6);
  Serial.print(", ");
  Serial.print(UV_Dose_7);
  Serial.print(", ");
  Serial.print(UV_Dose_8);
  Serial.print(", ");
  Serial.print(UV_Dose_9);
  Serial.print(", ");
  Serial.print(UV_Dose_10);
  Serial.print(", ");
  Serial.print(UV_Dose_11);
  Serial.print(", ");
  Serial.print(UV_Dose_12);
  Serial.print(", ");
  Serial.print(UV_Dose_13);
  Serial.print(", ");
  Serial.println(UV_Dose_14);

  // update the last measured time before the time delay
  last_time = millis();

  // Add delay
  delay(15);
}


float diode_current(float A_in) {
  float diode_current_val = 5.0 * A_in / 1023.0 / V_conversion;

  if (diode_current_val > .03) {
    return diode_current_val;
  }
  else {
    return 0.0;
  }
}


float mapfloat(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
