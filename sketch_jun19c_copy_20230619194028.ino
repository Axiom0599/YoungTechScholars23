//Servometer. 

#include <ESP32Servo.h>

Servo ser;

void setup() {
  // put your setup code here, to run once: 
  ser.attach(2);
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:

  for(int a = 0; a <= 180; a++){
    delay(10);
    ser.write(a);
  }


 for(int i = 180; i>=0; i--){
   delay(10);
   ser.write(i); 
   int currentpos = ser.read();
   Serial.println(currentpos);
 }   
}



//use the serial monitor or the plotter to display the graph.