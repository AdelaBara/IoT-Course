"""
IoT Course Interactive Presentation App
Using Streamlit for Node-RED, TP-Link Smart Plugs, and Broadlink Sensors
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="IoT Course - Node-RED Lab",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Helper functions for creating diagrams
def create_iot_architecture_diagram():
    """Create IoT architecture layered diagram"""
    fig = go.Figure()
    
    layers = [
        {"name": "Application Layer", "y": 4, "color": "#3498db", 
         "items": ["Dashboards", "Mobile Apps", "Web Interface"]},
        {"name": "Cloud/Backend", "y": 3, "color": "#9b59b6",
         "items": ["Data Storage", "Analytics", "ML/AI"]},
        {"name": "Edge/Gateway", "y": 2, "color": "#e67e22",
         "items": ["Node-RED", "Local Processing", "MQTT Broker"]},
        {"name": "Device Layer", "y": 1, "color": "#27ae60",
         "items": ["Sensors (Broadlink)", "Actuators (TP-Link)", "Smart Devices"]}
    ]
    
    for layer in layers:
        fig.add_trace(go.Bar(
            y=[layer["name"]],
            x=[10],
            orientation='h',
            name=layer["name"],
            marker=dict(color=layer["color"]),
            text=["<br>".join(layer["items"])],
            textposition='inside',
            textfont=dict(size=12, color='white'),
            hoverinfo='text',
            hovertext=f"<b>{layer['name']}</b><br>" + "<br>".join(layer["items"])
        ))
    
    fig.update_layout(
        title="IoT System Architecture - Layered View",
        showlegend=False,
        height=400,
        xaxis=dict(showticklabels=False, showgrid=False),
        yaxis=dict(showgrid=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def create_sensor_data_chart():
    """Create sample sensor data visualization"""
    hours = 24
    timestamps = pd.date_range(end=datetime.now(), periods=hours, freq='H')
    
    temp_base = 20
    temp_variation = 5 * np.sin(np.linspace(0, 2*np.pi, hours)) + np.random.normal(0, 0.5, hours)
    temperature = temp_base + temp_variation
    
    humidity = 65 - temp_variation + np.random.normal(0, 2, hours)
    
    df = pd.DataFrame({
        'Time': timestamps,
        'Temperature (°C)': temperature,
        'Humidity (%)': humidity
    })
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=df['Time'], y=df['Temperature (°C)'],
        mode='lines+markers',
        name='Temperature',
        line=dict(color='#e74c3c', width=3),
        marker=dict(size=6)
    ))
    
    fig.add_trace(go.Scatter(
        x=df['Time'], y=df['Humidity (%)'],
        mode='lines+markers',
        name='Humidity',
        line=dict(color='#3498db', width=3),
        marker=dict(size=6),
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="24-Hour Sensor Data Timeline",
        xaxis=dict(title="Time"),
        yaxis=dict(title="Temperature (°C)", titlefont=dict(color='#e74c3c')),
        yaxis2=dict(title="Humidity (%)", titlefont=dict(color='#3498db'),
                    overlaying='y', side='right'),
        hovermode='x unified',
        height=400
    )
    
    return fig

def create_energy_monitoring_chart():
    """Create energy consumption visualization"""
    hours = pd.date_range(end=datetime.now(), periods=24, freq='H')
    
    base_consumption = [50, 45, 40, 40, 45, 60, 150, 200, 180, 160, 140, 120,
                       130, 140, 150, 180, 200, 250, 220, 180, 150, 120, 80, 60]
    power = np.array(base_consumption) + np.random.normal(0, 10, 24)
    energy = np.cumsum(power) / 1000
    
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        x=hours, y=power,
        name='Power (W)',
        marker_color='#3498db',
        yaxis='y'
    ))
    
    fig.add_trace(go.Scatter(
        x=hours, y=energy,
        name='Energy (kWh)',
        line=dict(color='#e74c3c', width=3),
        mode='lines+markers',
        yaxis='y2'
    ))
    
    fig.update_layout(
        title="Smart Plug Energy Monitoring",
        xaxis=dict(title="Time"),
        yaxis=dict(title="Power (W)", titlefont=dict(color='#3498db')),
        yaxis2=dict(title="Cumulative Energy (kWh)", titlefont=dict(color='#e74c3c'),
                    overlaying='y', side='right'),
        height=400,
        hovermode='x unified'
    )
    
    return fig

def create_edge_vs_cloud_comparison():
    """Create edge vs cloud comparison chart"""
    categories = ['Latency', 'Privacy', 'Reliability<br>(offline)', 'Scalability', 
                  'Computing<br>Power', 'Cost<br>(long-term)']
    
    edge_scores = [95, 90, 95, 40, 50, 70]
    cloud_scores = [30, 40, 20, 95, 95, 60]
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatterpolar(
        r=edge_scores,
        theta=categories,
        fill='toself',
        name='Edge Computing',
        line_color='#27ae60'
    ))
    
    fig.add_trace(go.Scatterpolar(
        r=cloud_scores,
        theta=categories,
        fill='toself',
        name='Cloud Computing',
        line_color='#3498db'
    ))
    
    fig.update_layout(
        polar=dict(
            radialaxis=dict(visible=True, range=[0, 100])
        ),
        showlegend=True,
        title="Edge vs Cloud Computing Comparison",
        height=500
    )
    
    return fig

# Custom CSS for enhanced styling
st.markdown("""
<style>
    :root {
        --primary: #38bdf8;
        --primary-dark: #0ea5e9;
        --accent: #f97316;
        --bg-main: #f3f4f6;
        --bg-main-alt: #e5e7eb;
        --card-bg: #ffffff;
        --card-border: rgba(148, 163, 184, 0.35);
    }

    /* Light main content area */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at top left, #ffffff 0, var(--bg-main) 45%, var(--bg-main-alt) 100%);
        color: #0f172a;
    }

    /* Dark sidebar */
    [data-testid="stSidebar"] {
        background: radial-gradient(circle at top left, #020617 0, #020617 45%, #020617 100%);
        color: #e5e7eb;
        border-right: 1px solid rgba(148, 163, 184, 0.4);
        box-shadow: 8px 0 25px rgba(15, 23, 42, 0.7);
    }

    [data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    .main-header {
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 2.5rem;
        margin-top: 0.5rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        background: linear-gradient(120deg, #38bdf8, #a855f7, #f97316);
        -webkit-background-clip: text;
        background-clip: text;
        color: transparent;
        text-shadow: 0 0 25px rgba(56, 189, 248, 0.25);
    }

    .topic-header {
        font-size: 1.4rem;
        font-weight: 600;
        color: #0f172a;
        margin: 0.5rem 0 1rem 0;
        padding: 0.75rem 1.25rem;
        border-radius: 999px;
        display: inline-flex;
        align-items: center;
        gap: 0.6rem;
        background: linear-gradient(120deg, rgba(56, 189, 248, 0.18), rgba(168, 85, 247, 0.08));
        border: 1px solid rgba(148, 163, 184, 0.5);
        box-shadow: 0 8px 18px rgba(148, 163, 184, 0.35);
    }

    .topic-header::before {
        content: "●";
        font-size: 0.9rem;
        color: var(--primary);
        text-shadow: 0 0 12px rgba(56, 189, 248, 0.9);
    }

    .section-box,
    .lab-box {
        position: relative;
        background: var(--card-bg);
        border-radius: 16px;
        padding: 1.5rem 1.75rem;
        margin: 1.1rem 0;
        border: 1px solid var(--card-border);
        box-shadow: 0 10px 25px rgba(15, 23, 42, 0.08);
        transition: transform 0.18s ease-out,
                    box-shadow 0.18s ease-out,
                    border-color 0.18s ease-out;
    }

    .section-box:hover,
    .lab-box:hover {
        transform: translateY(-2px);
        border-color: rgba(56, 189, 248, 0.6);
        box-shadow: 0 14px 35px rgba(15, 23, 42, 0.18);
    }

    .lab-box {
        border-left: 4px solid #22c55e;
        background: linear-gradient(135deg, #ffffff 0, #ecfdf5 60%);
    }

    .section-box::before,
    .lab-box::before {
        content: "";
        position: absolute;
        inset: 0;
        border-radius: inherit;
        border: 1px solid rgba(148, 163, 184, 0.2);
        pointer-events: none;
        mix-blend-mode: screen;
        opacity: 0.9;
    }

    .code-example {
        background: radial-gradient(circle at 0% 0%, #111827 0, #020617 55%, #000000 100%);
        color: #e5e7eb;
        padding: 1rem 1.25rem;
        border-radius: 14px;
        font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
        font-size: 0.85rem;
        border: 1px solid rgba(15, 23, 42, 0.9);
        box-shadow: 0 16px 40px rgba(15, 23, 42, 0.9);
    }

    .code-example code {
        white-space: pre-wrap;
    }

    /* Slightly sleeker tabs */
    [data-testid="stHorizontalBlock"] > div[role="tablist"] button {
        border-radius: 999px;
        padding: 0.35rem 1.1rem;
    }
</style>
""", unsafe_allow_html=True)

# Course topics dictionary with detailed content
TOPICS = {
    "1. Introduction to IoT Systems": {
        "goal": "Give students a system-level view before touching tools.",
        "topics": [
            "What is IoT? Definitions and real-world applications",
            "IoT architecture: Devices, Gateway/Edge, Cloud/Backend, Applications",
            "IoT vs Cyber-Physical Systems (CPS)",
            "Examples: Smart home, smart grid, smart cities"
        ],
        "detailed_description": """
        The **Internet of Things (IoT)** refers to the paradigm where physical objects such as sensors, 
        actuators, and everyday devices are interconnected through the internet, enabling them to collect, 
        exchange, and act upon data. IoT systems bridge the physical and digital worlds, allowing automated 
        decision-making and intelligent services.

        An IoT system is typically composed of **four layers**: the perception layer (sensors and actuators), 
        the network layer (communication technologies), the processing layer (edge or cloud computing), and 
        the application layer (user-facing services). 

        IoT is closely related to **Cyber-Physical Systems (CPS)**, where computation, networking, and 
        physical processes are tightly integrated. Unlike traditional IT systems, IoT deployments must 
        handle real-world uncertainty, hardware constraints, and continuous data streams.
        """,
        "content": """
        ### Understanding IoT Systems
        
        **Internet of Things (IoT)** refers to the network of physical objects embedded with sensors, 
        software, and other technologies to connect and exchange data with other devices and systems 
        over the internet.
        
        #### IoT Architecture Layers:
        1. **Device Layer**: Sensors (Broadlink temperature/humidity) and actuators (TP-Link smart plugs)
        2. **Gateway/Edge Layer**: Local processing and data aggregation (Node-RED on Raspberry Pi)
        3. **Cloud/Backend**: Data storage and advanced analytics
        4. **Application Layer**: Dashboards and user interfaces
        
        #### Real-World Applications:
        - **Smart Homes**: Automated climate control, energy management
        - **Smart Buildings**: HVAC optimization, occupancy detection
        - **Industrial IoT**: Predictive maintenance, process automation
        """,
        "code": """
# Example: IoT System Architecture
# Device → Gateway → Cloud → Application

Sensor (Broadlink) → Node-RED (Raspberry Pi) → MQTT Broker → Dashboard
                            ↓
                    TP-Link Plug (Actuator)
        """
    },
    
    "2. Hardware platforms": {
        "goal": "Understand IoT hardware platforms and programming fundamentals.",
        "topics": [
            "Arduino: Microcontroller basics and C/C++ programming",
            "Raspberry Pi: Linux-based computing and Python",
            "ESP8266/ESP32: Wi-Fi enabled microcontrollers",
            "MicroPython: Python for microcontrollers",
            "Choosing the right platform for your project"
        ],
        "detailed_description": """
        **IoT hardware platforms** provide the foundation for building connected devices. Understanding 
        the capabilities and limitations of different platforms is essential for successful IoT development.

        **Arduino** is a popular microcontroller platform ideal for simple sensor reading and actuator 
        control. It uses C/C++ programming and is excellent for real-time, deterministic tasks with low 
        power consumption.

        **Raspberry Pi** is a full Linux computer that offers more processing power, networking capabilities, 
        and support for high-level languages like Python. It's suitable for edge computing, running Node-RED, 
        and hosting local services.

        **ESP8266 and ESP32** are Wi-Fi-enabled microcontrollers that bridge the gap between simple 
        microcontrollers and full computers. They're cost-effective, low-power, and can run **MicroPython**, 
        allowing Python programming on resource-constrained devices.

        Selecting the appropriate hardware depends on **power requirements, processing needs, connectivity 
        options, cost constraints, and development complexity**. Each platform has its ecosystem of libraries, 
        tools, and community support.
        """,
        "content": """
        ### IoT Hardware Platforms
        
        #### Arduino Platform
        - **Microcontroller**: ATmega328P (Arduino Uno), ARM Cortex (Arduino Due)
        - **Programming**: C/C++ using Arduino IDE
        - **Best for**: Real-time control, low power applications, simple sensors
        - **Limitations**: No built-in networking, limited memory
        
        #### Raspberry Pi
        - **Processor**: ARM-based Linux computer
        - **Programming**: Python, Node.js, Java, C++
        - **Best for**: Edge computing, Node-RED, complex applications
        - **Features**: Full OS, USB ports, HDMI, GPIO pins
        - **Power**: Higher consumption (2-4W)
        
        #### ESP8266/ESP32
        - **Microcontroller**: Xtensa 32-bit processor with Wi-Fi
        - **Programming**: Arduino IDE, MicroPython, ESP-IDF
        - **Best for**: Wi-Fi IoT devices, battery-powered sensors
        - **Features**: Built-in Wi-Fi (and Bluetooth on ESP32)
        - **Cost**: Very affordable ($2-5)
        
        #### MicroPython
        - **Language**: Python 3 subset for microcontrollers
        - **Platforms**: ESP8266, ESP32, Raspberry Pi Pico, PyBoard
        - **Advantages**: Rapid prototyping, familiar syntax, REPL interface
        - **Use cases**: Quick IoT prototypes, educational projects
        
        #### Platform Comparison
        
        | Feature | Arduino | Raspberry Pi | ESP8266/32 |
        |---------|---------|--------------|------------|
        | Processing | Low | High | Medium |
        | Memory | KB | GB | MB |
        | Power | Very Low | High | Low |
        | Networking | External | Built-in | Wi-Fi Built-in |
        | OS | None | Linux | RTOS |
        | Price | $20-40 | $35-75 | $2-10 |
        """,
        "code": """
// Arduino - Read sensor and control actuator
#include <DHT.h>

#define DHTPIN 2
#define RELAY_PIN 3
DHT dht(DHTPIN, DHT11);

void setup() {
  Serial.begin(9600);
  pinMode(RELAY_PIN, OUTPUT);
  dht.begin();
}

void loop() {
  float temp = dht.readTemperature();
  float humidity = dht.readHumidity();
  
  Serial.print("Temp: ");
  Serial.print(temp);
  Serial.print(" °C, Humidity: ");
  Serial.println(humidity);
  
  if (temp > 25) {
    digitalWrite(RELAY_PIN, HIGH);
  } else {
    digitalWrite(RELAY_PIN, LOW);
  }
  
  delay(2000);
}

# MicroPython on ESP8266 - MQTT sensor
import machine
import dht
import time
from umqtt.simple import MQTTClient

# Setup
sensor = dht.DHT11(machine.Pin(2))
client = MQTTClient("esp8266", "mqtt.broker.com")
client.connect()

while True:
    sensor.measure()
    temp = sensor.temperature()
    humidity = sensor.humidity()
    
    # Publish to MQTT
    client.publish(b"home/temperature", str(temp))
    client.publish(b"home/humidity", str(humidity))
    
    time.sleep(60)

# Raspberry Pi Python - Read and log
import board
import adafruit_dht
import time
import sqlite3

sensor = adafruit_dht.DHT11(board.D4)
db = sqlite3.connect('sensor_data.db')

while True:
    try:
        temp = sensor.temperature
        humidity = sensor.humidity
        
        db.execute("INSERT INTO readings VALUES (?, ?, ?)",
                   (time.time(), temp, humidity))
        db.commit()
        
        print(f"Temp: {temp}°C, Humidity: {humidity}%")
    except RuntimeError:
        continue
    
    time.sleep(30)
        """
    },
    
    "3. Sensors & Actuators": {
        "goal": "Understand how physical-world data and control are handled.",
        "topics": [
            "Temperature & humidity sensor fundamentals",
            "Sampling rate, resolution, accuracy, calibration",
            "Actuators: Relays, smart plugs, energy monitoring",
            "Device constraints: power, connectivity, latency"
        ],
        "detailed_description": """
        **Sensors** are the fundamental components that enable IoT systems to perceive the physical 
        environment. Temperature and humidity sensors measure environmental conditions using physical 
        principles such as electrical resistance, capacitance, or semiconductor behavior. Key performance 
        metrics include accuracy, resolution, sampling frequency, and response time.

        **Actuators**, on the other hand, allow IoT systems to influence the physical world. Smart plugs 
        are a common actuator that enable remote switching of electrical loads. 

        In practice, sensors and actuators are subject to **noise, drift, and failures**. Therefore, IoT 
        applications must incorporate validation, filtering, and fault-tolerant design principles.
        """,
        "content": """
        ### Sensors in IoT
        
        **Broadlink Temperature & Humidity Sensors** measure environmental conditions:
        - **Temperature**: Typically in Celsius/Fahrenheit
        - **Humidity**: Relative humidity percentage (0-100%)
        - **Sampling Rate**: How often the sensor takes readings
        - **Accuracy**: ±0.5°C for temperature, ±3% for humidity (typical)
        
        ### Actuators in IoT
        
        **TP-Link Smart Plugs** are network-controlled switches that:
        - Turn devices ON/OFF remotely
        - Monitor energy consumption (power, voltage, current)
        - Provide scheduling capabilities
        - Support local and cloud control
        
        #### Key Considerations:
        - Sensor noise and calibration requirements
        - Response time and latency
        - Power consumption and connectivity reliability
        """,
        "code": """
// Node-RED Function Node Example
// Read Broadlink sensor data and control smart plug

if (msg.payload.temperature > 25) {
    msg.payload = {
        "system": {"set_relay_state": {"state": 1}}
    };
    node.status({fill:"red", shape:"dot", text:"Cooling ON"});
} else if (msg.payload.temperature < 20) {
    msg.payload = {
        "system": {"set_relay_state": {"state": 0}}
    };
    node.status({fill:"blue", shape:"dot", text:"Cooling OFF"});
}
return msg;
        """
    },
    
    "4. IoT Communication protocols": {
        "goal": "Explain how devices talk to each other.",
        "topics": [
            "Network layers: Wi-Fi, BLE, Zigbee, Z-Wave",
            "Application protocols: HTTP/REST, MQTT",
            "Device discovery & local vs cloud control",
            "Publish-subscribe model"
        ],
        "detailed_description": """
        **Communication** is the backbone of IoT systems. Devices typically connect using wireless 
        technologies such as Wi-Fi, Bluetooth Low Energy (BLE), Zigbee, or Z-Wave. Each technology 
        involves trade-offs in terms of range, bandwidth, power consumption, and scalability.

        At the application layer, protocols such as **HTTP, MQTT** are widely used. HTTP 
        follows a request–response model, while MQTT uses a lightweight publish–subscribe approach 
        that is particularly well-suited for IoT environments. 

        **Reliability, latency, and security** are key concerns in IoT communication, especially when 
        devices operate over public networks.
        """,
        "content": """
        ### Communication Protocols in IoT
        
        #### Network Protocols:
        - **Wi-Fi**: High bandwidth, higher power consumption (TP-Link plugs use Wi-Fi)
        - **Bluetooth Low Energy (BLE)**: Low power, short range
        - **Zigbee/Z-Wave**: Mesh networks, low power, smart home focus
        
        #### Application Protocols:
        
        **HTTP/REST**: Request-response model
        - Used by TP-Link Kasa API
        - Synchronous communication
        - Easy to debug and implement
        
        **MQTT**: Publish-subscribe model
        - MQTT is a lightweight messaging protocol designed for resource-constrained devices and unreliable networks, which makes it ideal for IoT systems.
        - Instead of devices talking directly to each other, MQTT uses an asynchronous publish–subscribe model where devices publish messages to topics, and subscribers receive messages from those topics. A central broker manages message delivery.
        - MQTT decouples who sends data from who receives it. 
        MQTT Architecture
        - Publisher - a device or application that sends data (temperature sensor, humidity sensor). It publishes messages to a topic
        - Subscriber - a device or application that receives data (Node-RED flow, database writer)
        - Broker (Core of MQTT) - central server that receives messages from publishers and forwards them to subscribers (Mosquitto, HiveMQ)
      
        #### MQTT vs HTTP Comparisson
        |Feature | MQTT | HTTP|
        |---------|---------|------------|
        |Model	| Publish–Subscribe	| Request–Response|
        |Overhead |	Very low	| High |
        |Latency |	Low |	Higher|
        |Scalability |	Excellent |	Limited|
        |Battery usage |	Low |	High |
        |Use cases |	Sensor networks, real-time updates |	Web services, REST APIs |
        - MQTT is event-driven, HTTP is polling-based.
        
        #### Local vs Cloud Control:
        - **Local**: Faster response, works offline, privacy
        - **Cloud**: Remote access, vendor features, requires internet
        """,
        "code": """
// MQTT Topic Structure Example
home/living_room/temperature     → 23.5
home/living_room/humidity        → 65
home/bedroom/plug/status         → ON
home/bedroom/plug/power          → 125.4

// Node-RED MQTT Subscribe Node
Topic: home/+/temperature
Output: All temperature readings from any room

// Node-RED MQTT Publish Node
Topic: home/bedroom/plug/command
Payload: {"state": "ON"}
        """
    },
    
    "5. Node-RED as IoT middleware": {
        "goal": "Make Node-RED the core workflow tool.",
        "topics": [
            "What is Node-RED and why it's used in IoT",
            "Flow-based programming paradigm",
            "Node types: Input, Function, Output",
            "Context storage: flow, global, persistent",
            "JavaScript logic in Function nodes"
        ],
        "detailed_description": """
        **Node-RED** is a flow-based development environment designed to simplify the integration of 
        hardware devices, APIs, and online services. It acts as middleware, orchestrating data flows 
        between sensors, processing logic, and actuators.

        Node-RED uses **visual programming concepts** where nodes represent functional blocks and flows 
        represent data paths. Function nodes allow custom logic using JavaScript, enabling rapid 
        prototyping and deployment.

        In IoT systems, Node-RED often runs on **edge devices** such as Raspberry Pi or local servers, 
        providing low-latency processing and resilience against network failures.
        """,
        "content": """
        ### Node-RED: Visual Programming for IoT
        
        **Node-RED** is a flow-based programming tool built on Node.js, perfect for IoT applications.
        
        #### Key Features:
        - **Visual Programming**: Drag-and-drop interface
        - **Extensive Library**: Thousands of community nodes
        - **JavaScript Support**: Custom logic in Function nodes
        - **Integration Ready**: HTTP, MQTT, WebSockets, databases
        
        #### Node Types:
        
        **Input Nodes**: 
        - MQTT In, HTTP In, Inject (testing)
        - Sensor data sources (Broadlink)
        
        **Function Nodes**:
        - JavaScript processing
        - Data transformation
        - Logic and decision making
        
        **Output Nodes**:
        - MQTT Out, HTTP Request
        - Smart plug control (TP-Link)
        - Debug nodes
        - Dashboard widgets
        
        #### Context Storage:
        - **Flow Context**: Shared within a flow/tab
        - **Global Context**: Shared across all flows
        - **Persistent**: Survives Node-RED restarts
        """,
        "code": """
// Node-RED Function Node - Temperature Control with Hysteresis
var temp = msg.payload.temperature;
var currentState = flow.get('plugState') || 'OFF';
var threshold_high = 25;
var threshold_low = 22;

if (temp > threshold_high && currentState === 'OFF') {
    flow.set('plugState', 'ON');
    msg.payload = {"state": "ON"};
    node.status({fill:"red", shape:"dot", text:`ON: ${temp}°C`});
} else if (temp < threshold_low && currentState === 'ON') {
    flow.set('plugState', 'OFF');
    msg.payload = {"state": "OFF"};
    node.status({fill:"blue", shape:"dot", text:`OFF: ${temp}°C`});
} else {
    return null; // No change
}

return msg;
        """
    },
    
    "6. Device integration in Node-RED": {
        "goal": "Teach real-world integration challenges.",
        "topics": [
            "Vendor ecosystems (TP-Link, Broadlink)",
            "Local vs cloud APIs",
            "Reverse engineering & community nodes",
            "Rate limits and authentication tokens",
            "Device reliability & failure handling"
        ],
        "detailed_description": """
        Integrating **heterogeneous devices** is one of the main challenges in IoT. Vendors such as 
        TP-Link and Broadlink provide proprietary ecosystems, APIs, and cloud services. Node-RED 
        supports device integration through community-contributed nodes and API-based communication.

        A key design decision is whether devices are **controlled locally or via cloud platforms**. 
        Local control improves latency and privacy, while cloud-based control enables remote access.

        Robust IoT applications must handle **device disconnections, API changes, and authentication 
        token expiration** gracefully.
        """,
        "content": """
        ### Device Integration in Node-RED
        
        #### TP-Link Smart Plugs:
        - **TP-Link Cloud API**: Requires authentication, remote access
        - **Local API**: UDP protocol on port 9999, faster response
        - **Community Nodes**: `node-red-contrib-tplink-tapo`
        
        #### Broadlink Sensors:
        - **RF Communication**: 433MHz protocol
        - **Python Libraries**: python-broadlink
        - **Node-RED Integration**: HTTP bridge or MQTT
        
        #### Integration Challenges:
        
        1. **Authentication**: OAuth tokens, API keys
        2. **Rate Limiting**: API call restrictions
        3. **Device Discovery**: Finding devices on local network
        4. **Error Handling**: Network failures, device offline
        5. **Firmware Updates**: API changes over time
        
        #### Best Practices:
        - Test local control first before cloud
        - Implement retry logic for failed commands
        - Use MQTT for decoupling devices from logic
        - Log all API errors for debugging
        """,
        "code": """
// Example: TP-Link Local Control (Python)
from pyHS100 import SmartPlug

plug = SmartPlug("192.168.1.100")
print(f"Plug state: {plug.state}")
print(f"Power: {plug.get_emeter_realtime()}")

plug.turn_on()

// Node-RED Function - Error Handling
try {
    // Attempt to control plug
    msg.payload = {"state": "ON"};
} catch(err) {
    node.error("Failed to control plug: " + err.message);
    msg.payload = null;
    flow.set('deviceStatus', 'offline');
}
return msg;
        """
    },
    
    "7. Data management": {
        "goal": "Move from automation to data-driven IoT.",
        "topics": [
            "Time-series data in IoT",
            "Data formats: JSON, timestamps, metadata",
            "Local vs cloud storage",
            "Databases: InfluxDB, SQLite, MongoDB",
            "Data retention policies"
        ],
        "detailed_description": """
        **IoT systems generate large volumes of time-series data**. Proper data handling involves 
        structuring data with timestamps, metadata, and contextual information. JSON is the most 
        common data format due to its readability and flexibility.

        Data can be stored **locally for low-latency access** or in the cloud for scalability and 
        long-term analytics. Time-series databases such as **InfluxDB** are optimized for sensor 
        data and support efficient querying and aggregation.

        **Preprocessing steps** such as filtering, aggregation, and anomaly detection are often 
        applied before data is used for visualization or decision-making.
        """,
        "content": """
        ### IoT Data Management
        
        #### Time-Series Data:
        IoT sensors generate time-stamped measurements continuously.
        
        **Example Data Point**:
        ```json
        {
            "timestamp": "2025-12-13T10:30:00Z",
            "sensor_id": "broadlink_bedroom",
            "temperature": 23.5,
            "humidity": 65.2,
            "location": "bedroom"
        }
        ```
        
        #### Storage Options:
        
        **InfluxDB** (Time-Series Database):
        - Optimized for time-stamped data
        - Efficient storage and query
        - Built-in downsampling. 
        
        **SQLite** (Lightweight):
        - File-based, no server required
        - Good for local storage
        - Limited scalability
        
        **MongoDB** (NoSQL):
        - Flexible schema
        - Good for JSON data
        - Scalable
        
        #### Data Retention:
        - **Raw Data**: Keep for 7-30 days
        - **Aggregated Data**: Keep for months/years
        - **Downsampling**: Hourly → Daily → Monthly averages. Built-in downsampling refers to a database feature that automatically reduces the resolution of time-series data over time, by storing aggregated versions (e.g., averages, min/max, counts) of high-frequency measurements.
        """,
        "code": """
// Node-RED Function - Format Data for Storage
var timestamp = new Date().toISOString();
var data = {
    timestamp: timestamp,
    sensor_id: "broadlink_bedroom",
    temperature: msg.payload.temperature,
    humidity: msg.payload.humidity,
    location: msg.location || "unknown"
};

msg.topic = "INSERT INTO readings VALUES (?, ?, ?, ?, ?)";
msg.payload = [
    data.timestamp,
    data.sensor_id,
    data.temperature,
    data.humidity,
    data.location
];

return msg;

// SQL Query - Get Daily Average
SELECT 
    DATE(timestamp) as date,
    AVG(temperature) as avg_temp,
    MIN(temperature) as min_temp,
    MAX(temperature) as max_temp
FROM readings
WHERE timestamp > datetime('now', '-7 days')
GROUP BY DATE(timestamp);
        """
    },
    
    "8. Dashboards & Visualization": {
        "goal": "Turn data into insight.",
        "topics": [
            "Human-IoT interaction design",
            "Dashboards vs mobile apps",
            "Visualization best practices",
            "Node-RED Dashboard vs Grafana",
            "Real-time updates"
        ],
        "detailed_description": """
        **Visualization** plays a critical role in human–IoT interaction. Dashboards allow users to 
        monitor system status, understand trends, and manually control devices.

        Effective dashboards prioritize **clarity, real-time feedback, and usability**. Node-RED 
        provides built-in dashboard nodes for creating charts, gauges, and control elements with 
        minimal effort.

        For **advanced visualization and analytics**, external tools such as Grafana can be integrated 
        with Node-RED and time-series databases.
        """,
        "content": """
        ### IoT Dashboards
        
        #### Node-RED Dashboard:
        - Built-in solution for Node-RED
        - Real-time updates via WebSockets
        - Widgets: Gauges, charts, buttons, switches
        - Easy to deploy with flows
        
        #### Dashboard Design Principles:
        
        1. **Clarity**: Show only relevant information
        2. **Real-time**: Update without page refresh
        3. **Actionable**: Allow user control
        4. **Responsive**: Work on mobile devices
        5. **Visual Hierarchy**: Most important info first
        
        #### Widget Types:
        - **Gauges**: Current temperature/humidity
        - **Charts**: Time-series trends
        - **Switches**: Manual plug control
        - **Text**: Status messages
        - **Notifications**: Alerts and warnings
        
        #### Alternative Tools:
        - **Grafana**: Advanced analytics, multiple data sources
        - **Custom Web Apps**: More flexibility
        - **Mobile Apps**: Native device features
        """,
        "code": """
// Node-RED Dashboard Configuration
// Install: node-red-dashboard

[Dashboard Tab]
  ├── [Gauge] Temperature (0-50°C)
  ├── [Gauge] Humidity (0-100%)
  ├── [Chart] Temperature History (last 24h)
  ├── [Switch] Smart Plug Control
  └── [Text] Last Updated

// Function Node - Prepare Dashboard Data
msg.payload = parseFloat(msg.payload.temperature);
msg.topic = "Temperature";
return msg;

// Function Node - Color-coded Status
var temp = msg.payload;
var color = "green";

if (temp > 28) color = "red";
else if (temp > 25) color = "orange";
else if (temp < 18) color = "blue";

msg.color = color;
return msg;
        """
    },
    
    "9. Automation & Rule-based control": {
        "goal": "Core smart system behavior.",
        "topics": [
            "Rule-based logic and decision trees",
            "Event-driven vs time-based automation",
            "Scheduling with timers",
            "Hysteresis to avoid oscillations",
            "Multi-condition logic"
        ],
        "detailed_description": """
        **Automation** enables IoT systems to operate without continuous human intervention. Rule-based 
        control is commonly used, where predefined conditions trigger specific actions.

        IoT automation can be **event-driven** (reacting to sensor updates) or **time-based** (scheduled 
        actions). Care must be taken to avoid unstable behavior, such as frequent on/off switching, 
        which can be mitigated using **hysteresis and delays**.
        Hysteresis is a control concept where the system’s response depends not only on the current input value, but also on its previous state.
        In simple terms: you use two different thresholds instead of one, to avoid rapid on–off switching.
        More advanced systems may **combine multiple sensor inputs** and contextual information to make 
        decisions.
        """,
        "content": """
        ### Smart Automation Rules
        
        #### Rule-Based Control:
        Simple IF-THEN rules that respond to sensor data or events.
        
        **Example Rules**:
        - IF temperature > 25°C THEN turn ON cooling
        - IF humidity > 70% THEN activate dehumidifier
        - IF time = 10 PM THEN turn OFF lights
        
        #### Event-Driven Automation:
        - Triggered by sensor readings
        - Responds immediately to changes
        - Energy-efficient (no polling)
        
        #### Time-Based Automation:
        - Scheduled actions (cron jobs)
        - Daily routines
        - Energy optimization
        
        #### Hysteresis (Dead Band):
        Prevents rapid ON/OFF cycling:
        - Turn ON at 26°C
        - Turn OFF at 24°C
        - 2°C dead band prevents oscillation
        
        #### Multi-Condition Logic:
        ```
        IF (temperature > 25°C AND humidity > 60%) 
           OR time_between(14:00, 18:00)
        THEN activate_cooling()
        ```
        """,
        "code": """
// Node-RED Function - Advanced Control Logic
var temp = msg.payload.temperature;
var humidity = msg.payload.humidity;
var hour = new Date().getHours();
var manualOverride = flow.get('manualOverride') || false;

// Check manual override first
if (manualOverride) {
    return null;
}

// Time-based rules
var isNightMode = (hour >= 22 || hour < 6);
if (isNightMode) {
    msg.payload = {"state": "OFF"};
    return msg;
}

// Multi-condition automation
if (temp > 26 || (temp > 24 && humidity > 70)) {
    msg.payload = {
        "state": "ON",
        "reason": `High temp (${temp}°C) or humidity (${humidity}%)`
    };
} else if (temp < 22 && humidity < 50) {
    msg.payload = {
        "state": "OFF",
        "reason": "Comfortable conditions"
    };
} else {
    return null; // No change (hysteresis)
}

return msg;
        """
    },
    
    "10. Edge vs Cloud Computing": {
        "goal": "Critical design thinking for IoT architectures.",
        "topics": [
            "Edge computing concepts",
            "Latency, privacy, and reliability trade-offs",
            "When to process locally vs in cloud",
            "Hybrid architectures",
            "Offline operation"
        ],
        "detailed_description": """
        **IoT systems can process data at the edge, in the cloud, or using a hybrid approach**. Edge 
        computing reduces latency, improves privacy, and increases resilience by processing data close 
        to the source.

        **Cloud computing** offers scalability, centralized management, and advanced analytics. Hybrid 
        architectures combine both approaches, performing real-time control at the edge and long-term 
        analysis in the cloud.

        Understanding these **trade-offs** is essential for designing efficient and reliable IoT systems.
        """,
        "content": """
        ### Edge vs Cloud Computing
        
        #### Edge Computing (Local Processing):
        **Advantages**:
        - Low latency (milliseconds)
        - Works offline
        - Data privacy (stays local)
        - Reduced bandwidth usage
        - Lower cloud costs
        
        **Disadvantages**:
        - Limited compute power
        - Manual updates required
        - No remote access (without VPN)
        
        #### Cloud Computing:
        **Advantages**:
        - Unlimited compute/storage
        - Remote access from anywhere
        - Automatic updates
        - Advanced analytics (ML/AI)
        - Multi-device coordination
        
        **Disadvantages**:
        - Requires internet connection
        - Higher latency (seconds)
        - Monthly costs
        - Privacy concerns
        
        #### Hybrid Architecture (Best of Both):
        ```
        Local Edge (Node-RED):
        - Real-time control
        - Safety-critical logic
        - Privacy-sensitive data
        
        Cloud:
        - Historical analytics
        - Remote monitoring
        - Machine learning
        - Backup and sync
        ```
        
        #### Decision Framework:
        - **Latency-critical** → Edge
        - **Privacy-sensitive** → Edge
        - **Complex analytics** → Cloud
        - **Remote access needed** → Cloud/Hybrid
        """,
        "code": """
// Edge Processing (Node-RED)
function edgeControl(temp) {
    // Fast, local decision (< 100ms)
    if (temp > 26) {
        controlPlug("ON");
        logLocalData(temp);
    }
}

// Cloud Sync (Periodic)
function syncToCloud() {
    // Send summary data every 15 minutes
    var summary = {
        avg_temp: calculateAverage(),
        events: getLocalEvents(),
        timestamp: Date.now()
    };
    
    // Queue if offline, send when online
    if (isOnline()) {
        sendToCloud(summary);
    } else {
        queueForLater(summary);
    }
}

// Hybrid Decision Tree
if (criticalControl) {
    processOnEdge();  // Safety-critical, fast
} else if (complexAnalytics) {
    sendToCloud();    // ML/AI processing
} else {
    processOnEdge();  // Default to local
}
        """
    },
    
    "11. Security & Privacy": {
        "goal": "Address critical but often neglected concerns.",
        "topics": [
            "IoT threat model and attack vectors",
            "Weak authentication & default passwords",
            "Network segmentation (VLANs)",
            "Secure communication (TLS, certificates)",
            "Data privacy and GDPR implications"
        ],
        "detailed_description": """
        **Security** is a critical concern in IoT due to the large attack surface and often limited 
        device resources. Common threats include unauthorized access, data interception, and device 
        hijacking.

        Best practices include **strong authentication, encrypted communication, regular updates, and 
        network segmentation**. Node-RED dashboards and APIs should be protected using authentication 
        mechanisms.

        **Privacy considerations** are especially important when IoT systems collect personal or 
        sensitive data, requiring compliance with regulations such as GDPR.
        """,
        "content": """
        ### IoT Security Challenges
        
        #### Common Vulnerabilities:
        
        1. **Weak Authentication**:
           - Default passwords (admin/admin)
           - No password required
           - Hardcoded credentials
        
        2. **Unencrypted Communication**:
           - Plain HTTP vs HTTPS
           - Unencrypted MQTT
           - Wi-Fi without WPA3
        
        3. **Lack of Updates**:
           - Firmware vulnerabilities
           - Abandoned devices
           - No security patches
        
        4. **Physical Access**:
           - USB ports exposed
           - Debug interfaces
           - SD card access
        
        #### Security Best Practices:
        
        **Network Level**:
        - Separate IoT VLAN (guest network)
        - Firewall rules (block internet for local devices)
        - Strong Wi-Fi encryption (WPA3)
        
        **Device Level**:
        - Change default passwords immediately
        - Disable cloud access if not needed
        - Regular firmware updates
        - Disable unused features
        
        **Application Level**:
        - Use HTTPS/TLS for web interfaces
        - Secure MQTT with authentication
        - Encrypt stored credentials
        - Input validation
        
        #### Privacy Considerations:
        - Data minimization (collect only what's needed)
        - Local processing when possible
        - Clear data retention policies
        - User consent for cloud storage
        - GDPR compliance (EU)
        """,
        "code": """
// Node-RED Settings.js - Security Configuration

module.exports = {
    // Enable authentication
    adminAuth: {
        type: "credentials",
        users: [{
            username: "admin",
            password: "$2b$08$...",  // bcrypt hash
            permissions: "*"
        }]
    },
    
    // Enable HTTPS
    https: {
        key: fs.readFileSync('privatekey.pem'),
        cert: fs.readFileSync('certificate.pem')
    },
    
    // Secure headers
    httpNodeCors: {
        origin: "https://yourdomain.com",
        methods: "GET,PUT,POST,DELETE"
    },
    
    // Rate limiting
    rateLimit: {
        windowMs: 15 * 60 * 1000, // 15 minutes
        max: 100 // limit each IP to 100 requests per windowMs
    }
};

// MQTT with TLS and Authentication
mqtt://username:password@broker.example.com:8883
Options: {
    protocol: 'mqtts',
    rejectUnauthorized: true,
    ca: fs.readFileSync('ca.crt')
}
        """
    },
    
    "12. Cloud platforms": {
        "goal": "Understand cloud-based IoT services and data management.",
        "topics": [
            "AWS IoT Core: Device management and MQTT broker",
            "Azure IoT Hub: Device twins and messaging",
            "Cloud data storage and analytics",
            "IoT data pipelines and processing",
            "Cost considerations and pricing models"
        ],
        "detailed_description": """
        **Cloud platforms** provide comprehensive IoT services that handle device connectivity, data 
        storage, analytics, and application integration at scale. Major providers like **AWS and Azure** 
        offer specialized IoT services designed to manage thousands or millions of devices.

        **AWS IoT Core** provides secure device connectivity, message routing, and integration with other 
        AWS services. It supports MQTT, HTTPS, and WebSockets protocols, with built-in device shadows for 
        state management.

        **Azure IoT Hub** offers similar capabilities with device-to-cloud and cloud-to-device messaging, 
        device twins for metadata and state, and integration with Azure's analytics and machine learning 
        services.

        Cloud platforms enable **scalable data management** through services like time-series databases, 
        data lakes, and stream processing. They also provide device management features including 
        provisioning, monitoring, and over-the-air updates.

        Understanding **cost structures** is crucial—cloud services typically charge for data transfer, 
        storage, compute resources, and the number of messages processed. Hybrid edge-cloud architectures 
        can optimize costs while maintaining performance.
        """,
        "content": """
        ### Cloud IoT Platforms
        
        #### AWS IoT Core
        - **Device Gateway**: MQTT broker for device connectivity
        - **Device Shadow**: Virtual representation of device state
        - **Rules Engine**: Route messages to AWS services
        - **Thing Registry**: Device identity and metadata
        - **Integration**: Lambda, DynamoDB, S3, Kinesis, etc.
        
        **Key Features**:
        - Billions of devices and trillions of messages
        - Automatic scaling
        - Built-in security (X.509 certificates, IAM)
        - Pay per message pricing
        
        #### Azure IoT Hub
        - **Device-to-Cloud**: Telemetry ingestion at scale
        - **Cloud-to-Device**: Commands and configuration
        - **Device Twins**: JSON documents storing device metadata
        - **Direct Methods**: Synchronous invocations
        - **Integration**: Event Hub, Stream Analytics, Cosmos DB
        
        **Key Features**:
        - Per-device authentication
        - Protocol support: MQTT, AMQP, HTTPS
        - Edge integration with Azure IoT Edge
        - Device provisioning service
        
        #### Cloud Data Management
        
        **Storage Options**:
        - **Time-series databases**: AWS Timestream, Azure Time Series Insights
        - **Data lakes**: S3, Azure Data Lake
        - **NoSQL**: DynamoDB, Cosmos DB
        - **Relational**: RDS, Azure SQL
        
        **Data Processing**:
        - **Stream processing**: Kinesis, Event Hubs, Stream Analytics
        - **Batch processing**: EMR, Databricks
        - **Serverless**: Lambda, Azure Functions
        - **ML/AI**: SageMaker, Azure ML
        
        #### Architecture Patterns
        
        **1. Full Cloud Architecture**:
        ```
        Devices → Cloud IoT Gateway → Data Storage → Analytics → Dashboard
        ```
        
        **2. Hybrid Edge-Cloud**:
        ```
        Devices → Edge Gateway → Local Processing → Cloud Sync
                                      ↓
                                  Local Control
        ```
        
        **3. Multi-Cloud**:
        ```
        Devices → MQTT Broker → Multiple Cloud Providers
        ```
        
        #### Cost Considerations
        
        **AWS IoT Pricing** (example):
        - Connectivity: $0.08 per million minutes
        - Messaging: $1.00 per million messages
        - Device Shadow: $1.25 per million operations
        - Rules Engine: $0.15 per million actions
        
        **Azure IoT Hub Pricing**:
        - Basic tier: $10/month + $0.50 per million messages
        - Standard tier: $25/month + usage-based
        - Free tier: 8,000 messages/day
        
        **Cost Optimization**:
        - Batch messages when possible
        - Use edge processing to reduce cloud messages
        - Implement data retention policies
        - Choose appropriate tier for your scale
        - Monitor and set billing alerts
        """,
        "code": """
# AWS IoT - Python Device SDK
from awsiot import mqtt_connection_builder
import json
import time

# Build MQTT connection
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint="your-endpoint.iot.region.amazonaws.com",
    cert_filepath="device.pem.crt",
    pri_key_filepath="private.pem.key",
    ca_filepath="AmazonRootCA1.pem",
    client_id="my-device"
)

mqtt_connection.connect()

# Publish sensor data
topic = "sensors/temperature"
message = {
    "deviceId": "my-device",
    "temperature": 23.5,
    "humidity": 65,
    "timestamp": int(time.time())
}

mqtt_connection.publish(
    topic=topic,
    payload=json.dumps(message),
    qos=1
)

# Azure IoT Hub - Python Device SDK
from azure.iot.device import IoTHubDeviceClient, Message

# Create client
connection_string = "HostName=...;DeviceId=...;SharedAccessKey=..."
client = IoTHubDeviceClient.create_from_connection_string(connection_string)

# Connect
client.connect()

# Send telemetry
message = Message(json.dumps({
    "temperature": 23.5,
    "humidity": 65
}))
message.content_type = "application/json"
message.content_encoding = "utf-8"

client.send_message(message)

# Update device twin
twin_patch = {
    "location": "bedroom",
    "firmware_version": "1.0.2"
}
client.patch_twin_reported_properties(twin_patch)

# Node-RED AWS IoT Node Configuration
{
    "endpoint": "your-endpoint.iot.region.amazonaws.com",
    "clientId": "nodered-client",
    "privateKey": "/path/to/private.pem.key",
    "certificate": "/path/to/device.pem.crt",
    "caCert": "/path/to/AmazonRootCA1.pem"
}

// Node-RED Function - Format for Cloud
var cloudMessage = {
    deviceId: msg.deviceId || "unknown",
    timestamp: Date.now(),
    data: {
        temperature: msg.payload.temperature,
        humidity: msg.payload.humidity
    },
    metadata: {
        location: msg.location,
        sensor_type: "DHT11"
    }
};

msg.payload = JSON.stringify(cloudMessage);
return msg;
        """
    },
    
    "13. Energy awareness & sustainability": {
        "goal": "Add societal relevance to IoT systems.",
        "topics": [
            "Energy monitoring in smart homes",
            "Load shifting and demand response",
            "Energy-efficient automation strategies",
            "IoT for sustainability goals",
            "Carbon footprint reduction"
        ],
        "detailed_description": """
        **IoT plays a significant role in improving energy efficiency and sustainability**. Smart plugs 
        and sensors enable real-time monitoring of energy usage and environmental conditions.

        Automation strategies can **reduce waste by turning off devices** when not needed or shifting 
        loads to off-peak periods. These concepts are particularly relevant in smart homes and energy 
        communities.

        **Sustainable IoT design** also considers the environmental impact of devices, communication, 
        and data processing.
        """,
        "content": """
        ### Energy-Aware IoT
        
        #### Energy Monitoring:
        TP-Link smart plugs can measure:
        - **Real-time Power** (Watts)
        - **Voltage** (V)
        - **Current** (A)
        - **Total Energy** (kWh)
        
        #### Load Shifting Strategies:
        
        **Peak vs Off-Peak**:
        - Run heavy loads during off-peak hours
        - Example: Charge EV at night (cheaper rates)
        - Reduce grid stress during peak demand
        
        **Demand Response**:
        - Respond to grid signals
        - Temporarily reduce consumption
        - Get paid for flexibility
        
        #### Energy Optimization Rules:
        
        1. **Standby Elimination**:
           - Turn off devices when not in use
           - Detect phantom loads
           - Schedule daily power cycles
        
        2. **Adaptive Control**:
           - Adjust based on occupancy
           - Weather-responsive heating/cooling
           - Predictive pre-conditioning
        
        3. **Load Prioritization**:
           - Essential vs non-essential loads
           - Shed non-critical loads during peaks
        
        #### Sustainability Metrics:
        - Energy consumption (kWh/day)
        - Peak demand reduction (%)
        - Cost savings (€/month)
        - Carbon emissions avoided (kg CO₂)
        """,
        "code": """
// Node-RED Function - Energy Monitoring
var power = msg.payload.power;  // Watts
var timestamp = new Date();

// Store reading
var readings = flow.get('energyReadings') || [];
readings.push({
    time: timestamp,
    power: power
});

// Keep last 24 hours
if (readings.length > 1440) {  // 1 min intervals
    readings.shift();
}
flow.set('energyReadings', readings);

// Calculate daily consumption
var totalEnergy = readings.reduce((sum, r) => 
    sum + (r.power / 1000 / 60), 0  // kWh
);

msg.payload = {
    current_power: power,
    daily_energy: totalEnergy.toFixed(2),
    estimated_cost: (totalEnergy * 0.25).toFixed(2)  // €/kWh
};

return msg;

// Smart Scheduling - Off-Peak Operation
var hour = new Date().getHours();
var isOffPeak = (hour >= 23 || hour < 7);  // Night hours

if (isOffPeak && msg.payload.pending_load) {
    msg.payload = {
        "state": "ON",
        "reason": "Off-peak operation"
    };
} else if (!isOffPeak && !msg.payload.essential) {
    msg.payload = {
        "state": "OFF",
        "reason": "Avoiding peak hours"
    };
}

return msg;
        """
    },
    
    "14. Scalability & system design": {
        "goal": "Prepare students for real-world deployments.",
        "topics": [
            "Scaling from 1 to 1,000 devices",
            "Naming, addressing, and device management",
            "Fault tolerance and logging",
            "Over-the-air (OTA) updates",
            "Production vs prototype differences"
        ],
        "detailed_description": """
        While many IoT projects start as **small prototypes, real-world deployments must scale to hundreds 
        or thousands of devices**. Scalability requires careful system design, modular architectures, and 
        standardized data models.

        **Device management, logging, and monitoring** are essential for maintaining large-scale IoT 
        systems. Differences between prototype and production environments should be clearly understood 
        by system designers.
        """,
        "content": """
        ### Scalable IoT System Design
        
        #### Design Principles:
        
        **1. Systematic Naming Convention**:
        ```
        <location>/<room>/<device_type>/<device_id>
        
        Examples:
        building_a/floor_2/bedroom_201/temp_sensor_1
        building_a/floor_2/bedroom_201/smart_plug_1
        ```
        
        **2. Device Management**:
        - Centralized inventory database
        - Automatic device discovery
        - Health monitoring
        - Firmware version tracking
        
        **3. Fault Tolerance**:
        - Graceful degradation
        - Retry mechanisms
        - Fallback values
        - Circuit breakers
        
        **4. Logging and Monitoring**:
        ```
        [timestamp] [device_id] [level] [message]
        2025-12-13 10:30:00 plug_201 INFO State changed to ON
        2025-12-13 10:30:15 sensor_201 ERROR Connection timeout
        ```
        
        #### Production Considerations:
        
        **Prototype**:
        - Hardcoded IPs and credentials
        - Manual configuration
        - Console logging
        - Single instance
        
        **Production**:
        - Configuration files/database
        - Auto-discovery and provisioning
        - Structured logging to files/databases
        - High availability / redundancy
        - Monitoring and alerting
        - Backup and disaster recovery
        
        #### Performance Optimization:
        - Message batching
        - Connection pooling
        - Caching frequent queries
        - Load balancing
        """,
        "code": """
// Scalable Configuration Management
// devices.json
{
    "devices": [
        {
            "id": "plug_bedroom_201",
            "type": "smart_plug",
            "location": "building_a/floor_2/bedroom_201",
            "ip": "192.168.2.101",
            "model": "TP-Link HS110"
        },
        {
            "id": "sensor_bedroom_201",
            "type": "temp_humidity",
            "location": "building_a/floor_2/bedroom_201",
            "mqtt_topic": "sensors/bedroom_201",
            "model": "Broadlink RM4"
        }
    ]
}

// Node-RED Function - Device Registry
var devices = global.get('deviceRegistry') || {};

// Register device
function registerDevice(deviceId, metadata) {
    devices[deviceId] = {
        ...metadata,
        last_seen: new Date(),
        status: 'online'
    };
    global.set('deviceRegistry', devices);
}

// Health check
function checkDeviceHealth() {
    var now = new Date();
    Object.keys(devices).forEach(deviceId => {
        var timeSinceLastSeen = now - devices[deviceId].last_seen;
        if (timeSinceLastSeen > 300000) {  // 5 minutes
            devices[deviceId].status = 'offline';
            node.warn(`Device ${deviceId} is offline`);
        }
    });
}

// Structured Logging
function logEvent(deviceId, level, message, data = {}) {
    var logEntry = {
        timestamp: new Date().toISOString(),
        device_id: deviceId,
        level: level,  // INFO, WARN, ERROR
        message: message,
        data: data
    };
    
    // Write to database or file
    node.send({topic: 'logs', payload: logEntry});
}
        """
    },
    
    "15. Node-RED project": {
        "goal": "Integrate everything learned into a complete system.",
        "topics": [
            "Designing end-to-end IoT data flows",
            "Integrating virtual and physical sensors",
            "Using Node-RED for orchestration",
            "Implementing edge-to-cloud architectures",
            "Applying data aggregation, storage, and visualization",
            "Building smart energy and building management systems"
        ],
        "detailed_description": """
        Laboratory: IoT Systems and Smart Building Management
        The laboratory provides a hands-on, end-to-end introduction to IoT system design, focusing on edge devices, data acquisition, processing, storage, and control, using Node-RED and Python as core technologies. 

        """,
        "content": """  
        ### Core Technologies and Architecture

        The implemented architecture follows a layered IoT model:

        - Edge layer: Virtual and physical sensors and actuators simulated or controlled via Python.
        - Middleware layer: Node-RED for orchestration, data routing, and integration.
        - Data layer: Local storage using TinyDB (edge) and centralized storage using MongoDB.
        - Application layer: Streamlit dashboard for monitoring, analytics, and visualization.

        Key technologies:

        - Node.js & Node-RED - IoT orchestration and flow-based programming
        - Python - Edge simulation, data aggregation, external API access, and control logic
        - MongoDB - Centralized time-series and contextual data storage
        - TinyDB - Lightweight edge-level persistence
        - Streamlit - Data visualization and dashboarding

        ---

        ### Part I - Managing IoT Devices with Node-RED

        #### 2.1 Environment Setup and Basic Flow

        Install Node.js and Node-RED, configure MongoDB nodes, and create a basic HTTP-based ingestion flow:

        - HTTP In node receives edge data
        - JSON node parses payloads
        - MongoDB Out stores data
        - Debug node visualizes messages
        - HTTP Response ensures correct client-server communication

        #### 2.2 Edge Simulation and Data Flow

        A Python-based edge simulator generates synthetic sensor readings (PV power, battery SOC, HVAC load) for multiple virtual edges:

        - Data is generated every few seconds
        - Stored locally in TinyDB
        - Sent via HTTP POST to Node-RED
        - Persisted centrally in MongoDB

        #### 2.3 Data Aggregation

        Node-RED integrates Python Shell nodes to periodically:

        - Aggregate edge readings (e.g., every 15 minutes)
        - Store aggregated results in MongoDB for further analysis

        ---

        ### Part II - Smart Building Management Project

        #### 3.1 External Data Collection

        The system integrates contextual data sources:

        - Weather data retrieved from Open-Meteo API (temperature, wind, radiation, humidity, etc.)
        - Electricity prices scraped from the Romanian day-ahead market (OPCOM) using Selenium
        - Data is cleaned, time-zone aligned, and stored in MongoDB

        ---

        ### Sensor and Edge Modeling

        #### 4.1 Virtual Edge Devices

        Three virtual edges emulate a smart building:

        - PV edge: Solar generation and baseline load
        - Zone 1: HVAC and lighting
        - Zone 2: HVAC, lighting, and computing loads

        Sensor values are generated dynamically based on weather conditions and asset models, sent every 10 seconds to Node-RED, and archived both locally and centrally.

        #### 4.2 Sensor Data Processing

        Node-RED flows handle:

        - HTTP reception
        - JSON parsing
        - Debugging and monitoring
        - Periodic aggregation and MongoDB storage

        ---

        ### Integration of Real Devices and Sensors

        #### 5.1 Smart Plugs

        - TP-Link TAPO P115 smart plugs provide real power and energy measurements
        - Controlled and monitored via Node-RED TAPO nodes and Python scripts

        #### 5.2 Environmental Sensors

        - Broadlink sensors (RM4 Mini/Pro) provide temperature and humidity readings
        - Python scripts discover devices, authenticate, and collect sensor data

        ---

        ### Control Logic and Actuation

        A control room logic is implemented:

        - User preferences (temperature, humidity) are loaded from JSON
        - Real-time sensor data is evaluated
        - ON/OFF decisions are generated
        - Commands are translated into boolean signals
        - Smart plugs actuate heaters, AC units, or humidifiers accordingly

        This demonstrates a closed-loop IoT control system.

        ---

        ### Visualization and Dashboard

        A Streamlit dashboard provides:

        - Real-time monitoring of edges and zones
        - PV generation and consumption analytics
        - Electricity cost and billing analysis using market prices
        - KPIs, comparisons, and summary indicators
        - User guidance and troubleshooting support

        The dashboard connects directly to MongoDB for live data retrieval and visualization.
        """,
        "code": """ // Due to the comprehensive nature of this project, code is provided on Github.  
        """

    }
}

# Sidebar navigation
st.sidebar.title("🎓 Course Topics")
# Topic selection
topic_keys = list(TOPICS.keys())
selected_topic = st.sidebar.radio(
    "Select a Topic:",
    topic_keys,
    index=0
)

# Course info in sidebar
st.sidebar.markdown("---")
st.sidebar.info("""
**IoT Systems Lab**  
Node-RED Integration with:
- 🔌 TP-Link Smart Plugs
- 🌡️ Broadlink Sensors
- 📊 Real-time Dashboards
""")


# Main content area
st.markdown('<h1 class="main-header">🔬 IoT Systems Course</h1>', unsafe_allow_html=True)

# Display selected topic
if selected_topic:
    topic_data = TOPICS[selected_topic]
    
    # Topic header
    st.markdown(f'<div class="topic-header">{selected_topic}</div>', unsafe_allow_html=True)
    
    # Goal
    #st.markdown(f"**🎯 Goal:** {topic_data['goal']}")
    #st.markdown("---")
    
    # Create tabs for better organization
    # Only show Lab Activities tab for topic 15 (Capstone)
    if selected_topic == "15. Mini-Project / Capstone":
        tab1, tab2, tab3, tab4 = st.tabs(["📖 Content", "🔬 Lab Activities", "💻 Code Examples", "📝 Key Topics"])
    else:
        tab1, tab3, tab4 = st.tabs(["📖 Content", "💻 Code Examples", "📝 Key Topics"])
        tab2 = None  # No lab tab for other topics
    
    
    with tab1:
        # Display detailed academic description first
        if 'detailed_description' in topic_data:
            st.markdown("### 📖 Overview")
            st.info(topic_data['detailed_description'])
            st.markdown("---")
        
        # Display the practical content
        st.markdown(topic_data['content'])
        
        # Add topic-specific diagrams
        if selected_topic == "1. Introduction to IoT Systems":
            st.markdown("---")
            st.subheader("📊 System Architecture Visualization")
            st.plotly_chart(create_iot_architecture_diagram(), width='content')
            st.image("Pics/IoT overview.png", caption="IoT System Architecture", width='content')
            st.markdown("[GeeksforGeeks IoT Introduction](https://www.geeksforgeeks.org/computer-networks/introduction-to-internet-of-things-iot-set-1/)")
            
            
        elif selected_topic == "2. Hardware platforms":
            st.markdown("---")
            st.subheader("🔧 Hardware Platform Comparison")
            
            # Platform comparison chart
            platforms = ['Arduino', 'Raspberry Pi', 'ESP8266', 'ESP32']
            processing = [3, 10, 6, 8]
            power_efficiency = [10, 3, 8, 9]
            cost_efficiency = [7, 5, 10, 10]
            ease_of_use = [9, 8, 7, 7]
            
            fig_platforms = go.Figure()
            
            fig_platforms.add_trace(go.Bar(name='Processing Power', x=platforms, y=processing, marker_color='#3498db'))
            fig_platforms.add_trace(go.Bar(name='Power Efficiency', x=platforms, y=power_efficiency, marker_color='#27ae60'))
            fig_platforms.add_trace(go.Bar(name='Cost Efficiency', x=platforms, y=cost_efficiency, marker_color='#f39c12'))
            fig_platforms.add_trace(go.Bar(name='Ease of Use', x=platforms, y=ease_of_use, marker_color='#9b59b6'))
            
            fig_platforms.update_layout(
                title="IoT Hardware Platform Comparison (1-10 scale)",
                barmode='group',
                yaxis_title="Score",
                height=400
            )
            st.plotly_chart(fig_platforms, use_container_width=True)
            
            # Memory comparison
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 💾 Memory Specifications")
                memory_data = pd.DataFrame({
                    'Platform': ['Arduino Uno', 'Raspberry Pi 4', 'ESP8266', 'ESP32'],
                    'RAM': ['2 KB', '4 GB', '80 KB', '520 KB'],
                    'Flash': ['32 KB', '32 GB SD', '4 MB', '4 MB']
                })
                st.dataframe(memory_data, hide_index=True, use_container_width=True)
            
            with col2:
                st.markdown("### ⚡ Power Consumption")
                power_data = pd.DataFrame({
                    'Platform': ['Arduino Uno', 'Raspberry Pi 4', 'ESP8266', 'ESP32'],
                    'Active': ['50 mA', '600 mA', '80 mA', '160 mA'],
                    'Sleep': ['15 mA', 'N/A', '20 µA', '10 µA']
                })
                st.dataframe(power_data, hide_index=True, use_container_width=True)
            # Hardware platform images
            st.markdown("---")
            st.subheader("🖼️ IoT Hardware platforms")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                try:
                    st.image("Pics/arduino.jpg", caption="Arduino Uno", use_container_width=True)
                except:
                    st.info("Arduino Uno\n(Image not found)")
            
            with col2:
                try:
                    st.image("Pics/raspberry-pi-4.png", caption="Raspberry Pi 4", use_container_width=True)
                except:
                    st.info("Raspberry Pi 4\n(Image not found)")
            
            with col3:
                try:
                    st.image("Pics/esp8266.png", caption="ESP8266", use_container_width=True)
                except:
                    st.info("ESP8266\n(Image not found)")
            
        elif selected_topic == "3. Sensors & Actuators":
            st.markdown("---")
            st.subheader("📈 Sensor Data Example")
            st.plotly_chart(create_sensor_data_chart(), use_container_width=True)
            
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 🌡️ Temperature Sensor Specs")
                specs_temp = pd.DataFrame({
                    'Parameter': ['Range', 'Accuracy', 'Resolution', 'Sample Rate'],
                    'Value': ['-20 to 60°C', '±0.5°C', '0.1°C', '1-60 sec']
                })
                st.dataframe(specs_temp, hide_index=True, use_container_width=True)
            
            with col2:
                st.markdown("### 💧 Humidity Sensor Specs")
                specs_hum = pd.DataFrame({
                    'Parameter': ['Range', 'Accuracy', 'Resolution', 'Sample Rate'],
                    'Value': ['0-100%', '±3%', '0.1%', '1-60 sec']
                })
                st.dataframe(specs_hum, hide_index=True, use_container_width=True)
            
            # Sensors and actuators images
            st.markdown("---")
            st.subheader("🖼️ Sensors and Actuators")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                try:
                    st.image("Pics/broadlink RM4Mini.jpg", caption="Broadlink RM4 Mini", use_container_width=True)
                except:
                    st.info("Broadlink\n(Image not found)")
            
            with col2:
                try:
                    st.image("Pics/Tapo P110M.jpg", caption="Tapo P110 M", use_container_width=True)
                except:
                    st.info("Tapo P110M\n(Image not found)")
            
            with col3:
                try:
                    st.image("Pics/Tapo P115.jpg", caption="Tapo P115", use_container_width=True)
                except:
                    st.info("Tapo P115\n(Image not found)")
        elif selected_topic == "4. IoT Communication protocols":
            st.markdown("---")
            st.subheader("🔗 MQTT vs HTTP Comparison")
            st.markdown("### MQTT")
            try:
                    st.image("Pics/MQTT-Process.png", caption="MQTT Protocol", width=400)
            except:
                    st.info("MQTT Protocol\n(Image not found)")
            st.markdown("### HTTP")
            try:
                    st.image("Pics/HTTP-Process.png", caption="HTTP Protocol", width=400)
            except:
                    st.info("HTTP Protocol\n(Image not found)")
        elif selected_topic == "5. Node-RED as IoT middleware":
            st.markdown("---")
            st.subheader("🛠️ Node-RED Flow Example")
            try:
                    st.image("Pics/Node-RED-Flow.png", caption="Node-RED Flow Example", use_container_width=True)
            except:
                    st.info("Node-RED Flow Example\n(Image not found)")
            
        elif selected_topic == "8. Dashboards & Visualization":
            st.markdown("---")
            st.subheader("📊 Sample Dashboard Widgets")
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig_gauge = go.Figure(go.Indicator(
                    mode="gauge+number+delta",
                    value=23.5,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Temperature (°C)"},
                    delta={'reference': 22},
                    gauge={
                        'axis': {'range': [None, 50]},
                        'bar': {'color': "#e74c3c"},
                        'steps': [
                            {'range': [0, 20], 'color': "lightblue"},
                            {'range': [20, 25], 'color': "lightgreen"},
                            {'range': [25, 50], 'color': "lightyellow"}],
                        'threshold': {
                            'line': {'color': "red", 'width': 4},
                            'thickness': 0.75,
                            'value': 28}
                    }))
                fig_gauge.update_layout(height=300)
                st.plotly_chart(fig_gauge, use_container_width=True)
            
            with col2:
                fig_gauge2 = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=65,
                    domain={'x': [0, 1], 'y': [0, 1]},
                    title={'text': "Humidity (%)"},
                    gauge={
                        'axis': {'range': [None, 100]},
                        'bar': {'color': "#3498db"},
                        'steps': [
                            {'range': [0, 40], 'color': "lightyellow"},
                            {'range': [40, 70], 'color': "lightgreen"},
                            {'range': [70, 100], 'color': "lightblue"}]
                    }))
                fig_gauge2.update_layout(height=300)
                st.plotly_chart(fig_gauge2, use_container_width=True)
                            
                st.plotly_chart(create_sensor_data_chart(), use_container_width=True)
        
        elif selected_topic == "9. Automation & Rule-based control":
            st.markdown("---")
            st.subheader("🔄 Hysteresis Control Example")
            
            time_points = np.linspace(0, 24, 100)
            temp_signal = 23 + 4 * np.sin(time_points / 4) + np.random.normal(0, 0.3, 100)
            
            state = []
            current_state = False
            for temp in temp_signal:
                if temp > 26 and not current_state:
                    current_state = True
                elif temp < 22 and current_state:
                    current_state = False
                state.append(25 if current_state else 15)
            
            fig_hyst = go.Figure()
            fig_hyst.add_trace(go.Scatter(x=time_points, y=temp_signal, name='Temperature', 
                                         line=dict(color='#e74c3c', width=2)))
            fig_hyst.add_trace(go.Scatter(x=time_points, y=state, name='Plug State (scaled)', 
                                         line=dict(color='#27ae60', dash='dash', width=2), 
                                         fill='tozeroy', fillcolor='rgba(39, 174, 96, 0.2)'))
            fig_hyst.add_hline(y=26, line_dash="dot", line_color="red", annotation_text="Turn ON (26°C)")
            fig_hyst.add_hline(y=22, line_dash="dot", line_color="blue", annotation_text="Turn OFF (22°C)")
            fig_hyst.update_layout(title="Temperature Control with Hysteresis (2°C Dead Band)", 
                                  xaxis_title="Time (hours)", yaxis_title="Temperature (°C)", height=400)
            st.plotly_chart(fig_hyst, use_container_width=True)
            
            st.info("💡 **Hysteresis prevents rapid ON/OFF cycling** by having different thresholds for turning ON (26°C) and OFF (22°C). The green shaded area shows when the plug is active.")
        
        elif selected_topic == "10. Edge vs Cloud Computing":
            st.markdown("---")
            st.subheader("🖥️ Edge Computing Architecture")
            
            
            st.markdown("### 🌐 Local vs Cloud Processing")
            processing_data = pd.DataFrame({
                'Task': ['Data Filtering', 'Anomaly Detection', 'Control Decisions', 'Data Storage'],
                'Edge': ['Yes', 'Yes', 'Yes', 'No'],
                'Cloud': ['No', 'No', 'No', 'Yes']
            })
            st.dataframe(processing_data, hide_index=True, use_container_width=True)
            st.markdown("---")
            st.subheader("📊 Edge vs Cloud Analysis")
            st.image("Pics/Edge-vs-Cloud.png", caption="Edge vs Cloud Computing", width='content')
            st.plotly_chart(create_edge_vs_cloud_comparison(), use_container_width=True)
            
            st.markdown("### ⚡ Latency Comparison")
            latency_data = pd.DataFrame({
                'Operation': ['Sensor Read', 'Local Decision', 'Plug Control', 'Total Response'],
                'Edge (ms)': [10, 5, 15, 30],
                'Cloud (ms)': [10, 500, 600, 1110]
            })
            
            fig_latency = go.Figure()
            fig_latency.add_trace(go.Bar(name='Edge', x=latency_data['Operation'], 
                                         y=latency_data['Edge (ms)'], marker_color='#27ae60'))
            fig_latency.add_trace(go.Bar(name='Cloud', x=latency_data['Operation'], 
                                         y=latency_data['Cloud (ms)'], marker_color='#3498db'))
            fig_latency.update_layout(barmode='group', title='Response Time Comparison', 
                                     yaxis_title='Latency (ms)', height=350)
            st.plotly_chart(fig_latency, use_container_width=True)
        
        elif selected_topic == "12. Cloud platforms":
            st.markdown("---")
            st.subheader("☁️ Cloud Platform Services Comparison")
            
            # AWS vs Azure services comparison
            services_data = pd.DataFrame({
                'Service': ['Device Gateway', 'Device Management', 'Rules Engine', 'Time-series DB', 'Stream Processing', 'ML/AI Services'],
                'AWS': ['IoT Core', 'Device Management', 'Rules Engine', 'Timestream', 'Kinesis', 'SageMaker'],
                'Azure': ['IoT Hub', 'Device Provisioning', 'Routes & Endpoints', 'Time Series Insights', 'Stream Analytics', 'Azure ML']
            })
            st.dataframe(services_data, hide_index=True, use_container_width=True)
            
            # Cost comparison visualization
            st.markdown("### 💰 Monthly Cost Estimation")
            col1, col2 = st.columns(2)
            with col1:
                num_devices = st.slider("Number of Devices", 10, 10000, 100, step=10)
                messages_per_day = st.slider("Messages per Device per Day", 10, 1000, 100)
            
            with col2:
                total_messages = num_devices * messages_per_day * 30 / 1_000_000  # millions
                
                # Simplified pricing
                aws_cost = (num_devices * 30 * 0.08 / 1_000_000) + (total_messages * 1.00)
                azure_cost = 10 + (total_messages * 0.50)
                
                col_a, col_b = st.columns(2)
                col_a.metric("AWS IoT Cost", f"${aws_cost:.2f}/month")
                col_b.metric("Azure IoT Cost", f"${azure_cost:.2f}/month")
                
                st.info(f"📊 Processing {total_messages:.2f}M messages/month from {num_devices} devices")
            
            # Architecture diagram
            st.markdown("### 🏗️ Cloud IoT Architecture")
            st.markdown("""
            ```
            ┌─────────────┐
            │   Devices   │
            │ (Sensors &  │
            │  Actuators) │
            └──────┬──────┘
                   │ MQTT/HTTPS
                   ▼
            ┌─────────────────┐
            │  Cloud Gateway  │
            │  (IoT Core/Hub) │
            └──────┬──────────┘
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    ┌──────┐  ┌──────┐  ┌──────────┐
    │Rules │  │Device│  │ Telemetry│
    │Engine│  │Shadow│  │  Stream  │
    └──┬───┘  └──────┘  └────┬─────┘
       │                      │
       ▼                      ▼
    ┌──────────┐       ┌──────────┐
    │ Lambda/  │       │Time-series│
    │ Function │       │ Database  │
    └────┬─────┘       └────┬─────┘
         │                  │
         └────────┬─────────┘
                  ▼
            ┌──────────┐
            │Dashboard │
            │Analytics │
            └──────────┘
            ```
            """)
        
        elif selected_topic == "13. Energy awareness & sustainability":
            st.markdown("---")
            st.subheader("⚡ Energy Monitoring Dashboard")
            st.plotly_chart(create_energy_monitoring_chart(), use_container_width=True)
            
            st.markdown("### 💰 Energy Savings Calculator")
            col1, col2 = st.columns(2)
            with col1:
                daily_hours_before = st.slider("Hours ON per day (Before)", 0, 24, 16)
                power_watts = st.slider("Device Power (W)", 0, 2000, 500)
            with col2:
                daily_hours_after = st.slider("Hours ON per day (After)", 0, 24, 8)
                price_per_kwh = st.slider("Electricity Price (€/kWh)", 0.0, 1.0, 0.25)
            
            energy_before = (daily_hours_before * power_watts) / 1000
            energy_after = (daily_hours_after * power_watts) / 1000
            daily_savings = energy_before - energy_after
            monthly_savings = daily_savings * 30
            cost_savings = monthly_savings * price_per_kwh
            co2_savings = monthly_savings * 0.5
            
            col1, col2, col3 = st.columns(3)
            col1.metric("Daily Savings", f"{daily_savings:.2f} kWh", f"{daily_savings/energy_before*100:.0f}%")
            col2.metric("Monthly Cost Savings", f"€{cost_savings:.2f}")
            col3.metric("CO₂ Reduced", f"{co2_savings:.2f} kg")
        
 
    # Only display Lab Activities tab if it exists (topic 15)
    if tab2 is not None:
        with tab2:
            st.markdown("### Laboratory Exercises")
            if 'labs' in topic_data:
                for i, lab in enumerate(topic_data['labs'], 1):
                    st.markdown(f"{i}. {lab}")
            else:
                st.info("Lab activities for this topic have been consolidated into Topic 15")
    
    with tab3:
        st.markdown("### Code Examples & Implementation")
        st.code(topic_data['code'], language='javascript')
        
        # Download code button
        st.download_button(
            label="📥 Download Code Example",
            data=topic_data['code'],
            file_name=f"topic_{selected_topic.split('.')[0]}_example.js",
            mime="text/plain"
        )
    
    with tab4:
        st.markdown("### Key Topics Covered")
        for topic in topic_data['topics']:
            st.markdown(f"✓ {topic}")

# Quick reference section at the bottom
with st.expander("🔗 Quick Reference & Resources"):
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Node-RED Resources:**
        - [Official Documentation](https://nodered.org/docs/)
        - [Node-RED Flows Library](https://flows.nodered.org/)
        - [Community Forum](https://discourse.nodered.org/)
        """)
        
        st.markdown("""
        **TP-Link Integration:**
        - `node-red-contrib-tplink-tapo`
        - TAPO Cloud API
        """)
    
    with col2:
        st.markdown("""
        **MQTT Resources:**
        - [MQTT.org](https://mqtt.org/)
        - [Mosquitto Broker](https://mosquitto.org/)
        """)
        
        st.markdown("""
        **Broadlink Integration:**
        - python-broadlink library
        - HTTP/MQTT bridge options
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p>IoT Systems Course | Node-RED Laboratory | December 2025</p>
    <p>Built with Streamlit 🎈</p>
</div>
""", unsafe_allow_html=True)
