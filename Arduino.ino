//Latest code for FIVE FLEX sensors
//Date_ 16/01/2020
#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
RH_ASK rf_driver;

//Assigning variable names ro Analogs pins A0 to A5
const int FLEX_PIN1=A0;
const int FLEX_PIN2=A1;
const int FLEX_PIN3=A2;
const int FLEX_PIN4=A3;
const int FLEX_PIN5=A4;


// set pin numbers for switch
const int buttonPin = 12;
int buttonState = 0;

//Voltage to flex sensors
const float VCC=3.3;

int i;


//Initailize variables to store value of current position of sensor
int b1=0;
int b2=0;
int b3=0;
int b4=0;
int b5=0;


//Initializing input pins
void setup() {
rf_driver.init();  
Serial.begin(9600);   //Starting serial communication
pinMode(FLEX_PIN1,INPUT);
pinMode(FLEX_PIN2,INPUT);
pinMode(FLEX_PIN3,INPUT);
pinMode(FLEX_PIN4,INPUT);
pinMode(FLEX_PIN5,INPUT);
//Serial.println("1");  
// initialize the pushbutton pin as an input:
pinMode(buttonPin, INPUT);

buttonState = digitalRead(buttonPin);

if (buttonState == HIGH) {     
    // turn LED on:    
    //digitalWrite(ledPin, HIGH);
    Serial.println("1");  
  } 
  else {
    // turn LED off:
    //digitalWrite(ledPin, LOW);
   Serial.println("0"); 
  }
}


void loop()
        {
        //For finger 1 (THUMB):
        
        int flexADC1 = analogRead(FLEX_PIN1);
        //Serial.println("Flex1 = ");
        //delay(1500);
        //Serial.println(flexADC1);
        //delay(1500);
        if (flexADC1 >=130)
        {
          //Serial.println("No Bending");
          b1=0;
        }
        else
        {
          //Serial.println("Bending");
          b1=1;
         }
         
         
        //For finger 2 (INDEX):
        int flexADC2 = analogRead(FLEX_PIN2);
        //Serial.println("Flex2 = ");
        //delay(1500);
        //Serial.println(flexADC2);
        //delay(1500);
        if (flexADC2 >=60)
        {
          b2=0;
        }
        else
        {
          b2=1;
         }
         
         
        //For finger 3 (MIDDLE):
        int flexADC3 = analogRead(FLEX_PIN3);
        //Serial.println("Flex3 = ");
        //delay(1500);
        //Serial.println(flexADC3);
        //delay(1500);
        if (flexADC3 >=90)
        {
          b3=0;
        }
        else
        {
          b3=1;
         }
         
         
        //For finger 4 (RING):
        int flexADC4 = analogRead(FLEX_PIN4);
        //Serial.println("Flex4 = ");
        //delay(1500);
        //Serial.println(flexADC4);
        //delay(1500);
        if (flexADC4 >=80)
        {
          b4=0;
        }
        else
        {
          b4=1;
         }
         
         
        //For finger 5 (TINY):
        int flexADC5 = analogRead(FLEX_PIN5);
        //Serial.println("Flex5 = ");
        //delay(1500);
        //Serial.println(flexADC5);
        //delay(1500);
        if (flexADC5 >=80)
        {
          b5=0;
        }
        else
        {
          b5=1;
         }
        
        // send the data
        //Serial.println("DATA TO BE TRANSFERED:");
        //delay(3000);
        //Serial.println(String(b1)+String(b2)+String(b3)+String(b4)+String(b5));
        // give the loop some break
        delay(5000);    
        String a=String(b1)+String(b2)+String(b3)+String(b4)+String(b5);
        String str = a; 
 
        // Length (with one extra character for the null terminator)
        int str_len = str.length() + 1; 
 
       // Prepare the character array (the buffer) 
        char char_array[str_len];
        str.toCharArray(char_array, str_len);
        
        Serial.println(char_array);
        char *msg = char_array;
        rf_driver.send((uint8_t *)msg, strlen(msg));
        rf_driver.waitPacketSent();
        delay(1000);
 
         
        }  //End of loop
