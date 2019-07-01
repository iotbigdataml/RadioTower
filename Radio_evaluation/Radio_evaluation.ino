
#include <SoftwareSerial.h>
#include <SPI.h>
//#include <nRF24L01.h>
#include <RF24.h>

#define RX 9                            // Pin used for the receive port on the Arduino
#define TX 10                           // Pin used for the transmit port on the Arduino
#define MsgLn 25                        // Max size of a message

char character;                         // Character read from the serial port
SoftwareSerial mySerial(RX, TX, true);  // Here we define the serial port object


RF24 radio(7, 8);                       // Chip enable (7), Chip Select (8)
const byte address1[6] = "01011";        // Radio address - use only the channels that match the
                                        // numbers on your robots.
const byte address2[6] = "01100";        // Radio address - use only the channels that match the

char Msg[MsgLn];                        // Message buffer
int i;                                  // Loop index

void setup() 
{
  Serial.begin(9600);                   // Debug output in case you are connected to a monitor
  radio.begin();                        // Instantiate the radio object
    
  if (!radio.isChipConnected())
  {
      Serial.print("RADIO NOT CONNECTED!");
      while(!radio.isChipConnected());
  }
  
//  radio.openWritingPipe(address);       // Open the radio pipe using your address (read about pipes and channels)
//  radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
//  radio.stopListening();                // Now we listen for messages...
//  Serial.println("Radio Ready...");

  mySerial.begin(9600);                 // Open the software serial port. Once we open the port we
                                        // print a message and wait a second for things to settle
                                        // down.
                        
  Serial.println("Port setup complete...");
  delay(1000);

  i = 0;
}

void loop()                            
{
  radio.openReadingPipe(1,address1);
  radio.startListening();
  delay(100);
          if (radio.available())              // If we have messages, we print them out - otherwise we do nothing but listen.
           {
            char text[32] = "";
            radio.read(&text, sizeof(text));
            Serial.println(text);
            mySerial.write(text,sizeof(text));
           }
  

  while(mySerial.available())
  {
     character = mySerial.read();   // Here is where we read the data
      
     if (character == '+')          // Note that a '+' is a marker for the end of the message
     {
      
        if(!strcmp(Msg,"q"))
        {
            radio.openWritingPipe(address1);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
          Serial.println("Moving bot11");
          Serial.println(Msg);
//          mySerial.write("The quick red fox jumped over the lazy brown dog.\n");
          radio.write(&Msg, i);       // Here with send the message


        }
        else if(!strcmp(Msg,"p"))
        {
          radio.openWritingPipe(address2);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
          Serial.println("Moving bot12");
          Serial.println(Msg);
//           mySerial.write("The quick red fox jumped over the lazy brown dog.\n");
           radio.write(&Msg, i); 

        }
        else if(!strcmp(Msg,"m"))
        {
          Serial.println("Maintenance mode");
//           mySerial.write("The quick red fox jumped over the lazy brown dog.\n");
            radio.openWritingPipe(address1);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
            radio.write(&Msg, i);
            Serial.println(Msg);
            radio.openWritingPipe(address2);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
            radio.write(&Msg, i);
            Serial.println(Msg);

        }
           else if(!strcmp(Msg,"n"))
        {
          Serial.println("Exit Maintenance mode");
//           mySerial.write("The quick red fox jumped over the lazy brown dog.\n");
            radio.openWritingPipe(address1);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
            radio.write(&Msg, i);
            Serial.println(Msg);
            radio.openWritingPipe(address2);       // Open the radio pipe using your address (read about pipes and channels)
            radio.setPALevel(RF24_PA_MIN);        // Set the power level. Since the bots and the radio base station are close I use min power
            radio.stopListening();                // Now we listen for messages...
            radio.write(&Msg, i);
            Serial.println(Msg);

        }


        memset(Msg,0,MsgLn);
        i = 0;
     }
     else
     {
        Msg[i] = character;         // Here we build the message
        i++;  
     } // if
       
  } // while
}
  
