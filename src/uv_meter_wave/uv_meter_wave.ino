
//int sense_0 = A0; //Output from the sensor
int last_time = 0;
int delta_t;
float V_conversion = 1.22;
float UV_Dose_0, UV_Dose_1, UV_Dose_2;

void setup(){
  Serial.begin(9600);
}

void loop(){
//  Serial.print(millis());
//  Serial.print(", ");
  delta_t = millis() - last_time;

  float Di_0 = diode_current(analogRead(A0));

  float Ir_0 = mapfloat(Di_0, 0.0, 1.0, 0.0, 9.0); //Convert the voltage to a UV intensity level

  UV_Dose_0 += Ir_0 * delta_t/1000.0;
//  float uvDosage_0 = uvIntensity_0 *=
//  Serial.print(delta_t);
//  Serial.print(", ");
  Serial.print(Ir_0);
  Serial.print(", ");
  Serial.println(UV_Dose_0);
  last_time = millis();
  delay(1000);
}


float diode_current(float A_in){
  return 5.0 * A_in / 1023.0 / V_conversion;
}

float mapfloat(float x, float in_min, float in_max, float out_min, float out_max){
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

//float dosage(float Ir, T){
//  return
//}
