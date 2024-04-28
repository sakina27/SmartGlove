#include <VirtualWire.h>
#define RELAY1 4 //Defining the pin 7 of the Arduino for the 4 relay module
#define RELAY2 5 //Defining the pin 6 of the Arduino for the 4 relay module
const int datain = 11;
void setup()
{
    vw_set_ptt_inverted(true);
    vw_set_rx_pin(datain);
    vw_setup(2000);
    Serial.begin(9600);
    pinMode(RELAY1, OUTPUT); //Defining the pin 7 of the Arduino as output
    pinMode(RELAY2, OUTPUT); //Defining the pin 6 of the Arduino as output
    vw_rx_start();
}
    void loop()
{
    uint8_t buf[VW_MAX_MESSAGE_LEN];
    uint8_t buflen = VW_MAX_MESSAGE_LEN; 
    
    if (vw_get_message(buf, &buflen))
    {
      if(buf=='00001')
      {  
       digitalWrite(RELAY1,LOW); // This will Turn ON the relay 1
       delay(5000); // Wait for 5 seconds
       digitalWrite(RELAY1,HIGH); // This will Turn the Relay Off 
     }  
     if(buf=='00010')
     {
       digitalWrite(RELAY2,LOW); // This will Turn ON the relay
       delay(5000); // Wait for 5 seconds
       digitalWrite(RELAY2,HIGH); // This will Turn the Relay Off
     }
    }
}
