/*
print_time() returns a string in the format mm-dd-yyyy hh:mm:ss
*/

#include "RTClib.h"
#include <SD.h>
#include <SPI.h>

RTC_DS1307 rtc;
const int chipSelect = 10;

File dataFile;

String print_time(DateTime timestamp) {
  char message[120];

  int Year = timestamp.year();
  int Month = timestamp.month();
  int Day = timestamp.day();
  int Hour = timestamp.hour();
  int Minute = timestamp.minute();
  int Second= timestamp.second();

  sprintf(message, "%d-%d-%d %02d:%02d:%02d", Month,Day,Year,Hour,Minute,Second);
  
  return message;
}

void setup(){
  Serial.begin(9600);
  
  pinMode(chipSelect, OUTPUT);
  if (!SD.begin(chipSelect)){
    Serial.println("Error: SD card would not initiate.");
  }
  
  rtc.begin();
  if (!rtc.isrunning()){
    Serial.println("Clock is not running");
  }
  
  dataFile = SD.open("log0.csv", FILE_WRITE);
  if (!dataFile){
    Serial.println("Could not open file.");
  }
  
}

void loop(){
  Datetime now = rtc.now();
  dataFile.println(print_time(now));
  
  delay(3000);
}
