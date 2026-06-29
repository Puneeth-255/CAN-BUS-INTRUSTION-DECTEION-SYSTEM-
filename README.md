# CAN-BUS-INTRUSTION-DECTEION-SYSTEM-


Modern vehicles are no longer simple mechanical machines. They are highly complex computerized systems with dozens of Electronic Control Units (ECUs) communicating with each other through a network called the Controller Area Network (CAN Bus). The CAN Bus protocol was originally designed for reliability and speed, not for security. As a result, it lacks basic security features such as message authentication and encryption, making it highly vulnerable to cyber attacks.

Vehicle cybersecurity has become a critical area of concern in recent years. Hackers have demonstrated that it is possible to remotely control vehicle functions such as brakes, steering, and engine by injecting malicious CAN messages. This makes it extremely important to develop intelligent systems that can monitor CAN Bus traffic and detect abnormal or malicious messages before they cause harm.

An Intrusion Detection System (IDS) is a security tool that continuously monitors network traffic and raises an alert whenever it detects unusual or suspicious behavior. When applied to CAN Bus networks, an IDS can identify attack patterns like message spoofing, replay attacks, and Denial of Service (DoS) attacks.

Machine Learning (ML) has emerged as one of the most powerful tools for anomaly detection. Unlike traditional rule-based IDS systems that can only detect known attacks, ML-based IDS systems can learn the normal behavior of the network and identify any deviation from it, even if the attack has never been seen before.

This project presents the design and implementation of a CAN Bus Intrusion Detection System using Machine Learning. The system uses an Arduino UNO microcontroller connected to an MCP2515 CAN module and a DHT11 temperature/humidity sensor. CAN traffic is simulated on this hardware setup. The simulated CAN data is transmitted via serial communication to a Python-based IDS backend that processes the data in real time.

The ML model used is the Isolation Forest algorithm, which is an unsupervised anomaly detection algorithm particularly well-suited for detecting outliers in high-dimensional data. The system trains on normal CAN traffic patterns and identifies any anomalous messages as potential attacks. Detected intrusions are displayed on a Streamlit web dashboard in real time, and an alert is also triggered on an LCD display connected to the Arduino.

The project is simulation-based and is designed for academic learning and research purposes. It provides a strong foundation for understanding vehicle cybersecurity and demonstrates how machine learning can be effectively applied to protect automotive communication networks.

