#include <AFMotor.h>

namespace catch_motor {

    // commands
    enum COMMAND {
        SET_MOTOR_1 = 0,
        SET_MOTOR_2 = 1
    };

    // directions from AFMotor.h
    /*
        FORWARD = 1
        BACKWARD = 2
        BREAK = 3           // DOES NOT WORK WITH DC MOTORS
        RELEASE = 4
    */

    // command example
    // 3 bytes
    // SET_MOTOR_X DIRECTION SPEED


    // responses
    enum RESPONSES {
        NOT_ENOUGH_CHARACTERS = 0,
        TOO_MANY_CHARACTERS = 1
    };
}


