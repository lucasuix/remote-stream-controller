#include <IRremote.hpp>

const int rcvPin=3;
IRrecv irrecv(rcvPin);
decode_results results;

void setup()
{ 
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  pinMode(5, OUTPUT);
}


void loop() {
  
  if(IrReceiver.decode()) {
    auto value= IrReceiver.decodedIRData.decodedRawData;
    Serial.println(value)
    IrReceiver.resume(); // Receive the next value
  }
  
}
