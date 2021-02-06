
int UVOUT = A0; //Output from the sensor

void setup()
{
  Serial.begin(9600);
  pinMode(UVOUT, INPUT);

}

void loop()
{
//  float Vo = 5.0*analogRead(UVOUT)/1023.0;
//  float Vo_d = analogRead(UVOUT);
//  float Vo_map = map(Vo_d, 0, 755, 0, 1023);
//  float Di = (5.0*Vo_map/1023.0)/4.3;
    
  float V = 5.0*analogRead(UVOUT)/1023.0;

//  float uvIntensity = mapfloat(Di, 0.0, 1.0, 0.0, 9.0); //Convert the voltage to a UV intensity level
  //  Serial.print(millis());

  //  Serial.print(" / UV Intensity (mW/cm^2): ");
//  Serial.print(Vo_d);
//  Serial.print(", ");
//  Serial.print(Vo_map);
//  Serial.print(", ");
//  Serial.print(Di);
//  Serial.print(", ");
//  Serial.println(uvIntensity);
    Serial.println(V);

  delay(200);
}



float mapfloat(float x, float in_min, float in_max, float out_min, float out_max)
{
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}
