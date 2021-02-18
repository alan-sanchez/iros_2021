
// Delcare all constants and variables
volatile unsigned long last_time = 0;
volatile unsigned long delta_t;
volatile float UV_Dose_0, UV_Dose_1, UV_Dose_2;
float V_conversion = .725;

void setup(){
  // Set baud rate
  Serial.begin(9600);
}

void loop(){
  // Compute actual polling time difference
  float delta_t = millis() - last_time;

  // Compute the diode current of the sensor with diode_current function
  float Di_0 = diode_current(analogRead(A0));

  // Compute Irradaince at sensor with mapfloat function
  float Ir_0 = mapfloat(Di_0, 0.0, 1.0, 0.0, 9.0); //Convert the voltage to a UV intensity level

  // Update UV dosage at sensor
  UV_Dose_0 += Ir_0 * delta_t/1000.0;

  // Serial print the irradiance and uv dosage at sensor
  Serial.print(delta_t);
  Serial.print(",");
  Serial.print(Ir_0);
  Serial.print(", ");
  Serial.println(UV_Dose_0);

  // update the last measured time before the time delay
  last_time = millis();

  // Add delay
  delay(1000);
}


float diode_current(float A_in){
  return 5.0 * A_in / 1023.0 / V_conversion;
}

float mapfloat(float x, float in_min, float in_max, float out_min, float out_max){
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
