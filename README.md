# Medical Insurance Cost Prediction

## Project Overview
This project predicts medical insurance costs using machine learning based on various factors such as age, BMI, smoking status, and region. The model is deployed using Flask, Docker, Kubernetes, and Google Cloud Platform (GCP) for scalability and reliability.

## Features
- Predicts insurance costs based on user inputs.
- Machine learning model trained on a structured dataset.
- Flask-based web interface for user interaction.
- REST API for integrating predictions into other applications.
- Containerized using Docker for easy deployment and portability.
- Kubernetes for orchestration, load balancing, and scaling.
- Hosted on GCP for cloud-based accessibility and efficiency.
- Secure and efficient handling of user data.

## Technologies Used
- **Machine Learning**: Model trained using Python (Scikit-Learn, Pandas, NumPy).
- **Flask**: Web framework for building the API.
- **Docker**: Containerization for consistent deployment across environments.
- **Kubernetes**: Orchestration and scaling of containers.
- **Google Cloud Platform (GCP)**: Cloud infrastructure for hosting and managing services.

## Installation and Setup
### Prerequisites
- Docker installed
- Kubernetes configured
- Google Cloud account set up
- Python (if running locally)

### Steps
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-repo/medical-insurance-cost-prediction.git
   cd medical-insurance-cost-prediction
   ```
2. **Install dependencies (if running locally)**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Build and run Docker container**:
   ```bash
   docker build -t insurance-cost-predictor .
   docker run -p 8800:8800 insurance-cost-predictor
   ```
4. **Deploy with Kubernetes**:
   ```bash
   kubectl apply -f deployment.yaml
   ```
5. **Access the application**:
   Open `http://localhost:8800` in your browser or use the API endpoint.

## Usage
- Enter details like age, BMI, smoking status, and region in the web interface.
- Click 'Predict' to get the estimated insurance cost.
- API available for programmatic access to predictions.

## Deployment on GCP
- Build and push the Docker image to Google Container Registry.
- Deploy the application on Google Kubernetes Engine (GKE).
- Expose the service via LoadBalancer.
- Monitor performance and logs using GCP tools.

## Future Enhancements
- Improve model accuracy with advanced algorithms.
- Add more interactive visualizations and dashboards.
- Implement user authentication for secure access.
- Optimize API for higher efficiency and lower latency.
- Introduce more variables to enhance prediction reliability.

## License
This project is licensed under the MIT License.

