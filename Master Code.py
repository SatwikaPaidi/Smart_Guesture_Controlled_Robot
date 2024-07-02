#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#include <Wire.h>
#include <MPU6050.h>
#include <SoftwareSerial.h>

SoftwareSerial BTSerial(0, 1); // RX, TX pins for HC-05 module

MPU6050 mpu;

void setup() {
  Wire.begin();
  Serial.begin(9600); // Initialize serial communication for debugging
  BTSerial.begin(9600); // Initialize serial communication with HC-05 module
  
  mpu.initialize();
  if (!mpu.testConnection()) {
    Serial.println("MPU6050 connection failed");
    while (1);
  }
}

void loop() {
  int16_t ax, ay, az, gx, gy, gz;
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  // Convert raw accelerometer data to meaningful units (acceleration in g)
  float accX = ax / 16384.0;
  float accY = ay / 16384.0;
  float accZ = az / 16384.0;
  
  // Convert raw gyroscope data to meaningful units (angular velocity in degrees per second)
  float gyroX = gx / 131.0; // 131 LSB per degree per second for the gyroscope
  float gyroY = gy / 131.0;
  float gyroZ = gz / 131.0;
  
  // Calculate roll angle (rotation around X-axis) using accelerometer data
  float pitch = atan2(accY, accZ) * 180 / PI;
  
  // Calculate pitch angle (rotation around Y-axis) using accelerometer data
  float roll = atan2(-accX, sqrt(accY * accY + accZ * accZ)) * 180 / PI;
  
  // Print roll and pitch angles for debugging
  Serial.print("pitch ");
  Serial.print(pitch);
  Serial.print(" degrees, roll: ");
  Serial.print(roll);
  Serial.println(" degrees");
  
  // Send roll and pitch angles over Bluetooth
  BTSerial.print("Pitch:");
  BTSerial.print(pitch);
  BTSerial.print(" degrees, Roll:");
  BTSerial.print(roll);
  BTSerial.println(" degrees");

  // Print whether data is being sent
  Serial.println("Data sent to slave.");

  delay(1000); // Delay for 1 second before reading again
}
a  
  // Convert raw gyroscope data to meaningful units (angular velocity in degrees per second)
  float gyroX = gx / 131.0; // 131 LSB per degree per second for the gyroscope
  float gyroY = gy / 131.0;
  float gyroZ = gz / 131.0;
  
  // Calculate roll angle (rotation around X-axis) using accelerometer data
  float pitch = atan2(accY, accZ) * 180 / PI;
  
  // Calculate pitch angle (rotation around Y-axis) using accelerometer data
  float roll = atan2(-accX, sqrt(accY * accY + accZ * accZ)) * 180 / PI;
  
  // Print roll and pitch angles for debugging
  Serial.print("pitch ");
  Serial.print(pitch);
  Serial.print(" degrees, roll: ");
  Serial.print(roll);
  Serial.println(" degrees");
  
  // Send roll and pitch angles over Bluetooth
  Serial.print("pitch ");
  Serial.print(pitch);
  Serial.print(" degrees, roll: ");
  Serial.print(roll);
  Serial.println(" degrees");
  delay(1000); // Delay for 1 second before reading again
}

