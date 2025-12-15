# IoT Course Interactive Presentation App

An interactive Streamlit application for teaching IoT concepts with hands-on Node-RED, TP-Link Smart Plugs, and Broadlink sensors.

## 🎯 Features

### 📚 **13 Comprehensive Topics**
1. Introduction to IoT Systems
2. Sensors & Actuators
3. IoT Communication Protocols
4. Node-RED as IoT Middleware
5. Device Integration & APIs
6. Data Handling & Storage
7. Dashboards & Visualization
8. Automation & Rule-Based Control
9. Edge vs Cloud Computing
10. Security & Privacy
11. Energy Awareness & Sustainability
12. Scalability & System Design
13. Mini-Project / Capstone

### 📊 **Interactive Diagrams**
- **Architecture Visualizations**: Layered IoT system architecture
- **Sensor Data Charts**: Real-time temperature and humidity trends
- **Energy Monitoring**: Power consumption and cost analysis
- **Edge vs Cloud Comparison**: Radar charts comparing trade-offs
- **Hysteresis Control**: Visual demonstration of smart control logic
- **Dashboard Widgets**: Interactive gauges and indicators

### 🛠️ **Educational Tools**
- **Code Examples**: Node-RED JavaScript snippets for each topic
- **Lab Activities**: Hands-on exercises with real hardware
- **Progress Tracking**: Students can mark completed topics
- **Quick Reference**: Links to documentation and resources
- **Downloadable Content**: Export code examples for labs

### 💡 **Interactive Calculators**
- **Energy Savings Calculator**: Calculate cost and CO₂ savings
- **Latency Comparison**: Edge vs Cloud response times
- **Sensor Specifications**: Technical specs for Broadlink sensors

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Install Dependencies

```bash
pip install -r requirements_course_app.txt
```

Or install packages individually:
```bash
pip install streamlit plotly pandas numpy
```

## ▶️ Running the App

Navigate to the project directory and run:

```bash
streamlit run iot_course_app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## 📖 Usage Guide

### Navigation
- Use the **sidebar menu** to select topics (1-13)
- Each topic has **4 tabs**:
  - 📖 **Content**: Detailed explanations with diagrams
  - 🔬 **Lab Activities**: Hands-on exercises
  - 💻 **Code Examples**: Node-RED implementation
  - 📝 **Key Topics**: Quick reference list

### Progress Tracking
- Mark completed topics in the sidebar
- View your progress percentage
- Track which topics need review

### Interactive Elements
- Adjust sliders in the Energy Calculator
- Explore interactive charts (zoom, pan, hover)
- Download code examples
- View real-time sensor simulations

## 🎓 Course Structure

### Hardware Requirements (for Lab Activities)
- **TP-Link Smart Plugs** (Kasa HS110 or similar)
- **Broadlink Sensors** (RM4 Mini or similar)
- **Raspberry Pi** or PC for Node-RED
- **Wi-Fi Network**

### Software Requirements
- Node-RED (v3.x+)
- MQTT Broker (Mosquitto)
- Node-RED Dashboard
- Community nodes: `node-red-contrib-tplink-tapo`

## 📊 Diagram Types

### 1. Architecture Diagrams
- Layered IoT system architecture
- Network topology visualization

### 2. Data Visualizations
- Time-series sensor data (temperature/humidity)
- Energy consumption trends
- Power monitoring dashboards

### 3. Comparison Charts
- Edge vs Cloud radar chart
- Protocol comparison tables
- Latency bar charts

### 4. Control Logic
- Hysteresis control visualization
- Automation flow diagrams

### 5. Interactive Widgets
- Temperature gauges with thresholds
- Humidity indicators
- Real-time metrics

## 🔧 Customization

### Adding New Topics
Edit `iot_course_app.py` and add entries to the `TOPICS` dictionary:

```python
TOPICS = {
    "14. Your New Topic": {
        "goal": "Learning objective",
        "topics": ["Subtopic 1", "Subtopic 2"],
        "content": "Detailed explanation...",
        "labs": ["Lab exercise 1", "Lab exercise 2"],
        "code": "// Code example"
    }
}
```

### Modifying Diagrams
Update the diagram functions:
- `create_iot_architecture_diagram()`
- `create_sensor_data_chart()`
- `create_energy_monitoring_chart()`
- `create_edge_vs_cloud_comparison()`

### Styling
Modify the CSS in the `st.markdown()` section at the top of the file.

## 📝 Topics Overview

| Topic | Key Focus | Lab Equipment |
|-------|-----------|---------------|
| 1. Introduction | IoT architecture | All devices |
| 2. Sensors & Actuators | Data acquisition | Broadlink, TP-Link |
| 3. Communication | MQTT, HTTP | MQTT broker |
| 4. Node-RED | Flow programming | Node-RED |
| 5. Integration | Device APIs | All devices |
| 6. Data Storage | Databases | SQLite/InfluxDB |
| 7. Dashboards | Visualization | Node-RED Dashboard |
| 8. Automation | Rule-based logic | All devices |
| 9. Edge/Cloud | Architecture decisions | - |
| 10. Security | IoT security | All devices |
| 11. Energy | Sustainability | TP-Link plugs |
| 12. Scalability | System design | - |
| 13. Capstone | Complete project | All devices |

## 💻 Code Examples Included

Each topic includes working code examples:
- **Node-RED Function nodes**: JavaScript logic
- **MQTT topics**: Topic structure and payloads
- **SQL queries**: Database operations
- **Python snippets**: Device control
- **Configuration**: Settings and best practices

## 🎯 Learning Outcomes

After completing this course, students will be able to:
1. ✅ Design IoT system architectures
2. ✅ Integrate sensors and actuators with Node-RED
3. ✅ Implement MQTT communication
4. ✅ Create automation rules and logic
5. ✅ Build interactive dashboards
6. ✅ Store and visualize time-series data
7. ✅ Implement energy-efficient strategies
8. ✅ Understand security best practices
9. ✅ Make edge vs cloud decisions
10. ✅ Design scalable IoT systems

## 🔗 Resources

### Official Documentation
- [Node-RED Documentation](https://nodered.org/docs/)
- [MQTT.org](https://mqtt.org/)
- [Streamlit Docs](https://docs.streamlit.io/)

### Hardware APIs
- [TP-Link Kasa API](https://github.com/python-kasa/python-kasa)
- [Broadlink Library](https://github.com/mjg59/python-broadlink)

### Community
- [Node-RED Forum](https://discourse.nodered.org/)
- [Node-RED Flows](https://flows.nodered.org/)

## 📊 Assessment Ideas

### For Instructors
- **Quiz Mode**: Add multiple-choice questions per topic
- **Lab Reports**: Students document their implementations
- **Live Demos**: Present working Node-RED flows
- **Capstone Project**: Complete smart home system

## 🐛 Troubleshooting

### App Won't Start
```bash
# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install --upgrade streamlit plotly pandas numpy
```

### Diagrams Not Showing
- Ensure all packages are installed
- Check internet connection (first run downloads dependencies)
- Clear Streamlit cache: `streamlit cache clear`

### Port Already in Use
```bash
# Use a different port
streamlit run iot_course_app.py --server.port 8502
```

## 📄 License

This educational material is designed for academic use in IoT courses.

## 👥 Contributors

Created for IoT Systems course with practical Node-RED integration.

## 📧 Support

For questions about the app or course content, refer to:
- [topics.md](topics.md) - Original course outline
- Node-RED flows in the workspace
- Hardware integration examples

---

**Built with Streamlit 🎈 | Plotly 📊 | Python 🐍**

*Last Updated: December 2025*
