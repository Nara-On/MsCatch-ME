#include <AFMotor.h>

const unsigned int MAX_MESSAGE_LENGTH = 12; // saves 11 characters + end char '\0'

// communication
#include "catch_communication.h"
AF_DCMotor motor1 = AF_DCMotor(1, MOTOR12_1KHZ);
AF_DCMotor motor2 = AF_DCMotor(3, MOTOR34_1KHZ);


void message_to_command(char* message, int message_length) {
    if (message_length < 3) {
        Serial.println("NOT_ENOUGH_CHARACTERS");
        return;
    };

    AF_DCMotor* p_motor;
    switch (int(message[0])) {
        case catch_motor::SET_MOTOR_1:
            Serial.print("M1 ");
            p_motor = &motor1;
            break;
        case catch_motor::SET_MOTOR_2:
            Serial.print("M2 ");
            p_motor = &motor2;
            break;
    }

    switch (uint8_t(message[1])) {
        case FORWARD:
            p_motor->run(FORWARD);
            Serial.print("FORWARD ");
            break;
        case BACKWARD:
            p_motor->run(BACKWARD);
            Serial.print("BACKWARD ");
            break;
        case RELEASE:
            p_motor->run(RELEASE);
            Serial.print("STOP ");
            break;
    }

    Serial.print("SPEED ");
    p_motor->setSpeed(uint8_t(message[2]));
    Serial.print(uint8_t(message[2]));

    Serial.print("\n");
}


void setup() {
    Serial.begin(9600);
}


void loop() {
    static char message[MAX_MESSAGE_LENGTH];
    static unsigned int message_pos = 0;
    static bool too_many_chars = false;

    while (Serial.available() > 0) {
        char inByte = Serial.read(); // read the incoming byte:

        if ( inByte == '\n') { // message is over
            message[message_pos] = '\0';
            // Serial.println(message);
            if (!too_many_chars) {
                message_to_command(message, message_pos);
            } else {
                Serial.println("TOO_MANY_CHARS");
            }
            message_pos = 0;
            too_many_chars = false;
        }
        else if (message_pos >= MAX_MESSAGE_LENGTH - 1) {  // more characters sent than in buffer
            // message[message_pos] = '\0';
            // Serial.println(message);
            too_many_chars = true;
            message_pos = 0;
            message[message_pos] = inByte;
            message_pos++;
        }
        else {  // continue recording
            message[message_pos] = inByte;
            message_pos++;
        }
    }
}
